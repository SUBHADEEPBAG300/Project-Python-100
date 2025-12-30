# Mad Libs Story Generator ![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=yellow)
![Python Logo](https://www.python.org/static/community_logos/python-logo.png)

A fun and interactive **Mad Libs Story Generator** written in Python.  
Create hilarious stories by filling in the blanks with your own words!

---

## 📌 Features

- 📚 **Multiple Story Templates** - Choose from Adventure, Silly, and Space Mission stories
- 🎮 **Interactive Gameplay** - Fill in words to create unique stories
- 💾 **Save Stories** - Export your creations to text files
- ✨ **Input Validation** - Ensures no blank entries
- 🔄 **Replay Option** - Generate multiple stories in one session
- 🎨 **Formatted Output** - Beautiful story presentation with separators

---

## 📖 Story Templates

### 1. The Great Adventure 🗺️
An epic journey through mystical lands with brave heroes and legendary creatures.

**Required Inputs:** Adjectives, Nouns, Verbs, Animals, Numbers, Places

### 2. A Silly Day 😄
A ridiculous story about your friend's bizarre day filled with funny moments.

**Required Inputs:** Names, Food items, Body parts, Funny sounds, Places

### 3. Space Mission 🚀
An intergalactic adventure exploring alien planets and strange creatures.

**Required Inputs:** Planets, Colors, Animals, Exclamations, Numbers

---

## 🖥️ How It Works

The program uses **string formatting** to replace placeholders in story templates with user-provided words, creating unique and often hilarious narratives each time!

```python
# Example template structure
template = "Once upon a time in a {adjective} land..."
inputs = {"adjective": "magical"}
story = template.format(**inputs)
```

---

## 🚀 How to Run

### 1. Make sure you have Python 3 installed
Check using:
```bash
python --version
```
or
```bash
python3 --version
```

### 2. Run the program
```bash
python madlibs.py
```
or
```bash
python3 madlibs.py
```

### 3. Follow the Interactive Prompts
```
============================================================
            MAD LIBS STORY GENERATOR
============================================================

Create hilarious stories by filling in the blanks!

------------------------------------------------------------
Available Stories:
  1. The Great Adventure
  2. A Silly Day
  3. Space Mission
  q. Quit
------------------------------------------------------------

Select a story: 1
```

---

## 📝 Usage Example

### Step 1: Select a Story
```
Select a story: 2
```

### Step 2: Fill in the Blanks
```
============================================================
Enter the following words:
============================================================
Person's name: John
Adjective: crazy
Type of food: pizza
Verb: dance
Body part: nose
Animal: elephant
Funny sound: BOING
Place: Mars
Number: 47
```

### Step 3: Enjoy Your Story!
```
============================================================
📖 A SILLY DAY
============================================================

My friend John is so crazy! Yesterday, they ate 47 pounds of pizza
for breakfast! Then they decided to dance all the way to Mars.

On the way, they bumped into a giant elephant that made a loud "BOING" noise!
John was so surprised that their nose fell off!

What a crazy day!

============================================================
```

### Step 4: Save (Optional)
```
Save story to file? (y/n): y
Filename (default: madlibs_story.txt): johns_adventure.txt

✓ Story saved to johns_adventure.txt
```

---

## 📂 Folder Structure

```
Mad-Libs-Generator/
   ├── madlibs.py           # Main Python script
   ├── README.md            # Documentation
   └── madlibs_story.txt    # Saved stories (auto-generated)
```

---

## 🎯 Program Components

### Main Functions

**`get_user_inputs(prompts)`**
- Collects words from the user based on story requirements
- Validates that inputs are not empty
- Returns a dictionary of user inputs

**`display_story(title, story)`**
- Formats and displays the completed story
- Adds decorative borders for better readability

**`main()`**
- Handles menu navigation
- Story selection logic
- Loops for continuous play
- File saving functionality

---

## 🎓 Learning Concepts

This project demonstrates:
- **String Formatting** - Using `.format()` with dictionaries
- **Dictionary Data Structures** - Storing complex nested data
- **User Input Handling** - Collecting and validating input
- **File I/O Operations** - Writing stories to text files
- **Control Flow** - Loops, conditionals, and menu systems
- **Functions** - Modular code organization
- **Error Handling** - Try-except for input validation

---

## ✅ Purpose

- Practice Python string manipulation
- Learn interactive program design
- Understand file operations
- Have fun creating funny stories!
- Great project for beginners

---

## 🛠️ Technologies Used

- **Python 3.x** - Programming language
- **String Formatting** - Template-based text generation
- **File Handling** - Saving stories to .txt files
- **Input Validation** - Ensuring quality user input

---

## 🔮 Future Enhancements

- [ ] Add more story templates (Horror, Romance, Mystery)
- [ ] Implement difficulty levels (Easy, Medium, Hard)
- [ ] Random story generator mode
- [ ] Export to PDF format
- [ ] Add colorful terminal output using `colorama`
- [ ] GUI version using Tkinter
- [ ] Share stories online
- [ ] Word history to avoid repetition

---

## 🎮 Tips for Best Results

1. Be creative with your word choices!
2. Use unexpected or silly words for maximum humor
3. Try the same story multiple times with different words
4. Mix up adjectives and nouns for surprising combinations
5. Save your favorite stories to share with friends

---

## 👨‍💻 Author

**Developed by Debanga**

---

## 📝 License

This project is open source and available for educational purposes.

---

## 🤝 Contributing

Want to add your own story template? Feel free to fork and submit a pull request!

### Adding a New Story Template:
```python
"your_story": {
    "title": "Your Story Title",
    "prompts": [
        ("key", "Prompt text"),
        # Add more prompts...
    ],
    "template": """
    Your story template with {key} placeholders...
    """
}
```

---

**Have Fun Creating Stories! 📖✨**