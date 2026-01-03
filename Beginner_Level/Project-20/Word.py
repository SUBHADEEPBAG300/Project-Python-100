"""
Word Counter
Count words, sentences, characters, and more in any text.
"""

import string
import re


def count_characters(text):
    """Count total characters including spaces."""
    return len(text)


def count_characters_no_spaces(text):
    """Count characters excluding spaces."""
    return len(text.replace(" ", "").replace("\n", "").replace("\t", ""))


def count_words(text):
    """Count total words in text."""
    words = text.split()
    return len(words)


def count_sentences(text):
    """Count sentences (ending with . ! ?)."""
    sentence_endings = re.findall(r'[.!?]+', text)
    return len(sentence_endings)


def count_paragraphs(text):
    """Count paragraphs (separated by blank lines)."""
    paragraphs = [p for p in text.split('\n\n') if p.strip()]
    return len(paragraphs)


def count_lines(text):
    """Count lines in text."""
    lines = [line for line in text.split('\n') if line.strip()]
    return len(lines)


def average_word_length(text):
    """Calculate average word length."""
    words = text.split()
    if not words:
        return 0
    total_length = sum(len(word.strip(string.punctuation)) for word in words)
    return total_length / len(words)


def most_common_words(text, top_n=5):
    """Find most common words."""
    words = re.findall(r'\b\w+\b', text.lower())
    word_freq = {}
    for word in words:
        word_freq[word] = word_freq.get(word, 0) + 1
    
    sorted_words = sorted(word_freq.items(), key=lambda x: x[1], reverse=True)
    return sorted_words[:top_n]


def analyze_text(text):
    """Perform complete text analysis."""
    if not text.strip():
        return None
    
    analysis = {
        'characters': count_characters(text),
        'characters_no_spaces': count_characters_no_spaces(text),
        'words': count_words(text),
        'sentences': count_sentences(text),
        'paragraphs': count_paragraphs(text),
        'lines': count_lines(text),
        'avg_word_length': average_word_length(text),
        'common_words': most_common_words(text)
    }
    
    return analysis


def display_results(analysis):
    """Display analysis results in formatted output."""
    print("\n" + "="*60)
    print("📊 TEXT ANALYSIS RESULTS")
    print("="*60)
    
    print(f"\n📝 CHARACTER COUNT:")
    print(f"   Total characters (with spaces):    {analysis['characters']:,}")
    print(f"   Characters (without spaces):       {analysis['characters_no_spaces']:,}")
    
    print(f"\n📖 WORD COUNT:")
    print(f"   Total words:                       {analysis['words']:,}")
    print(f"   Average word length:               {analysis['avg_word_length']:.2f} letters")
    
    print(f"\n📄 STRUCTURE:")
    print(f"   Sentences:                         {analysis['sentences']:,}")
    print(f"   Paragraphs:                        {analysis['paragraphs']:,}")
    print(f"   Lines:                             {analysis['lines']:,}")
    
    if analysis['common_words']:
        print(f"\n🔥 MOST COMMON WORDS:")
        for i, (word, count) in enumerate(analysis['common_words'], 1):
            print(f"   {i}. '{word}' - {count} times")
    
    print("="*60)


def get_text_input():
    """Get text input from user."""
    print("\n" + "="*60)
    print("ENTER YOUR TEXT")
    print("="*60)
    print("(Type or paste your text. Press Enter twice to finish)")
    print("-"*60)
    
    lines = []
    empty_count = 0
    
    while True:
        try:
            line = input()
            if line == "":
                empty_count += 1
                if empty_count >= 2:
                    break
            else:
                empty_count = 0
            lines.append(line)
        except EOFError:
            break
    
    return "\n".join(lines)


def read_from_file(filename):
    """Read text from a file."""
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        print(f"❌ Error: File '{filename}' not found.")
        return None
    except Exception as e:
        print(f"❌ Error reading file: {e}")
        return None


def save_results(analysis, filename="word_count_results.txt"):
    """Save analysis results to a file."""
    try:
        with open(filename, 'w') as f:
            f.write("="*60 + "\n")
            f.write("TEXT ANALYSIS RESULTS\n")
            f.write("="*60 + "\n\n")
            
            f.write("CHARACTER COUNT:\n")
            f.write(f"  Total characters (with spaces):    {analysis['characters']:,}\n")
            f.write(f"  Characters (without spaces):       {analysis['characters_no_spaces']:,}\n\n")
            
            f.write("WORD COUNT:\n")
            f.write(f"  Total words:                       {analysis['words']:,}\n")
            f.write(f"  Average word length:               {analysis['avg_word_length']:.2f} letters\n\n")
            
            f.write("STRUCTURE:\n")
            f.write(f"  Sentences:                         {analysis['sentences']:,}\n")
            f.write(f"  Paragraphs:                        {analysis['paragraphs']:,}\n")
            f.write(f"  Lines:                             {analysis['lines']:,}\n\n")
            
            if analysis['common_words']:
                f.write("MOST COMMON WORDS:\n")
                for i, (word, count) in enumerate(analysis['common_words'], 1):
                    f.write(f"  {i}. '{word}' - {count} times\n")
            
            f.write("\n" + "="*60 + "\n")
        
        print(f"\n✅ Results saved to '{filename}'")
    except Exception as e:
        print(f"❌ Error saving file: {e}")


def main():
    """Main program execution."""
    print("="*60)
    print("           📊 WORD COUNTER TOOL 📊")
    print("="*60)
    print("\nAnalyze any text - count words, characters, sentences & more!")
    
    while True:
        print("\n" + "-"*60)
        print("OPTIONS:")
        print("  1. Enter text manually")
        print("  2. Read from file")
        print("  3. Quick count (simple stats)")
        print("  4. Exit")
        print("-"*60)
        
        choice = input("\nSelect option (1-4): ").strip()
        
        if choice == '1':
            text = get_text_input()
            if text.strip():
                analysis = analyze_text(text)
                if analysis:
                    display_results(analysis)
                    
                    save_option = input("\nSave results to file? (y/n): ").lower()
                    if save_option == 'y':
                        filename = input("Filename (default: word_count_results.txt): ").strip()
                        if not filename:
                            filename = "word_count_results.txt"
                        save_results(analysis, filename)
            else:
                print("⚠️  No text entered!")
        
        elif choice == '2':
            filename = input("Enter filename: ").strip()
            text = read_from_file(filename)
            if text:
                analysis = analyze_text(text)
                if analysis:
                    display_results(analysis)
                    
                    save_option = input("\nSave results to file? (y/n): ").lower()
                    if save_option == 'y':
                        save_filename = input("Output filename (default: word_count_results.txt): ").strip()
                        if not save_filename:
                            save_filename = "word_count_results.txt"
                        save_results(analysis, save_filename)
        
        elif choice == '3':
            print("\n" + "="*60)
            print("QUICK COUNT MODE")
            print("="*60)
            text = input("Enter your text: ")
            if text.strip():
                words = count_words(text)
                chars = count_characters(text)
                chars_no_space = count_characters_no_spaces(text)
                print(f"\n📊 Quick Results:")
                print(f"   Words: {words}")
                print(f"   Characters: {chars}")
                print(f"   Characters (no spaces): {chars_no_space}")
            else:
                print("⚠️  No text entered!")
        
        elif choice == '4':
            print("\n" + "="*60)
            print("Thanks for using Word Counter!")
            print("="*60)
            print("Goodbye! 👋\n")
            break
        
        else:
            print("❌ Invalid option. Please enter 1-4.")


if __name__ == "__main__":
    main()