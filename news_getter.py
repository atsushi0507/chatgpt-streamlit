import pandas as pd
import requests
import os

pd.options.display.max_colwidth = 25

headers = {"X-Api-Key": os.environ["NEWS_API_KEY"]}
url = "https://newsapi.org/v2/everything"


def get_news(topic: str, nArticles=3):
    params = {
        "q": topic,
        "sortBy": "publishedAt",
        "pageSize": nArticles
    }

    try:
        response = requests.get(
            url,
            headers=headers,
            params=params
        )

        if response.ok:
            data = response.json()
            df = pd.DataFrame(data["articles"])
            return df
    except Exception as e:
        return f"Could not get news: {str(e)}"
