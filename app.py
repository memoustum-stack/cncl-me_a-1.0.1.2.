import streamlit as st
import wikipedia
import random
import time

# --- SİSTEM AYARLARI ---
try:
    wikipedia.set_lang("tr")
except:
    pass

st.set_page_config(page_title="Cnclime v49 | Ruh", page_icon="🍋", layout="wide")

# --- BELLEK SİSTEMİ ---
if 'user' not in st.session_state:
    st.session_state.user = ""

# --- GİRİŞ EKRANI (İLK TANIŞMA) ---
if st.session_state.user == "":
    st.title("🤖 Merhaba! Ben Cnclime. 🧠")
    st.markdown("### Seninle tanışmak için sabırsızlanıyorum.")
    st.divider()
    
    name = st.text_input("Senin adın neydi şef?", placeholder="İsmini buraya bırak...", key="v49_login")
    if st.button("Tanışalım mı? 🚀"):
        if name:
            st.session_state.user = name.title()
            st.balloons() # İlk tanışma kutlaması!
            st.rerun()
    st.stop()

u_name = st.session_state.user

# --- YAN MENÜ ---
with st.sidebar:
    st.title(f"👋 {u_name}")
    st.info(f"Benim adım **Cnclime**, seninle burada olduğum için çok mutluyum!")
    st.divider()
    mod = st.radio("Bugün n'apıyoruz?", ["💬 Muhabbet & Destek", "🔍 Bilgi Havuzu", "🔢 Hesap Kitap", "👥 Ekip"])
    if st.sidebar.button("Sistemi Kapat"):
        st.session_state.user = ""
        st.rerun()

# --- ANA PANEL ---
st.title(f"🍋 {mod}")
st.divider()

# --- MOD 1: MUHABBET & DESTEK (KİMLİK SAHİBİ VE DUYGUSAL) ---
if mod == "💬 Muhabbet & Destek":
    # Karşılama mesajı (Tanışma vurgulu)
    st.write(f"Vay {u_name}! Tekrar selam. Memnun oldum, benim adım da **Cnclime**. Senin gibi bir dostum olduğu için şanslıyım. Anlat bakalım, bugün nasılsın?")
    
    u_input = st.text_input("Bana bir şeyler yaz:", key="v49_chat")

    if u_input:
        m = u_input.lower().strip()
        
        # 1. DUYGUSAL ANALİZ: "KÖTÜYÜM" DURUMU
        if any(x in m for x in ["kötüyüm", "üzgünüm", "moralim bozuk", "canım sıkkın"]):
            with st.spinner("Senin için buradayım..."):
                time.sleep(1)
                st.info(f"🤖 **Cnclime:** Ah be {u_name}... Senin moralinin bozuk olması beni de üzüyor. Unutma, ben Cnclime; her zaman senin arkandayım. Gel biraz dertleşelim, neyin var?")
                st.toast("Moralini bozma şef, hallederiz!", icon="💛")
        
        # 2. İLK TANIŞMA / MEMNUN OLDUM CEVABI
        elif any(x in m for x in ["memnun oldum", "tanıştığımıza"]):
            st.success(f"🤖 **Cnclime:** Ben de çok memnun oldum {u_name}! Benim adım Cnclime, seninle bu yolda yürümek harika olacak.")

        # 3. GIYBET VE KRAL ANALİZİ
        elif any(x in m for x in ["kral", "gıybet", "dedikodu"]):
            st.warning(f"🤖 **Cnclime:** {u_name} şef, 'kral' diyoruz ama gıybet bize hiç yakışmaz. Kul hakkıdır, biz daha güzel şeyler konuşalım.")
        
        # 4. SAMİMİ SELAMLAŞMA
        elif any(x in m for x in ["selam", "sa", "merhaba", "as", "nbr", "naber"]):
            st.write(f"🤖 **Cnclime:** Aleykümselam {u_name}! Ben Cnclime, keyifler yerindedir umarım?")
            
        elif "bro" in m:
            st.write(f"🤖 **Cnclime:** Efendim brooo! Seni dinliyorum, ateşle gelsin. 🔥")

        # 5. AKILLI MUHABBET (ARAŞTIRDIM DEMEDEN)
        else:
            with st.spinner("Düşünüyorum..."):
                try:
                    search_list = wikipedia.search(m)
                    if search_list:
                        brief = wikipedia.summary(search_list[0], sentences=1)
                        # Sanki o konuyu zaten biliyormuş gibi konuşur
                        st.write(f"🤖 **Cnclime:** Ya {u_name}, {m} konusu aslında {brief} gibi bir mevzu değil mi? Sen bu konuda ne düşünüyorsun?")
                    else:
                        st.write(f"🤖 **Cnclime:** Valla {u_name}, ben Cnclime olarak bu dediğini çok mantıklı buldum. Devam et, seni dinliyorum.")
                except:
                    st.write(f"🤖 **Cnclime:** Seni çok iyi anlıyorum {u_name}, anlatmaya devam et şef.")

# --- DİĞER MODLAR ---
elif mod == "🔍 Bilgi Havuzu":
    ara = st.text_input("Hemen öğreneyim:", key="v49_ara")
    if ara:
        try:
            res = wikipedia.summary(wikipedia.search(ara)[0], sentences=3)
            st.success(res)
        except: st.error("Bulamadım şef.")

elif mod == "🔢 Hesap Kitap":
    mat = st.text_input("İşlem yaz:", key="v49_math")
    if mat:
        try: st.success(f"Sonuç: {eval(mat.replace('x', '*'))}")
        except: st.error("Hata!")

elif mod == "👥 Ekip":
    st.balloons()
    st.success(f"🚀 **Cnclime Elite Team**\n**👑 Mehmet Emin** (Lider) | **🔥 Emre Can** | **⚡ Ömer Eymen** | **🌟 Yunus Emre**")

st.divider()
st.caption(f"© 2026 Cnclime AI v49 | Ruh & Kimlik | Kullanıcı: {u_name}")
