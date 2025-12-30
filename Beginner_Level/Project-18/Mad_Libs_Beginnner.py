# Beginner level

def mad_libs_story():
    print("Welcome to the Mad Libs Story Generator!")
    
    # User inputs
    adjective = input("Enter an adjective: ")
    noun1 = input("Enter a noun: ")
    noun2 = input("Enter another noun: ")
    verb = input("Enter a verb: ")
    place = input("Enter a place: ")
    
    # Story template
    story = f"Once upon a time in a {adjective} {noun1}, there lived a {noun2} who loved to {verb}. " \
            f"Every day, it would go to {place} to have adventures."
    
    print("\nHere is your story:")
    print(story)

mad_libs_story()
