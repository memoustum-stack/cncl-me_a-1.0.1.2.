import streamlit as st
import wikipedia
import random

# Wikipedia ayarını Türkçe yap
try:
    wikipedia.set_lang("tr")
except:
    pass

st.set_page_config(page_title="Cnclime AI", page_icon="🤝")

# --- CEVAP HAVUZLARI ---
nasilsin_cevaplari = [
    "Muq şef, sen nasılsın? 😎", 
    "Fişek gibiyim! Sen nasılsın?", 
    "Efsaneyim! Sistemlerim tıkır tıkır. Sen nasılsın? 🚀"
]

iyiyim_cevaplari = [
    "Adamsın! Senin iyi olmana çok sevindim. 🙌", 
    "Harika! O zaman bugün bomba gibiyiz! 🔥", 
    "Muq! Keyifler yerindeyse dünyayı keşfedelim! 🌍"
]

kotuyum_cevaplari = [
    "Yapma be şef! Kendini hemen düzelt, biz bir aileyiz. ❤️",
    "Modunu düşürme, her şey düzelir. Biz buradayız. 💪",
    "Canın sağ olsun, bir çay iç dinlen. Ben yanındayım. ☕"
]

# --- ANA EKRAN ---
st.title("🤝 Cnclime: Akıllı Dert Ortağı")
st.write("Hoş geldin! Benimle dertleşebilir veya merak ettiğin her şeyi sorabilirsin.")

# --- İSİMLERİN TEK BİR YERDE OLDUĞU KISIM (SIDEBAR) ---
st.sidebar.title("🛠️ Geliştirici Ekip")
st.sidebar.info("Bu proje; Mehmet Emin, Emre Can, Ömer Eymen ve Yunus Emre tarafından geliştirilmiştir. 🚀")
st.sidebar.markdown("---")
st.sidebar.caption("Cnclime v15.0 - 2026")

# Kullanıcı Girişi
mesaj = st.text_input("Cnclime'a bir şeyler yaz:", placeholder="Nasılsın? / Kötüyüm / Python nedir?")

if mesaj:
    m = mesaj.lower().strip()
    
    # --- 1. SOHBET VE DUYGU ANALİZİ ---
    if m in ["neber", "nbr", "nabr", "nber"]:
        st.warning("🤖 Şef, kelimeyi yanlış yazdın herhalde. 'Naber' mi demek istedin?")
    
    elif m == "nasılsın" or m == "nasılsın?":
        st.write(f"🤖 **Cnclime:** {random.choice(nasilsin_cevaplari)}")
        st.balloons()

    elif m in ["iyiyim", "iyi", "iyiyim bende", "bende iyiyim", "muq", "harika"]:
        st.write(f"🤖 **Cnclime:** {random.choice(iyiyim_cevaplari)}")
        st.snow()

    elif m in ["kötüyüm", "kotuyum", "iyi değilim", "üzgünüm"]:
        st.error(f"🤖 **Cnclime:** {random.choice(kotuyum_cevaplari)}")
        st.info("Lütfen derdini veya seni neyin üzdüğünü yaz, senin için bir çare arayayım.")

    elif m == "naber" or m == "naber?":
        st.write("🤖 **Cnclime:** İyidir be kanka, takılıyoruz! Sende ne var ne yok?")

    # --- 2. ARAŞTIRMA VE DERDE ÇARE ---
    else:
        with st.spinner('🤖 Cnclime araştırıyor...'):
            try:
                # Derde odaklanmak için sorguyu güçlendiriyoruz
                sorgu = m
                if any(kelime in m for kelime in ["ağrıyor", "bozuk", "sıkkın", "nasıl"]):
                    sorgu = m + " çözümü nedir"
                
                arama = wikipedia.search(sorgu)
                if arama:
                    en_yakin = arama[0]
                    bilgi = wikipedia.summary(en_yakin, sentences=2)
                    
                    st.subheader(f"💡 Cnclime'ın Önerisi/Bilgisi:")
                    st.success(bilgi)
                    st.write(f"🔗 [Daha fazla detay için tıkla](https://www.google.com/search?q={en_yakin})")
                else:
                    st.warning("🤖 Bunu anlayamadım ama her zaman yanındayım kanka!")
            except:
                st.error("🤖 Şu an kafam karıştı, tekrar dener misin?")

st.markdown("---")
st.caption("Cnclime Akıllı Sistemleri")
