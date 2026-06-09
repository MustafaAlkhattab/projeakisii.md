import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import time
from datetime import datetime, timedelta
import streamlit as st
import requests


# ==========================================
# 1. SAYFA YAPILANDIRMASI
# ==========================================
st.set_page_config(
    page_title="Fraud Shield AI | Dolandırıcılık Tespit Sistemi",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)
st.title("💳 Fraud Detection System")

st.write("Enter transaction details:")

amount = st.number_input("Transaction Amount")

if st.button("Predict"):
    data = {
        "amount": amount
    }

    try:
        response = requests.post("http://127.0.0.1:5000/predict", json=data)
        result = response.json()

        st.success(f"Prediction: {result['prediction']}")

    except:
        st.error("API connection error!")
# ==========================================
# 2. KAPSAMLI CSS + ANİMASYONLAR
# ==========================================
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');

/* === KEYFRAME ANİMASYONLAR === */
@keyframes fadeInUp {
  from { opacity: 0; transform: translateY(24px); }
  to   { opacity: 1; transform: translateY(0); }
}
@keyframes fadeIn {
  from { opacity: 0; }
  to   { opacity: 1; }
}
@keyframes slideInLeft {
  from { opacity: 0; transform: translateX(-30px); }
  to   { opacity: 1; transform: translateX(0); }
}
@keyframes slideInRight {
  from { opacity: 0; transform: translateX(30px); }
  to   { opacity: 1; transform: translateX(0); }
}
@keyframes pulse {
  0%,100% { box-shadow: 0 0 0 0 rgba(239,68,68,0.35); }
  50%     { box-shadow: 0 0 0 14px rgba(239,68,68,0); }
}
@keyframes safePulse {
  0%,100% { box-shadow: 0 0 0 0 rgba(16,185,129,0.3); }
  50%     { box-shadow: 0 0 0 14px rgba(16,185,129,0); }
}
@keyframes shimmer {
  0%   { background-position: -400% 0; }
  100% { background-position: 400% 0; }
}
@keyframes glowBorder {
  0%,100% { border-color: rgba(37,99,235,0.25); }
  50%     { border-color: rgba(37,99,235,0.7); }
}
@keyframes popIn {
  0%  { transform: scale(0.75); opacity: 0; }
  70% { transform: scale(1.04); }
  100%{ transform: scale(1);    opacity: 1; }
}
@keyframes spin {
  from { transform: rotate(0deg); }
  to   { transform: rotate(360deg); }
}
@keyframes float {
  0%,100% { transform: translateY(0px); }
  50%     { transform: translateY(-6px); }
}

/* === GENEL === */
* { font-family: 'Inter', sans-serif; }
#MainMenu, footer, header { visibility: hidden; }
.block-container { padding-top: 1.5rem !important; padding-bottom: 2rem !important; }

