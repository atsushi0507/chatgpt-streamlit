import streamlit as st
from streamlit_pills import pills
import news_getter


def select_topic():
    use_recommend = st.toggle("Recommended topics") 
    if use_recommend:
        recommended_topics = [
            "LLM", "RAG", "機械学習", "人工知能", "仮想通貨", "ビットコイン",
            "クラウドコンピューティング", "IoT", "画像認識", "生成AI", "ブロックチェーン技術"
            ]
        topic = pills("Topic", recommended_topics)
        return topic
    else:
        topic = st.text_input("検索したいニューストピック")
        return topic


def get_news(topic: str):
    articles = news_getter.get_news(topic, 5)
    st.dataframe(articles[["publishedAt", "title"]])
    return articles.title.unique().tolist()


def main():
    st.set_page_config(
        page_title="ニュース要約アプリ",
        page_icon=":newspaper"
    )
    topic = select_topic()

    if not topic == "":
        news_titles = get_news(topic)
        selected_news = st.selectbox("ニュースを選択する", news_titles)
        st.write(f"選択したニュース: {selected_news}")


if __name__ == "__main__":
    main()
