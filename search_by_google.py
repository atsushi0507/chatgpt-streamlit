from langchain.agents import initialize_agent, Tool
from langchain.utilities import GoogleSearchAPIWrapper
from langchain.prompts import PromptTemplate
from langchain.agents import AgentType
from langchain.chat_models import ChatOpenAI
from langchain.output_parsers import CommaSeparatedListOutputParser
from langchain.schema import HumanMessage


class GoogleSearch:
    def __init__(self, query):
        self.chat = ChatOpenAI(
            model="gpt-3.5-turbo",
            temperature=0,
            max_tokens=2000
        )
        self.parser = CommaSeparatedListOutputParser()
        self.tools = self.define_tools()
        self.prompt = self.create_prompt(query)
        
    def define_tools(self):
        search = GoogleSearchAPIWrapper()
        return [
            Tool(
                name="GoogleSearch",
                func=search.run,
                description="最新情報をGoogleで検索する。"
            )
        ]
    
    def create_prompt(self, query):
        prompt = PromptTemplate(
            input_variables=["query"],
            template="""
            あなたは以下の質問の分野を詳細に理解し、かつアウトリーチに力を入れており解説にも定評のある人物です。
            以下の質問について、Google検索で最新の情報を取得し、その情報に基づいて素人でも分かりやすいと感じるようやくを書いてください。
            要約は500~1000字程度で、日本語で出力してください。
            記事の末尾には参照元としてGoogleで検索したURLをタイトルとともに出力してください。
            ###
            質問: {query}
            """
        )
        return prompt.format(query=query)

    def init_agent(self):
        return initialize_agent(
            self.tools,
            self.chat,
            agent=AgentType.OPENAI_FUNCTIONS
        )

    def make_summary(self):
        agent = self.init_agent()
        self.response = agent.run(self.prompt)
        return self.response
        
    def get_relevant_topics(self):
        self.result = self.chat([
            HumanMessage(
                content=f"""
                以下の内容を理解するために必要な学術的、または技術的な知識について、最大で10個ピックアップしてください。
                結果は日本語で出力してください。
                ###
                内容: {self.response}
                """
            ),
            HumanMessage(
                content=self.parser.get_format_instructions()
            )
        ])
        return self.parser.parse(self.result.content)
