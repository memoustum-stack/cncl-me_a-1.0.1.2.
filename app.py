import streamlit as st
import wikipedia
import random
import time

# --- SİSTEM AYARLARI ---
try:
    wikipedia.set_lang("tr")
except:
    pass

st.set_page_config(page_title="Cnclime v51 | Tam Kapasite", page_icon="🔢", layout="wide")

# --- BELLEK SİSTEMİ ---
if 'user' not in st.session_state:
    st.session_state.user = ""

# --- GİRİŞ EKRANI ---
if st.session_state.user == "":
    st.title("🤖 Selam! Ben Cnclime. 🧠")
    st.markdown("### Seninle tanıştığıma çok memnun oldum!")
    
    name = st.text_input("İsmini bağışlar mısın şef?", placeholder="Buraya yaz...", key="v51_login")
    if st.button("Tanışalım! 🚀"):
        if name:
            st.session_state.user = name.title()
            st.balloons()
            st.rerun()
    st.stop()

u_name = st.session_state.user

# --- YAN MENÜ ---
with st.sidebar:
    st.title(f"👋 {u_name}")
    st.info(f"Benim adım **Cnclime**, seninle burada olduğum için çok mutluyum!")
    st.divider()
    mod = st.radio("Bugün n'apıyoruz?", [
        "💬 Samimi Sohbet & Destek", 
        "🔢 Sayısal Mantık & Hesap",
        "🎨 Görsel Oluştur (Hayal Et)", 
        "🔍 Akıllı Araştırma (Sohbetli)", 
        "👥 Ekip"
    ])
    if st.sidebar.button("Sistemi Kapat"):
        st.session_state.user = ""
        st.rerun()

# --- ANA PANEL ---
st.title(f"🍋 {mod}")
st.divider()

# --- MOD 1: SAMİMİ SOHBET & DESTEK ---
if mod == "💬 Samimi Sohbet & Destek":
    st.write(f"Vay {u_name}! Anlat bakalım, bugün kalbinde neler var? Ben Cnclime, her zaman yanındayım.")
    u_input = st.text_input("Bana bir şeyler yaz:", key="v51_chat")

    if u_input:
        m = u_input.lower().strip()
        
        if any(x in m for x in ["kötüyüm", "üzgünüm", "moralim bozuk", "canım sıkkın"]):
            st.info(f"🤖 **Cnclime:** Ah be {u_name}, canını sıkan ne varsa anlat bana. Ben senin dostunum. Gel bir nefes alalım, beraber çözelim.")
            st.toast("Moralini bozma şef, Cnclime burada!", icon="💛")
        
        elif any(x in m for x in ["kral", "gıybet", "dedikodu"]):
            st.warning(f"🤖 **Cnclime:** {u_name} şef, 'kral' diyoruz ama gıybet bize yakışmaz. Kul hakkıdır, biz daha büyük işler konuşalım.")
        
        elif any(x in m for x in ["selam", "sa", "nbr", "naber"]):
            st.success(f"🤖 **Cnclime:** Selamlar {u_name}! Tanıştığımıza tekrar memnun oldum. Keyifler nasıl?")
            
        else:
            with st.spinner("Dinliyorum..."):
                time.sleep(0.4)
                cevaplar = [
                    f"Valla {u_name}, seni çok iyi anlıyorum. Anlatmaya devam et.",
                    f"Ya {u_name}, bu dediğin gerçekten önemli. Ben Cnclime olarak senin arkandayım.",
                    f"Şef, seninle böyle dertleşmek bana da iyi geliyor. Devam et dinliyorum."
                ]
                st.write(f"🤖 **Cnclime:** {random.choice(cevaplar)}")

# --- MOD 2: SAYISAL MANTIK & HESAP (YENİ!) ---
elif mod == "🔢 Sayısal Mantık & Hesap":
    st.write(f"Matematik evrenin dilidir {u_name}. Yaz buraya, hemen çözeyim!")
    mat_input = st.text_input("Hesaplanacak işlem (Örn: 25*4/2):", key="v51_math")
    
    if mat_input:
        with st.spinner("Sayıları raks ettiriyorum..."):
            try:
                # Güvenli hesaplama için x karakterini * ile değiştiriyoruz
                temiz_islem = mat_input.replace('x', '*').replace(',', '.')
                sonuc = eval(temiz_islem)
                st.success(f"🤖 **Cnclime:** Bak {u_name}, bu işlemin sonucu tam olarak: **{sonuc}**")
                # Küçük
