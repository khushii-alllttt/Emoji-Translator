# Emoji Dictionary
emoji_dict = {
    "happy": "😊",
    "sad": "😢",
    "love": "❤️",
    "cat": "🐱",
    "dog": "🐶",
    "sun": "☀️",
    "heart": "💖",
    "fire": "🔥",
    "coffee": "☕",
    "pizza": "🍕",
    "music": "🎵"
}

def emoji_translator(text):
    words = text.lower().split()
    translated_words = [emoji_dict.get(word, word) for word in words]
    return " ".join(translated_words)

# Example usage
print("Welcome to Emoji Translator!")
sentence = input("Enter a sentence: ")
translated = emoji_translator(sentence)
print("\nTranslated with Emojis:")
print(translated)
