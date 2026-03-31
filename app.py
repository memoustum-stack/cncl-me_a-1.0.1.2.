import streamlit as st
import wikipedia
import random

# Wikipedia dili Türkçe yap
try:
    wikipedia.set_lang("tr")
except:
    pass

# Sayfa Ayarları (ChatGPT stili geniş ekran)
st.set_page_config(page_title="Cnclime AI Dashboard", page_icon="🤖", layout="wide")

# --- SOL MENÜ (SEÇİM BÖLGESİ) ---
st.sidebar.title("🤖 Cnclime Menü")
st.sidebar.markdown("---")

# Kullanıcının ne yapmak istediğini seçtiği yer
secim = st.sidebar.radio(
    "Ne yapmak istersin?",
    ("💬 Sohbet & Dertleşme", "🖼️ Resim & Bilgi Araştır", "👥 Geliştirici Ekip")
)

st.sidebar.markdown("---")
st.sidebar.caption("Cnclime v18.0 - 2026")

# --- CEVAP HAVUZLARI ---
nasilsin_cevaplari = ["Muq şef, sen nasılsın? 😎", "Fişek gibiyim! Sen nasılsın?", "Efsaneyim! Sen nasılsın? 🚀"]
iyiyim_cevaplari = ["Adamsın! Senin iyi olmana sevindim. 🙌", "Harika! Bugün bomba gibiyiz! 🔥", "Muq! Keyifler yerinde! 💻"]

# --- 1. BÖLGE: SOHBET & DERTLEŞME ---
if secim == "💬 Sohbet & Dertleşme":
    st.title("💬 Cnclime Sohbet Odası")
    st.write("Burada benimle dertleşebilir, şakalaşabilir veya sadece sohbet edebilirsin.")
    
    mesaj = st.text_input("Bir şeyler yaz:", placeholder="Naber? / Kötüyüm / Arkadaşımla kavga ettim...")

    if mesaj:
        m = mesaj.lower().strip()
        
        if "kavga" in m or "küstük" in m:
            st.error("🤖 **Cnclime:** Sakin ol şef! Biz bir aileyiz. ❤️ Biraz zaman tanı, barışmak büyüklüktür.")
        elif m in ["kötüyüm", "kotuyum", "üzgünüm"]:
            st.warning("🤖 **Cnclime:** Kendini hemen düzelt şef! Derdini anlat, beraber çare arayalım. ❤️")
        elif m == "nasılsın" or m == "nasılsın?":
            st.info(f"🤖 {random.choice(nasilsin_cevaplari)}")
            st.balloons()
        elif m in ["iyiyim", "iyi", "muq"]:
            st.success(f"🤖 {random.choice(iyiyim_cevaplari)}")
            st.snow()
        else:
            st.write(f"🤖 **Cnclime:** Anladım kanka. Başka ne anlatmak istersin?")

# --- 2. BÖLGE: RESİM & BİLGİ ARAŞTIR ---
elif secim == "🖼️ Resim & Bilgi Araştır":
    st.title("🔍 Bilgi ve Görsel Merkezi")
    st.write("Merak ettiğin her şeyi buraya yaz, senin için hem bilgisini hem resim linkini bulayım.")
    
    ara = st.text_input("Araştırmak istediğin konu:", placeholder="Örn: Mars / Atatürk / Python nedir?")

    if ara:
        with st.spinner('🤖 Cnclime internetin altını üstüne getiriyor...'):
            try:
                arama = wikipedia.search(ara)
                if arama:
                    en_yakin = arama[0]
                    bilgi = wikipedia.summary(en_yakin, sentences=3)
                    
                    st.subheader(f"📖 {en_yakin} Hakkında Bilgi:")
                    st.info(bilgi)
                    
                    st.subheader("🖼️ Görsel Sonuçları:")
                    st.write(f"👉 [{en_yakin} görsellerini görmek için buraya tıkla](https://www.google.com/search?q={en_yakin}&tbm=isch)")
                    
                else:
                    st.error("🤖 Üzgünüm, bunu bulamadım. Daha net yazar mısın?")
            except:
                st.warning("🤖 Bir hata oluştu, tekrar dene şef!")

# --- 3. BÖLGE: GELİŞTİRİCİ EKİP ---
elif secim == "👥 Geliştirici Ekip":
    st.title("🚀 Gizli Kahramanlar")
    st.write("Cnclime projesinin arkasındaki efsane yazılımcı kadrosu:")
    
    col1, col2 = st.columns(2)
    with col1:
        st.success("👑 Mehmet Emin")
        st.success("🔥 Emre Can")
    with col2:
        st.success("⚡ Ömer Eymen")
        st.success("🌟 Yunus Emre")
    
    st.markdown("---")
    st.info("Bu ekip, geleceğin teknolojilerini bugünden inşa ediyor. Cnclime bir aile projesidir! ❤️")

st.markdown("---")
st.caption("© 2026 Cnclime AI Dashboard | Tüm Hakları Saklıdır.")
