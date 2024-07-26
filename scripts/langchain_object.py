from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain.memory import ChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory
from src.definitions.credentials import Credentials


class LangChainChatModel:
    def __init__(self):
        self.chat_history = ChatMessageHistory()
        self.chat_model = ChatOpenAI(model="gpt-3.5-turbo", api_key=Credentials.openai_api_key())
        self.prompt = ChatPromptTemplate.from_messages(
            [
                ("system", "You are a helpful assistant"),
                MessagesPlaceholder(variable_name='chat_history'),
                ('human', '{input}')
            ]
        )
        self.chain = self.prompt | self.chat_model

        self.chain_with_message_history = RunnableWithMessageHistory(
            self.chain,
            lambda session_id: self.chat_history,
            input_messages_key='input',
            history_messages_key='chat_history'
        )

    def chat(self, user_prompt: str = ""):
        response = self.chain_with_message_history.invoke(
            {"input": user_prompt},
            {"configurable": {"session_id": "unused"}}
        )
        return response.content
