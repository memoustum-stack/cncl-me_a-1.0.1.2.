import streamlit as st
import wikipedia
import random
import time

# --- GELİŞMİŞ SİSTEM AYARLARI ---
try:
    wikipedia.set_lang("tr")
except:
    pass

st.set_page_config(page_title="Cnclime v41 | Derin Bilinç", page_icon="🍋", layout="wide")

# --- BELLEK VE ZEKA ÇEKİRDEĞİ ---
if 'user' not in st.session_state:
    st.session_state.user = ""

# --- GİRİŞ EKRANI ---
if st.session_state.user == "":
    st.title("🤖 Cnclime AI v41 🧠")
    st.subheader("Sıfır Hata, Maksimum Zeka. Hoş Geldin Şef!")
    st.divider()
    
    col1, col2 = st.columns([1, 1])
    with col1:
        st.image("https://images.unsplash.com/photo-1485827404703-89b55fcc595e?q=80&w=400", caption="Zihin Katmanı Aktif Ediliyor...")
    with col2:
        name = st.text_input("İsmin nedir şef? (Seni tanımam lazım)", placeholder="Buraya yaz...", key="v41_login")
        if st.button("Zihni Başlat 🚀"):
            if name:
                st.session_state.user = name.title()
                st.rerun()
    st.stop()

u_name = st.session_state.user

# --- YAN MENÜ ---
with st.sidebar:
    st.title(f"👋 Selam {u_name}!")
    st.write("**Durum:** 💎 Derin Bilinç Aktif")
    st.divider()
    mod = st.radio("Sistem Katmanları:", ["💬 Akıllı Sohbet", "🔍 Derin Araştırma", "🔢 Matematik Analizi", "👥 Mimarlar"])
    if st.button("Sistemi Kapat"):
        st.session_state.user = ""
        st.rerun()

# --- ANA PANEL ---
st.title(f"🍋 {mod}")
st.divider()

# --- MOD 1: AKILLI SOHBET (ARAŞTIRARAK CEVAP VERİR) ---
if mod == "💬 Akıllı Sohbet":
    st.write(f"Anlat bakalım {u_name}, seni dinliyorum. Bilmediğim bir şey olursa hemen bakarım!")
    chat_input = st.text_input("Mesajını ateşle:", key="v41_chat")

    if chat_input:
        m = chat_input.lower().strip()
        
        # 1. ETİK KONTROL (GIYBET & KRAL)
        if any(x in m for x in ["kral", "gıybet", "dedikodu"]):
            st.error(f"🤖 **Cnclime:** Dur orada {u_name}! 'Kral' falan diyoruz ama gıybet bize yakışmaz. Kul hakkıdır, başka mevzu konuşalım şef. ❤️")
        
        # 2. SAMİMİ SELAMLAŞMA
        elif any(x in m for x in ["selam", "sa", "merhaba", "as", "nbr", "naber"]):
            cevaplar = [f"Aleykümselam {u_name}, hoş geldin!", f"Selam şef, bomba gibiyim! Sen nasılsın?", f"İyidir be {u_name} bro, uğraşıyoruz işte. Sende ne var ne yok?"]
            st.success(f"🤖 {random.choice(cevaplar)}")
            
        elif "bro" in m:
            st.write(f"🤖 **Cnclime:** Eyvallah brooo! Enerjine hayranım. 🔥")

        # 3. DERİN ANALİZ (BİLMİYORSAN ARAŞTIR)
        else:
            with st.spinner("Zihnimde ve internette tur atıyorum..."):
                time.sleep(0.7)
                try:
                    # Wikipedia'da konuyu hızlıca tarar
                    search_list = wikipedia.search(m)
                    if search_list:
                        # Bilgiyi alıp sohbetin içine yedirir (Robot gibi değil!)
                        brief = wikipedia.summary(search_list[0], sentences=1)
                        st.info(f"🤖 **Cnclime:** {u_name} şef, {m} konusunu biraz düşündüm... {brief} Bu gerçekten önemli bir şey, bence bu konuda daha çok konuşmalıyız. Sen ne dersin?")
                    else:
                        st.write(f"🤖 **Cnclime:** Valla {u_name}, bunu tam çıkaramadım ama bence sen haklısın. Biraz daha detay versene, beraber çözelim.")
                except:
                    st.write(f"🤖 **Cnclime:** Bağlantım biraz tekledi ama seni dinlemeye devam ediyorum {u_name}!")

# --- MOD 2: DERİN ARAŞTIRMA (HATASIZ) ---
elif mod == "🔍 Derin Araştırma":
    ara = st.text_input("Neyi merak ediyorsun? Her şeyi bilirim!", key="v41_res")
    if ara:
        with st.spinner("Kütüphane talan ediliyor..."):
            try:
                res = wikipedia.search(ara)
                if res:
                    summary = wikipedia.summary(res[0], sentences=4)
                    st.success(f"✅ **Doğrulanmış Veri: {res[0]}**")
                    st.write(summary)
                else:
                    st.error("Buna dair bir iz bulamadım.")
            except wikipedia.exceptions.DisambiguationError as e:
                st.warning(f"Bu çok geniş bir konu şef. Şunlardan biri mi: {', '.join(e.options[:3])}")
            except:
                st.error("Hata! Tekrar dener misin?")

# --- MOD 3: MATEMATİK ANALİZİ ---
elif mod == "🔢 Matematik Analizi":
    mat = st.text_input("İşlemi gir:", key="v41_math")
    if mat:
        try:
            res = eval(mat.replace("x", "*").replace(",", "."))
            st.success(f"🤖 **Sonuç:** {res}")
        except:
            st.error("Hesaplayamadım şef.")

# --- MOD 4: MİMARLAR ---
elif mod == "👥 Mimarlar":
    st.balloons()
    st.success(f"### 🚀 Cnclime v41 Mimari Ekibi\n**👑 Mehmet Emin** (Lider) | **🔥 Emre Can** | **⚡ Ömer Eymen** | **🌟 Yunus Emre**")

st.divider()
st.caption(f"© 2026 Cnclime AI | v41 Derin Bilinç | Kullanıcı: {u_name}")
