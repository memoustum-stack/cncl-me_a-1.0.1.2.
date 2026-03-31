import streamlit as st
import wikipedia

# Wikipedia ayarları
try:
    wikipedia.set_lang("tr")
except:
    pass

# Sayfa Ayarları (Limon Teması)
st.set_page_config(
    page_title="Cnclime AI v30", 
    page_icon="🍋", 
    layout="wide"
)

# --- SİSTEM HAFIZASI ---
if 'kullanici_adi' not in st.session_state:
    st.session_state.kullanici_adi = ""

# --- GİRİŞ EKRANI ---
if st.session_state.kullanici_adi == "":
    st.title("🤖 Cnclime AI v30 🍋")
    st.divider()
    st.image("https://images.unsplash.com/photo-1590502160461-7f9a562dfd8b?q=80&w=400&auto=format&fit=crop", caption="Sapsarı ve Akıllı!", width=350)
    
    st.subheader("Hoş Geldin! Önce ismini öğrenebilir miyim?")
    isim = st.text_input("İsmin nedir şef?", placeholder="Buraya yaz ve Enter'a bas...", key="login_v30")
    
    if isim:
        st.session_state.kullanici_adi = isim.title()
        st.rerun()
    st.stop()

k_adi = st.session_state.kullanici_adi

# --- YAN MENÜ (MODLAR) ---
st.sidebar.title(f"👋 Selam {k_adi}! 🍋")
st.sidebar.image("https://images.unsplash.com/photo-1568471120021-9966d540306c?q=80&w=150&auto=format&fit=crop", width=120)
st.sidebar.divider()

# İstediğin Modlar
mod = st.sidebar.radio(
    "Modlar", 
    ["💬 Sadece Sohbet", "🔢 Matematik Çözücü", "🔍 Bilgi Araştırma", "👥 Geliştirici Ekip"]
)

st.sidebar.divider()
if st.sidebar.button("🗑️ Çıkış Yap / İsmi Unut"):
    st.session_state.kullanici_adi = ""
    st.rerun()

# --- ANA EKRAN ---
st.title(f"🍋 {mod}")
st.divider()

# --- MOD 1: SADECE SOHBET (ARAŞTIRMA YAPMAZ) ---
if mod == "💬 Sadece Sohbet":
    st.write(f"Selam {k_adi}! Bu modda sadece seninle muhabbet ederim, internette vakit kaybetmem. 😊")
    user_input = st.text_input("Bana bir şeyler yaz:", placeholder="Naber? / Nasılsın?", key="chat_only_v30")

    if user_input:
        m = user_input.lower().strip()
        if "nasılsın" in m:
            st.info(f"🤖 **Cnclime:** Muq {k_adi}, sen nasılsın? Ekibimle yeni özellikler ekliyoruz! 😎")
            st.balloons()
        elif "kavga" in m or "küstük" in m:
            st.warning(f"🤖 **Cnclime:** Sakin ol {k_adi}, biz bir aileyiz! ❤️")
        elif m in ["iyiyim", "iyi", "muq", "harika"]:
            st.success(f"🤖 **Cnclime:** Harika {k_adi}! Keyfin hep yerinde olsun. 🙌")
            st.snow()
        else:
            st.write(f"🤖 **Cnclime:** Seni dinliyorum {k_adi}, anlat bakalım...")

# --- MOD 2: MATEMATİK ÇÖZÜCÜ (ARAŞTIRMA YAPAR) ---
elif mod == "🔢 Matematik Çözücü":
    st.write(f"Sayılarla aran nasıl {k_adi}? Zorlandığın işlemleri yaz, hemen çözeyim! 🧠")
    mat_input = st.text_input("İşlem veya matematik terimi yaz:", placeholder="Örn: 25*4 veya Karekök nedir?", key="math_v30")

    if mat_input:
        with st.spinner("Hesaplanıyor ve araştırılıyor..."):
            # 1. Adım: Önce basit matematik işlemini yapmayı dene
            try:
                # 'x' yerine '*' koyuyoruz ki kod anlasın
                temiz_islem = mat_input.replace("x", "*").replace(",", ".")
                sonuc = eval(temiz_islem)
                st.success(f"🤖 **Cnclime Matematik Sonucu:** **{sonuc}**")
            except:
                # 2. Adım: Eğer işlem değilse internetten araştır
                try:
                    arama = wikipedia.summary(f"Matematik {mat_input}", sentences=2)
                    st.info(f"🤖 **Cnclime Araştırma Sonucu:** \n\n {arama}")
                except:
                    st.error(f"🤖 Üzgünüm {k_adi}, bu matematik sorusunu ne çözebildim ne de bulabildim.")

# --- MOD 3: BİLGİ ARAŞTIRMA ---
elif mod == "🔍 Bilgi Araştırma":
    st.subheader("🔍 Genel Kültür Merkezi")
    ara = st.text_input("Hangi konuda bilgi istersin?", placeholder="Örn: Uzay, Atatürk, İstanbul...", key="info_search_v30")
    if ara:
        with st.spinner("Kütüphaneye bakıyorum..."):
            try:
                bilgi = wikipedia.summary(ara, sentences=3)
                st.info(bilgi)
                st.write(f"🔗 [Daha fazla resim için tıkla](https://www.google.com/search?q={ara})")
            except:
                st.error("🤖 Bunu kütüphanemde bulamadım şef.")

# --- MOD 4: GELİŞTİRİCİ EKİP ---
elif mod == "👥 Geliştirici Ekip":
    st.subheader("🚀 Proje Mimarları")
    st.success("👑 Mehmet Emin | 🔥 Emre Can | ⚡ Ömer Eymen | 🌟 Yunus Emre")
    st.info("Cnclime bir aile projesidir! ❤️")

st.divider()
st.caption(f"© 2026 Cnclime | v30 Matematik Güncellemesi | Kullanıcı: {k_adi}")
