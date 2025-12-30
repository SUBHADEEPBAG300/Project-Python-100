"""
Mad Libs Story Generator 
Interactive story generation with user inputs.
Advanced level
"""

# Story templates
STORIES = {
    "adventure": {
        "title": "The Great Adventure",
        "prompts": [
            ("adjective", "Adjective"),
            ("noun1", "Noun"),
            ("verb_past", "Verb (past tense)"),
            ("adjective2", "Adjective"),
            ("noun2", "Noun"),
            ("animal", "Animal"),
            ("verb_ing", "Verb ending in -ing"),
            ("noun3", "Noun (plural)"),
            ("number", "Number"),
            ("place", "Place")
        ],
        "template": """
Once upon a time in a {adjective} land, there lived a brave {noun1}.
One day, they {verb_past} into a {adjective2} forest to find the legendary {noun2}.

Along the way, they met a talking {animal} who was {verb_ing} by the river.
The {animal} said, "Beware of the {noun3}! There are {number} of them!"

Despite the warning, our hero continued to {place} where they discovered...
THE END!
        """
    },
    "silly": {
        "title": "A Silly Day",
        "prompts": [
            ("name", "Person's name"),
            ("adjective", "Adjective"),
            ("food", "Type of food"),
            ("verb", "Verb"),
            ("body_part", "Body part"),
            ("animal", "Animal"),
            ("sound", "Funny sound"),
            ("place", "Place"),
            ("number", "Number")
        ],
        "template": """
My friend {name} is so {adjective}! Yesterday, they ate {number} pounds of {food}
for breakfast! Then they decided to {verb} all the way to {place}.

On the way, they bumped into a giant {animal} that made a loud "{sound}" noise!
{name} was so surprised that their {body_part} fell off!

What a {adjective} day!
        """
    },
    "space": {
        "title": "Space Mission",
        "prompts": [
            ("adjective", "Adjective"),
            ("noun", "Noun"),
            ("verb", "Verb"),
            ("planet", "Planet name"),
            ("number", "Number"),
            ("color", "Color"),
            ("animal", "Animal"),
            ("verb_ing", "Verb ending in -ing"),
            ("exclamation", "Exclamation")
        ],
        "template": """
Captain's Log: We have reached the {adjective} planet {planet}!
The surface is covered with {color} {noun}. There are {number} of them!

Our mission is to {verb} the alien {animal} species we discovered.
They communicate by {verb_ing} loudly. How fascinating!

{exclamation}! We must return to Earth immediately!
        """
    }
}


def get_user_inputs(prompts):
    """Collect inputs from user based on prompts."""
    inputs = {}
    print("\n" + "=" * 60)
    print("Enter the following words:")
    print("=" * 60)
    
    for key, prompt in prompts:
        value = input(f"{prompt}: ").strip()
        while not value:
            print("  ⚠️  Cannot be empty!")
            value = input(f"{prompt}: ").strip()
        inputs[key] = value
    
    return inputs


def display_story(title, story):
    """Display the completed story."""
    print("\n" + "=" * 60)
    print(f"📖 {title.upper()}")
    print("=" * 60)
    print(story)
    print("=" * 60)


def main():
    """Main program execution."""
    print("=" * 60)
    print("            MAD LIBS STORY GENERATOR")
    print("=" * 60)
    print("\nCreate hilarious stories by filling in the blanks!")
    
    while True:
        print("\n" + "-" * 60)
        print("Available Stories:")
        for i, (key, story) in enumerate(STORIES.items(), 1):
            print(f"  {i}. {story['title']}")
        print("  q. Quit")
        print("-" * 60)
        
        choice = input("\nSelect a story: ").strip().lower()
        
        if choice == 'q':
            print("\nThanks for playing! Goodbye!")
            break
        
        # Get story by number
        story_keys = list(STORIES.keys())
        try:
            idx = int(choice) - 1
            if 0 <= idx < len(story_keys):
                story_key = story_keys[idx]
                story_data = STORIES[story_key]
                
                # Get user inputs
                inputs = get_user_inputs(story_data["prompts"])
                
                # Generate story
                story = story_data["template"].format(**inputs)
                
                # Display result
                display_story(story_data["title"], story)
                
                # Save option
                save = input("\nSave story to file? (y/n): ")
                if save.lower() == 'y':
                    filename = input("Filename (default: madlibs_story.txt): ").strip()
                    if not filename:
                        filename = "madlibs_story.txt"
                    
                    with open(filename, 'w') as f:
                        f.write(f"{story_data['title']}\n")
                        f.write("=" * 60 + "\n")
                        f.write(story)
                    print(f"\n✓ Story saved to {filename}")
            else:
                print("❌ Invalid selection.")
        except ValueError:
            print("❌ Please enter a number.")


if __name__ == "__main__":
    main()