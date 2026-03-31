import streamlit as st
import wikipedia
import random

# Wikipedia dili Türkçe yap
try:
    wikipedia.set_lang("tr")
except:
    pass

# Sayfa Ayarları
st.set_page_config(page_title="Cnclime AI", page_icon="🤖", layout="wide")

# --- İSİM HAFIZASI SİSTEMİ (Session State) ---
if 'kullanici_adi' not in st.session_state:
    st.session_state.kullanici_adi = ""

# --- GİRİŞ EKRANI (İsim sorma) ---
if st.session_state.kullanici_adi == "":
    st.title("🤖 Cnclime AI'ya Hoş Geldin!")
    st.subheader("Başlamadan önce seni tanımak isterim...")
    isim = st.text_input("Senin ismin ne şef?", placeholder="Buraya ismini yaz ve Enter'a bas...")
    
    if isim:
        st.session_state.kullanici_adi = isim.title()
        st.rerun() # Sayfayı yenileyerek ana menüye geçer
    st.stop() # İsim girilene kadar aşağıyı çalıştırma

# --- ANA PANEL (İsim girildikten sonra burası açılır) ---
k_adi = st.session_state.kullanici_adi

st.sidebar.title(f"👋 Selam, {k_adi}!")
st.sidebar.markdown(f"**Cnclime v19** senin için hazır.")
st.sidebar.markdown("---")

secim = st.sidebar.radio(
    "Nereye gitmek istersin?",
    ("💬 Sohbet & Dertleşme", "🖼️ Resim & Bilgi Araştır", "👥 Geliştirici Ekip")
)

st.sidebar.markdown("---")
if st.sidebar.button("İsmimi Değiştir"):
    st.session_state.kullanici_adi = ""
    st.rerun()

# --- CEVAP HAVUZLARI ---
nasilsin_cevaplari = [
    f"Muq {k_adi}, sen nasılsın? 😎", 
    f"Fişek gibiyim {k_adi}! Piksellerim yanıyor! 🔥", 
    f"Efsaneyim! Seninle konuşmak güzel {k_adi}. 🚀"
]

iyiyim_cevaplari = [
    f"Adamsın {k_adi}! Senin iyi olmana sevindim. 🙌", 
    f"Harika! O zaman bugün bomba gibiyiz {k_adi}! 🔥", 
    f"Muq! Keyifler yerinde {k_adi}! 💻"
]

# --- 1. BÖLGE: SOHBET & DERTLEŞME ---
if secim == "💬 Sohbet & Dertleşme":
    st.title(f"💬 {k_adi} ile Sohbet Odası")
    st.write(f"Merhaba {k_adi}! Bugün nasıl hissediyorsun? Benimle her şeyi paylaşabilirsin.")
    
    mesaj = st.text_input("Bir şeyler yaz:", placeholder="Naber? / Kötüyüm / Arkadaşımla kavga ettim...")

    if mesaj:
        m = mesaj.lower().strip()
        
        if "kavga" in m or "küstük" in m:
            st.error(f"🤖 **Cnclime:** Sakin ol {k_adi}! Biz bir aileyiz. ❤️ Biraz zaman tanı, barışmak büyüklüktür.")
        elif m in ["kötüyüm", "kotuyum", "üzgünüm"]:
            st.warning(f"🤖 **Cnclime:** Kendini hemen düzelt {k_adi}! Derdini anlat, beraber çare arayalım. ❤️")
        elif m == "nasılsın" or m == "nasılsın?":
            st.info(f"🤖 {random.choice(nasilsin_cevaplari)}")
            st.balloons()
        elif m in ["iyiyim", "iyi", "muq"]:
            st.success(f"🤖 {random.choice(iyiyim_cevaplari)}")
            st.snow()
        else:
            st.write(f"🤖 **Cnclime:** Anladım {k_adi}. Başka ne anlatmak istersin?")

# --- 2. BÖLGE: RESİM & BİLGİ ARAŞTIR ---
elif secim == "🖼️ Resim & Bilgi Araştır":
    st.title(f"🔍 Bilgi Merkezi - Hoş geldin {k_adi}")
    st.write("Merak ettiğin konuyu yaz, senin için araştırayım.")
    
    ara = st.text_input("Araştırmak istediğin konu:", placeholder="Örn: Mars / Atatürk / Python nedir?")

    if ara:
        with st.spinner('🤖 Cnclime araştırıyor...'):
            try:
                arama = wikipedia.search(ara)
                if arama:
                    en_yakin = arama[0]
                    bilgi = wikipedia.summary(en_yakin, sentences=3)
                    
                    st.subheader(f"📖 {en_yakin} Hakkında Bilgi:")
                    st.info(bilgi)
                    
                    st.subheader("🖼️ Görsel Sonuçları:")
                    st.write(f"👉 [{en_yakin} görselleri için tıkla](https://www.google.com/search?q={en_yakin}&tbm=isch)")
                else:
                    st.error(f"🤖 Üzgünüm {k_adi}, bunu bulamadım.")
            except:
                st.warning("🤖 Bir hata oluştu şef!")

# --- 3. BÖLGE: GELİŞTİRİCİ EKİP ---
elif secim == "👥 Geliştirici Ekip":
    st.title("🚀 Gizli Kahramanlar")
    st.write(f"{k_adi}, bu efsane yazılımcı kadrosunu tanımanı isterim:")
    
    col1, col2 = st.columns(2)
    with col1:
        st.success("👑 Mehmet Emin")
        st.success("🔥 Emre Can")
    with col2:
        st.success("⚡ Ömer Eymen")
        st.success("🌟 Yunus Emre")
    
    st.info("Cnclime bir aile projesidir! ❤️")

st.markdown("---")
st.caption(f"© 2026 Cnclime AI | Kullanıcı: {k_adi}")
