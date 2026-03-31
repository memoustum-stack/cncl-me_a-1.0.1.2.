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
st.caption("Cnclime v9.0 - Mehmet Emin & Ekibi")
