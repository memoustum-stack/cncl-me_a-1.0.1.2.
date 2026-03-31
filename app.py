import streamlit as st
import wikipedia
import random

# Wikipedia dili Türkçe ve Hata Korumalı
try:
    wikipedia.set_lang("tr")
except:
    pass

# Sayfa Ayarları
st.set_page_config(
    page_title="Cnclime AI v36", 
    page_icon="🍋", 
    layout="wide"
)

# --- SİSTEM HAFIZASI ---
if 'kullanici_adi' not in st.session_state:
    st.session_state.kullanici_adi = ""

# --- GİRİŞ EKRANI ---
if st.session_state.kullanici_adi == "":
    st.title("🤖 Cnclime AI v36 🍋")
    st.divider()
    st.image("https://images.unsplash.com/photo-1677442136019-21780ecad995?q=80&w=400&auto=format&fit=crop", caption="Yapay Zeka Gücüyle!", width=350)
    
    st.subheader("Hoş Geldin! İsmini öğrenebilir miyim?")
    isim = st.text_input("İsmin nedir şef?", placeholder="Buraya yaz...", key="v36_login_input")
    
    if isim:
        st.session_state.kullanici_adi = isim.title()
        st.rerun()
    st.stop()

k_adi = st.session_state.kullanici_adi

# --- YAN MENÜ (MODLAR) ---
st.sidebar.title(f"👋 Selam {k_adi}! 🍋")
st.sidebar.image("https://images.unsplash.com/photo-1568471120021-9966d540306c?q=80&w=150&auto=format&fit=crop", width=120)
st.sidebar.divider()

mod = st.sidebar.radio(
    "Modlar", 
    ["💬 AI Sohbet", "🔍 Derin Araştırma", "🔢 Matematik Üstadı", "👥 Geliştirici Ekip"]
)

st.sidebar.divider()
if st.sidebar.button("🗑️ Çıkış Yap"):
    st.session_state.kullanici_adi = ""
    st.rerun()

# --- ANA EKRAN ---
st.title(f"🍋 {mod}")
st.divider()

# --- MOD 1: AI SOHBET (AKILLI & GIYBET KARŞITI) ---
if mod == "💬 AI Sohbet":
    st.write(f"Selam {k_adi}, seni dinliyorum. Gerçek bir AI gibi seninle sohbet etmeye hazırım.")
    u_input = st.text_input("Bana bir şeyler yaz:", placeholder="Naber? / Ne yapıyorsun?", key="v36_chat_key")

    if u_input:
        m = u_input.lower().strip()
        
        # 1. Gıybet / Kral / Dedikodu Filtresi
        if any(x in m for x in ["kral", "gıybet", "dedikodu", "duydun mu"]):
            st.warning(f"⚠️ **Uyarı:** Bak {k_adi}, 'kral' mral diyoruz ama birinin arkasından konuşmak gıybete girer. Gıybet kul hakkıdır, yakışmaz bize! Başka şey konuşalım. ❤️")
        
        # 2. Ayna Kuralı & Bro Modu (Sadece sen dersen)
        elif "bro" in m:
            st.info(f"🤖 **Cnclime:** İyidir bro, takılıyoruz işte. Sende ne var ne yok? 🔥")
        
        # 3. Selamlaşma ve Kısa Cevaplar (Saçmalamayı Engelleme)
        elif any(x in m for x in ["selam", "sa", "nbr", "naber", "merhaba"]):
            cevaplar = [f"Selam {k_adi}, nasılsın?", f"Merhabalar {k_adi}, her şey yolunda mı?", "Selam şef, seni dinliyorum!"]
            st.write(f"🤖 **Cnclime:** {random.choice(cevaplar)}")
        
        # 4. Genel Sohbet Akışı
        else:
            if len(m) < 5:
                st.write(f"🤖 **Cnclime:** Seni can kulağıyla dinliyorum {k_adi}, anlat bakalım...")
            else:
                st.write(f"🤖 **Cnclime:** Bu dediğin gerçekten ilginç bir bakış açısı. Üzerine biraz daha konuşalım mı?")

# --- MOD 2: DERİN ARAŞTIRMA (HATASIZ BİLGİ) ---
elif mod == "🔍 Derin Araştırma":
    st.write(f"Neyi öğrenmek istiyorsun {k_adi}? İnternetin altını üstüne getireyim! 🕵️‍♂️")
    ara = st.text_input("Araştırma konusu:", placeholder="Örn: Yapay zeka nedir?", key="v36_search_key")
    if ara:
        with st.spinner("🕵️‍♂️ En doğru bilgi taranıyor..."):
            try:
                # Sadece en alakalı bilgiyi getirir
                wiki_res = wikipedia.summary(ara, sentences=3)
                st.success(f"🤖 **Kesin Bilgi:**")
                st.write(wiki_res)
            except:
                st.error("🤖 Üzgünüm şef, buna dair net bir veri bulamadım.")

# --- MOD 3: MATEMATİK ÜSTADI ---
elif mod == "🔢 Matematik Üstadı":
    st.write(f"Zor soruları bana bırak {k_adi}! 🧠")
    mat = st.text_input("İşlemi yaz (Örn: 50*2/5):", key="v36_math_key")
    if mat:
        try:
            # İşlemi temizle ve hesapla
            islem = mat.replace("x", "*").replace(",", ".")
            sonuc = eval(islem)
            st.success(f"🤖 **Hesaplama Sonucu:** **{sonuc}**")
        except:
            st.error("Bunu hesaplayamadım, sayıları ve işaretleri kontrol et.")

# --- MOD 4: EKİP ---
elif mod == "👥 Geliştirici Ekip":
    st.info("🚀 Bu yapay zeka projesi şu efsane kadro tarafından geliştirildi:")
    st.success("👑 Mehmet Emin (Kurucu) | 🔥 Emre Can | ⚡ Ömer Eymen | 🌟 Yunus Emre")

st.divider()
st.caption(f"© 2026 Cnclime AI | v36 | Kullanıcı: {k_adi}")
