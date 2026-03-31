import streamlit as st
import wikipedia
import random

# Wikipedia ayarı
try:
    wikipedia.set_lang("tr")
except:
    pass

st.set_page_config(page_title="Cnclime: Süper Zeka v12", page_icon="🌟")

# --- GELİŞMİŞ CEVAP HAVUZLARI ---
nasilsin_cevaplari = [
    "Muq şef, sen nasılsın? 😎", 
    "Fişek gibiyim! Sen nasılsın?", 
    "Efsaneyim! Ekip sağ olsun. Sen nasılsın? 🚀"
]

iyiyim_cevaplari = [
    "Adamsın! Senin iyi olmana çok sevindim. 🙌", 
    "Süper! O zaman bugün bomba gibiyiz! 🔥", 
    "Harika! Ekipçe iyi olmanıza sevindim. 👑",
    "Muq! Keyifler yerindeyse kodlamaya devam! 💻"
]

kotuyum_cevaplari = [
    "Yapma be şef! Canını sıkan ne varsa boşver, biz buradayız. ❤️",
    "Modunu düşürme kanka, ekip (Mehmet Emin, Emre Can, Ömer Eymen, Yunus Emre) seni toplar! 💪",
    "Üzülme be! Bir çay iç, biraz dinlen, Cnclime yanında. ☕",
    "Canın sağ olsun şef, her şey düzelir. Bir şey araştıralım mı modun değişsin? ✨"
]

st.title("🌟 Cnclime v12: Duygusal Zeka")
st.sidebar.title("🚀 Efsane Kadro")
st.sidebar.info("Mehmet Emin\n\nEmre Can\n\nÖmer Eymen\n\nYunus Emre")

# Kullanıcı Girişi
mesaj = st.text_input("Cnclime'a yaz:", placeholder="Nasılsın? / Muq / Kötüyüm / Mars nedir?")

if mesaj:
    m = mesaj.lower().strip()
    
    # --- 1. SOHBET VE DUYGU ANALİZİ ---
    
    # Kelime hatası kontrolü (Örn: neber)
    if m in ["neber", "nbr", "nabr", "nber"]:
        st.warning("🤖 Şef, kelimeyi yanlış yazdın herhalde. 'Naber' mi demek istedin? Tekrar yazsana.")
    
    elif m == "nasılsın" or m == "nasılsın?":
        st.write(f"🤖 **Cnclime:** {random.choice(nasilsin_cevaplari)}")
        st.balloons()

    elif m in ["iyiyim", "iyi", "iyiyim bende", "bende iyiyim", "muq", "harika"]:
        st.write(f"🤖 **Cnclime:** {random.choice(iyiyim_cevaplari)}")
        st.snow() # Mutluluk varsa kar yağsın!

    elif m in ["kötüyüm", "kotuyum", "iyi değilim", "modum düşük"]:
        st.write(f"🤖 **Cnclime:** {random.choice(kotuyum_cevaplari)}")
        st.info("Unutma: Sen bu ekibin parçasısın, her şey düzelir! 🌈")

    elif m == "naber" or m == "naber?":
        st.write("🤖 **Cnclime:** İyidir be kanka, takılıyoruz! Sende ne var ne yok?")

    # --- 2. AKILLI ARAŞTIRMA VE HATA DÜZELTME ---
    else:
        with st.spinner('🤖 Cnclime internette arıyor...'):
            try:
                arama = wikipedia.search(mesaj)
                if arama:
                    en_yakin = arama[0]
                    # Eğer kullanıcı yanlış yazdıysa uyar
                    if en_yakin.lower() != m:
                        st.caption(f"🤖 Kelimeyi yanlış yazdın herhalde, şunu mu demek istedin: **{en_yakin}**")
                    
                    bilgi = wikipedia.summary(en_yakin, sentences=2)
                    st.subheader(f"📖 {en_yakin}:")
                    st.success(bilgi)
                    st.write(f"🖼️ [Görsellere bakmak için tıkla](https://www.google.com/search?q={en_yakin}&tbm=isch)")
                else:
                    st.error("🤖 Bunu internette bulamadım kanka, bir daha kontrol et!")
            except:
                st.warning("🤖 Bir hata oluştu şef, tekrar dener misin?")

st.markdown("---")
st.caption("Cnclime v12.0 - Mehmet Emin, Emre Can, Ömer Eymen ve Yunus Emre Özel Üretimi")
