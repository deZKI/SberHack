from langchain.chat_models.gigachat import GigaChat
from langchain.schema import HumanMessage


def gigachat_answer(query: str) -> str:
    # Это синхронная функция для вызова GigaChat
    chat = GigaChat(
        credentials="YjQ5NjBkYTMtNjI0NC00NjFiLWEyMjMtODZhYTdhMjZlNzczOmZkMmM3YjU0LTQ5YTEtNGU2Yy1iMzQ1LTZjNDU2NzQ0MzA4YQ==",
        verify_ssl_certs=False)

    messages = [
        HumanMessage(content=query)
    ]
    # "Ответ Гигачата на ваш запрос: " +
    return chat(messages).content
