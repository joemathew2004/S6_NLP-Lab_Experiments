from deep_translator import GoogleTranslator

def translate_text(text, target_language):
    translator = GoogleTranslator(source='auto', target=target_language)  # Initialize the Translator object
    return translator.translate(text)

# List of supported languages
languages = {
    "english": "en",
    "spanish": "es",
    "french": "fr",
    "german": "de",
    "hindi": "hi",
    "chinese": "zh",
    "japanese": "ja",
    "russian": "ru"
}

print("Language Translator: Type 'exit' to quit.")

while True:
    text = input("\nEnter text to translate: ")
    if text.lower() == "exit":
        print("Exiting Translator...")
        break
    
    print("Available languages: English, Spanish, French, German, Hindi, Chinese, Japanese, Russian")
    lang = input("Enter target language: ").lower()
    
    if lang in languages:
        translated_text = translate_text(text, languages[lang])
        print(f"Translated to {lang.capitalize()}: {translated_text}")
    else:
        print("Sorry, language not supported. Try again.")
