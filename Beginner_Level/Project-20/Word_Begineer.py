# Word Counter

def count_words(text):
    words = text.split()
    return len(words)

def count_sentences(text):
    sentences = text.split('.')
    return len([s for s in sentences if s.strip()])

def count_characters(text):
    return len(text)

# Example usage
text = "Hello world. This is a test text."
word_count = count_words(text)
sentence_count = count_sentences(text)
character_count = count_characters(text)

print(f"Word Count: {word_count}")
print(f"Sentence Count: {sentence_count}")
print(f"Character Count: {character_count}")
