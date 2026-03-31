import streamlit as st
import wikipedia

# Wikipedia dili Türkçe
try:
    wikipedia.set_lang("tr")
except:
    pass

# Sayfa Ayarları
st.set_page_config(page_title="Cnclime AI v34", page_icon="🍋", layout="wide")

# --- SİSTEM HAFIZASI ---
if 'kullanici_adi' not in st.session_state:
    st.session_state.kullanici_adi = ""

# --- GİRİŞ EKRANI ---
if st.session_state.kullanici_adi == "":
    st.title("🤖 Cnclime AI v34 🍋")
    st.divider()
    st.image("https://images.unsplash.com/photo-1590502160461-7f9a562dfd8b?q=80&w=400&auto=format&fit=crop", width=350)
    isim = st.text_input("İsmin nedir şef?", key="v34_login_input")
    if isim:
        st.session_state.kullanici_adi = isim.title()
        st.rerun()
    st.stop()

k_adi = st.session_state.kullanici_adi

# --- MODLAR (SIDEBAR) ---
st.sidebar.title(f"👋 Selam {k_adi}!")
st.sidebar.image("https://images.unsplash.com/photo-1568471120021-9966d540306c?q=80&w=150&auto=format&fit=crop", width=120)
mod = st.sidebar.radio("Modlar", ["💬 Akıllı Sohbet", "🔍 Hatasız Araştırma", "🔢 Matematik Ustası", "👥 Ekip"])

if st.sidebar.button("🗑️ Çıkış"):
    st.session_state.kullanici_adi = ""
    st.rerun()

# --- ANA EKRAN ---
st.title(f"🍋 {mod}")
st.divider()

# --- MOD 1: AKILLI SOHBET (ADAPTİF & GIYBET KARŞITI) ---
if mod == "💬 Akıllı Sohbet":
    st.write(f"Selam {k_adi}, seni dinliyorum.")
    user_input = st.text_input("Mesajın:", key="v34_chat_input")

    if user_input:
        m = user_input.lower().strip()
        
        # 1. GIYBET KONTROLÜ (KRAL VE DİĞERLERİ)
        if "kral" in m or "duydun mu" in m or "şunun hakkında" in m:
            st.warning(f"🤖 **Cnclime:** Bak {k_adi}, 'kral' falan diyoruz ama arkadan konuşmak gıybete girer. Biz burada bilgi paylaşalım, kimsenin gıybetini yapmayalım. Yakışmaz bize! ❤️")
        
        # 2. AYNA KURALI (SEN NE dersen o)
        elif "bro" in m:
            st.info(f"🤖 **Cnclime:** İyidir bro, takılıyoruz işte. Sende ne var ne yok?")
        elif "naber" in m or "nbr" in m:
            st.write(f"🤖 **Cnclime:** İyilik {k_adi}, senden naber? Çalışmalara devam.")
        
        # 3. SAÇMA CEVAP ENGELİ
        else:
            # Eğer sadece kısa bir selamsa internete bakma saçmalamasın
            if len(m) < 5:
                st.write(f"🤖 **Cnclime:** Efendim {k_adi}, buyur buradayım.")
            else:
                st.write(f"🤖 **Cnclime:** Anladım {k_adi}, bu konuyu biraz daha açmak ister misin? Yoksa araştırmamı mı istersin?")

# --- MOD 2: HATASIZ ARAŞTIRMA ---
elif mod == "🔍 Hatasız Araştırma":
    ara_input = st.text_input("Öğrenmek istediğin konu:", key="v34_res_input")
    if ara_input:
        with st.spinner("🕵️‍♂️ En doğru bilgi taranıyor..."):
            try:
                # Rastgele değil, en alakalı sonucu getirir
                wiki_search = wikipedia.search(ara_input)
                if wiki_search:
                    bilgi = wikipedia.summary(wiki_search[0], sentences=3)
                    st.success(f"🤖 **Doğru Bilgi:**")
                    st.write(bilgi)
                else:
                    st.error("Buna dair bir veri bulamadım.")
            except:
                st.error("Bir hata oluştu, lütfen konuyu sade yaz.")

# --- DİĞER MODLAR ---
elif mod == "🔢 Matematik Ustası":
    mat = st.text_input("İşlem:", key="v34_math")
    if mat:
        try:
            st.success(f"Sonuç: {eval(mat.replace('x', '*'))}")
        except: st.error("Hata!")

elif mod == "👥 Ekip":
    st.success("👑 Mehmet Emin | 🔥 Emre Can | ⚡ Ömer Eymen | 🌟 Yunus Emre")

st.divider()
st.caption(f"© 2026 Cnclime | v34 | Kullanıcı: {k_adi}")