/* === SIDEBAR === */
[data-testid="stSidebar"] {
  background: linear-gradient(180deg, #060d1f 0%, #0d1b3e 45%, #060d1f 100%) !important;
  border-right: 1px solid rgba(37,99,235,0.18);
}
[data-testid="stSidebar"] > div { animation: slideInLeft 0.45s cubic-bezier(0.16,1,0.3,1); }
[data-testid="stSidebar"] .stButton>button {
  background: transparent;
  color: rgba(255,255,255,0.7);
  border: 1px solid rgba(255,255,255,0.06);
  border-radius: 10px;
  text-align: left;
  transition: all 0.22s ease;
  font-size: 13.5px;
  font-weight: 400;
  padding: 9px 14px;
  margin-bottom: 3px;
  width: 100%;
}
[data-testid="stSidebar"] .stButton>button:hover {
  background: rgba(37,99,235,0.18) !important;
  border-color: rgba(37,99,235,0.45) !important;
  color: #fff !important;
  transform: translateX(5px);
  box-shadow: 0 4px 16px rgba(37,99,235,0.15);
}
[data-testid="stSidebar"] p,
[data-testid="stSidebar"] span,
[data-testid="stSidebar"] label { color: rgba(255,255,255,0.65) !important; }
[data-testid="stSidebar"] h1,
[data-testid="stSidebar"] h2,
[data-testid="stSidebar"] h3 { color: #fff !important; }
[data-testid="stSidebar"] hr { border-color: rgba(255,255,255,0.08) !important; }

/* === BUTONLAR === */
.stButton>button {
  border-radius: 10px;
  font-weight: 500;
  letter-spacing: 0.2px;
  transition: all 0.22s ease;
}
.stButton>button:hover {
  transform: translateY(-2px);
  box-shadow: 0 8px 22px rgba(0,0,0,0.18);
}
button[kind="primary"] {
  background: linear-gradient(135deg,#2563EB,#7C3AED) !important;
  border: none !important;
  color: white !important;
  font-weight: 600 !important;
}
button[kind="primary"]:hover {
  background: linear-gradient(135deg,#1d4ed8,#6d28d9) !important;
  box-shadow: 0 8px 24px rgba(37,99,235,0.35) !important;
}

/* === METRİK KARTLARI === */
div[data-testid="metric-container"] {
  background: rgba(37,99,235,0.06);
  border: 1px solid rgba(37,99,235,0.18);
  border-radius: 14px;
  padding: 18px 22px;
  transition: all 0.28s ease;
  animation: fadeInUp 0.5s ease-out;
}
div[data-testid="metric-container"]:hover {
  border-color: rgba(37,99,235,0.45);
  transform: translateY(-3px);
  box-shadow: 0 10px 28px rgba(37,99,235,0.12);
}

/* === INPUT ALANLARI === */
.stTextInput>div>div>input {
  border-radius: 10px !important;
  transition: all 0.2s ease !important;
  font-size: 14px !important;
}
.stTextInput>div>div>input:focus {
  border-color: #2563EB !important;
  box-shadow: 0 0 0 3px rgba(37,99,235,0.12) !important;
}
.stSelectbox>div>div,
.stSlider>div { border-radius: 10px !important; }

/* === TABS === */
.stTabs [data-baseweb="tab-list"] {
  background: transparent;
  border-bottom: 1px solid rgba(255,255,255,0.08);
  gap: 4px;
}
.stTabs [data-baseweb="tab"] {
  border-radius: 10px 10px 0 0;
  padding: 10px 22px;
  font-size: 13.5px;
  font-weight: 500;
  transition: all 0.2s;
}

/* === PROGRESS BAR === */
.stProgress>div>div>div>div {
  border-radius: 20px;
  background: linear-gradient(90deg, #2563EB, #7C3AED) !important;
}

/* === ÖZEL HTML KARTLARI === */
.card {
  border-radius: 16px;
  padding: 22px 26px;
  margin-bottom: 14px;
  animation: fadeInUp 0.45s cubic-bezier(0.16,1,0.3,1);
  transition: all 0.28s ease;
}
.card:hover { transform: translateY(-3px); }

.card-base {
  background: rgba(255,255,255,0.03);
  border: 1px solid rgba(255,255,255,0.08);
}
.card-blue {
  background: rgba(37,99,235,0.07);
  border: 1px solid rgba(37,99,235,0.2);
}
.card-fraud {
  background: rgba(239,68,68,0.07);
  border: 1px solid rgba(239,68,68,0.28);
  animation: pulse 2.2s infinite, fadeInUp 0.45s ease-out;
}
.card-safe {
  background: rgba(16,185,129,0.07);
  border: 1px solid rgba(16,185,129,0.28);
  animation: safePulse 2.5s infinite, popIn 0.5s ease-out;
}
.card-warning {
  background: rgba(245,158,11,0.07);
  border: 1px solid rgba(245,158,11,0.25);
}

.badge {
  display: inline-block;
  padding: 3px 11px;
  border-radius: 20px;
  font-size: 11px;
  font-weight: 600;
  letter-spacing: 0.6px;
  text-transform: uppercase;
}
.badge-fraud { background:rgba(239,68,68,0.15); color:#f87171; border:1px solid rgba(239,68,68,0.3); }
.badge-safe  { background:rgba(16,185,129,0.15); color:#34d399; border:1px solid rgba(16,185,129,0.3); }
.badge-warn  { background:rgba(245,158,11,0.15); color:#fbbf24; border:1px solid rgba(245,158,11,0.3); }
.badge-blue  { background:rgba(37,99,235,0.15);  color:#60a5fa; border:1px solid rgba(37,99,235,0.3); }

.page-title {
  font-size: 26px;
  font-weight: 700;
  letter-spacing: -0.5px;
  animation: fadeInUp 0.4s ease-out;
  margin-bottom: 4px;
}
.page-subtitle {
  font-size: 13.5px;
  opacity: 0.55;
  animation: fadeInUp 0.5s ease-out;
  margin-bottom: 20px;
}

.stat-big {
  font-size: 30px;
  font-weight: 800;
  letter-spacing: -1px;
  animation: popIn 0.5s ease-out;
}
.stat-label {
  font-size: 12px;
  font-weight: 500;
  opacity: 0.55;
  text-transform: uppercase;
  letter-spacing: 0.8px;
}

.progress-track {
  background: rgba(255,255,255,0.07);
  border-radius: 20px;
  height: 7px;
  overflow: hidden;
  margin-top: 8px;
}
.progress-fill {
  height: 100%;
  border-radius: 20px;
  transition: width 1.2s cubic-bezier(0.16,1,0.3,1);
}

.shimmer-loader {
  background: linear-gradient(90deg,
    rgba(255,255,255,0.02) 0%,
    rgba(255,255,255,0.07) 50%,
    rgba(255,255,255,0.02) 100%);
  background-size: 400% 100%;
  animation: shimmer 1.6s infinite;
  border-radius: 10px;
  height: 54px;
}

.login-card {
  background: rgba(13,27,62,0.6);
  backdrop-filter: blur(20px);
  border: 1px solid rgba(37,99,235,0.2);
  border-radius: 20px;
  padding: 40px 36px;
  animation: glowBorder 3s ease-in-out infinite, fadeIn 0.6s ease-out;
  box-shadow: 0 24px 60px rgba(0,0,0,0.4), inset 0 1px 0 rgba(255,255,255,0.05);
}

.logo-icon {
  font-size: 48px;
  animation: float 3s ease-in-out infinite;
  display: block;
  text-align: center;
}

.divider-custom {
  border: none;
  border-top: 1px solid rgba(255,255,255,0.07);
  margin: 16px 0;
}

.sidebar-section-label {
  font-size: 10.5px;
  font-weight: 600;
  letter-spacing: 1.2px;
  text-transform: uppercase;
  opacity: 0.35;
  padding: 4px 4px 8px;
}

.table-row {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 11px 0;
  border-bottom: 1px solid rgba(255,255,255,0.05);
  font-size: 13.5px;
  animation: fadeIn 0.4s ease-out;
  transition: background 0.2s;
}
.table-row:hover { background: rgba(255,255,255,0.03); border-radius: 8px; padding-left: 8px; }

/* toggle ve alert renkleri */
.stAlert { border-radius: 12px !important; }
.stSuccess { border-radius: 12px !important; }
.stWarning { border-radius: 12px !important; }
</style>
""", unsafe_allow_html=True)

# ==========================================
# 3. SESSION STATE
# ==========================================
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False
if 'current_page' not in st.session_state:
    st.session_state.current_page = "Ana Menü"
if 'analysis_done' not in st.session_state:
    st.session_state.analysis_done = False

def navigate(page_name):
    st.session_state.current_page = page_name

# ==========================================
# 4. GİRİŞ SAYFASI (Login Screen)
# ==========================================
if not st.session_state.logged_in:
    col1, col2, col3 = st.columns([1, 1.2, 1])
    with col2:
        st.markdown("""
        <div class="login-card">
          <span class="logo-icon">🛡️</span>
          <h2 style="text-align:center; font-size:22px; font-weight:700; margin:16px 0 4px; letter-spacing:-0.5px;">
            Fraud Shield AI
          </h2>
          <p style="text-align:center; opacity:0.45; font-size:13px; margin-bottom:28px;">
            Yapay Zeka Destekli Dolandırıcılık Tespit Sistemi
          </p>
        </div>
        """, unsafe_allow_html=True)

        # Spacer için boş div kapatma - formu login_card'ın dışında tutuyoruz
        email    = st.text_input("📧  E-posta", placeholder="kullanici@firat.edu.tr")
        password = st.text_input("🔒  Şifre",  type="password", placeholder="••••••••")

        c1, c2 = st.columns(2)
        with c1:
            if st.button("🚀  Giriş Yap", use_container_width=True, type="primary"):
                with st.spinner("Kimlik doğrulanıyor..."):
                    time.sleep(0.9)
                st.session_state.logged_in = True
                st.rerun()
        with c2:
            st.button("📝  Kayıt Ol", use_container_width=True)

        st.markdown("""
        <p style="text-align:center; font-size:12px; opacity:0.4; margin-top:14px;">
          <a href="#" style="color:inherit;">Şifremi Unuttum</a>
          &nbsp;·&nbsp;
          Fırat Üniversitesi · 2025-2026
        </p>
        """, unsafe_allow_html=True)

# ==========================================
# 5. ANA UYGULAMA
# ==========================================
else:
    # ─── SİDEBAR ───────────────────────────────
    with st.sidebar:
        st.markdown("""
        <div style="display:flex;align-items:center;gap:12px;padding:8px 4px 20px;
             border-bottom:1px solid rgba(255,255,255,0.07);margin-bottom:18px;">
          <div style="width:42px;height:42px;border-radius:12px;
               background:linear-gradient(135deg,#2563EB,#7C3AED);
               display:flex;align-items:center;justify-content:center;
               font-size:20px;flex-shrink:0;">🛡️</div>
          <div>
            <div style="color:#fff;font-weight:700;font-size:15px;line-height:1.2;">Fraud Shield</div>
            <div style="color:rgba(255,255,255,0.4);font-size:11px;">Yapay Zeka Dedektifleri</div>
          </div>
        </div>
        """, unsafe_allow_html=True)

        # Kullanıcı profili
        st.markdown("""
        <div style="display:flex;align-items:center;gap:10px;
             background:rgba(37,99,235,0.12);border:1px solid rgba(37,99,235,0.2);
             border-radius:12px;padding:11px 13px;margin-bottom:18px;
             animation:fadeIn 0.5s ease-out;">
          <div style="width:36px;height:36px;border-radius:50%;
               background:linear-gradient(135deg,#2563EB,#7C3AED);
               display:flex;align-items:center;justify-content:center;
               color:#fff;font-weight:700;font-size:14px;flex-shrink:0;">MA</div>
          <div>
            <div style="color:#fff;font-weight:600;font-size:13px;">Mustafa Alkhattab</div>
            <div style="color:rgba(255,255,255,0.4);font-size:11px;">Veri Analisti</div>
          </div>
        </div>
        """, unsafe_allow_html=True)

        st.markdown('<div class="sidebar-section-label">Navigasyon</div>', unsafe_allow_html=True)
        if st.button("🏠  Ana Menü",          use_container_width=True): navigate("Ana Menü")
        if st.button("🔬  Yeni Analiz",        use_container_width=True): navigate("Yeni Analiz")
        if st.button("📊  Analiz Sonuçları",   use_container_width=True): navigate("Aktif Raporlar")
        if st.button("🔍  İşlem Detayları",    use_container_width=True): navigate("Tahmin Detayları")
        if st.button("⚙️  Ayarlar",             use_container_width=True): navigate("Ayarlar")

        st.markdown("<hr class='divider-custom'>", unsafe_allow_html=True)

        # Model Durumu
        st.markdown('<div class="sidebar-section-label">Model Durumu</div>', unsafe_allow_html=True)
        st.markdown("""
        <div style="background:rgba(16,185,129,0.1);border:1px solid rgba(16,185,129,0.25);
             border-radius:10px;padding:12px 14px;animation:fadeIn 0.6s ease-out;">
          <div style="display:flex;align-items:center;gap:8px;margin-bottom:10px;">
            <div style="width:8px;height:8px;border-radius:50%;background:#10B981;
                 box-shadow:0 0 0 3px rgba(16,185,129,0.25);animation:safePulse 2s infinite;"></div>
            <span style="color:#34d399;font-size:12.5px;font-weight:600;">Aktif · Hazır</span>
          </div>
          <div style="font-size:11.5px;opacity:0.5;margin-bottom:6px;">Doğruluk Skoru</div>
          <div style="font-size:20px;font-weight:800;color:#34d399;letter-spacing:-0.5px;">%96.8</div>
          <div style="background:rgba(255,255,255,0.06);border-radius:20px;height:4px;margin-top:8px;">
            <div style="width:96.8%;height:100%;border-radius:20px;background:#10B981;"></div>
          </div>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)
        if st.button("🚪  Çıkış Yap", use_container_width=True):
            st.session_state.logged_in = False
            st.rerun()

    # ─── ANA MENÜ ─────────────────────────────────────────────────
    if st.session_state.current_page == "Ana Menü":
        st.markdown('<div class="page-title">🏠 Dashboard</div>', unsafe_allow_html=True)
        st.markdown('<div class="page-subtitle">Yapay Zeka analiz özetleri ve sistem metrikleri</div>', unsafe_allow_html=True)

        # Metrik satırı
        m1, m2, m3, m4 = st.columns(4)
        m1.metric("💳 Toplam İşlem",      "12.450",  "↑ Yükselişte")
        m2.metric("🚨 Şüpheli İşlem",     "342",     "-12% İyileşme",  delta_color="inverse")
        m3.metric("💰 Önlenen Zarar",      "₺1.2M",  "+₺50K Bu Ay")
        m4.metric("🎯 Model Doğruluğu",   "%96.8",   "+0.4%")

        st.markdown("<br>", unsafe_allow_html=True)

        # Grafikler
        col_g1, col_g2 = st.columns([2.2, 1])

        with col_g1:
            st.markdown("""
            <div class="card card-blue" style="padding:18px 22px 8px;">
              <div style="font-size:15px;font-weight:600;margin-bottom:4px;">📈 Son 7 Günlük İşlem Hacmi</div>
              <div style="font-size:12px;opacity:0.45;">Normal ve şüpheli işlem karşılaştırması</div>
            </div>
            """, unsafe_allow_html=True)

            dates       = [datetime.today() - timedelta(days=i) for i in range(7)][::-1]
            normal_tx   = np.random.randint(1100, 2100, 7)
            fraud_tx    = np.random.randint(12, 55, 7)
            df_trend    = pd.DataFrame({'Tarih': dates, 'Normal İşlem': normal_tx, 'Şüpheli İşlem': fraud_tx})

            fig_line = px.line(
                df_trend, x='Tarih', y=['Normal İşlem', 'Şüpheli İşlem'],
                color_discrete_sequence=['#10B981', '#EF4444'],
                markers=True
            )
            fig_line.update_layout(
                paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)',
                margin=dict(l=0, r=0, t=12, b=0), legend_title_text='',
                xaxis=dict(showgrid=False, color='rgba(255,255,255,0.35)'),
                yaxis=dict(gridcolor='rgba(255,255,255,0.05)', color='rgba(255,255,255,0.35)'),
                font_color='rgba(255,255,255,0.6)',
                legend=dict(bgcolor='rgba(0,0,0,0)')
            )
            fig_line.update_traces(line_width=2.5)
            st.plotly_chart(fig_line, use_container_width=True)

        with col_g2:
            st.markdown("""
            <div class="card card-blue" style="padding:18px 22px 8px;">
              <div style="font-size:15px;font-weight:600;margin-bottom:4px;">🛡️ Risk Dağılımı</div>
              <div style="font-size:12px;opacity:0.45;">İşlem güvenlik kategorileri</div>
            </div>
            """, unsafe_allow_html=True)

            fig_pie = px.pie(
                values=[94, 4, 2],
                names=['Güvenli', 'İncelemede', 'Dolandırıcılık'],
                hole=0.52,
                color_discrete_sequence=['#10B981', '#F59E0B', '#EF4444']
            )
            fig_pie.update_traces(textposition='inside', textinfo='percent+label',
                                  textfont_size=12, marker_line_width=0)
            fig_pie.update_layout(
                paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)',
                margin=dict(l=0, r=0, t=12, b=0),
                showlegend=False, font_color='rgba(255,255,255,0.7)'
            )
            st.plotly_chart(fig_pie, use_container_width=True)

        # Son İşlemler tablosu
        st.markdown("""
        <div class="card card-base" style="margin-top:8px;">
          <div style="font-size:15px;font-weight:600;margin-bottom:16px;">⚡ Son İşlemler</div>
          <div class="table-row">
            <span>#TRX-9982</span>
            <span>₺15.000</span>
            <span>İstanbul</span>
            <span><span class="badge badge-fraud">FRAUD</span></span>
            <span style="opacity:0.45;font-size:12px;">02:45</span>
          </div>
          <div class="table-row">
            <span>#TRX-9901</span>
            <span>₺8.450</span>
            <span>Ankara</span>
            <span><span class="badge badge-warn">İNCELEME</span></span>
            <span style="opacity:0.45;font-size:12px;">01:18</span>
          </div>
          <div class="table-row">
            <span>#TRX-9845</span>
            <span>₺2.300</span>
            <span>İzmir</span>
            <span><span class="badge badge-safe">GÜVENLİ</span></span>
            <span style="opacity:0.45;font-size:12px;">00:54</span>
          </div>
          <div class="table-row">
            <span>#TRX-9810</span>
            <span>₺550</span>
            <span>Bursa</span>
            <span><span class="badge badge-safe">GÜVENLİ</span></span>
            <span style="opacity:0.45;font-size:12px;">00:31</span>
          </div>
          <div class="table-row" style="border-bottom:none;">
            <span>#TRX-9790</span>
            <span>₺45.000</span>
            <span>Yurt Dışı</span>
            <span><span class="badge badge-fraud">FRAUD</span></span>
            <span style="opacity:0.45;font-size:12px;">dün</span>
          </div>
        </div>
        """, unsafe_allow_html=True)

    # ─── YENİ ANALİZ ───────────────────────────────────────────────
    elif st.session_state.current_page == "Yeni Analiz":
        st.markdown('<div class="page-title">🔬 Yeni Analiz</div>', unsafe_allow_html=True)
        st.markdown('<div class="page-subtitle">Veri seti yükleyin ve makine öğrenmesi modelini yapılandırın</div>', unsafe_allow_html=True)

        tab1, tab2 = st.tabs(["📁  Dosya Yükle", "🗄️  Veritabanı Bağlantısı"])

        with tab1:
            uploaded_file = st.file_uploader(
                "Kredi kartı işlem veri setini yükleyin (.csv veya .json)",
                type=["csv", "json"]
            )

            if uploaded_file:
                st.success(f"✅  **{uploaded_file.name}** başarıyla yüklendi!")
                st.markdown("<br>", unsafe_allow_html=True)

                st.markdown("""
                <div class="card card-blue">
                  <div style="font-size:15px;font-weight:600;margin-bottom:16px;">⚙️ Analiz Konfigürasyonu</div>
                </div>
                """, unsafe_allow_html=True)

                col1, col2 = st.columns(2)
                with col1:
                    hedef = st.selectbox("1. Analiz Hedefi",
                        ["Tahmin (Prediction)", "Sınıflandırma (Classification)"])
                    model = st.selectbox("3. Kullanılacak Model",
                        ["Lojistik Regresyon", "Karar Ağacı (Decision Tree)", "Random Forest"])
                with col2:
                    sutun = st.selectbox("2. Hedef Sütun",
                        ["Is_Fraud", "Class", "Risk_Score"])
                    split = st.slider("4. Eğitim / Test Ayrımı (%)", 50, 90, 80)

                st.markdown(f"""
                <div class="card card-base" style="margin-top:12px;">
                  <div style="font-size:13px;opacity:0.55;margin-bottom:10px;">Yapılandırma Özeti</div>
                  <div style="display:grid;grid-template-columns:1fr 1fr;gap:10px;font-size:13.5px;">
                    <div>📌 Hedef: <strong>{hedef}</strong></div>
                    <div>📌 Sütun: <strong>{sutun}</strong></div>
                    <div>🤖 Model: <strong>{model}</strong></div>
                    <div>📐 Eğitim: <strong>%{split} / Test: %{100-split}</strong></div>
                  </div>
                </div>
                """, unsafe_allow_html=True)

                if st.button("🚀  Makine Öğrenmesi Analizini Başlat",
                             type="primary", use_container_width=True):
                    progress_text = "⏳  Veriler ön işleniyor..."
                    bar = st.progress(0, text=progress_text)
                    for i in range(100):
                        time.sleep(0.022)
                        if   i == 30: bar.progress(i+1, text="🔧  Özellikler çıkarılıyor (Feature Extraction)...")
                        elif i == 55: bar.progress(i+1, text="🤖  Model eğitiliyor (Model Training)...")
                        elif i == 80: bar.progress(i+1, text="📊  Sonuçlar değerlendiriliyor...")
                        elif i == 95: bar.progress(i+1, text="✅  Tamamlanıyor...")
                        else:         bar.progress(i+1)
                    st.balloons()
                    st.success("🎉  Analiz başarıyla tamamlandı! Sonuçlar hazır.")
                    st.session_state.analysis_done = True
                    time.sleep(1.2)
                    navigate("Aktif Raporlar")
                    st.rerun()
            else:
                st.markdown("""
                <div class="card card-base" style="text-align:center;padding:40px 20px;">
                  <div style="font-size:36px;margin-bottom:12px;animation:float 3s ease-in-out infinite;display:block;">📁</div>
                  <div style="font-size:15px;font-weight:500;margin-bottom:6px;">Veri seti seçin</div>
                  <div style="font-size:13px;opacity:0.4;">Desteklenen formatlar: .csv · .json</div>
                </div>
                """, unsafe_allow_html=True)

        with tab2:
            st.markdown("""
            <div class="card card-base" style="text-align:center;padding:36px;">
              <div style="font-size:32px;margin-bottom:12px;">🗄️</div>
              <div style="font-size:15px;font-weight:500;margin-bottom:6px;">Veritabanı Bağlantısı</div>
              <div style="font-size:13px;opacity:0.4;">Bu özellik yakında eklenecektir.</div>
            </div>
            """, unsafe_allow_html=True)
            st.text_input("Host", placeholder="localhost:5432")
            st.text_input("Veritabanı Adı", placeholder="fraud_db")
            st.button("🔌  Bağlan", use_container_width=True, type="primary")

    # ─── AKTİF RAPORLAR ────────────────────────────────────────────
    elif st.session_state.current_page == "Aktif Raporlar":
        st.markdown('<div class="page-title">📊 Analiz Sonuçları</div>', unsafe_allow_html=True)
        st.markdown('<div class="page-subtitle">Makine öğrenmesi modeli tahmin ve değerlendirme paneli</div>', unsafe_allow_html=True)

        c1, c2, c3 = st.columns(3)
        c1.metric("📋 Tahmin Edilen İşlem", "8.432")
        c2.metric("🎯 Ortalama Güven Skoru", "%92.5")
        c3.metric("🚨 Tespit Edilen Şüpheli", "142")

        st.markdown("<br>", unsafe_allow_html=True)

        col1, col2 = st.columns([1.1, 1])

        with col1:
            st.markdown("""
            <div class="card card-blue" style="padding-bottom:8px;">
              <div style="font-size:15px;font-weight:600;margin-bottom:4px;">🔍 Özellik Önemi (Feature Importance)</div>
              <div style="font-size:12px;opacity:0.45;">Hangi faktörler tahmine en çok katkı sağlıyor?</div>
            </div>
            """, unsafe_allow_html=True)

            features = pd.DataFrame({
                'Özellik':      ['İşlem Tutarı', 'Zaman (Time)', 'V14', 'V4', 'Konum'],
                'Etki Değeri':  [93, 75, 62, 55, 27]
            })
            fig_bar = px.bar(
                features, x='Etki Değeri', y='Özellik',
                orientation='h', color='Etki Değeri',
                color_continuous_scale=['#3B82F6', '#EF4444'],
                text='Etki Değeri'
            )
            fig_bar.update_traces(texttemplate='%{text}%', textposition='outside')
            fig_bar.update_layout(
                paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)',
                margin=dict(l=0, r=50, t=12, b=0),
                yaxis={'categoryorder': 'total ascending'},
                xaxis=dict(showgrid=False, visible=False),
                yaxis2=dict(color='rgba(255,255,255,0.4)'),
                coloraxis_showscale=False,
                font_color='rgba(255,255,255,0.6)',
                height=280
            )
            st.plotly_chart(fig_bar, use_container_width=True)

            # Model karşılaştırması
            st.markdown("""
            <div class="card card-base" style="margin-top:4px;">
              <div style="font-size:14px;font-weight:600;margin-bottom:14px;">🤖 Model Karşılaştırması</div>
              <div style="margin-bottom:12px;">
                <div style="display:flex;justify-content:space-between;font-size:13px;margin-bottom:5px;">
                  <span>Lojistik Regresyon</span><span style="opacity:0.55;">%94.2</span>
                </div>
                <div class="progress-track"><div class="progress-fill" style="width:94.2%;background:linear-gradient(90deg,#2563EB,#7C3AED);"></div></div>
              </div>
              <div>
                <div style="display:flex;justify-content:space-between;font-size:13px;margin-bottom:5px;">
                  <span>Karar Ağacı</span><span style="opacity:0.55;">%91.7</span>
                </div>
                <div class="progress-track"><div class="progress-fill" style="width:91.7%;background:linear-gradient(90deg,#10B981,#059669);"></div></div>
              </div>
            </div>
            """, unsafe_allow_html=True)

        with col2:
            st.markdown("""
            <div class="card card-fraud" style="margin-bottom:14px;">
              <div style="font-size:15px;font-weight:600;margin-bottom:14px;">🚨 Acil İnceleme Gerekli</div>
            """, unsafe_allow_html=True)

            suspicious = [
                ("#TRX-9982", "₺15.000", "%98", "badge-fraud",  "Kritik"),
                ("#TRX-9901", "₺8.450",  "%94", "badge-fraud",  "Yüksek"),
                ("#TRX-8732", "₺12.000", "%89", "badge-warn",   "Yüksek"),
                ("#TRX-1123", "₺45.000", "%85", "badge-warn",   "Orta"),
            ]
            rows = ""
            for tid, amt, risk, cls, durum in suspicious:
                rows += f"""
                <div style="display:flex;align-items:center;justify-content:space-between;
                     padding:9px 0;border-bottom:1px solid rgba(255,255,255,0.05);font-size:13px;">
                  <span style="font-weight:500;">{tid}</span>
                  <span style="opacity:0.7;">{amt}</span>
                  <span><span class="badge {cls}">{risk}</span></span>
                </div>"""
            st.markdown(rows + "</div>", unsafe_allow_html=True)

            if st.button("🔍  Tüm Detayları Görüntüle", use_container_width=True, type="primary"):
                navigate("Tahmin Detayları")
                st.rerun()

            # Confusion Matrix
            st.markdown("""
            <div class="card card-base" style="margin-top:14px;">
              <div style="font-size:14px;font-weight:600;margin-bottom:14px;">📐 Confusion Matrix</div>
              <div style="display:grid;grid-template-columns:1fr 1fr;gap:8px;text-align:center;">
                <div style="background:rgba(16,185,129,0.12);border:1px solid rgba(16,185,129,0.2);
                     border-radius:10px;padding:14px;">
                  <div style="font-size:22px;font-weight:800;color:#34d399;">7.940</div>
                  <div style="font-size:11px;opacity:0.5;margin-top:3px;">True Negative</div>
                </div>
                <div style="background:rgba(239,68,68,0.1);border:1px solid rgba(239,68,68,0.2);
                     border-radius:10px;padding:14px;">
                  <div style="font-size:22px;font-weight:800;color:#f87171;">44</div>
                  <div style="font-size:11px;opacity:0.5;margin-top:3px;">False Positive</div>
                </div>
                <div style="background:rgba(245,158,11,0.1);border:1px solid rgba(245,158,11,0.2);
                     border-radius:10px;padding:14px;">
                  <div style="font-size:22px;font-weight:800;color:#fbbf24;">18</div>
                  <div style="font-size:11px;opacity:0.5;margin-top:3px;">False Negative</div>
                </div>
                <div style="background:rgba(16,185,129,0.12);border:1px solid rgba(16,185,129,0.2);
                     border-radius:10px;padding:14px;">
                  <div style="font-size:22px;font-weight:800;color:#34d399;">430</div>
                  <div style="font-size:11px;opacity:0.5;margin-top:3px;">True Positive</div>
                </div>
              </div>
            </div>
            """, unsafe_allow_html=True)

    # ─── TAHMİN DETAYLARI ─────────────────────────────────────────
    elif st.session_state.current_page == "Tahmin Detayları":
        st.markdown('<div class="page-title">🔍 İşlem Detay İncelemesi</div>', unsafe_allow_html=True)
        st.markdown('<div class="page-subtitle">Yapay zeka kararı ve işlem analizi</div>', unsafe_allow_html=True)

        st.markdown("""
        <div class="card card-fraud">
          <div style="display:flex;align-items:center;gap:10px;margin-bottom:4px;">
            <span style="font-size:22px;">🚨</span>
            <div>
              <div style="font-size:16px;font-weight:700;color:#f87171;">Kritik Uyarı</div>
              <div style="font-size:13px;opacity:0.6;">Bu işlem yapay zeka tarafından <strong>%98 dolandırıcılık riski</strong> ile işaretlendi.</div>
            </div>
            <span class="badge badge-fraud" style="margin-left:auto;">KRİTİK</span>
          </div>
        </div>
        """, unsafe_allow_html=True)

        col_d1, col_d2 = st.columns(2)

        with col_d1:
            st.markdown("""
            <div class="card card-base">
              <div style="font-size:15px;font-weight:600;margin-bottom:16px;">💳 İşlem Kartı</div>
              <div class="table-row">
                <span style="opacity:0.5;">İşlem ID</span>
                <span style="font-weight:600;">#TRX-9982</span>
              </div>
              <div class="table-row">
                <span style="opacity:0.5;">Tutar</span>
                <span style="font-weight:700;color:#f87171;">₺15.000</span>
              </div>
              <div class="table-row">
                <span style="opacity:0.5;">Konum</span>
                <span>İstanbul / Türkiye</span>
              </div>
              <div class="table-row">
                <span style="opacity:0.5;">Tarih & Saat</span>
                <span>15/05/2026 · 02:45</span>
              </div>
              <div class="table-row">
                <span style="opacity:0.5;">IP Adresi</span>
                <span style="color:#fbbf24;">Bilinmeyen (VPN?)</span>
              </div>
              <div class="table-row" style="border-bottom:none;">
                <span style="opacity:0.5;">İşlem Türü</span>
                <span>Online Alışveriş</span>
              </div>
            </div>
            """, unsafe_allow_html=True)

            # Risk faktörleri
            st.markdown("""
            <div class="card card-base" style="margin-top:14px;">
              <div style="font-size:14px;font-weight:600;margin-bottom:14px;">⚠️ Risk Faktörleri</div>
              <div style="margin-bottom:10px;">
                <div style="display:flex;justify-content:space-between;font-size:13px;margin-bottom:5px;">
                  <span>Olağandışı Tutar</span><span style="color:#f87171;font-weight:600;">Yüksek</span>
                </div>
                <div class="progress-track"><div class="progress-fill" style="width:88%;background:#EF4444;"></div></div>
              </div>
              <div style="margin-bottom:10px;">
                <div style="display:flex;justify-content:space-between;font-size:13px;margin-bottom:5px;">
                  <span>Gece Saati (02:45)</span><span style="color:#fbbf24;font-weight:600;">Orta</span>
                </div>
                <div class="progress-track"><div class="progress-fill" style="width:60%;background:#F59E0B;"></div></div>
              </div>
              <div>
                <div style="display:flex;justify-content:space-between;font-size:13px;margin-bottom:5px;">
                  <span>Bilinmeyen IP</span><span style="color:#f87171;font-weight:600;">Yüksek</span>
                </div>
                <div class="progress-track"><div class="progress-fill" style="width:82%;background:#EF4444;"></div></div>
              </div>
            </div>
            """, unsafe_allow_html=True)

        with col_d2:
            # Gauge
            fig_gauge = go.Figure(go.Indicator(
                mode="gauge+number+delta",
                value=98,
                number={'suffix': '%', 'font': {'size': 44, 'color': '#EF4444'}},
                title={'text': "Dolandırıcılık Olasılığı", 'font': {'size': 14, 'color': 'rgba(255,255,255,0.6)'}},
                delta={'reference': 50, 'increasing': {'color': '#EF4444'}},
                gauge={
                    'axis': {'range': [0, 100], 'tickcolor': 'rgba(255,255,255,0.2)',
                             'tickfont': {'color': 'rgba(255,255,255,0.4)', 'size': 11}},
                    'bar': {'color': '#EF4444', 'thickness': 0.28},
                    'bgcolor': 'rgba(0,0,0,0)',
                    'borderwidth': 0,
                    'steps': [
                        {'range': [0, 40],  'color': 'rgba(16,185,129,0.15)'},
                        {'range': [40, 70], 'color': 'rgba(245,158,11,0.15)'},
                        {'range': [70, 100],'color': 'rgba(239,68,68,0.2)'}
                    ],
                    'threshold': {'line': {'color': '#f87171', 'width': 3}, 'value': 98}
                }
            ))
            fig_gauge.update_layout(
                paper_bgcolor='rgba(0,0,0,0)',
                margin=dict(l=24, r=24, t=40, b=10),
                height=260, font_color='rgba(255,255,255,0.7)'
            )
            st.markdown('<div class="card card-fraud" style="padding:12px;">', unsafe_allow_html=True)
            st.plotly_chart(fig_gauge, use_container_width=True)
            st.markdown('</div>', unsafe_allow_html=True)

            st.markdown("""
            <div class="card card-base" style="margin-top:14px;">
              <div style="font-size:14px;font-weight:600;margin-bottom:14px;">🤖 Model Kararı</div>
              <div style="display:grid;grid-template-columns:1fr 1fr;gap:10px;text-align:center;">
                <div style="padding:12px;background:rgba(37,99,235,0.08);border-radius:10px;border:1px solid rgba(37,99,235,0.18);">
                  <div style="font-size:18px;font-weight:700;color:#60a5fa;">%92</div>
                  <div style="font-size:11px;opacity:0.5;margin-top:3px;">Güven Skoru</div>
                </div>
                <div style="padding:12px;background:rgba(239,68,68,0.08);border-radius:10px;border:1px solid rgba(239,68,68,0.18);">
                  <div style="font-size:18px;font-weight:700;color:#f87171;">12ms</div>
                  <div style="font-size:11px;opacity:0.5;margin-top:3px;">Tahmin Süresi</div>
                </div>
              </div>
              <div style="margin-top:12px;font-size:12px;opacity:0.45;text-align:center;">
                Algoritma: Lojistik Regresyon + Karar Ağacı (Ensemble)
              </div>
            </div>
            """, unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)
        col_a1, col_a2, col_a3 = st.columns(3)
        with col_a1:
            if st.button("✅  Güvenli Olarak Onayla", use_container_width=True):
                st.success("İşlem güvenli olarak veritabanına kaydedildi.")
        with col_a2:
            if st.button("🚫  Dolandırıcılık Olarak İşaretle",
                         use_container_width=True, type="primary"):
                st.error("🔴  Kart bloke edildi ve yetkililer bildirildi!")
        with col_a3:
            if st.button("📞  Müşteriyle İletişime Geç", use_container_width=True):
                st.info("📩  Müşteri bildirim e-postası gönderildi.")

    # ─── AYARLAR ──────────────────────────────────────────────────
    elif st.session_state.current_page == "Ayarlar":
        st.markdown('<div class="page-title">⚙️ Sistem Ayarları</div>', unsafe_allow_html=True)
        st.markdown('<div class="page-subtitle">Hesap, bildirim ve model tercihleri</div>', unsafe_allow_html=True)

        col_s1, col_s2 = st.columns(2)

        with col_s1:
            st.markdown("""
            <div class="card card-blue">
              <div style="font-size:15px;font-weight:600;margin-bottom:14px;">🔔 Bildirim Ayarları</div>
            </div>
            """, unsafe_allow_html=True)
            st.toggle("Şüpheli işlemde e-posta bildirimi",     value=True)
            st.toggle("Haftalık rapor otomatik indir",          value=False)
            st.toggle("Kritik fraud tespitinde SMS gönder",     value=True)
            st.toggle("Dashboard günlük özet bildirimi",        value=False)

            st.markdown("""
            <div class="card card-base" style="margin-top:14px;">
              <div style="font-size:15px;font-weight:600;margin-bottom:14px;">🎨 Görünüm</div>
              <div style="font-size:13px;opacity:0.55;">
                Dark / Light mod için sağ üst köşedeki ⋮ menüsü → Settings → Theme bölümünü kullanın.
              </div>
            </div>
            """, unsafe_allow_html=True)

        with col_s2:
            st.markdown("""
            <div class="card card-blue">
              <div style="font-size:15px;font-weight:600;margin-bottom:14px;">🤖 Model Ayarları</div>
            </div>
            """, unsafe_allow_html=True)
            st.selectbox("Varsayılan Algoritma",
                ["Lojistik Regresyon", "Karar Ağacı (Decision Tree)"])
            st.slider("Fraud Eşik Değeri (%)", 50, 99, 75,
                help="Bu değerin üzerindeki işlemler fraud olarak sınıflandırılır")
            st.slider("Güven Skoru Minimum (%)", 70, 99, 85)
            st.toggle("Ensemble (Çoklu Model) Kullan", value=True)

            st.markdown("""
            <div class="card card-base" style="margin-top:14px;border-color:rgba(239,68,68,0.2);">
              <div style="font-size:14px;font-weight:600;margin-bottom:12px;color:#f87171;">⚠️ Tehlikeli Alan</div>
            </div>
            """, unsafe_allow_html=True)
            if st.button("🗑️  Veritabanı Önbelleğini Temizle", use_container_width=True):
                st.warning("⚠️  Önbellek temizlendi.")
            if st.button("🔄  Model Verilerini Sıfırla", use_container_width=True):
                st.error("❌  Bu işlem model geçmişini siler. Onaylıyor musunuz?")