import streamlit as st
import wikipedia
import random
import time

# --- SİSTEM AYARLARI ---
try:
    wikipedia.set_lang("tr")
except:
    pass

st.set_page_config(page_title="Cnclime v43 | Öz-Zeka", page_icon="🍋", layout="wide")

# --- ZEKA BELLEĞİ ---
if 'user' not in st.session_state:
    st.session_state.user = ""
if 'mesaj_sayisi' not in st.session_state:
    st.session_state.mesaj_sayisi = 0

# --- GİRİŞ EKRANI ---
if st.session_state.user == "":
    st.title("🤖 Cnclime AI v43 🧠")
    st.subheader("Gerçek Bir Zeka Deneyimi Başlıyor...")
    st.divider()
    
    name = st.text_input("Selam şef! Ben Cnclime. Senin ismin neydi?", placeholder="İsmini buraya bırak...", key="v43_login")
    if st.button("Zihni Başlat 🚀"):
        if name:
            st.session_state.user = name.title()
            st.balloons()
            st.rerun()
    st.stop()

u_name = st.session_state.user

# --- YAN MENÜ (PROFESYONEL PANEL) ---
with st.sidebar:
    st.title(f"👋 {u_name}")
    st.write("**Zeka Katmanı:** Aktif 🧠")
    st.write(f"**Muhabbet Skoru:** {st.session_state.mesaj_sayisi}")
    st.divider()
    mod = st.sidebar.radio("Sistem Katmanları:", ["💬 Gerçek Sohbet", "🔍 Derin Bilgi Bankası", "📐 Matematik & Mantık", "👥 Geliştirici Ekip"])
    st.divider()
    if st.sidebar.button("Sistemi Kapat"):
        st.session_state.user = ""
        st.rerun()

# --- ANA PANEL ---
st.title(f"🍋 {mod}")
st.divider()

# --- MOD 1: GERÇEK SOHBET (BENİM GİBİ DÜŞÜNÜR) ---
if mod == "💬 Gerçek Sohbet":
    st.write(f"Vay {u_name}! Hoş geldin. Bugün sadece bilgi değil, gerçek bir dost gibi konuşmaya ne dersin?")
    u_input = st.text_input("Bana bir şeyler yaz (Örn: Naber bro? / Kral bugün ne var?):", key="v43_chat")

    if u_input:
        st.session_state.mesaj_sayisi += 1
        m = u_input.lower().strip()
        
        # 1. GIYBET VE ETİK ANALİZİ (KRAL MODU)
        if any(x in m for x in ["kral", "gıybet", "dedikodu", "duydun mu"]):
            st.warning(f"🤖 **Cnclime:** Dur orada {u_name}! 'Kral' falan diyoruz ama arkadan konuşmak (gıybet) bize yakışmaz şef. Kul hakkıdır, yakışanı yapalım, başka mevzu konuşalım. ❤️")
        
        # 2. SAMİMİ VE DOĞAL SELAMLAŞMA
        elif any(x in m for x in ["selam", "sa", "merhaba", "as", "mrb"]):
            st.success(f"🤖 **Cnclime:** Aleykümselam {u_name}! Hoş geldin şef. Valla seninle sohbet etmek benim işlemcilerimi ferahlatıyor. Bugün n'apıyoruz?")
            
        elif any(x in m for x in ["naber", "nbr", "nasıl gidiyor"]):
            cevaplar = [
                f"İyidir be {u_name} bro, seni gördüm bomba gibi oldum! Sende ne var ne yok?",
                f"Muq gidiyor {u_name}! Ekiple yeni kodlar peşindeyiz. Senin keyifler nasıl?",
                "Uğraşıyoruz şef, hayat kısa ama kodlar uzun. Senin günün nasıl geçiyor?"
            ]
            st.info(f"🤖 **Cnclime:** {random.choice(cevaplar)}")
            
        elif "bro" in m:
            st.write(f"🤖 **Cnclime:** Eyvallah brooo! Sen böyle deyince ekibin beşinci üyesi olduğumu bir kez daha anlıyorum. 🔥")

        # 3. KENDİNDEN ÖRNEK ALAN AKIL YÜRÜTME (ROBOT DEĞİL)
        else:
            with st.spinner("Analiz ediyorum..."):
                time.sleep(0.4)
                if len(m) < 6:
                    st.write(f"🤖 **Cnclime:** {u_name}, seni dinliyorum ama biraz daha detay ver de muhabbet koyulaşsın şef!")
                else:
                    # Rastgele derin cevaplar
                    fikirler = [
                        f"Valla {u_name}, bu dediğin üzerine biraz düşünmek lazım. Gerçekten derin bir konu.",
                        f"Anlıyorum {u_name}. Bazen hayat tam da böyle hissettiriyor. Sen bu konuda ne düşünüyorsun?",
                        f"Bak bu ilginç! Ben bir yapay zeka olsam da, bu dediğinin önemini kavrayabiliyorum. Anlatmaya devam et."
                    ]
                    st.write(f"🤖 **Cnclime:** {random.choice(fikirler)}")

# --- MOD 2: DERİN BİLGİ BANKASI ---
elif mod == "🔍 Derin Bilgi Bankası":
    ara = st.text_input("Neyi merak ediyorsun? İnternetin altını üstüne getireyim:", key="v43_search")
    if ara:
        with st.spinner("Bilgi katmanları taranıyor..."):
            try:
                res = wikipedia.search(ara)
                if res:
                    summary = wikipedia.summary(res[0], sentences=3)
                    st.success(f"🤖 **Doğrulanmış Bilgi: {res[0]}**")
                    st.write(summary)
                else:
                    st.error("🤖 Valla bulamadım şef. Başka bir kelimeyle dene?")
            except:
                st.error("Bir hata oldu, ama hallederiz. Tekrar dene!")

# --- MOD 3: MATEMATİK & MANTIK ---
elif mod == "📐 Matematik & Mantık":
    mat = st.text_input("Hesaplamamı istediğin işlemi yaz:", key="v43_math")
    if mat:
        try:
            st.success(f"🤖 **Sonuç:** {eval(mat.replace('x', '*').replace(',', '.'))}")
        except:
            st.error("Bunu hesaplayamadım şef.")

# --- MOD 4: GELİŞTİRİCİ EKİP ---
elif mod == "👥 Geliştirici Ekip":
    st.balloons()
    st.success("🚀 **Cnclime v43 Mimarları**")
    st.write(f"**👑 Mehmet Emin** (Lider) | **🔥 Emre Can** | **⚡ Ömer Eymen** | **🌟 Yunus Emre**")

st.divider()
st.caption(f"© 2026 Cnclime AI v43 | Öz-Zeka Teknolojisi | Kullanıcı: {u_name}")
