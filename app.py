import streamlit as st
import wikipedia
import requests
import io
from PIL import Image

# --- SAYFA AYARLARI ---
st.set_page_config(page_title="Cnclime AI", page_icon="🤖", layout="centered")

# --- TASARIM VE EKİP BİLGİSİ ---
st.title("🤖 Cnclime Süper Yapay Zeka")
st.markdown("### Geliştirici Ekip:")
st.info("🚀 Mehmet Emin Üstün | Emre Can Günel | Ömer Eymen Atsayar | Yunus Emre Uysal")
st.write("---")

# Wikipedia Dil Ayarı
wikipedia.set_lang("tr")

# --- MENÜ SEÇENEKLERİ ---
menu = ["Ana Sayfa & Sohbet", "İnternetten Araştır", "Yapay Zekaya Resim Çizdir"]
secim = st.sidebar.selectbox("Menü", menu)

# 1. BÖLÜM: ANA SAYFA VE SOHBET
if secim == "Ana Sayfa & Sohbet":
    st.subheader("Cnclime ile Sohbet Et")
    kullanici_mesaji = st.text_input("Mesajınızı yazın:")
    
    if kullanici_mesaji:
        mesaj = kullanici_mesaji.lower()
        if "seni kim yaptı" in mesaj or "yapımcın kim" in mesaj:
            st.success("Beni harika bir ekip olan Mehmet Emin Üstün, Emre Can Günel, Ömer Eymen Atsayar ve Yunus Emre Uysal yaptı!")
        elif "nasılsın" in mesaj:
            st.write("🤖 Cnclime: Harikayım! Sen nasılsın?")
        elif "merhaba" in mesaj or "selam" in mesaj:
            st.write("🤖 Cnclime: Selam dostum! Bugün senin için ne yapabilirim?")
        else:
            st.write("🤖 Cnclime: Bunu henüz tam bilmiyorum ama arkadaşlarımla beni geliştirmeye devam edebilirsin!")

# 2. BÖLÜM: İNTERNETTEN ARAŞTIRMA
elif secim == "İnternetten Araştır":
    st.subheader("🔍 Bilgi Bankası")
    konu = st.text_input("Hangi konuyu merak ediyorsun? (Örn: Mars, Aslan, Robotlar)")
    
    if st.button("Araştır"):
        if konu:
            with st.spinner('İnternette aranıyor...'):
                try:
                    ozet = wikipedia.summary(konu, sentences=3)
                    st.write("### Bulduğum Bilgiler:")
                    st.success(ozet)
                except wikipedia.exceptions.PageError:
                    st.error("Üzgünüm, bu konuda bir şey bulamadım.")
                except Exception as e:
                    st.error("Bir hata oluştu, lütfen tekrar dene.")

# 3. BÖLÜM: RESİM ÇİZDİRME
elif secim == "Yapay Zekaya Resim Çizdir":
    st.subheader("🎨 Hayalindekini Çiz")
    st.write("Not: İngilizce yazmak daha iyi sonuç verir.")
    istek = st.text_input("Ne çizmemi istersin? (Örn: A futuristic city, a flying cat)")
    
    if st.button("Resmi Oluştur"):
        if istek:
            st.warning("Resim çiziliyor, lütfen 10-15 saniye bekle...")
            # Ücretsiz resim çizme API'si (Hugging Face)
            API_URL = "https://api-inference.huggingface.co/models/runwayml/stable-diffusion-v1-5"
            headers = {"Authorization": "Bearer hf_placeholder"} # Burayı böyle bırakabilirsin
            
            try:
                response = requests.post(API_URL, headers=headers, json={"inputs": istek})
                image_bytes = response.content
                image = Image.open(io.BytesIO(image_bytes))
                st.image(image, caption=f"Cnclime Çizimi: {istek}")
            except:
                st.error("Resim çizme sunucusu şu an meşgul. Lütfen biraz sonra tekrar dene.")import streamlit as st
import wikipedia

# Wikipedia dil ayarı
wikipedia.set_lang("tr")

st.set_page_config(page_title="Cnclime Sohbet Robotu", page_icon="💬")

st.title("💬 Cnclime: Akıllı Asistan")
st.sidebar.info("Geliştiriciler: Mehmet Emin, Emre Can, Ömer Eymen, Yunus Emre")

# Kullanıcıdan gelen mesaj
mesaj = st.text_input("Cnclime'a bir şey yaz:", placeholder="Nasılsın? / İyiyim / Naber?")

