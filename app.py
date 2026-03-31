import streamlit as st
import wikipedia
import random

# Wikipedia ayarları
try:
    wikipedia.set_lang("tr")
except:
    pass

# --- SAYFA AYARLARI ---
st.set_page_config(
    page_title="Cnclime: Bilge Limon v23", 
    page_icon="🍋", 
    layout="wide"
)

# --- SİSTEM HAFIZASI ---
if 'kullanici_adi' not in st.session_state:
    st.session_state.kullanici_adi = ""
if 'bellek' not in st.session_state:
    st.session_state.bellek = {}

# --- GİRİŞ EKRANI ---
if st.session_state.kullanici_adi == "":
    st.title("🤖 Cnclime v23: Bilge Limon 🍋")
    st.image("https://images.unsplash.com/photo-1590502160461-7f9a562dfd8b?q=80&w=600&auto=format&fit=crop", width=300)
    isim = st.text_input("Senin adın ne şef?", placeholder="İsmini yaz...")
    if isim:
        st.session_state.kullanici_adi = isim.title()
        st.rerun()
    st.stop()

k_adi = st.session_state.kullanici_adi

# --- YAN MENÜ ---
st.sidebar.title(f"👋 Selam, {k_adi}! 🍋")
st.sidebar.image("https://images.unsplash.com/photo-1568471120021-9966d540306c?q=80&w=150&auto=format&fit=crop", width=100)
mod = st.sidebar.radio("Bölge Seç:", ["💬 Sohbet & Araştırma", "💾 Hafıza Bankası", "👥 Ekip"])

# --- ANA EKRAN ---
st.title(f"🍋 Cnclime Dashboard: {mod}")

if mod == "💬 Sohbet & Araştırma":
    st.write(f"Merhaba {k_adi}! Ne istersen sor, anlamazsam hemen internetten araştırırım.")
    
    user_input = st.text_input("Bana bir şeyler söyle veya sor:", placeholder="Nasılsın? / Kötüyüm / Kuantum nedir?")

    if user_input:
        m = user_input.lower().strip()
        
        # 1. Önce Özel Durumları Kontrol Et (Sohbet)
        if "kavga" in m or "küstük" in m:
            st.error(f"🤖 **Cnclime:** Sakin ol {k_adi}! Arkadaşlıkta olur böyle şeyler. Biz bir aileyiz! ❤️")
        elif "nasılsın" in m:
            st.info(f"🤖 Muq {k_adi}! Sen nasılsın?")
            st.balloons()
        elif m in ["iyiyim", "iyi", "muq"]:
            st.success(f"🤖 Harika {k_adi}! Keyfin yerinde olsun.")
            st.snow()
        elif "kötü" in m or "üzgün" in m:
            st.warning(f"🤖 Modunu düşürme {k_adi}, anlat beraber çözelim.")
        
        # 2. Eğer yukarıdakilerden biri değilse OTOMATİK İNTERNETTEN ARAŞTIR
        else:
            with st.spinner('🤖 Bunu tam anlayamadım, hemen internetten araştırıyorum... 🔍'):
                try:
                    # Hafızada varsa oradan getir
                    if m in st.session_state.bellek:
                        st.info(f"🤖 {k_adi}, bunu hafızamdan getirdim: {st.session_state.bellek[m]}")
                    else:
                        # İnternetten bul
                        sonuc = wikipedia.summary(m, sentences=2)
                        st.session_state.bellek[m] = sonuc # Hafızaya kaydet
                        st.success(f"🤖 {k_adi}, senin için araştırdım ve şunu buldum:")
                        st.write(sonuc)
                        st.write(f"🖼️ [Resimlere bakmak için tıkla](https://www.google.com/search?q={m}&tbm=isch)")
                except:
                    st.error(f"🤖 Üzgünüm {k_adi}, internette de bulamadım. Daha net yazar mısın?")

elif mod == "💾 Hafıza Bankası":
    st.write("🤖 Şimdiye kadar öğrendiklerim:")
    if st.session_state.bellek:
        for konu, bilgi in st.session_state.bellek.items():
            with st.expander(f"📌 {konu.title()}"):
                st.write(bilgi)
    else:
        st.info("Henüz bir şey öğrenmedim.")

elif mod == "👥 Ekip":
    st.success("👑 Mehmet Emin | 🔥 Emre Can | ⚡ Ömer Eymen | 🌟 Yunus Emre")

st.divider()
st.caption(f"© 2026 Cnclime AI | v23 Limon")
