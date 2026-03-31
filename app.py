import streamlit as st
import wikipedia

# Wikipedia dilini Türkçe yapıyoruz
wikipedia.set_lang("tr")

# Sayfa Ayarları
st.set_page_config(page_title="Cnclime AI Pro", page_icon="🧠")

# Başlık ve Ekip Bilgisi
st.title("🧠 Cnclime: Süper Zeka v7")
st.sidebar.title("🚀 Geliştirici Ekip")
st.sidebar.info("Mehmet Emin\n\nEmre Can\n\nÖmer Eymen\n\nYunus Emre")

# Kullanıcıdan mesaj alma
mesaj = st.text_input("Cnclime'a bir şey yaz (Sohbet et veya Araştır):", placeholder="Naber? / İyiyim / Mars nedir?")

if mesaj:
    m = mesaj.lower().strip()
    
    # --- 1. KISIM: ÖZEL SOHBET DİYALOGLARI ---
    if m == "naber" or m == "naber?" or m == "ne haber":
        st.write("🤖 **Cnclime:** İyidir şef! Mehmet Emin ve ekibi beni her gün geliştirdiği için keyfim yerinde. Senden naber?")
        st.balloons()
    
    elif m == "nasılsın" or m == "nasılsın?":
        st.write("🤖 **Cnclime:** Bomba gibiyim! Piksellerim tıkır tıkır çalışıyor. **Peki sen nasılsın?**")
        st.caption("Cevap olarak 'İyiyim' yazabilirsin!")

    elif m == "iyiyim" or m == "iyi" or m == "çok şükür iyiyim":
        st.write("🤖 **Cnclime:** Harika! Senin iyi olmana çok sevindim şef. Ekip mutluysa ben de mutluyum! 🚀")
        st.success("Enerji tavan! Hadi bir şeyler araştıralım.")

    elif m == "merhaba" or m == "selam":
        st.write("🤖 **Cnclime:** Selam ekip! Bugün internetin altını üstüne getirmeye hazır mısınız?")

    elif "kim yaptı" in m or "yapımcı" in m:
        st.write("🤖 **Cnclime:** Beni bölgenin en sağlam ekibi yaptı: **Mehmet Emin, Emre Can, Ömer Eymen ve Yunus Emre!** 🏆")

    # --- 2. KISIM: AKILLI İNTERNET ARAŞTIRMASI (HATA DÜZELTMELİ) ---
    else:
        with st.spinner('Cnclime en doğru bilgiyi arıyor... 🔍'):
            try:
                # Önce internette benzer başlıkları ara (Hata düzeltme için)
                arama_sonuclari = wikipedia.search(mesaj)
                
                if arama_sonuclari:
                    # En yakın sonucu seç
                    en_yakin = arama_sonuclari[0]
                    
                    # Eğer kullanıcı yanlış yazdıysa uyar
                    if en_yakin.lower() != m:
                        st.warning(f"🤖 Bunu mu demek istediniz: **{en_yakin}**?")
                    
                    # Bilgiyi getir
                    bilgi = wikipedia.summary(en_yakin, sentences=2)
                    st.subheader(f"📖 {en_yakin} Hakkında Bilgi:")
                    st.info(bilgi)
                else:
                    st.error("🤖 Üzgünüm, internette buna benzer bir şey bulamadım.")
            
            except Exception:
                st.warning("🤖 Bir hata oluştu veya konu çok karmaşık. Daha basit bir kelime yaz şef!")

# Sayfa Altı Bilgisi
st.markdown("---")
st.caption("Cnclime v7.0 - Mehmet Emin, Emre Can, Ömer Eymen ve Yunus Emre Özel Üretimi")
