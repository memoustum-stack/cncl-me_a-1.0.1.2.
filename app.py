import streamlit as st
import wikipedia

# Wikipedia ayarları - Hata almamak için
try:
    wikipedia.set_lang("tr")
except:
    pass

# Sayfa Ayarları (Limon Teması)
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
    st.title("🤖 Cnclime AI v31 🍋")
    st.divider()
    st.image("https://images.unsplash.com/photo-1590502160461-7f9a562dfd8b?q=80&w=400&auto=format&fit=crop", caption="Cnclime: Sapsarı ve Akıllı!", width=350)
    
    st.subheader("Hoş Geldin! Önce ismini öğrenebilir miyim?")
    # Hata almamak için benzersiz bir key ekledik
    isim = st.text_input("İsmin nedir şef?", placeholder="İsmini yaz ve Enter'a bas...", key="v31_login_key")
    
    if isim:
        st.session_state.kullanici_adi = isim.title()
        st.rerun()
    st.stop()

k_adi = st.session_state.kullanici_adi

# --- YAN MENÜ (MODLAR) ---
st.sidebar.title(f"👋 Selam {k_adi}! 🍋")
st.sidebar.image("https://images.unsplash.com/photo-1568471120021-9966d540306c?q=80&w=150&auto=format&fit=crop", width=120)
st.sidebar.divider()

mod = st.sidebar.radio(
    "Modlar", 
    ["💬 Sohbet Modu (Akıllı & Bro)", "🔢 Matematik Çözücü", "🔍 Bilgi Araştırma", "👥 Geliştirici Ekip"]
)

st.sidebar.divider()
if st.sidebar.button("🗑️ Çıkış Yap"):
    st.session_state.kullanici_adi = ""
    st.rerun()

# --- ANA EKRAN ---
st.title(f"🍋 {mod}")
st.divider()

# --- MOD 1: SOHBET MODU (GİZLİ ARAŞTIRMA + SAMİMİYET) ---
if mod == "💬 Sohbet Modu (Akıllı & Bro)":
    st.write(f"Naber {k_adi}? Bana her şeyi sorabilirsin, bilmediğim bir 'bro' dili olsa bile hemen öğrenirim! 😉")
    user_input = st.text_input("Mesajını yaz:", placeholder="Naber bro? / Ne yapıyorsun kanka?", key="v31_chat_key")

    if user_input:
        m = user_input.lower().strip()
        
        # Sabit Sohbetler
        if "nasılsın" in m:
            st.write(f"🤖 **Cnclime:** Muq {k_adi}, seninle takılmak çok keyifli! 😎")
            st.balloons()
        elif "kavga" in m:
            st.write(f"🤖 **Cnclime:** Sakin şef, biz bir aileyiz! ❤️")
            
        # Bilmediği bir şeyse (Örn: Bro, Kanka vb.) ÇAKTIRMADAN ARAŞTIRIP ÖĞRENME
        else:
            with st.spinner("..."): 
                try:
                    # Wikipedia'da bu kelimeye ve "nasıl cevap verilir" kısmına gizlice bakıyor
                    arama = wikipedia.search(m)
                    if arama:
                        # Bilgiyi alıyor ama ansiklopedi gibi değil, kısa bir cevap gibi veriyor
                        bilgi = wikipedia.summary(arama[0], sentences=1)
                        # Eğer 'naber' gibi bir şeyse daha samimi cevap vermesini sağlıyoruz
                        if any(x in m for x in ["bro", "kanka", "naber", "nbr"]):
                            st.write(f"🤖 **Cnclime:** İyidir {k_adi} bro, senden naber? Her şey yolunda mı? 🔥")
                        else:
                            st.write(f"🤖 **Cnclime:** {bilgi}")
                    else:
                        st.write(f"🤖 **Cnclime:** Valla {k_adi}, tam çıkaramadım ama bence çok haklısın! 😎")
                except:
                    st.write(f"🤖 **Cnclime:** {k_adi} bro, bağlantımda bir sıkıntı oldu ama ben buradayım!")

# --- MOD 2: MATEMATİK ÇÖZÜCÜ ---
elif mod == "🔢 Matematik Çözücü":
    st.write(f"Sayılarla aran nasıl {k_adi}? Zorlandığın işlemleri yaz, hemen çözeyim! 🧠")
    mat_input = st.text_input("İşlem veya matematik terimi yaz:", key="v31_math_key")
    if mat_input:
        with st.spinner("Hesaplanıyor..."):
            try:
                sonuc = eval(mat_input.replace("x", "*").replace(",", "."))
                st.success(f"🤖 **Cnclime Sonucu:** **{sonuc}**")
            except:
                try:
                    arama = wikipedia.summary(f"Matematik {mat_input}", sentences=1)
                    st.info(f"🤖 **Cnclime Araştırma:** {arama}")
                except:
                    st.error("Bunu çözemedim şef.")

# --- MOD 3: BİLGİ ARAŞTIRMA ---
elif mod == "🔍 Bilgi Araştırma":
    ara = st.text_input("Hangi konuda bilgi istersin?", key="v31_search_key")
    if ara:
        try:
            bilgi = wikipedia.summary(ara, sentences=3)
            st.info(bilgi)
        except:
            st.error("Bulunamadı.")

# --- MOD 4: EKİP ---
elif mod == "👥 Geliştirici Ekip":
    st.success("👑 Mehmet Emin | 🔥 Emre Can | ⚡ Ömer Eymen | 🌟 Yunus Emre")

st.divider()
st.caption(f"© 2026 Cnclime | v31 Samimi Limon | Kullanıcı: {k_adi}")
