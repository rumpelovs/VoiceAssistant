import speech_recognition as sr
import openai

r = sr.Recognizer()

def audio_to_text(file_path):
    with sr.AudioFile(file_path) as source:
        audio_data = r.record(source)
        text = r.recognize_google(audio_data, language="ru-RU") # Используем Google для распознавания голоса на русском языке
        return text

def process_voice_command(text):
    if "Румпель" in text.lower(): # Проверяем команду на наличие ключевого слова "запуск"
        code_word = extract_code_word(text)
        if code_word:
            print("Кодовое слово:", code_word)
        else:
            print("Не удалось извлечь кодовое слово.")
    else:
        print("Голосовая команда не содержит ключевого слова 'запуск'.")

def extract_code_word(text):
    def extract_code_word(text):
        words = text.split() # Разбиваем текст на слова
        for word in words:

           if word.lower() != "Румпель": # Ищем первое слово, которое не равно "запуск"
            return word
    pass

openai.api_key = 'KEY'

def process_text_command(command):
    response = openai.Completion.create(
        engine="text-davinci-004",  
        prompt=command,
        max_tokens=100,  
        temperature=0.7,  
        n=1,  
        stop=None,  
    )

    if len(response.choices) > 0:
        answer = response.choices[0].text.strip()
        print("Ответ:", answer)
    else:
        print("Не удалось получить ответ от GPT-4.")
if __name__ == "__main__":
    audio_file = "voice_command.wav"
    text = audio_to_text(audio_file)
    process_voice_command(text)

    command = "Какой будет погода завтра?"
    process_text_command(command)

