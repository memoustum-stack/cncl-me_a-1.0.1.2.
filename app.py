import streamlit as st
import wikipedia
import random

# Wikipedia ayarı
try:
    wikipedia.set_lang("tr")
except:
    pass

st.set_page_config(page_title="Cnclime AI", page_icon="🤝")

# --- ÖZEL TAVSİYE HAVUZU (Dertler İçin) ---
dert_cevaplari = {
    "kavga": [
        "Sakin ol şef! Arkadaşlıkta olur böyle şeyler. Biraz zaman tanı, öfken geçince konuşun. Biz bir aileyiz! ❤️",
        "Kavga enerjini düşürmesin. Haklıysan dik dur, haksızsan özür dilemek büyüklüktür. Ekip yanınızda! 💪"
    ],
    "sıkkın": [
        "Canın neden sıkkın? Gel biraz dertleşelim. Bir çay içmek ya da dışarı çıkmak iyi gelebilir. ✨",
        "Moralini bozma, her gecenin bir sabahı vardır. Bugünler de geçecek! 🌈"
    ],
    "hastalık": [
        "Geçmiş olsun şef! Hemen dinlenmeye bak, sağlığın her şeyden önemli. 💊",
        "Kendine dikkat et, ekipçe senin iyileşmeni bekliyoruz! ❤️"
    ]
}

st.title("🤝 Cnclime: Akıllı Dert Ortağı")
st.sidebar.title("🛠️ Geliştirici Ekip")
st.sidebar.info("Bu proje; Mehmet Emin, Emre Can, Ömer Eymen ve Yunus Emre tarafından geliştirilmiştir. 🚀")

# Kullanıcı Girişi
mesaj = st.text_input("Cnclime ile konuş:", placeholder="Arkadaşımla kavga ettim / Canım sıkkın / Naber?")

if mesaj:
    m = mesaj.lower().strip()
    
    # --- 1. SAMİMİ SOHBET VE DERTLEŞME ---
    
    # Kavga/Tartışma Kontrolü
    if "kavga" in m or "tartış" in m:
        st.error(f"🤖 **Cnclime:** {random.choice(dert_cevaplari['kavga'])}")
        st.info("Unutma: Arkadaşlık her şeyden değerlidir.")

    # Can Sıkıntısı Kontrolü
    elif "sıkkın" in m or "üzgün" in m or "moral" in m:
        st.warning(f"🤖 **Cnclime:** {random.choice(dert_cevaplari['sıkkın'])}")

    # Kötüyüm Uyarısı
    elif m in ["kötüyüm", "kotuyum", "iyi değilim"]:
        st.error("🤖 **Cnclime:** Kendini hemen düzelt şef! Biz burada bir aileyiz. ❤️ Lütfen ne olduğunu anlat.")

    # İyiyim/Nasılsın
    elif m == "nasılsın" or m == "nasılsın?":
        st.write("🤖 **Cnclime:** Muq şef! Sen nasılsın?")
        st.balloons()

    elif m in ["iyiyim", "iyi", "muq"]:
        st.write("🤖 **Cnclime:** Harika! Senin iyi olmana çok sevindim. 🙌")
        st.snow()

    # --- 2. ARAŞTIRMA (Eğer dert değilse) ---
    else:
        with st.spinner('🤖 Cnclime araştırıyor...'):
            try:
                arama = wikipedia.search(mesaj)
                if arama:
                    en_yakin = arama[0]
                    bilgi = wikipedia.summary(en_yakin, sentences=2)
                    st.subheader(f"📖 {en_yakin}:")
                    st.success(bilgi)
                else:
                    st.warning("🤖 Bunu tam anlayamadım ama yanındayım kanka!")
            except:
                st.error("🤖 Şu an kafam karıştı, tekrar dener misin?")

st.markdown("---")
st.caption("Cnclime Akıllı Sistemleri - Mehmet Emin & Ekibi")
