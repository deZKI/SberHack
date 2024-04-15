import torch
import numpy as np

from sklearn.metrics.pairwise import cosine_similarity


def get_embedding(text: str) -> np.array:
    from main import TOKENIZER, RUSSIAN_STOP_WORDS, MODEL, DEVICE
    # Токенизация текста и удаление стоп-слов
    # print(text)
    # print("_________________________________________")
    tokens = TOKENIZER.tokenize(text)
    tokens_without_sw = [word for word in tokens if word not in RUSSIAN_STOP_WORDS]

    # Проверка на пустоту списка токенов после удаления стоп-слов
    if not tokens_without_sw:
        raise ValueError("Text is empty after removing stop words.")

    # Конвертация обратно в строку для корректного кодирования
    text_without_sw = ' '.join(tokens_without_sw)

    # Кодирование текста для T5
    encoded_input = TOKENIZER(text_without_sw, return_tensors='pt', padding='max_length', truncation=True,
                              max_length=512)

    # Получение выходных данных модели
    with torch.no_grad():
        model_output = MODEL(**encoded_input.to(DEVICE))

    # Использование эмбеддинга последнего слоя
    return model_output.last_hidden_state[:, 0, :].detach().cpu().numpy()


def find_top_matches(texts: list[str], reference_text: str):
    """Функция для нахождения топ 15% текстов по сходству с reference_text."""
    reference_embedding = get_embedding(reference_text)
    embeddings = np.vstack([get_embedding(text) for text in texts])
    similarities = cosine_similarity(reference_embedding.reshape(1, -1), embeddings).flatten()
    top_15_percent_index = np.argsort(similarities)[-int(len(similarities) * 0.15):][::-1]
    return [texts[idx] for idx in top_15_percent_index], similarities[top_15_percent_index]
