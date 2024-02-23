import streamlit as st
from streamlit_pills import pills
from search_by_google import GoogleSearch


def make_query():
    use_recommend = st.toggle("検索例") 
    if use_recommend:
        recommended_queries = [
            "LLMってなんですか？", "LLMで使われるRAGのメリット、デメリットは？",
            "機械学習の学習ロードマップを知りたい", "人工知能とはなんですか？",
            "仮想通貨の仕組みは？", "ビットコインって危険？",
            "クラウドコンピューティングの代表的なものはなんですか？", 
            "IoTについて知りたい", "画像認識で何ができる？",
            "生成AIの活用方法を知りたい", "ブロックチェーン技術はどう応用されている？"
            ]
        query = pills("Topic", recommended_queries)
        return query
    else:
        query = st.text_input("ex) RAGの実装方法について")
        return query


def main():
    st.set_page_config(
        page_title="要約アプリ",
        page_icon="🔍"
    )
    query = make_query()

    if not query == "":
        gSearch = GoogleSearch(query)
        googleSearchSummary = gSearch.make_summary()
        st.write(googleSearchSummary)

        topics = gSearch.get_relevant_topics()
        pills("関連トピック", topics)


if __name__ == "__main__":
    main()
