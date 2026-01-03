# Word Counter ![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=yellow)

Comprehensive text analysis tool providing detailed statistics about words, characters, sentences, and reading metrics.

## Features

### Basic Statistics
- **Word Count**: Total words in text
- **Character Count**: With and without spaces
- **Sentence Count**: Number of sentences
- **Paragraph Count**: Number of paragraphs
- **Line Count**: Number of lines

### Advanced Metrics
- **Average Word Length**: Mean characters per word
- **Average Sentence Length**: Mean words per sentence
- **Reading Time**: Estimated time at 200 WPM
- **Most Common Words**: Top 5 frequently used words

### Input Methods
- **Manual Entry**: Type or paste text
- **File Import**: Load from text files
- **Real-time Analysis**: Instant results

## Requirements

- Python 3.x
- Built-in modules: `re`, `collections`

## Installation

```bash
python word_counter.py
```

## Quick Start

### Manual Text Entry

```
==================================================
                WORD COUNTER
==================================================

Options:
  1. Enter text manually
  2. Load from file
  q. Quit

Your choice: 1

Enter your text (type 'END' on a new line when done):
The quick brown fox jumps over the lazy dog.
This is a sample text for analysis.
END
```

### File Input

```
Your choice: 2
Enter filename: document.txt

✓ Loaded from document.txt
```

## Analysis Output

```
======================================================================
TEXT ANALYSIS RESULTS
======================================================================

📊 Basic Statistics:
  Words:              150
  Characters:         850 (with spaces)
                      725 (without spaces)
  Sentences:          8
  Paragraphs:         3
  Lines:              12

📈 Advanced Metrics:
  Avg word length:    4.8 characters
  Avg sentence length: 18.8 words
  Reading time:       0.8 minutes (200 WPM)

🔤 Most Common Words:
  example         5 time(s)
  text            4 time(s)
  analysis        3 time(s)
  word            3 time(s)
  document        2 time(s)
======================================================================
```

## Detailed Metrics Explained

