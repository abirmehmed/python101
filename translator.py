import argostranslate.package
import argostranslate.translate
import warnings

# Suppress warnings
warnings.filterwarnings("ignore")

# Update package index
argostranslate.package.update_package_index()

# Get available packages
available_packages = argostranslate.package.get_available_packages()

# Install English to Italian package
en_it_package = next(filter(lambda x: x.from_code == "en" and x.to_code == "it", available_packages), None)
if en_it_package:
    argostranslate.package.install_from_path(en_it_package.download())

# Install English to Bengali package
en_bn_package = next(filter(lambda x: x.from_code == "en" and x.to_code == "bn", available_packages), None)
if en_bn_package:
    argostranslate.package.install_from_path(en_bn_package.download())
def translate_text(text, from_lang, to_lang):
    return argostranslate.translate.translate(text, from_lang, to_lang)

# Get user input
text_to_translate = input("Enter the text you want to translate: ")

# Translate to Italian
translated_to_italian = translate_text(text_to_translate, 'en', 'it')
print(f"Translated to Italian: {translated_to_italian}")

# Translate to Bengali
translated_to_bengali = translate_text(text_to_translate, 'en', 'bn')
print(f"Translated to Bengali: {translated_to_bengali}")
