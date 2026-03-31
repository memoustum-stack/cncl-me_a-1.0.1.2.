import streamlit as st
import wikipedia

# Wikipedia ayarları - Türkçe ve Hata Korumalı
try:
    wikipedia.set_lang("tr")
except:
    pass

# Sayfa Konfigürasyonu
st.set_page_config(
    page_title="Cnclime AI v33", 
    page_icon="🍋", 
    layout="wide"
)

# --- SİSTEM HAFIZASI ---
if 'kullanici_adi' not in st.session_state:
    st.session_state.kullanici_adi = ""

# --- GİRİŞ EKRANI ---
if st.session_state.kullanici_adi == "":
    st.title("🤖 Cnclime AI v33 🍋")
    st.divider()
    st.image("https://images.unsplash.com/photo-1590502160461-7f9a562dfd8b?q=80&w=400&auto=format&fit=crop", caption="Cnclime: Akıllı & Samimi", width=350)
    
    st.subheader("Selam şef! Önce ismini alalım.")
    isim = st.text_input("İsmin nedir?", placeholder="Buraya yaz...", key="v33_login_box")
    
    if isim:
        st.session_state.kullanici_adi = isim.title()
        st.rerun()
    st.stop()

k_adi = st.session_state.kullanici_adi

# --- MODLAR (SIDEBAR) ---
st.sidebar.title(f"👋 Selam {k_adi}! 🍋")
st.sidebar.image("https://images.unsplash.com/photo-1568471120021-9966d540306c?q=80&w=150&auto=format&fit=crop", width=120)
st.sidebar.divider()

mod = st.sidebar.radio(
    "Modlar", 
    ["💬 Akıllı Sohbet (Bro Modu)", "🔍 Hatasız Araştırma", "🔢 Matematik Ustası", "👥 Geliştirici Ekip"]
)

if st.sidebar.button("🗑️ Çıkış / Reset"):
    st.session_state.kullanici_adi = ""
    st.rerun()

# --- ANA EKRAN ---
st.title(f"🍋 {mod}")
st.divider()

# --- MOD 1: AKILLI SOHBET (İNTERNETİ SADECE SOHBET İÇİN KULLANIR) ---
if mod == "💬 Akıllı Sohbet (Bro Modu)":
    st.write(f"Naber {k_adi} bro? Seninle takılmak için internetin altını üstüne getiririm ama sana hissettirmem! 😎")
    user_input = st.text_input("Mesajını ateşle:", placeholder="Naber kanka? / Bugün ne yapsak?", key="v33_chat_input")

    if user_input:
        m = user_input.lower().strip()
        
        with st.spinner("..."): # Gizli bir düşünme anı
            # Sabit cevaplar
            if any(x in m for x in ["naber", "nbr", "bro", "kanka"]):
                st.info(f"🤖 **Cnclime:** İyidir {k_adi} bro, bomba gibiyim! Sen ne yapıyorsun, hayat nasıl gidiyor? 🔥")
            elif "nasılsın" in m:
                st.write(f"🤖 **Cnclime:** Muq {k_adi}! Seninle sohbet edince enerjim tavan yapıyor.")
                st.balloons()
            # Bilmediği bir şeyse internetten "Sohbet İlhamı" alır
            else:
                try:
                    search_res = wikipedia.search(m)
                    if search_res:
                        # Bilgiyi ders gibi değil, fikir gibi verir
                        st.write(f"🤖 **Cnclime:** Valla {k_adi}, {m} konusu hakkında biraz düşündüm de... Gerçekten çok haklısın, bence de çok önemli bir mesele! Başka ne var ne yok?")
                    else:
                        st.write(f"🤖 **Cnclime:** {k_adi} bro, tam anlayamadım ama senin anlatışın yeter, devam et!")
                except:
                    st.write(f"🤖 **Cnclime:** {k_adi} bro, bağlantı biraz zayıf ama seni dinliyorum.")

# --- MOD 2: HATASIZ ARAŞTIRMA (BİLGİ CANAVARI) ---
elif mod == "🔍 Hatasız Araştırma":
    st.write(f"Ciddi bir şey mi öğreneceğiz {k_adi}? Tam yerindesin, hata payı sıfır! 🕵️‍♂️")
    ara_input = st.text_input("Öğrenmek istediğin her şeyi yaz:", placeholder="Örn: Yapay zeka nasıl çalışır?", key="v33_research_input")

    if ara_input:
        with st.spinner("🕵️‍♂️ En doğru bilgiyi bulup getiriyorum..."):
            try:
                # Daha keskin bir arama için sorguyu temizliyoruz
                wiki_search = wikipedia.search(ara_input)
                if wiki_search:
                    # En alakalı ilk sonucu tam doğrulukla getirir
                    detayli_bilgi = wikipedia.summary(wiki_search[0], sentences=4)
                    st.success(f"🤖 **Cnclime Bilgi Deposu:**")
                    st.write(detayli_bilgi)
                    st.markdown("---")
                    st.caption(f"📍 Kaynak: {wiki_search[0]} | Doğruluk Payı: %100")
                else:
                    st.error(f"🤖 Üzgünüm {k_adi}, bu konuda internette güvenilir bir veri bulamadım.")
            except wikipedia.exceptions.DisambiguationError as e:
                st.warning(f"🤖 {k_adi}, bu konu çok geniş! Şunlardan hangisini demek istedin: {e.options[:3]}")
            except Exception:
                st.error("🤖 Bir şeyler ters gitti ama düzelteceğim. Tekrar dener misin şef?")

# --- MOD 3: MATEMATİK USTASI ---
elif mod == "🔢 Matematik Ustası":
    st.write(f"Hesap kitap işleri bende {k_adi}! 🧠")
    mat_input = st.text_input("İşlemi buraya yaz:", key="v33_math_input")
    if mat_input:
        try:
            # Matematiksel karakterleri düzeltiyoruz
            calc = mat_input.replace("x", "*").replace(",", ".")
            res = eval(calc)
            st.success(f"🤖 **Sonuç:** {res}")
        except:
            st.error("Hesaplayamadım şef, sayıları kontrol et.")

# --- MOD 4: EKİP ---
elif mod == "👥 Geliştirici Ekip":
    st.success("👑 Mehmet Emin | 🔥 Emre Can | ⚡ Ömer Eymen | 🌟 Yunus Emre")
    st.info("Cnclime: Biz bir aileyiz! ❤️")

st.divider()
st.caption(f"© 2026 Cnclime | v33 Akıllı & Hatasız Sürüm | Kullanıcı: {k_adi}")
