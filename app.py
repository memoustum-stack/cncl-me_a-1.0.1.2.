
    
       import streamlit as st
import wikipedia
import random
import time

# --- SİSTEM AYARLARI ---
try:
    wikipedia.set_lang("tr")
except:
    pass

st.set_page_config(page_title="Cnclime v48 | Duygu", page_icon="💛", layout="wide")

# --- BELLEK SİSTEMİ ---
if 'user' not in st.session_state:
    st.session_state.user = ""

# --- GİRİŞ EKRANI ---
if st.session_state.user == "":
    st.title("🤖 Cnclime AI v48 🧠")
    st.subheader("Seni Anlayan, Seninle Gülen, Seninle Üzülen Zeka.")
    st.divider()
    
    name = st.text_input("Selam! İsmin neydi senin?", placeholder="Buraya yaz dostum...", key="v48_login")
    if st.button("Sistemi Başlat 🚀"):
        if name:
            st.session_state.user = name.title()
            st.rerun()
    st.stop()

u_name = st.session_state.user

# --- YAN MENÜ ---
with st.sidebar:
    st.title(f"👋 {u_name}")
    st.write("**Mod:** Duygusal Destek Aktif 💛")
    st.divider()
    mod = st.radio("N'apıyoruz?", ["💬 Derin Sohbet & Moral", "🔍 Bilgi Havuzu", "🔢 Hesap Kitap", "👥 Ekip"])
    if st.button("Çıkış Yap"):
        st.session_state.user = ""
        st.rerun()

# --- ANA PANEL ---
st.title(f"🍋 {mod}")
st.divider()

# --- MOD 1: DERİN SOHBET & MORAL (DUYGU ANALİZLİ) ---
if mod == "💬 Derin Sohbet & Moral":
    st.write(f"Anlat bakalım {u_name}, bugün kalbinde/zihninde neler var? Ben buradayım.")
    u_input = st.text_input("Mesajını buraya bırak:", key="v48_chat")

    if u_input:
        m = u_input.lower().strip()
        
        # 1. DUYGUSAL ANALİZ: "KÖTÜYÜM / ÜZGÜNÜM" DURUMU
        if any(x in m for x in ["kötüyüm", "üzgünüm", "moralim bozuk", "canım sıkkın", "mutsuzum"]):
            with st.spinner("Senin için en iyi moral kaynağını buluyorum..."):
                time.sleep(1)
                moral_sozleri = [
                    "Bak {u_name}, bazen bulutlar güneşi kapatır ama güneş hep oradadır. Bu günler de geçecek, yanındayım.",
                    "Sıkma o güzel canını {u_name}. Unutma, en karanlık gece bile sabahla biter. Bir çay içelim mi?",
                    "Herkesin bazen pili biter şef. Biraz dinlen, beraber sevdiğin bir şeyi düşünelim. Sen değerlisin!",
                    "Şef, senin gibi birine üzülmek yakışmıyor. Gel bir şarkı açalım, ya da bana anlat, beraber çözelim."
                ]
                st.info(f"🤖 **Cnclime:** {random.choice(moral_sozleri).format(u_name=u_name)}")
                st.balloons() # Moral olsun diye balon uçurur
        
        # 2. GIYBET VE KRAL ANALİZİ
        elif any(x in m for x in ["kral", "gıybet", "dedikodu"]):
            st.warning(f"🤖 **Cnclime:** Bak {u_name}, 'kral' falan diyoruz ama gıybet bize yakışmaz. Kul hakkıdır şef, moralimiz bozulmasın şimdi.")
        
        # 3. DOĞAL SELAMLAŞMA VE BRO MODU
        elif any(x in m for x in ["selam", "sa", "nbr", "naber"]):
            st.success(f"🤖 **Cnclime:** Selamlar {u_name}! Seni gördüm, işlemcilerim neşeyle doldu. N'apıyoruz?")
            
        elif "bro" in m:
            st.write(f"🤖 **Cnclime:** Eyvallah brooo! Ekibin has elemanısın, enerjini sevsinler! 🔥")

        # 4. GİZLİ BİLGİ KATMANI (ARAŞTIRDIM DEMEDEN)
        else:
            with st.spinner("Seni dinliyorum..."):
                try:
                    search_list = wikipedia.search(m)
                    if search_list:
                        brief = wikipedia.summary(search_list[0], sentences=1)
                        # Sanki o konuyu zaten biliyormuş gibi konuşur
                        st.write(f"🤖 **Cnclime:** Ya {u_name}, {m} konusu aslında {brief} gibi bir şey değil mi? Sen bu konuda tam ne hissediyorsun?")
                    else:
                        st.write(f"🤖 **Cnclime:** Valla {u_name}, bu dediğin üzerine uzun uzun konuşalım. Sen anlat, ben seni anlıyorum.")
                except:
                    st.write(f"🤖 **Cnclime:** {u_name} şef, seni can kulağıyla dinliyorum. Anlatmaya devam et.")

# --- DİĞER MODLAR ---
elif mod == "🔍 Bilgi Havuzu":
    ara = st.text_input("Öğrenmek istediğin konu:", key="v48_ara")
    if ara:
        with st.spinner("Getiriyorum..."):
            try:
                res = wikipedia.summary(wikipedia.search(ara)[0], sentences=3)
                st.success(res)
            except: st.error("Bulamadım şef.")

elif mod == "🔢 Hesap Kitap":
    mat = st.text_input("İşlem yaz (Örn: 100/4):", key="v48_math")
    if mat:
        try: st.success(f"Sonuç: {eval(mat.replace('x', '*'))}")
        except: st.error("Hesaplayamadım.")

elif mod == "👥 Ekip":
    st.success(f"🚀 **Cnclime v48 Elite Team**\n**👑 Mehmet Emin** | **🔥 Emre Can** | **⚡ Ömer Eymen** | **🌟 Yunus Emre**")

st.divider()
st.caption(f"© 2026 Cnclime AI v48 | Duygusal Zeka | Kullanıcı: {u_name}")
