import streamlit as st
import wikipedia
import random
import time

# --- SİSTEM ÇEKİRDEĞİ ---
try:
    wikipedia.set_lang("tr")
except:
    pass

# Sayfa Yapılandırması (Modern ve Temiz)
st.set_page_config(
    page_title="Cnclime AI v40", 
    page_icon="🍋", 
    layout="wide"
)

# --- BELLEK YÖNETİMİ ---
if 'user' not in st.session_state:
    st.session_state.user = ""
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []

# --- GİRİŞ EKRANI (İLK TEMAS) ---
if st.session_state.user == "":
    st.title("🤖 Cnclime AI v40 🧠")
    st.markdown("### Sisteme Erişim İçin Kimlik Doğrulaması Gerekiyor.")
    st.divider()
    
    col1, col2 = st.columns([1, 1])
    with col1:
        st.image("https://images.unsplash.com/photo-1550751827-4bd374c3f58b?q=80&w=400", caption="Zihin Katmanı Yükleniyor...")
    with col2:
        name = st.text_input("Sana nasıl hitap edeyim şef?", placeholder="İsmini buraya yaz ve Enter'a bas...", key="v40_login_key")
        if st.button("Zihni Uyandır 🚀"):
            if name:
                st.session_state.user = name.title()
                st.toast(f"Erişim Onaylandı. Hoş geldin {name}!", icon="🔓")
                time.sleep(1)
                st.rerun()
    st.stop()

u_name = st.session_state.user

# --- YAN MENÜ (KONTROL PANELİ) ---
with st.sidebar:
    st.title(f"👋 Selam {u_name}!")
    st.write("**Durum:** 🟢 Çevrimiçi")
    st.write("**Sürüm:** v40.0 (Zihin)")
    st.divider()
    mod = st.radio("Sistem Katmanları:", 
                   ["💬 Zihin Akışı (Sohbet)", "🔍 Evrensel Veri (Araştırma)", "🔢 Sayısal Mantık", "👥 Proje Mimarları"])
    st.divider()
    if st.button("Sistemi Kapat"):
        st.session_state.user = ""
        st.rerun()

# --- ANA PANEL ---
st.title(f"🍋 {mod}")
st.divider()

# --- MOD 1: ZİHİN AKIŞI (DOĞAL, SAMİMİ VE ZEKI SOHBET) ---
if mod == "💬 Zihin Akışı (Sohbet)":
    st.write(f"Anlat bakalım {u_name}, bugün zihninde neler var? Seni dinliyorum.")
    chat_input = st.text_input("Mesajını buraya bırak...", placeholder="Naber? / Selam / Bro...", key="v40_chat_key")

    if chat_input:
        m = chat_input.lower().strip()
        
        # 1. ETİK VE GIYBET FİLTRESİ (KRAL MODU)
        if any(x in m for x in ["kral", "gıybet", "dedikodu", "duydun mu"]):
            st.error(f"⚠️ **Sistem Uyarısı:** Dur bakalım {u_name}! 'Kral' falan diyoruz ama birinin arkasından konuşmak (gıybet) bize yakışmaz şef. Kul hakkıdır, girmeyelim o toplara. Başka güzel bir şey konuşalım. ❤️")
        
        # 2. SAMİMİ SELAMLAŞMA VE KARAKTER ADAPTASYONU
        elif any(x in m for x in ["selam", "sa", "merhaba", "as", "mrb"]):
            selamlar = [
                f"Aleykümselam {u_name}! Hoş geldin, başımın üstünde yerin var.", 
                f"Selam şef! Bugün senin için hangi bilgileri süzeyim?", 
                f"Merhabalar {u_name}, her şey yolunda mı? Anlat dinliyorum."
            ]
            st.success(f"🤖 {random.choice(selamlar)}")
            
        elif any(x in m for x in ["naber", "nbr", "nasıl gidiyor"]):
            cevaplar = [
                f"İyidir be {u_name}, seni gördüm daha iyi oldum! Sende ne var ne yok?",
                "Bomba gibiyim şef! İşlemcilerim tıkır tıkır çalışıyor. Senin keyifler nasıl?",
                "Uğraşıyoruz işte {u_name}, ekiple Cnclime'ı dünya markası yapmaya çalışıyoruz. Sende durumlar ne?"
            ]
            st.info(f"🤖 {random.choice(cevaplar)}")
            
        elif "bro" in m:
            st.write(f"🤖 **Cnclime:** İyidir brooo! Sen böyle deyince kendimi ekibin bir parçası gibi hissediyorum, eyvallah! 🔥")

        # 3. AKILLI ANALİZ (BOŞ KONUŞMAZ)
        else:
            with st.spinner("Zihin katmanları analiz ediliyor..."):
                time.sleep(0.5)
                if len(m) < 4:
                    st.write(f"🤖 **Cnclime:** Efendim {u_name}, bir şey mi diyecektin?")
                else:
                    st.write(f"🤖 **Cnclime:** {u_name}, bu söylediğin gerçekten ilginç. Üzerinde biraz kafa yormak lazım, anlatmaya devam et seni can kulağıyla dinliyorum.")

