# -*- coding: utf-8 -*-
from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib
import numpy as np
import pandas as pd

app = Flask(__name__)
CORS(app)

# 1. Modeli Yükleme
try:
    model = joblib.load('Nihai_RandomForest_Modeli.pkl')
    print("=== BAŞARILI: Model Yüklendi ===")
except Exception as e:
    print(f"=== HATA: Model yüklenemedi! Hata: {e} ===")

TIME_MEAN, TIME_STD = 94813.86, 47488.15
AMOUNT_MEAN, AMOUNT_STD = 88.35, 250.12

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.json
        amount = float(data.get('amount', 0))
        time = float(data.get('time', 0))
        country = data.get('country', '')
        device = data.get('device', '')
        payment = data.get('payment', '')
        
        # الأساس: أرقام بنكية سليمة
        v = [0.0] * 28
        
        # ترجمة الخطورة إلى أرقام يفهمها الموديل
        badness = 0.0
        if amount > 5000: badness += 1.0
        if amount > 20000: badness += 1.5
        if country in ['RU', 'NG']: badness += 1.8
        if device == 'unknown': badness += 0.8
        if payment == 'transfer': badness += 0.5
        
        hour = (time % 86400) / 3600
        if 0 <= hour < 5: badness += 1.0
        
        # حقن الخطورة في المتغيرات السرية لكي يكتشفها الموديل
        if badness > 0:
            v[0] = -2.0 * badness   # V1
            v[2] = -3.0 * badness   # V3
            v[3] = 2.0 * badness    # V4
            v[9] = -2.5 * badness   # V10
            v[11] = -3.0 * badness  # V12
            v[13] = -4.0 * badness  # V14
            v[16] = -3.5 * badness  # V17

        scaled_time = (time - TIME_MEAN) / TIME_STD
        scaled_amount = (amount - AMOUNT_MEAN) / AMOUNT_STD
        
        input_data = v + [scaled_time, scaled_amount]
        input_array = np.array([input_data])
        
        # الموديل الحقيقي يفكر ويعطي النتيجة
        prediction = int(model.predict(input_array)[0])
        probability = float(model.predict_proba(input_array)[0][1])
        
        return jsonify({
            'status': 'success',
            'prediction': prediction,
            'probability': round(probability * 100, 2)
        })
        
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 400

@app.route('/predict_csv', methods=['POST'])
def predict_csv():
    try:
        if 'file' not in request.files:
            return jsonify({'status': 'error', 'message': 'Dosya bulunamadı'}), 400
            
        file = request.files['file']
        if file and file.filename.endswith('.csv'):
            df = pd.read_csv(file)
            
            if len(df.columns) >= 30:
                if 'Class' in df.columns:
                    X_csv = df.drop('Class', axis=1)
                else:
                    X_csv = df
                
                predictions = model.predict(X_csv)
                df['Tahmin'] = predictions
                fraud_cases = df[df['Tahmin'] == 1].head(50).to_dict(orient='records')
                
                return jsonify({
                    'status': 'success',
                    'total_records': len(df),
                    'fraud_count': int(np.sum(predictions)),
                    'fraud_cases': fraud_cases
                })
            else:
                return jsonify({'status': 'error', 'message': 'Eksik sütun'}), 400
                
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)