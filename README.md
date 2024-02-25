# プロジェクト名

このプロジェクトは、Google検索を利用して得た情報をChatGPTを使って要約するアプリです。

## インストール

以下の手順に従って、プロジェクトをローカル環境にクローンしてください。

```bash
git clone https://github.com/atsushi0507/chatgpt-streamlit.git
cd chatgpt-streamlit
```

必要なパッケージをインストールします。
```bash
pip install -r requirements.txt
```

## APIキーの取得と環境変数の設定
このアプリの利用には OpenAI の API を利用するため、

## 使用方法
以下の手順で streamlit によるウェブサーバを起動します。
```bash
streamlit run front-end.py
```
ローカルホスト上で起動します。自動でウェブブラウザが立ち上がりページが表示されます。
ウェブブラウザが立ち上がらない、またはページが表示されない場合、http://localhost:8501 にアクセスしてアプリを使用します。

## ライセンス
このプロジェクトは MIT ライセンスの下で公開されています。詳細については LICENSE ファイルを参照してください。