import streamlit as st
import wikipedia
import random

# Wikipedia ayarını Türkçe yap
try:
    wikipedia.set_lang("tr")
except:
    pass

st.set_page_config(page_title="Cnclime: Muq Edition", page_icon="😎")

# --- RASTGELE CEVAP HAVUZLARI (Sohbeti Canlandıran Kısım) ---
nasilsin_cevaplari = [
    "Muq şef, sen nasılsın? 😎",
    "Fişek gibiyim! Piksellerim yanıyor! 🔥",
    "Efsaneyim! Ekip (Mehmet Emin, Emre Can, Ömer Eymen, Yunus Emre) sağ olsun! 🚀",
    "Bomba gibiyim, internetin altını üstüne getirmeye hazırım! 💣",
    "Gıcır gıcır çalışıyorum, senin keyifler nasıl? ✨"
]

iyiyim_cevaplari = [
    "Adamsın! Senin iyi olmana çok sevindim. 👑",
    "Süper! O zaman bugün yeni bir şeyler öğrenme vakti! 📚",
    "Harika! Ekip tam kadro iyiyse ben de uçuyorum! ✈️",
    "Muq haber! Hadi bir şeyler aratalım! 🔍"
]

# Başlık ve Yan Menü
st.title("😎 Cnclime: Muq v10")
st.sidebar.title("🚀 Efsane Kadro")
st.sidebar.info("Mehmet Emin\n\nEmre Can\n\nÖmer Eymen\n\nYunus Emre")

# Kullanıcı Girişi
mesaj = st.text_input("Cnclime'a bir şeyler yaz:", placeholder="Nasılsın? / İyiyim / Mars nedir?")

if mesaj:
    m = mesaj.lower().strip()
    
    # --- 1. KISIM: SAMİMİ SOHBET MODÜLÜ ---
    
    if m == "nasılsın" or m == "nasılsın?":
        cevap = random.choice(nasilsin_cevaplari)
        st.write(f"🤖 **Cnclime:** {cevap}")
        if "muq" in cevap.lower():
            st.balloons() # Muq cevabı gelince balonlar uçsun!

    elif m == "iyiyim" or m == "iyi" or m == "muq":
        st.write(f"🤖 **Cnclime:** {random.choice(iyiyim_cevaplari)}")
        st.snow() # İyiysen kar yağsın!

    elif "naber" in m:
        st.write("🤖 **Cnclime:** İyidir be kanka, takılıyoruz piksellerin arasında! Sende ne var ne yok?")

    elif "merhaba" in m or "selam" in m:
        st.write("🤖 **Cnclime:** Selam ekip! Bugün hangi bilgiyi patlatıyoruz?")

    # --- 2. KISIM: AKILLI ARAŞTIRMA VE HATA DÜZELTME ---
    else:
        with st.spinner('🤖 Cnclime internete dalıyor... 🔍'):
            try:
                # İnternette en yakın sonuçları ara
                arama = wikipedia.search(mesaj)
                if arama:
                    en_yakin = arama[0]
                    
                    # Eğer kullanıcı yanlış yazdıysa uyar (Örn: Atatrk -> Atatürk)
                    if en_yakin.lower() != m:
                        st.caption(f"🤖 Sanırım şunu demek istedin: **{en_yakin}**")
                    
                    # Bilgiyi getir
                    bilgi = wikipedia.summary(en_yakin, sentences=2)
                    st.subheader(f"📖 {en_yakin} Hakkında Bilgi:")
                    st.success(bilgi)
                    
                    # Resim Linki (Google Görseller'e yönlendirir)
                    st.write(f"🖼️ [Buraya tıklayarak {en_yakin} resimlerine bakabilirsin](https://www.google.com/search?q={en_yakin}&tbm=isch)")
                else:
                    st.error("🤖 Bunu internette bulamadım kanka, başka bir şey yaz!")
            except:
                st.warning("🤖 Bağlantı koptu veya konu çok karışık şef!")

st.markdown("---")
st.caption("Cnclime v10.0 - Mehmet Emin, Emre Can, Ömer Eymen ve Yunus Emre Özel Üretimi")
