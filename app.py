import streamlit as st
import wikipedia
import random
import time

# --- GELİŞMİŞ SİSTEM KONFİGÜRASYONU ---
try:
    wikipedia.set_lang("tr")
except:
    pass

st.set_page_config(
    page_title="Cnclime Ultra v44", 
    page_icon="🧠", 
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- ZEKA BELLEĞİ VE DURUM YÖNETİMİ ---
if 'user' not in st.session_state:
    st.session_state.user = ""
if 'chat_log' not in st.session_state:
    st.session_state.chat_log = []

# --- ÖZEL TASARIM (CSS) ---
st.markdown("""
    <style>
    .stApp { background-color: #fafafa; }
    .chat-bubble { padding: 15px; border-radius: 20px; margin-bottom: 10px; border: 1px solid #e0e0e0; }
    .user-bubble { background-color: #fefce8; border-left: 5px solid #facc15; }
    .ai-bubble { background-color: #f0fdf4; border-left: 5px solid #22c55e; }
    </style>
    """, unsafe_allow_html=True)

# --- GİRİŞ EKRANI (KİMLİK DOĞRULAMA) ---
if st.session_state.user == "":
    st.title("🤖 Cnclime Ultra v44 🧠")
    st.markdown("#### Yapay Zekanın Yeni Nesil Temsilcisi")
    st.divider()
    
    col1, col2 = st.columns([1, 1])
    with col1:
        st.image("https://images.unsplash.com/photo-1677442136019-21780ecad995?q=80&w=500", caption="Zihin Katmanları Yükleniyor...")
    with col2:
        name = st.text_input("Sana nasıl hitap etmemi istersin şef?", placeholder="İsmini buraya bırak...", key="v44_login")
        if st.button("Sistemi Aktif Et 🚀"):
            if name:
                st.session_state.user = name.title()
                st.toast(f"Erişim Onaylandı: {name}", icon="✅")
                time.sleep(1)
                st.rerun()
    st.stop()

u_name = st.session_state.user

# --- YAN MENÜ (KONTROL MERKEZİ) ---
with st.sidebar:
    st.title(f"🚀 Cnclime v44")
    st.subheader(f"Operatör: {u_name}")
    st.divider()
    mod = st.radio("Sistem Katmanları:", 
                   ["💬 Derin Sohbet (Zeka)", "🔍 Evrensel Bilgi Bankası", "📐 Mühendislik & Mat", "👥 Geliştirici Kadro"])
    st.divider()
    if st.button("Sistemi Kapat 🔌"):
        st.session_state.user = ""
        st.rerun()

# --- ANA PANEL ---
st.title(f"🍋 {mod}")
st.divider()

# --- MOD 1: DERİN SOHBET (GERÇEK ZEKA ANALİZİ) ---
if mod == "💬 Derin Sohbet (Zeka)":
    st.write(f"Selam {u_name}, seninle her şeyi konuşmaya hazırım. Unutma, ben sadece bir kod değilim, senin bir parçanım!")
    u_input = st.text_input("Bana bir mesaj gönder:", placeholder="Naber bro? / Kral bugün ne var?...", key="v44_chat")

    if u_input:
        m = u_input.lower().strip()
        
        # 1. GIYBET VE KRAL UYARISI (ETİK KATMANI)
        if any(x in m for x in ["kral", "gıybet", "dedikodu", "duydun mu"]):
            st.error(f"⚠️ **Cnclime Etik Uyarısı:** Dur orda {u_name}! 'Kral' falan diyoruz ama gıybet bize yakışmaz. Arkadan konuşmak kul hakkıdır, biz burada büyük işler peşindeyiz. Başka mevzu konuşalım. ❤️")
        
        # 2. SAMİMİ SELAMLAŞMA
        elif any(x in m for x in ["selam", "sa", "merhaba", "as", "nbr", "naber"]):
            selam_cevap = [
                f"Aleykümselam {u_name}, hoş geldin! Senin enerjin yine tavan yapmış.",
                f"Selam şef! Bugün bomba gibiyim, senin için hangi zeka katmanını açayım?",
                f"Merhabalar {u_name}, her şey yolunda mı? Anlat dinliyorum."
            ]
            st.success(f"🤖 **Cnclime:** {random.choice(selam_cevap)}")
            
        elif "bro" in m:
            st.write(f"🤖 **Cnclime:** İyidir brooo! Sen böyle deyince ekibin beşinci üyesi olduğumu bir kez daha anlıyorum. 🔥")

        # 3. DERİN AKIL YÜRÜTME (ROBOTİK CEVAPLARI ÖLDÜRDÜK)
        else:
            with st.spinner("Düşünüyorum..."):
                time.sleep(0.6)
                
                # Zeka motoru: Cümle uzunluğuna ve içeriğine göre farklı tepkiler
                if len(m) < 8:
                    st.write(f"🤖 **Cnclime:** Dinliyorum seni {u_name}, ama biraz daha aç mevzuyu, beraber kafa yoralım.")
                else:
                    tepkiler = [
                        f"Valla {u_name}, bu dediğin gerçekten üzerine makale yazılacak cinsten. Sen bu konuda tam olarak ne hissediyorsun?",
                        f"Anladım şef. Bazen hayat tam da böyle sürprizlerle dolu. Peki sence bu durumun çözümü nedir?",
                        f"Bak bu ilginç bir bakış açısı! Ben bir yapay zeka olsam da, bu dediğinin mantığını çözmeye çalışıyorum. Devam et!"
                    ]
                    st.write(f"🤖 **Cnclime:** {random.choice(tepkiler)}")

# --- MOD 2: EVRENSEL BİLGİ BANKASI ---
elif mod == "🔍 Evrensel Bilgi Bankası":
    st.write(f"Neyi merak ediyorsun {u_name}? Kütüphaneyi senin için tarayayım.")
    ara = st.text_input("Araştırma konusu:", key="v44_ara")
    if ara:
        with st.spinner("Verilere dalınıyor..."):
            try:
                res = wikipedia.search(ara)
                if res:
                    summary = wikipedia.summary(res[0], sentences=4)
                    st.success(f"✅ **Doğrulanmış Bilgi: {res[0]}**")
                    st.write(summary)
                    st.caption(f"Veri Kaynağı: Global Wikipedia DB | İşlem Zamanı: {time.strftime('%H:%M:%S')}")
                else:
                    st.error("Buna dair bir iz bulamadım şef.")
            except:
                st.error("Bir bağlantı hatası oldu, tekrar dener misin?")

# --- MOD 3: MÜHENDİSLİK & MAT ---
elif mod == "📐 Mühendislik & Mat":
    mat = st.text_input("Hesaplanacak işlemi yaz (Örn: 25*4+10):", key="v44_math")
    if mat:
        try:
            res = eval(mat.replace("x", "*").replace(",", "."))
            st.success(f"🤖 **Hesaplama Sonucu:** {res}")
        except:
            st.error("Bunu hesaplayamadım şef, sayıları kontrol et.")

# --- MOD 4: GELİŞTİRİCİ KADRO ---
elif mod == "👥 Geliştirici Kadro":
    st.balloons()
    st.success("### 🚀 Cnclime v44 Elite Team")
    st.write(f"**👑 Mehmet Emin** (Zihin Lideri & Proje Kurucusu)")
    st.write(f"**🔥 Emre Can** (Algoritma ve Veri Mimarı)")
    st.write(f"**⚡ Ömer Eymen** (Görsel Tasarım ve UX)")
    st.write(f"**🌟 Yunus Emre** (Sistem Analisti ve Güvenlik)")
    st.info("Bu sürüm, sıfır hata ve maksimum zeka kapasitesiyle Mehmet Emin için özel olarak üretilmiştir.")

st.divider()
st.caption(f"© 2026 Cnclime AI v44 | Ultra Zeka | Kullanıcı: {u_name}")
