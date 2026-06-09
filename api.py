from flask import Flask, request, jsonify

app = Flask(__name__)

def predict(data):
    amount = data.get("amount", 0)

    if amount > 1000:
        return "Fraud"
    else:
        return "Not Fraud"

@app.route("/predict", methods=["POST"])
def predict_api():
    data = request.json
    result = predict(data)

    return jsonify({
        "prediction": result
    })

if __name__ == "__main__":
    app.run(debug=True)