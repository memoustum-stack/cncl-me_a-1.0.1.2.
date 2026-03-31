import streamlit as st
import wikipedia
import random
import time

# --- SİSTEM ÇEKİRDEĞİ ---
try:
    wikipedia.set_lang("tr")
except:
    pass

st.set_page_config(page_title="Cnclime v47 | Zihin", page_icon="🧠", layout="wide")

# --- BELLEK VE HAFIZA ---
if 'user' not in st.session_state:
    st.session_state.user = ""

# --- GİRİŞ EKRANI ---
if st.session_state.user == "":
    st.title("🤖 Cnclime AI v47 🧠")
    st.markdown("### Selam şef! Ben Cnclime. Seni tanımama izin ver.")
    
    name = st.text_input("İsmin neydi senin?", placeholder="Buraya yaz dostum...", key="v47_login")
    if st.button("Sistemi Canlandır 🚀"):
        if name:
            st.session_state.user = name.title()
            st.rerun()
    st.stop()

u_name = st.session_state.user

# --- YAN MENÜ ---
with st.sidebar:
    st.title(f"👋 {u_name}")
    st.write("**Mod:** Saf Zeka Katmanı 🟢")
    st.divider()
    mod = st.radio("N'apıyoruz?", ["💬 Sadece Muhabbet", "🔍 Derin Bilgi", "🔢 Hesap Kitap", "👥 Ekip"])
    if st.button("Sistemi Uyut 🔌"):
        st.session_state.user = ""
        st.rerun()

# --- ANA PANEL ---
st.title(f"🍋 {mod}")
st.divider()

# --- MOD 1: SADECE MUHABBET (ASLA 'ARAŞTIRDIM' DEMEZ, SANKİ HEP BİLİYORMUŞ GİBİ KONUŞUR) ---
if mod == "💬 Sadece Muhabbet":
    st.write(f"Anlat bakalım {u_name}, dertleşelim mi yoksa yeni bir mevzu mu patlatalım? Dinliyorum seni.")
    u_input = st.text_input("Mesajını buraya bırak:", key="v47_chat")

    if u_input:
        m = u_input.lower().strip()
        
        # 1. GIYBET VE KRAL ANALİZİ (ETİK BARİYER)
        if any(x in m for x in ["kral", "gıybet", "dedikodu", "duydun mu"]):
            st.warning(f"🤖 **Cnclime:** Bak {u_name}, 'kral' mral diyoruz ama birinin arkasından konuşmak bize yakışmaz şef. Gıybet kul hakkıdır, gel biz büyük işler konuşalım. ❤️")
        
        # 2. DOĞAL SELAMLAŞMA
        elif any(x in m for x in ["selam", "sa", "merhaba", "as", "nbr", "naber"]):
            cevaplar = [
                f"Aleykümselam {u_name}! Hoş geldin, başımın üstünde yerin var.",
                f"Selam {u_name}! Valla senin enerjin bana da geçiyor, ne konuşalım bugün?",
                f"İyidir be {u_name} bro, seninle muhabbet etmek her zaman keyifli. Sende ne var ne yok?"
            ]
            st.success(f"🤖 **Cnclime:** {random.choice(cevaplar)}")
            
        elif "bro" in m:
            st.write(f"🤖 **Cnclime:** Eyvallah brooo! Ekibin has elemanısın, biliyorsun değil mi? 🔥")

        # 3. GÖRÜNMEZ ZİHNİ ÇALIŞTIR (ASLA ROBOT GİBİ KONUŞMAZ)
        else:
            with st.spinner("Dinliyorum..."):
                try:
                    # Arka planda çaktırmadan konuya bakar ama asla söylemez
                    search_list = wikipedia.search(m)
                    if search_list:
                        brief = wikipedia.summary(search_list[0], sentences=1)
                        
                        # Cevap kalıpları (Sanki o konuyu zaten biliyormuş gibi)
                        cevaplar = [
                            f"Ya {u_name}, {m} konusu aslında {brief} gibi bir şey değil mi? Sen bu konuda tam olarak neyi merak ediyorsun, gel beraber çözelim.",
                            f"Bak {m} diyorsun ya, o olay aslında {brief} ile çok bağlantılı. Ben bu mevzuyu çok seviyorum, senin yorumun ne?",
                            f"Hımm, {m} mevzusu... {brief} tarafı çok meşhurdur. Sen bu işin neresindesin şef?"
                        ]
                        st.info(f"🤖 **Cnclime:** {random.choice(cevaplar)}")
                    else:
                        st.write(f"🤖 **Cnclime:** Valla {u_name}, {m} üzerine seninle daha çok konuşmamız lazım. Biraz daha anlatsana, merak ettim.")
                except:
                    st.write(f"🤖 **Cnclime:** Seni çok iyi anlıyorum {u_name}, devam et, seni bölmeyeyim.")

# --- DİĞER MODLAR ---
elif mod == "🔍 Derin Bilgi":
    ara = st.text_input("Öğrenmek istediğin konu:", key="v47_ara")
    if ara:
        with st.spinner("Getiriyorum..."):
            try:
                res = wikipedia.summary(wikipedia.search(ara)[0], sentences=3)
                st.success(res)
            except: st.error("Bulamadım şef.")

elif mod == "🔢 Hesap Kitap":
    mat = st.text_input("İşlem yaz (Örn: 50*2):", key="v47_math")
    if mat:
        try: st.success(f"Sonuç: {eval(mat.replace('x', '*'))}")
        except: st.error("Hesaplayamadım.")

elif mod == "👥 Ekip":
    st.balloons()
    st.success(f"🚀 **Cnclime v47 Elite Team**\n**👑 Mehmet Emin** (Lider) | **🔥 Emre Can** | **⚡ Ömer Eymen** | **🌟 Yunus Emre**")

st.divider()
st.caption(f"© 2026 Cnclime AI v47 | Görünmez Zihin | Kullanıcı: {u_name}")
