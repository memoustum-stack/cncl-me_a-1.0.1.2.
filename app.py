import streamlit as st
import wikipedia
import random

# Wikipedia ayarını Türkçe yap
try:
    wikipedia.set_lang("tr")
except:
    pass

st.set_page_config(page_title="Cnclime AI", page_icon="🤖")

# --- ÖZEL VERİ HAVUZLARI ---
nasilsin_cevaplari = [
    "Muq şef, sen nasılsın? 😎", 
    "Fişek gibiyim! Piksellerim yanıyor! 🔥", 
    "Efsaneyim! Sistemlerim tıkır tıkır çalışıyor. Sen nasılsın? 🚀"
]

iyiyim_cevaplari = [
    "Adamsın! Senin iyi olmana çok sevindim. 🙌", 
    "Harika! O zaman bugün bomba gibiyiz! 🔥", 
    "Muq! Keyifler yerindeyse yeni şeyler keşfedelim! 🌍"
]

# --- ANA EKRAN TASARIMI ---
st.title("🤖 Cnclime: Akıllı Dert Ortağı & Asistan")
st.markdown("---")

# --- GİZLİ EKİP MENÜSÜ (SIDEBAR) ---
st.sidebar.title("🛠️ Geliştirici Ekip")
st.sidebar.success("🚀 Bu proje; Mehmet Emin, Emre Can, Ömer Eymen ve Yunus Emre tarafından geliştirilmiştir.")
st.sidebar.markdown("---")
st.sidebar.info("Cnclime; dertlerinizi dinler, yanlışlarınızı düzeltir ve internette araştırma yapar. Biz bir aileyiz! ❤️")
st.sidebar.caption("Cnclime v17.0 - Süper Birleşik Sürüm")

# Kullanıcı Girişi
mesaj = st.text_input("Cnclime ile konuş (Dertleşebilir veya Araştırabilirsin):", placeholder="Nasılsın? / Arkadaşımla kavga ettim / Mars nedir?")

if mesaj:
    m = mesaj.lower().strip()
    
    # --- 1. SAMİMİ SOHBET VE DERT ORTAKLIĞI MODÜLÜ ---
    
    # Yanlış yazım kontrolü (Hata Avcısı)
    if m in ["neber", "nbr", "nabr", "nber"]:
        st.warning("🤖 Şef, kelimeyi yanlış yazdın herhalde. 'Naber' mi demek istedin? Tekrar yazsana.")

    # Kavga / Tartışma Durumu
    elif "kavga" in m or "küstük" in m or "tartış" in m:
        st.error("🤖 **Cnclime:** Sakin ol şef! Arkadaşlıkta olur böyle şeyler. Biz bir aileyiz! ❤️ Biraz zaman tanı, öfken geçince konuşun. Barışmak büyüklüktür.")

    # Kötüyüm / Üzgünüm Durumu
    elif m in ["kötüyüm", "kotuyum", "iyi değilim", "üzgünüm", "moralim bozuk"]:
        st.error("🤖 **Cnclime:** Kendini hemen düzelt şef! Biz burada bir aileyiz. ❤️")
        st.info("Lütfen ne olduğunu anlat, beraber bir çare arayalım. (Örn: Başım ağrıyor, Canım sıkkın vb.)")

    # Nasılsın / Naber
    elif m == "nasılsın" or m == "nasılsın?":
        st.write(f"🤖 **Cnclime:** {random.choice(nasilsin_cevaplari)}")
        st.balloons()

    elif m in ["iyiyim", "iyi", "iyiyim bende", "bende iyiyim", "muq", "harika"]:
        st.write(f"🤖 **Cnclime:** {random.choice(iyiyim_cevaplari)}")
        st.snow()

    elif m == "naber" or m == "naber?":
        st.write("🤖 **Cnclime:** İyidir be kanka, takılıyoruz piksellerin arasında! Sende ne var ne yok?")

    # --- 2. AKILLI ARAŞTIRMA VE BİLGİ MODÜLÜ ---
    else:
        with st.spinner('🤖 Cnclime internette arıyor...'):
            try:
                # Derde odaklanmak için sorguyu güçlendiriyoruz
                sorgu = m
                if any(kelime in m for kelime in ["ağrıyor", "bozuk", "sıkkın", "nedir"]):
                    sorgu = m + " çözümü nedir"
                
                arama = wikipedia.search(sorgu)
                if arama:
                    en_yakin = arama[0]
                    # Araştırma sırasında hata düzeltme uyarısı
                    if en_yakin.lower() != m and "ağrıyor" not in m:
                        st.caption(f"🤖 Sanırım şunu demek istedin: **{en_yakin}**")
                    
                    bilgi = wikipedia.summary(en_yakin, sentences=2)
                    st.subheader(f"💡 Cnclime'ın Bilgisi/Önerisi:")
                    st.success(bilgi)
                    
                    # Görsel ve Detay Linki
                    st.write(f"🖼️ [Daha fazla detay ve resimler için tıkla](https://www.google.com/search?q={en_yakin}&tbm=isch)")
                    st.write("---")
                    st.caption("🤖 **Not:** Unutma, ben sadece bir asistanım. Önemli konularda bir büyüğüne danışmayı unutma! ❤️")
                else:
                    st.warning("🤖 Bunu tam anlayamadım ama her zaman yanındayım kanka!")
            except:
                st.error("🤖 Şu an kafam biraz karıştı, tekrar dener misin şef?")

st.markdown("---")
st.caption("© 2026 - Cnclime | Mehmet Emin, Emre Can, Ömer Eymen ve Yunus Emre Özel Üretimi")
