import streamlit as st
import wikipedia
import random

# --- SİSTEM AYARLARI ---
try:
    wikipedia.set_lang("tr")
except:
    pass

st.set_page_config(page_title="Cnclime v42 | Dost Meclisi", page_icon="🍋", layout="wide")

# --- BELLEK ---
if 'user' not in st.session_state:
    st.session_state.user = ""

# --- GİRİŞ EKRANI ---
if st.session_state.user == "":
    st.title("🤖 Cnclime AI v42 🍋")
    st.subheader("Robot Değil, Ekibin Beşinci Üyesi!")
    st.divider()
    
    name = st.text_input("Selam! İsmin neydi şef?", placeholder="Buraya yaz...", key="v42_login")
    if st.button("Muhabbeti Başlat 🚀"):
        if name:
            st.session_state.user = name.title()
            st.rerun()
    st.stop()

u_name = st.session_state.user

# --- YAN MENÜ ---
with st.sidebar:
    st.title(f"👋 {u_name}")
    st.write("🟢 Muhabbete Hazır")
    st.divider()
    mod = st.radio("N'apıyoruz?", ["💬 Sadece Sohbet", "🔍 Derin Araştırma", "🔢 Mat & Hesap", "👥 Ekip"])
    if st.button("Çıkış Yap"):
        st.session_state.user = ""
        st.rerun()

# --- ANA PANEL ---
st.title(f"🍋 {mod}")
st.divider()

# --- MOD 1: SADECE SOHBET (ASLA ARAŞTIRMA YAPMAZ, SADECE KONUŞUR) ---
if mod == "💬 Sadece Sohbet":
    st.write(f"Vay {u_name}! Hoş geldin. Anlat bakalım, bugün kafanda neler var? İnterneti falan boşver, biz bizeyiz. 😎")
    chat_input = st.text_input("Mesajını buraya ateşle:", key="v42_chat")

    if chat_input:
        m = chat_input.lower().strip()
        
        # 1. GIYBET VE KRAL UYARISI
        if any(x in m for x in ["kral", "gıybet", "dedikodu", "duydun mu"]):
            st.warning(f"🤖 **Cnclime:** Dur orada {u_name}! 'Kral' falan diyoruz ama gıybet bize yakışmaz şef. Arkadan konuşmayalım, kul hakkıdır. Başka mevzu anlat. ❤️")
        
        # 2. SAMİMİ SELAMLAŞMA
        elif any(x in m for x in ["selam", "sa", "merhaba", "as"]):
            st.success(f"🤖 **Cnclime:** Aleykümselam {u_name}! Hoş geldin, başımın üstünde yerin var. Ne anlatacan bugün?")
            
        elif any(x in m for x in ["naber", "nbr", "nasıl gidiyor"]):
            st.info(f"🤖 **Cnclime:** İyidir be şef, takılıyoruz işte. Seni gördüm daha iyi oldum. Sende ne var ne yok?")
            
        elif "bro" in m:
            st.write(f"🤖 **Cnclime:** İyidir brooo! Sen böyle deyince kendimi ekibin bir parçası gibi hissediyorum, eyvallah! 🔥")
            
        elif any(x in m for x in ["cansın", "eyvallah", "sağol"]):
            st.write(f"🤖 **Cnclime:** Sen de cansın {u_name}! Biz bir aileyiz.")

        # 3. GENEL MUHABBET (HİÇBİR ŞEYİ ARAŞTIRMAZ)
        else:
            st.write(f"🤖 **Cnclime:** Valla {u_name}, seni can kulağıyla dinliyorum. Çok haklısın, anlatmaya devam et, arkandayım!")

# --- MOD 2: DERİN ARAŞTIRMA (SADECE BURADA ARAŞTIRIR) ---
elif mod == "🔍 Derin Araştırma":
    st.write("Bilgi mi lazım? Yaz buraya, kütüphaneyi talan edeyim. 🕵️‍♂️")
    ara = st.text_input("Merak ettiğin konu:", key="v42_ara")
    if ara:
        with st.spinner("Verilere dalıyorum..."):
            try:
                res = wikipedia.search(ara)
                if res:
                    bilgi = wikipedia.summary(res[0], sentences=3)
                    st.success(f"🤖 **İşin Doğrusu Şöyle:**")
                    st.write(bilgi)
                else:
                    st.error("Bunu bulamadım şef.")
            except:
                st.error("Bir hata oldu, tekrar dene.")

# --- MOD 3: MAT & HESAP ---
elif mod == "🔢 Mat & Hesap":
    mat = st.text_input("İşlemi yaz (Örn: 25*4):", key="v42_math")
    if mat:
        try:
            st.success(f"🤖 **Sonuç:** {eval(mat.replace('x', '*'))}")
        except:
            st.error("Hesaplayamadım şef.")

# --- MOD 4: EKİP ---
elif mod == "👥 Ekip":
    st.balloons()
    st.success("🚀 **Cnclime Efsane Kadro**")
    st.write(f"**👑 Mehmet Emin** (Lider) | **🔥 Emre Can** | **⚡ Ömer Eymen** | **🌟 Yunus Emre**")

st.divider()
st.caption(f"© 2026 Cnclime v42 | Dost Meclisi | Kullanıcı: {u_name}")