### Word Count
- Counts all words separated by whitespace
- Includes contractions as single words (don't = 1)
- Hyphenated words count as one (twenty-five = 1)

### Character Count
- **With spaces**: Total including all characters
- **Without spaces**: Excludes spaces, tabs, newlines
- Useful for social media character limits

### Sentence Count
- Sentences ending with: . ! ?
- Handles multiple punctuation: !!! = 1 sentence
- Ignores abbreviations when possible

### Paragraph Count
- Separated by double newlines (\n\n)
- Empty paragraphs ignored
- Standard document formatting

### Average Word Length
```
Formula: Total characters / Total words
Example: 850 chars / 150 words = 5.7 chars/word
```

### Average Sentence Length
```
Formula: Total words / Total sentences
Example: 150 words / 8 sentences = 18.8 words/sentence
```

### Reading Time
```
Formula: Total words / 200 WPM
Example: 1,000 words / 200 = 5 minutes
```
*Based on average adult reading speed of 200-250 WPM*

### Most Common Words
- Excludes stopwords (the, a, an, and, or, but, etc.)
- Shows top 5 by default
- Case-insensitive counting
- Helps identify key themes

## Use Cases

### Writing & Blogging
- **Blog Posts**: Track word count targets (300-2000 words)
- **Articles**: Ensure proper length
- **Essays**: Meet assignment requirements
- **Books**: Monitor chapter/section lengths

### SEO & Marketing
- **Meta Descriptions**: 150-160 characters
- **Title Tags**: 50-60 characters
- **Content Length**: Optimal 1,500-2,500 words
- **Keyword Density**: Track term frequency

### Social Media
- **Twitter**: 280 character limit
- **Instagram**: Caption optimization
- **LinkedIn**: Post length analysis
- **Facebook**: Engagement sweet spot

### Academic
- **Research Papers**: Word count requirements
- **Abstracts**: 150-300 word limits
- **Thesis**: Chapter length tracking
- **Assignments**: Meet specifications

### Professional
- **Reports**: Executive summary length
- **Emails**: Conciseness check
- **Presentations**: Script length
- **Documentation**: Completeness measure

## Reading Level Context

### Words Per Sentence
- **10-15**: Simple, easy to read
- **15-20**: Standard, comfortable
- **20-25**: More complex
- **25+**: Advanced, challenging

### Average Word Length
- **3-4 chars**: Very simple (kids' books)
- **4-5 chars**: Simple (newspapers)
- **5-6 chars**: Standard (novels)
- **6+ chars**: Complex (academic)

### Reading Time Estimates
| Word Count | Reading Time (200 WPM) |
|------------|------------------------|
| 500 | 2.5 minutes |
| 1,000 | 5 minutes |
| 1,500 | 7.5 minutes |
| 2,000 | 10 minutes |
| 5,000 | 25 minutes |

## Code Structure

```python
# Core counting functions
count_words(text)                    # Total words
count_characters(text, spaces)       # Character count
count_sentences(text)                # Sentence count
count_paragraphs(text)               # Paragraph count
count_lines(text)                    # Line count

# Advanced metrics
average_word_length(text)            # Mean chars/word
most_common_words(text, n)           # Top N words
reading_time(text, wpm)              # Minutes to read

# Main functions
analyze_text(text)                   # Full analysis
main()                               # Program loop
```

## Stopwords List

Common words excluded from frequency analysis:
```
the, a, an, and, or, but, in, on, at, to, for, of, is, it, 
was, are, been, being, have, has, had, do, does, did, will, 
would, should, could, may, might, must, can, this, that, 
these, those, i, you, he, she, we, they, what, which, who, 
when, where, why, how
```

## File Format Support

### Supported
- **Plain Text** (.txt)
- **UTF-8 Encoding** (handles international characters)
- **Any text-based format**

### Input Validation
- Checks file existence
- Handles encoding errors
- Reports file read errors
- Validates text content

## Example Text Samples

### Short Text (50 words)
```
The quick brown fox jumps over the lazy dog. This classic 
pangram contains every letter of the alphabet. It's commonly 
used for testing fonts and keyboards. The phrase dates back 
to the late 19th century.

Analysis: 50 words, ~12 seconds to read
```

### Medium Text (200 words)
```
[Blog post excerpt]
Analysis: 200 words, ~1 minute to read
```

### Long Text (1000+ words)
```
[Article or document]
Analysis: 1000 words, ~5 minutes to read
```

## Practical Examples

### Blog Post Analysis
```
Title: "10 Tips for Python Programming"
Words: 1,247
Characters: 7,823 (with spaces)
Sentences: 67
Reading time: 6.2 minutes
Top words: python, code, programming, function, data
```

### Email Analysis
```
Subject: Project Update
Words: 156
Characters: 892 (with spaces)
Sentences: 11
Reading time: 0.8 minutes
Assessment: Concise, professional length
```

### Tweet Analysis
```
Tweet: "Just launched our new product! 🚀 Check it out..."
Words: 8
Characters: 52 (without spaces: 44)
Assessment: Within 280 character limit ✓
```

## Performance Metrics

### Speed
- Small text (<1KB): Instant
- Medium text (10KB): <0.1 seconds
- Large text (1MB): ~1 second
- Very large (10MB+): Few seconds

### Memory
- Efficient text processing
- Minimal memory footprint
- Handles large documents

## Error Handling

- **Empty Text**: Detects and reports
- **File Not Found**: Clear error message
- **Encoding Errors**: UTF-8 fallback
- **Invalid Input**: Validation checks

## Tips & Best Practices

### For Accurate Counts
1. Clean your text (remove extra spaces)
2. Check formatting (consistent paragraphs)
3. Remove headers/footers if analyzing body
4. Consider what to include/exclude

### For Better Analysis
1. Compare against benchmarks
2. Track changes over time
3. Use for goal setting
4. Combine with other metrics

### Writing Optimization
1. Aim for 15-20 words per sentence
2. Vary sentence length for rhythm
3. Keep paragraphs focused (3-5 sentences)
4. Use active voice (affects word count)

## Advanced Features (Code Extensions)

### Readability Scores
```python
def flesch_reading_ease(text):
    # Calculate Flesch Reading Ease score
    # 90-100: Very Easy
    # 60-70: Standard
    # 0-30: Very Difficult
```

### Keyword Density
```python
def keyword_density(text, keyword):
    # Calculate percentage of specific word
    # SEO target: 1-2% for focus keyword
```

### Unique Word Ratio
```python
def unique_word_ratio(text):
    # Unique words / Total words
    # Measures vocabulary diversity
```

## Integration Ideas

- Export analysis to CSV
- Compare multiple documents
- Track writing progress over time
- Generate reports
- API for programmatic access

## Troubleshooting

### Incorrect Word Count
- Check for multiple spaces
- Verify text encoding
- Remove special characters

### File Won't Load
- Check file path
- Verify file permissions
- Ensure UTF-8 encoding

### Unexpected Results
- Review text formatting
- Check for hidden characters
- Validate input method

## Future Enhancements

- [ ] Readability scores (Flesch-Kincaid)
- [ ] Grammar checking
- [ ] Style analysis
- [ ] Keyword density
- [ ] Export to CSV/PDF
- [ ] Batch file processing
- [ ] GUI interface
- [ ] Cloud storage integration
- [ ] Real-time analysis
- [ ] Language detection

## License

Free to use and modify for any purpose.

## Author Notes

Professional text analysis tool suitable for writers, students, marketers, and anyone needing text statistics. Built with clean, maintainable code following Python best practices.