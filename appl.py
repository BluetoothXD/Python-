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
    c1, c2 = st.columns(2)
    with c1:
        st.subheader("мої улюблені ігри")
        st.markdown("Genshin Impact")
        st.markdown("Roblox")
        st.markdown("omori")
        st.markdown("ENA Dream BBQ")
    with c2:
        st.image("https://cdn2.unrealengine.com/genshin-impact-version-2-8-3840x2160-357d3d64d056.png?resize=1&w=1280&h=720&quality=medium", width=300)    
        st.image("https://static0.makeuseofimages.com/wordpress/wp-content/uploads/2020/11/roblox.jpg?w=1600&h=900&fit=crop", width=300)
        st.image("https://img-eshop.cdn.nintendo.net/i/151f6f31fd0a03be3bfa17d07dfd9f6b7c423063bb46a8678c2ca15b1acce398.jpg", width=300)
        st.image("https://shared.fastly.steamstatic.com/store_item_assets/steam/apps/2134320/capsule_616x353.jpg?t=1755357900", width=300)

#я не до кінця зрозуміла що означають емодзі-іконки тому просто додала картинки цих ігор:((
    