if mesaj:
    m = mesaj.lower().strip() # Mesajı küçük harf yap ve boşlukları sil
    
    # --- KARŞILIKLI DİYALOG KISMI ---
    
    if m == "nasılsın" or m == "nasılsın?":
        st.write("🤖 **Cnclime:** Bomba gibiyim şef! Piksellerim tıkır tıkır çalışıyor. **Peki sen nasılsın?**")
        st.info("İpucu: 'İyiyim' yazarak cevap verebilirsin!")

    elif m == "iyiyim" or m == "iyi" or m == "çok şükür iyiyim":
        st.balloons() # Sen iyiysen kutlama yapalım!
        st.write("🤖 **Cnclime:** Harika! Senin iyi olmana çok sevindim. Mehmet Emin ve ekibi (Emre Can, Ömer Eymen, Yunus Emre) mutluysa ben de mutluyum! 🚀")
        st.success("Enerji tavan!")

    elif "naber" in m or "ne haber" in m:
        st.write("🤖 **Cnclime:** İyidir şef, takılıyorum öyle internet kablolarının arasında. Senden naber?")

    elif "merhaba" in m or "selam" in m:
        st.write("🤖 **Cnclime:** Selam ekip! Bugün neyi araştırıyoruz?")

    # --- İNTERNETTEN ARAŞTIRMA MODU ---
    else:
        with st.spinner('Cnclime internette araştırıyor... 🔍'):
            try:
                bilgi = wikipedia.summary(mesaj, sentences=2)
                st.subheader("📖 Bulduğum Bilgi:")
                st.info(bilgi)
            except:
                st.warning("🤖 Bunu tam anlayamadım şef. Ama 'Nasılsın' dersen seninle sohbet edebilirim!")

st.markdown("---")
st.caption("Cnclime v6.0 - Karşılıklı Sohbet Modülü")import streamlit as st
import wikipedia

# Wikipedia dil ayarı ve arama derinliği
wikipedia.set_lang("tr")

st.set_page_config(page_title="Cnclime Akıllı Robot", page_icon="🧠")

st.title("🧠 Cnclime: Süper Zeka v7")
st.sidebar.info("Yazılımcılar: Mehmet Emin, Emre Can, Ömer Eymen, Yunus Emre")

# Kullanıcıdan gelen mesaj
mesaj = st.text_input("Cnclime'a bir şey yaz veya araştır:", placeholder="Nasılsın? / Atytürk / Mars")

if mesaj:
    m = mesaj.lower().strip()
    
    # --- ÖZEL SOHBET DİLOGLARI ---
    if m == "nasılsın" or m == "nasılsın?":
        st.write("🤖 **Cnclime:** Bomba gibiyim şef! Piksellerim tıkır tıkır çalışıyor. **Peki sen nasılsın?**")
    
    elif m == "iyiyim" or m == "iyi" or m == "çok şükür iyiyim":
        st.balloons()
        st.write("🤖 **Cnclime:** Harika! Senin iyi olmana çok sevindim. Ekip mutluysa ben de mutluyum! 🚀")

    elif "naber" in m:
        st.write("🤖 **Cnclime:** İyidir şef, takılıyorum öyle internet kablolarının arasında. Senden naber?")

    # --- AKILLI İNTERNET ARAŞTIRMASI (Hata Düzeltmeli) ---
    else:
        with st.spinner('Cnclime en doğru bilgiyi arıyor... 🔍'):
            try:
                # Önce kelimeyi doğrula veya en yakın sonucu bul
                arama_sonuclari = wikipedia.search(mesaj)
                
                if arama_sonuclari:
                    # En yakın kelimeyi seç (Hata düzeltme mantığı)
                    en_yakin_kelime = arama_sonuclari[0]
                    
                    if en_yakin_kelime.lower() != m:
                        st.caption(f"🤖 Bunu mu demek istediniz: **{en_yakin_kelime}**?")
                    
                    # Bilgiyi getir
                    bilgi = wikipedia.summary(en_yakin_kelime, sentences=2)
                    st.subheader(f"📖 {en_yakin_kelime} Hakkında Bilgi:")
                    st.info(bilgi)
                else:
                    st.warning("🤖 Üzgünüm, internette buna benzer bir şey bulamadım.")
            
            except wikipedia.exceptions.DisambiguationError as e:
                st.warning(f"🤖 Çok fazla sonuç var. Şunlardan birini mi demek istedin: {e.options[:3]}")
            except:
                st.error("🤖 Bir hata oluştu veya bu konu bulunamadı şef!")

st.markdown("---")
st.caption("Cnclime v7.0 - Otomatik Düzeltme ve Global Arama Aktif")
