# -*- coding: utf-8 -*-
# Define the vocabulary for translation
translations = {
    "i": "Zylo",
    "will": "Ta-",
    "do": "Klyth",
    "it": "Thyra",
    "want": "Zyra",
    "see": "Fyn",
    # Add more words as needed
}

# Function to translate English to Zylarian
def translate_to_zylarian(sentence):
    words = sentence.split()
    translated_words = []
    
    for word in words:
        translated_word = translations.get(word.lower(), word)  # Default to original if not found
        translated_words.append(translated_word)
    
    return ' '.join(translated_words)

# Main program execution
if __name__ == "__main__":
    input_sentence = input("Enter a sentence in English: ")
    translated_sentence = translate_to_zylarian(input_sentence)
    print("Translated to Zylarian:", translated_sentence)
