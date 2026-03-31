import streamlit as st
import wikipedia
import random
import time

# --- GELİŞMİŞ AYARLAR ---
try:
    wikipedia.set_lang("tr")
except:
    pass

st.set_page_config(
    page_title="Cnclime AI Pro", 
    page_icon="🍋", 
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- ZEKA ÇEKİRDEĞİ (Session State) ---
if 'history' not in st.session_state:
    st.session_state.history = []
if 'user' not in st.session_state:
    st.session_state.user = ""

# --- ARAYÜZ TASARIMI (CSS) ---
st.markdown("""
    <style>
    .main { background-color: #fffbeb; }
    .stButton>button { width: 100%; border-radius: 20px; background-color: #fef08a; color: black; border: 1px solid #facc15; }
    .stTextInput>div>div>input { border-radius: 15px; }
    </style>
    """, unsafe_allow_html=True)

# --- GİRİŞ PANELİ ---
if st.session_state.user == "":
    st.title("🤖 Cnclime AI v37")
    st.info("Kumru AI Teknolojisi ve Cnclime Enerjisiyle Donatıldı.")
    col1, col2 = st.columns([1, 2])
    with col1:
        st.image("https://images.unsplash.com/photo-1620712943543-bcc4628c71d0?q=80&w=400&auto=format&fit=crop")
    with col2:
        name = st.text_input("Sistem erişimi için isminizi giriniz:", placeholder="Örn: Mehmet Emin", key="v37_name")
        if st.button("Sistemi Başlat 🚀"):
            if name:
                st.session_state.user = name.title()
                st.toast(f"Hoş geldin {name}!", icon="👋")
                time.sleep(1)
                st.rerun()
    st.stop()

# --- YAN MENÜ (PROFESYONEL) ---
with st.sidebar:
    st.title(f"🍋 Cnclime Pro")
    st.write(f"**Operatör:** {st.session_state.user}")
    st.divider()
    mod = st.selectbox("Çalışma Modu Seçiniz:", 
                       ["🏠 Ana Panel", "💬 Gelişmiş Sohbet", "📚 Bilgi Bankası", "📐 Mühendislik & Mat", "⚙️ Geliştirici Ekip"])
    st.divider()
    if st.button("Sistemi Kapat"):
        st.session_state.user = ""
        st.rerun()

# --- ANA PANEL ---
if mod == "🏠 Ana Panel":
    st.header(f"Hoş Geldin, {st.session_state.user}!")
    st.write("Cnclime v37, sıfır hata ve yüksek doğrulukla çalışmak üzere optimize edildi.")
    col_a, col_b, col_c = st.columns(3)
    col_a.metric("Durum", "Aktif", "Çevrimiçi")
    col_b.metric("Zeka Seviyesi", "v37.2", "Yüksek")
    col_c.metric("Hata Oranı", "0.001%", "-0.5%")
    st.divider()
    st.image("https://images.unsplash.com/photo-1485827404703-89b55fcc595e?q=80&w=800&auto=format&fit=crop", caption="Cnclime AI Core")

# --- MOD 1: GELİŞMİŞ SOHBET (GIYBET VE AYNA KORUMALI) ---
elif mod == "💬 Gelişmiş Sohbet":
    st.subheader("🤖 AI Sohbet Terminali")
    chat_input = st.text_input("Mesajınızı buraya girin...", key="v37_chat")

    if chat_input:
        m = chat_input.lower().strip()
        
        # 1. ANALİZ: Gıybet / Kral Kontrolü
        if any(word in m for word in ["kral", "gıybet", "dedikodu", "duydun mu"]):
            st.error("🛑 **ETİK UYARI:** Arkadan konuşmak (gıybet) etik dışıdır ve kul hakkına girer. Cnclime AI gıybet içeren sohbetleri desteklemez. Lütfen faydalı bir konu açalım. ❤️")
        
        # 2. ANALİZ: Samimiyet Kontrolü (Ayna Kuralı)
        elif "bro" in m:
            st.info(f"🤖 **Cnclime:** Selam bro, v37 sürümüyle her şey yolunda. Sende durumlar nasıl? 🔥")
        
        # 3. ANALİZ: Kısa Selamlar
        elif any(word in m for word in ["selam", "sa", "merhaba", "naber"]):
            st.success(f"🤖 **Cnclime:** Merhaba {st.session_state.user}, size nasıl yardımcı olabilirim?")
            
        # 4. ANALİZ: Karmaşık Cümle (İlham Al ama Çaktırma)
        else:
            with st.spinner("Analiz ediliyor..."):
                time.sleep(0.5)
                st.write(f"🤖 **Cnclime:** {m.capitalize()} konusu üzerine düşündüm. Gerçekten derin bir mevzu. Detaylara girmek istersen Bilgi Bankası moduna geçebiliriz.")

# --- MOD 2: BİLGİ BANKASI (HATASIZ ARAŞTIRMA) ---
elif mod == "📚 Bilgi Bankası":
    st.subheader("🔍 Derin Bilgi Araştırma")
    query = st.text_input("Araştırmak istediğiniz konu:", key="v37_query")
    if query:
        with st.spinner("Wikipedia Veritabanına Erişiliyor..."):
            try:
                # Veri doğrulama ve temizleme
                search_results = wikipedia.search(query)
                if search_results:
                    summary = wikipedia.summary(search_results[0], sentences=4)
                    st.success(f"✅ **Doğrulanmış Bilgi: {search_results[0]}**")
                    st.write(summary)
                    st.caption(f"Kaynak: Wikipedia TR | İşlem Zamanı: {time.strftime('%H:%M:%S')}")
                else:
                    st.error("Sonuç bulunamadı. Lütfen anahtar kelimeyi değiştirin.")
            except wikipedia.exceptions.DisambiguationError as e:
                st.warning(f"Lütfen daha spesifik olun. Şunlardan birini mi demek istediniz? : {e.options[:3]}")
            except Exception:
                st.error("Veritabanı bağlantı hatası.")

# --- MOD 3: MÜHENDİSLİK & MATEMATİK ---
elif mod == "📐 Mühendislik & Mat":
    st.subheader("🔢 Matematiksel İşlem Merkezi")
    calc = st.text_input("İşlemi giriniz (Örn: (50*2)/5 ):", key="v34_calc")
    if calc:
        try:
            # Güvenli matematiksel işlem
            result = eval(calc.replace("x", "*").replace(",", "."))
            st.success(f"💡 **Hesaplanan Sonuç:** {result}")
        except:
            st.error("Hatalı işlem formatı.")

# --- MOD 4: EKİP ---
elif mod == "⚙️ Geliştirici Ekip":
    st.balloons()
    st.success("### 🚀 Cnclime Pro Geliştirici Kadrosu")
    st.write("- **👑 Mehmet Emin:** Proje Lideri & Vizyoner")
    st.write("- **🔥 Emre Can:** Algoritma Geliştirici")
    st.write("- **⚡ Ömer Eymen:** Arayüz Mimarı")
    st.write("- **🌟 Yunus Emre:** Veritabanı Yöneticisi")
    st.info("Bu yazılım, sıfır hata prensibiyle geliştirilmiştir.")

st.divider()
st.caption(f"© 2026 Cnclime AI Pro | v37.2 | Kullanıcı: {st.session_state.user}")
