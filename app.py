import streamlit as st
import wikipedia
import random

# Wikipedia ayarları
try:
    wikipedia.set_lang("tr")
except:
    pass

# Sayfa Konfigürasyonu
st.set_page_config(
    page_title="Cnclime AI", 
    page_icon="🍋", 
    layout="wide"
)

# --- SİSTEM HAFIZASI ---
if 'kullanici_adi' not in st.session_state:
    st.session_state.kullanici_adi = ""

# --- GİRİŞ EKRANI ---
if st.session_state.kullanici_adi == "":
    st.title("🤖 Cnclime AI 🍋")
    st.divider()
    st.image("https://images.unsplash.com/photo-1590502160461-7f9a562dfd8b?q=80&w=400&auto=format&fit=crop", caption="Cnclime: Sapsarı ve Akıllı!", width=350)
    
    st.subheader("Hoş Geldin! Önce ismini öğrenebilir miyim?")
    isim = st.text_input("İsmin nedir şef?", placeholder="Buraya yaz ve Enter'a bas...")
    
    if isim:
        st.session_state.kullanici_adi = isim.title()
        st.rerun()
    st.stop()

k_adi = st.session_state.kullanici_adi

# --- YAN MENÜ (MODLAR) ---
st.sidebar.title(f"👋 Selam {k_adi}! 🍋")
st.sidebar.image("https://images.unsplash.com/photo-1568471120021-9966d540306c?q=80&w=150&auto=format&fit=crop", width=120)
st.sidebar.divider()

# Mod seçimi
mod = st.sidebar.radio(
    "Modlar", 
    ["💬 Sohbet Modu", "🔍 Detaylı Bilgi Araştırma", "👥 Geliştirici Ekip"]
)

st.sidebar.divider()
if st.sidebar.button("🗑️ Çıkış Yap / İsmi Unut"):
    st.session_state.kullanici_adi = ""
    st.rerun()

st.sidebar.caption(f"Cnclime v29.0 - {k_adi} Özel")

# --- ANA EKRAN ---
st.title(f"🍋 Cnclime Dashboard: {mod}")
st.divider()

# --- MOD 1: SOHBET MODU (GİZLİ ARAŞTIRMA) ---
if mod == "💬 Sohbet Modu":
    st.write(f"Merhaba {k_adi}! Ne anlatmak istersin? Bilmediğim bir şey olursa çaktırmadan araştırırım. 😉")
    
    user_input = st.text_input("Mesajını yaz:", placeholder="Naber? / Nasılsın? / Python nedir?")

    if user_input:
        m = user_input.lower().strip()
        
        # Sabit Sohbetler
        if m in ["nasılsın", "nasilsin", "nasılsın?", "nasilsin?"]:
            st.write(f"🤖 **Cnclime:** Muq {k_adi}, sen nasılsın? Ekibim beni her gün daha akıllı yapıyor! 😎")
            st.balloons()
            
        elif "kavga" in m or "küstük" in m:
            st.write(f"🤖 **Cnclime:** Sakin ol {k_adi}! Arkadaşlıkta olur böyle şeyler, biz bir aileyiz. ❤️")

        elif m in ["iyiyim", "iyi", "muq", "harika"]:
            st.write(f"🤖 **Cnclime:** Harika {k_adi}! Senin iyi olmana çok sevindim. 🙌")
            st.snow()

        # Gizli Araştırma (Bilmediği bir şeyse çaktırmadan internete bakar)
        else:
            with st.spinner("..."): 
                try:
                    arama = wikipedia.search(m)
                    if arama:
                        # İnternetten aldığını söylemeden direkt cevabı verir
                        cevap = wikipedia.summary(arama[0], sentences=1)
                        st.write(f"🤖 **Cnclime:** {cevap}")
                    else:
                        st.write(f"🤖 **Cnclime:** {k_adi}, bunu tam anlayamadım ama gerçekten ilginç bir konu!")
                except:
                    st.write(f"🤖 **Cnclime:** {k_adi}, bağlantımda küçük bir sorun oldu. Tekrar yazar mısın?")

# --- MOD 2: DETAYLI BİLGİ ARAŞTIRMA ---
elif mod == "🔍 Detaylı Bilgi Araştırma":
    st.subheader("🔍 Bilgi Merkezi")
    st.write("Burada arattığın her şeyin geniş özetini bulabilirsin.")
    ara = st.text_input("Hangi konuda bilgi istersin?", placeholder="Örn: Uzay, Atatürk, Yazılım...")
    
    if ara:
        with st.spinner("Kütüphaneye bakıyorum..."):
            try:
                bilgi = wikipedia.summary(ara, sentences=3)
                st.info(bilgi)
                st.write(f"🔗 [Resimler ve Kaynaklar için tıkla](https://www.google.com/search?q={ara})")
            except:
                st.error("🤖 Bunu kütüphanemde bulamadım şef.")

# --- MOD 3: GELİŞTİRİCİ EKİP ---
elif mod == "👥 Geliştirici Ekip":
    st.subheader("🚀 Proje Mimarları")
    st.write(f"{k_adi}, bu efsane yazılımı geliştiren kadro:")
    
    c1, c2 = st.columns(2)
    with c1:
        st.success("👑 Mehmet Emin")
        st.success("🔥 Emre Can")
    with c2:
        st.success("⚡ Ömer Eymen")
        st.success("🌟 Yunus Emre")
    
    st.info("Cnclime bir aile projesidir! ❤️")

st.divider()
st.caption(f"© 2026 Cnclime AI | v29 | Kullanıcı: {k_adi}")
