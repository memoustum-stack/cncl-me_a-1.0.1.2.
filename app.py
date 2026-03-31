import streamlit as st
import wikipedia
import random

# Wikipedia dilini Türkçe yap
try:
    wikipedia.set_lang("tr")
except:
    pass

st.set_page_config(page_title="Cnclime Süper Zeka", page_icon="🧠")

# --- GÜNÜN GÖREVİ SİSTEMİ ---
gorevler = [
    "Bugün Python'da yeni bir kelime öğren! 🐍",
    "Ekipçe birbirinize bir teknoloji terimi sorun! 💡",
    "En zor soruyu kim soracak? Yarışın! 🏆",
    "Bir bardak su iç ve kod yazmaya devam et! 💧"
]

st.title("🧠 Cnclime: Süper Zeka v9")
st.sidebar.title("🚀 Geliştirici Ekip")
st.sidebar.info("Mehmet Emin\n\nEmre Can\n\nÖmer Eymen\n\nYunus Emre")
st.sidebar.markdown("---")
st.sidebar.subheader("🌟 Günün Görevi:")
st.sidebar.warning(random.choice(gorevler))

# Kullanıcıdan mesaj alma
mesaj = st.text_input("Cnclime ile konuş veya bir şey ara:", placeholder="Naber? / İstanbul hava durumu / Mars")

if mesaj:
    m = mesaj.lower().strip()
    
    # --- SOHBET KISMI ---
    if "naber" in m:
        st.write("🤖 **Cnclime:** İyidir şef! Ekip sayesinde her gün daha zekiyim. Senden naber?")
        st.balloons()
    
    elif "iyiyim" in m:
        st.write("🤖 **Cnclime:** Harika! Senin iyi olman beni de mutlu etti şef! ⚡")
        st.snow()

    elif "hava durumu" in m or "hava nasıl" in m:
        st.write(f"🤖 **Cnclime:** Şu an {mesaj} için internete bakıyorum... Bence ekipçe kod yazmak için harika bir hava var! ✨")
        st.info("İpucu: Gerçek hava durumu için Google'da 'hava durumu' diye aratabilirsin!")

    # --- ARAŞTIRMA VE HATA DÜZELTME KISMI ---
    else:
        with st.spinner('🤖 Cnclime araştırıyor...'):
            try:
                # İnternette en yakın sonuçları ara
                arama = wikipedia.search(mesaj)
                if arama:
                    en_yakin = arama[0]
                    # Hata düzeltme uyarısı
                    if en_yakin.lower() != m:
                        st.caption(f"🤖 Bunu mu demek istedin: **{en_yakin}**?")
                    
                    # Bilgiyi getir
                    bilgi = wikipedia.summary(en_yakin, sentences=2)
                    st.subheader(f"📖 {en_yakin} Hakkında Bilgi:")
                    st.success(bilgi)
                    
                    # Resim Linki Oluştur (Basit Yöntem)
                    st.write(f"🖼️ [Buraya tıklayarak {en_yakin} resimlerine bakabilirsin](https://www.google.com/search?q={en_yakin}&tbm=isch)")
                else:
                    st.error("🤖 Üzgünüm, bunu internette bulamadım!")
            except:
                st.warning("🤖 Bağlantı hatası! Lütfen tekrar dene.")

st.markdown("---")
st.caption("Cnclime v9.0 - Mehmet Emin & Ekibi") import streamlit as st
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
