import streamlit as st

st.set_page_config(page_title="сіксєвєн", page_icon="https://cdn.pulsar.ua/products/46000-46999/orig-nal-na-an-me-f-gurka-omori-sitting-figure-omori/migrated-c3b7f8857552-omorisittingfigure-omori2-wwwpulsarua.jpg", layout="wide")

st.title("привіт")

tab1, tab2, tab3 = st.tabs(["Про мене", "Мій інструмент", "Корисні посилання"])

with tab1:
    st.header("Знайомство з автором")
    col1, col2 = st.columns([1, 2])
    with col1:
        st.image("https://cdn.pulsar.ua/products/46000-46999/orig-nal-na-an-me-f-gurka-omori-sitting-figure-omori/migrated-c3b7f8857552-omorisittingfigure-omori2-wwwpulsarua.jpg",  width=400)
    with col2:
        st.subheader("Привіт я анімє псіх")
        st.write("я навчаюсь в Малій академії IT STEP. Створюю круті проекти")

        with st.container():
            st.info("Зв'язок зі мною")
            st.markdown("-Email: kliza6056@gmail.com")
with tab2:
    st.info("у розробці")

with tab3:
    st.subheader("мої улюблені ігри")
    c1, c2 = st.columns(2)  
    with c1:
        st.markdown("❤️ - Genshin Impact")
        st.markdown("👽 - Roblox")

    with c2:
        st.markdown("🐈‍⬛ - omori")
        st.markdown("😻 - ENA Dream BBQ")