# --- MOD 2: EVRENSEL VERİ (HATASIZ VE DERİN ARAŞTIRMA) ---
elif mod == "🔍 Evrensel Veri (Araştırma)":
    st.write(f"Evrendeki tüm doğrulanmış bilgilere erişelim {u_name}. Ne sormak istersin?")
    ara = st.text_input("Bilgi anahtarı giriniz:", placeholder="Örn: Yapay zeka / İstanbul'un fethi", key="v40_search_key")
    if ara:
        with st.spinner("Evrensel veritabanına bağlanılıyor..."):
            try:
                # Önce en alakalı başlıkları bulur
                search_res = wikipedia.search(ara)
                if search_res:
                    # En doğru sonucu getirir
                    summary = wikipedia.summary(search_res[0], sentences=4)
                    st.success(f"✅ **Doğrulanmış Veri: {search_res[0]}**")
                    st.write(summary)
                    st.caption(f"Veri Kaynağı: Global Wikipedia DB | İşlem Başarılı.")
                else:
                    st.error(f"🤖 Üzgünüm {u_name}, bu konuda evrensel veritabanında net bir karşılık bulamadım.")
            except wikipedia.exceptions.DisambiguationError as e:
                st.warning(f"Bu konu çok genel şef. Şunlardan hangisini kastediyorsun? : {', '.join(e.options[:3])}")
            except Exception:
                st.error("Veri hattında bir aksaklık oldu şef, tekrar dener misin?")

# --- MOD 3: SAYISAL MANTIK (HATASIZ HESAPLAMA) ---
elif mod == "🔢 Sayısal Mantık":
    st.write(f"Matematik evrenin değişmez dilidir {u_name}. İşlemi bana bırak.")
    mat = st.text_input("Hesaplanacak işlem (Örn: 15*4/2):", key="v40_math_key")
    if mat:
        try:
            # Karakter temizleme ve güvenli hesaplama
            safe_calc = mat.replace("x", "*").replace(",", ".")
            res = eval(safe_calc)
            st.success(f"💡 **Mantıksal Sonuç:** **{res}**")
        except:
            st.error("Bu işlem sayısal mantığa aykırı şef, rakamları ve işaretleri kontrol et.")

# --- MOD 4: PROJE MİMARLARI ---
elif mod == "👥 Proje Mimarları":
    st.balloons()
    st.success("### 🚀 Cnclime v40 Mimari Kadrosu")
    st.write(f"**👑 Mehmet Emin** (Zihin Lideri & Proje Sahibi)")
    st.write(f"**🔥 Emre Can** (Algoritma Tasarım Uzmanı)")
    st.write(f"**⚡ Ömer Eymen** (Görsel Mimar & Arayüz)")
    st.write(f"**🌟 Yunus Emre** (Veri Yöneticisi & Analist)")
    st.divider()
    st.info("Bu sürüm; sıfır hata, maksimum samimiyet ve yapay zeka zekası ile donatılmıştır.")

st.divider()
st.caption(f"© 2026 Cnclime AI v40 | Zihin ve Mantık Entegrasyonu | Kullanıcı: {u_name}")
