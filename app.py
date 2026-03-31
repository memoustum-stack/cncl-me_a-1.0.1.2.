

import streamlit as st
import wikipedia
import random

# Wikipedia dili Türkçe yap
try:
    wikipedia.set_lang("tr")
except:
    pass

# --- SAYFA AYARLARI (LİMON GİBİ ENERJİK) ---
st.set_page_config(
    page_title="Cnclime: Limon Sürümü v22", 
    page_icon="🍋", 
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- SİSTEM HAFIZASI (Session State) ---
if 'kullanici_adi' not in st.session_state:
    st.session_state.kullanici_adi = ""
if 'bellek' not in st.session_state:
    st.session_state.bellek = {} # Aratılan bilgileri burada tutar

# --- GİRİŞ EKRANI (İsim Sorar) ---
if st.session_state.kullanici_adi == "":
    st.title("🤖 Cnclime AI: Limon Sürümü v22 🍋")
    st.divider()
    
    # Giriş ekranında büyük bir limon resmi
    st.image("https://images.unsplash.com/photo-1590502160461-7f9a562dfd8b?q=80&w=600&auto=format&fit=crop", caption="Cnclime: Sapsarı ve Enerjik!", width=300)
    
    st.subheader("Merhaba! Ben Cnclime. Seninle tanışmak istiyorum.")
    isim = st.text_input("Senin adın ne şef?", placeholder="İsmini yaz ve Enter'a bas...")
    
    if isim:
        st.session_state.kullanici_adi = isim.title()
        st.rerun()
    st.stop()

k_adi = st.session_state.kullanici_adi

# --- SOL MENÜ (NAVİGASYON BÖLGESİ - LİMONLU) ---
st.sidebar.title(f"👋 Selam, {k_adi}! 🍋")
st.sidebar.markdown("---")

# Menüde küçük bir limon resmi
st.sidebar.image("https://images.unsplash.com/photo-1568471120021-9966d540306c?q=80&w=150&auto=format&fit=crop", width=100)

mod = st.sidebar.selectbox(
    "Bir Bölge Seç:", 
    ["💬 Sohbet & Dertleşme", "🔍 Akıllı Araştırma (Öğrenme)", "💾 Hafıza Bankası", "👥 Geliştirici Ekip"]
)

st.sidebar.divider()
if st.sidebar.button("🗑️ İsmi Temizle / Çıkış"):
    st.session_state.kullanici_adi = ""
    st.rerun()

st.sidebar.caption(f"Cnclime v22.0 - {k_adi} Özel")

# --- ANA EKRAN TASARIMI (LİMONLU) ---
# Başlıkta limon emojileri
st.title(f"🍋 Cnclime Dashboard: {mod} 🤖")
st.divider()

# --- BÖLGE 1: SOHBET & DERTLEŞME ---
if mod == "💬 Sohbet & Dertleşme":
    st.write(f"Burada benimle dertleşebilir veya havadan sudan konuşabilirsin {k_adi}. Biz bir aileyiz! ❤️")
    
    chat_input = st.text_input("Bana bir şeyler söyle:", placeholder="Nasılsın? / Arkadaşımla kavga ettim...")

    if chat_input:
        m = chat_input.lower().strip()
        if "kavga" in m or "küstük" in m:
            st.error(f"🤖 **Cnclime:** {k_adi}, sakin ol şef! Biz bir aileyiz. ❤️ Barışmak her zaman en iyisidir. Biraz zaman tanı.")
        elif "kötü" in m or "üzgün" in m:
            st.warning(f"🤖 **Cnclime:** {k_adi} sakın modunu düşürme! Derdini anlat, çare bulalım.")
        elif "nasılsın" in m:
            st.info(f"🤖 Muq {k_adi}! Ekip beni geliştirdikçe uçuyorum. Sen nasılsın?")
            st.balloons()
        elif "iyiyim" in m or "muq" in m:
            st.success(f"🤖 Harika {k_adi}! Keyfin hep yerinde olsun.")
            st.snow()
        else:
            st.write(f"🤖 **Cnclime:** Seni anlıyorum {k_adi}, anlatmaya devam et...")

# --- BÖLGE 2: AKILLI ARAŞTIRMA (GOOGLE/WİKİ ÖĞRENME) ---
elif mod == "🔍 Akıllı Araştırma (Öğrenme)":
    st.write("Bir konu yaz, internetten araştırıp hafızama kaydedeyim.")
    
    ara = st.text_input("Neyi öğrenmemi istersin?", placeholder="Örn: Karadelik, Python, Limon Faydaları...")

    if ara:
        konu = ara.lower().strip()
        
        # Önce Hafızaya bak
        if konu in st.session_state.bellek:
            st.success(f"🤖 {k_adi}, ben bunu zaten biliyorum! Hafızamdan getiriyorum:")
            st.info(st.session_state.bellek[konu])
        else:
            with st.spinner('🤖 İnternete bağlanıp öğreniyorum...'):
                try:
                    bilgi = wikipedia.summary(konu, sentences=2)
                    # HAFIZAYA KAYDET
                    st.session_state.bellek[konu] = bilgi
                    st.success(f"✅ {k_adi}, yeni bir bilgi öğrendim ve hafızama attım!")
                    st.info(bilgi)
                    st.write(f"🔗 [Daha fazla resim ve detay için tıkla](https://www.google.com/search?q={konu})")
                except:
                    st.error("🤖 Bunu internette bulamadım şef, daha net bir kelime yazar mısın?")

# --- BÖLGE 3: HAFIZA BANKASI ---
elif mod == "💾 Hafıza Bankası":
    st.write(f"🤖 {k_adi}, işte şimdiye kadar öğrendiğim ve kaydettiğim konular:")
    
    if not st.session_state.bellek:
        st.warning("⚠️ Henüz hiçbir şey öğrenmedim. Önce araştırma yapmalısın!")
    else:
        for k in st.session_state.bellek.keys():
            st.button(f"📌 {k.title()}", on_click=lambda k=k: st.info(st.session_state.bellek[k]))
        
        if st.button("🗑️ Hafızayı Sıfırla"):
            st.session_state.bellek = {}
            st.rerun()

# --- BÖLGE 4: GELİŞTİRİCİ EKİP ---
elif mod == "👥 Geliştirici Ekip":
    st.write(f"Bu zekanın arkasındaki efsane ekip:")
    
    c1, c2 = st.columns(2)
    with c1:
        st.success("👑 Mehmet Emin")
        st.success("🔥 Emre Can")
    with c2:
        st.success("⚡ Ömer Eymen")
        st.success("🌟 Yunus Emre")
    
    st.markdown("---")
    st.info("Cnclime bir aile projesidir! ❤️")

st.divider()
# Alt kısımda küçük bir limon simgesi
st.caption(f"🍋 Cnclime AI | v22 | Geliştirici: Mehmet Emin & Ekibi")



































