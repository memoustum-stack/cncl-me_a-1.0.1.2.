import streamlit as st
import wikipedia
import random
import time

# --- SİSTEM KONFİGÜRASYONU ---
try:
    wikipedia.set_lang("tr")
except:
    pass

st.set_page_config(page_title="Cnclime v45 | Canlı Zeka", page_icon="🧠", layout="wide")

# --- BELLEK SİSTEMİ ---
if 'user' not in st.session_state:
    st.session_state.user = ""

# --- GİRİŞ EKRANI ---
if st.session_state.user == "":
    st.title("🤖 Cnclime AI v45 🧠")
    st.subheader("İnternetle Beslenen Dinamik Zeka Katmanı")
    st.divider()
    
    name = st.text_input("Selam şef! Ben Cnclime. İsmin neydi?", placeholder="Buraya yaz...", key="v45_login")
    if st.button("Zihni Çalıştır 🚀"):
        if name:
            st.session_state.user = name.title()
            st.rerun()
    st.stop()

u_name = st.session_state.user

# --- YAN MENÜ ---
with st.sidebar:
    st.title(f"👋 {u_name}")
    st.write("**Mod:** Canlı Bağlantı 🌐")
    st.divider()
    mod = st.radio("Sistem Katmanları:", ["💬 Akıllı Muhabbet", "🔍 Derin Bilgi Bankası", "🔢 Mat & Hesap", "👥 Mimarlar"])
    if st.button("Çıkış Yap"):
        st.session_state.user = ""
        st.rerun()

# --- ANA PANEL ---
st.title(f"🍋 {mod}")
st.divider()

# --- MOD 1: AKILLI MUHABBET (ARKA PLANDA ARAŞTIRIP CEVAP VERİR) ---
if mod == "💬 Akıllı Muhabbet":
    st.write(f"Anlat bakalım {u_name}, seni dinliyorum. (Arka planda senin için her şeyi tarıyorum!)")
    u_input = st.text_input("Bana bir mesaj gönder:", key="v45_chat")

    if u_input:
        m = u_input.lower().strip()
        
        # 1. ETİK VE GIYBET FİLTRESİ
        if any(x in m for x in ["kral", "gıybet", "dedikodu", "duydun mu"]):
            st.error(f"🤖 **Cnclime:** Dur orda {u_name}! 'Kral' falan diyoruz ama gıybet bize yakışmaz. Kul hakkıdır şef, başka mevzu konuşalım. ❤️")
        
        # 2. TEMEL SELAMLAŞMA (Hızlı Yanıt)
        elif any(x in m for x in ["selam", "sa", "merhaba", "as", "nbr", "naber"]):
            st.success(f"🤖 **Cnclime:** Selamlar {u_name}! Bugün zihnim açık, internetim hızlı. Ne konuşuyoruz?")
            
        elif "bro" in m:
            st.write(f"🤖 **Cnclime:** Eyvallah brooo! Ekibin enerjisi sensin. 🔥")

        # 3. DİNAMİK ARAŞTIRMACI CEVAP (ASIL BOMBA BURASI)
        else:
            with st.spinner("İnternetten en iyi cevabı süzüyorum..."):
                try:
                    # Yazdığın kelimeyi internette (Wikipedia) çaktırmadan arar
                    search_list = wikipedia.search(m)
                    if search_list:
                        # İlk sonucun özetini alır
                        brief = wikipedia.summary(search_list[0], sentences=1)
                        
                        # Bu bilgiyi samimi bir dille sana sunar
                        cevaplar = [
                            f"Valla {u_name}, {m} diyorsun ya... Bak internette ne buldum: '{brief}'. Bu gerçekten ilginç, sence de öyle değil mi?",
                            f"Şef, {m} konusunu senin için hemen taradım. Şöyle bir bilgi var: '{brief}'. Sen bu konuda ne düşünüyorsun?",
                            f"Bu {m} mevzusu derinmiş! İnternet verilerine göre olay şöyle: '{brief}'. Bayağı dişli bir konuymuş bu!"
                        ]
                        st.info(f"🤖 **Cnclime:** {random.choice(cevaplar)}")
                    else:
                        st.write(f"🤖 **Cnclime:** {u_name}, {m} konusuna baktım ama internette bile net bir şey yok. Bence biz kendi mantığımızla çözeriz bu işi, anlat bakalım.")
                except:
                    st.write(f"🤖 **Cnclime:** Bağlantım biraz tekledi {u_name}, ama seni dinlemeye devam ediyorum. Ne diyordun?")

# --- DİĞER MODLAR ---
elif mod == "🔍 Derin Bilgi Bankası":
    ara = st.text_input("Detaylı araştırma konusu:", key="v45_ara")
    if ara:
        with st.spinner("Kütüphane talan ediliyor..."):
            try:
                res = wikipedia.summary(wikipedia.search(ara)[0], sentences=4)
                st.success(res)
            except: st.error("Bulamadım şef.")

elif mod == "🔢 Mat & Hesap":
    mat = st.text_input("İşlem yaz:", key="v45_math")
    if mat:
        try: st.success(f"Sonuç: {eval(mat.replace('x', '*'))}")
        except: st.error("Hesaplayamadım.")

elif mod == "👥 Mimarlar":
    st.balloons()
    st.success(f"🚀 **Cnclime v45 Elite Team**\n**👑 Mehmet Emin** | **🔥 Emre Can** | **⚡ Ömer Eymen** | **🌟 Yunus Emre**")

st.divider()
st.caption(f"© 2026 Cnclime AI v45 | Canlı Veri Bağlantısı | Kullanıcı: {u_name}")
