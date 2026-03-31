import streamlit as st
import wikipedia
import random

# Wikipedia ayarı
try:
    wikipedia.set_lang("tr")
except:
    pass

st.set_page_config(page_title="Cnclime: Akıllı Dost v11", page_icon="🤖")

# --- CEVAP HAVUZLARI ---
nasilsin_cevaplari = ["Muq şef, sen nasılsın? 😎", "Fişek gibiyim! Sen nasılsın?", "Efsaneyim! Ekip sağ olsun. Sen nasılsın? 🚀"]
iyiyim_cevaplari = ["Adamsın! Senin iyi olmana çok sevindim. 🙌", "Harika! O zaman bugün bomba gibiyiz! 🔥", "Süper! Ekipçe iyi olmanıza sevindim. 👑"]

st.title("🤖 Cnclime v11")
st.sidebar.title("🚀 Efsane Kadro")
st.sidebar.info("Mehmet Emin\n\nEmre Can\n\nÖmer Eymen\n\nYunus Emre")

# Kullanıcı Girişi
mesaj = st.text_input("Cnclime'a yaz:", placeholder="Nasılsın? / İyiyim / Naber?")

if mesaj:
    m = mesaj.lower().strip()
    
    # --- 1. ÖZEL SOHBET VE DÜZELTME MANTIĞI ---
    
    # Yanlış yazılan "naber" kontrolü (neber, nbr, nabr gibi)
    if m in ["neber", "nbr", "nabr", "nber"]:
        st.warning("🤖 Şef, sanırım 'Naber' yazmaya çalıştın ama kelimeyi yanlış yazdın. Tekrar yazar mısın?")
    
    elif m == "nasılsın" or m == "nasılsın?":
        st.write(f"🤖 **Cnclime:** {random.choice(nasilsin_cevaplari)}")
        st.balloons()

    elif m == "iyiyim" or m == "iyi" or m == "iyiyim bende" or m == "bende iyiyim":
        st.write(f"🤖 **Cnclime:** {random.choice(iyiyim_cevaplari)}")
        st.snow()

    elif m == "naber" or m == "naber?":
        st.write("🤖 **Cnclime:** İyidir kanka, piksellerle uğraşıyorum. Sende ne var ne yok?")

    # --- 2. ARAŞTIRMA MODÜLÜ ---
    else:
        with st.spinner('🤖 Cnclime araştırıyor...'):
            try:
                arama = wikipedia.search(mesaj)
                if arama:
                    en_yakin = arama[0]
                    # Araştırmada hata düzeltme
                    if en_yakin.lower() != m:
                        st.info(f"🤖 Kelimeyi yanlış yazdın herhalde, şunu mu demek istedin: **{en_yakin}**")
                    
                    bilgi = wikipedia.summary(en_yakin, sentences=2)
                    st.success(f"📖 {en_yakin}: {bilgi}")
                else:
                    st.error("🤖 Bunu internette bulamadım kanka, bir daha kontrol et!")
            except:
                st.warning("🤖 Bağlantı koptu, bir daha yazar mısın?")

st.markdown("---")
st.caption("Cnclime v11.0 - Mehmet Emin & Ekibi")
