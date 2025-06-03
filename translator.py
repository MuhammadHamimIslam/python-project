from deep_translator import GoogleTranslator

text = input("Enter text: ")
target_lang = input("Translate to (e.g. 'bangla', 'english', 'french'): ").lower()

lang_dict = GoogleTranslator.get_supported_languages(as_dict=True)

if target_lang in lang_dict:
    lang_code = lang_dict[target_lang]
    translated = GoogleTranslator(source='auto', target=lang_code).translate(text)
    print(f"Translated text: {translated}")
else:
    print("Unsupported language name.")