from langchain_openai import ChatOpenAI
from langchain_core.messages import AIMessage, HumanMessage
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain.memory import ChatMessageHistory
from src.definitions.credentials import Credentials
from langchain_core.runnables.history import RunnableWithMessageHistory

chat_history = ChatMessageHistory()

chat = ChatOpenAI(model='gpt-3.5-turbo', api_key=Credentials.openai_api_key())
prompt = ChatPromptTemplate.from_messages(
    [
        ('system', 'You are a helpful assistant.'),
        MessagesPlaceholder(variable_name='chat_history'),
        ('human', '{input}')
    ]
)

chain = prompt | chat

chain_with_message_history = RunnableWithMessageHistory(
    chain,
    lambda session_id: chat_history,
    input_messages_key="input",
    history_messages_key="chat_history",
)

def chat(user_prompt: str):
    response = chain_with_message_history.invoke(
        {"input": user_prompt},
        {"configurable": {"session_id": "unused"}}
    )
    return response.content

if __name__ == "__main__":
    print(chat("Hi my name is Bob"))
    print(chat("What's my name?"))

