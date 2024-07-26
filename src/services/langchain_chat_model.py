from langchain.memory import ChatMessageHistory
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_openai import ChatOpenAI

from src.definitions.credentials import Credentials, EnvVariables
from src.services.prompts.prompts import SYSTEM_PROMPT


class LangChainChatModel:
    def __init__(self):
        self.chat_history = ChatMessageHistory()
        self.chat_model = self.init_chat_model()
        self.prompt = ChatPromptTemplate.from_messages(
            [
                ("system", SYSTEM_PROMPT),
                MessagesPlaceholder(variable_name='chat_history'),
                ('human', '{input}')
            ]
        )
        self.chain = self.prompt | self.chat_model
        self.chain_with_message_history = self.init_message_history()

    def init_chat_model(self):
        return ChatOpenAI(
            model=EnvVariables.chat_model(),
            api_key=Credentials.openai_api_key()
        )

    def init_message_history(self):
        return RunnableWithMessageHistory(
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
