# Purpose: Project for CSC 2017x40 to read a text file and count the number of occurrences of a word
# in the sample text words.txt

FILENAME = "words.txt"
word_count = len(FILENAME.split())
word = FILENAME.split()
count = 0

print("Welcome to Project 1 program")

# Open the words text document for writing
def write_words():
    with open(FILENAME, "w") as file:
        for word in word:
            file.write(f"Total word count: {word_count}\n")

# Read the words list
def read_words():
    words = []
    with open(FILENAME) as file:
        for line in file:
            line = line.replace("\n", "")
            words.append(line)
    return words

# function to list the words
def list_words(words):
    for i, word in enumerate(sorted(words)):
        print(f"{i}. {word}")
    print()

# An algorithm to count the words. When the current word read is different from the last word,
# write that word and its count to a file named words.count
def count_words(words, count):
    count = 0
    word = input("Enter a word to count its occurrences: ").lower()
    word = word.strip()  # Remove any leading/trailing whitespace
    words = sorted(words) # Sort the words list
    with open(FILENAME, "r") as file:
        for line in file:
            # Strip whitespace and convert to lowercase to avoid mismatch errors
            line = line.strip()
            line = file.read().lower()
            words = line.split()
            for i in words:
                if i == word:
                    count += 1
    print(f"Occurences of {word}: ", "appears", count, "times")
    return word, count

# Function to write the the list into a word.count document 
# and display it as rows
def write_words_count(words):
    # Counts and writes word occurences to 'words.count'
    word_dict = {}  # Manual dictionary for counting words
    words = sorted(words)  # Sort the words list
    for word in words:
        word = word.lower().strip()
        if word in word_dict:
            word_dict[word] += 1
        else:
            word_dict[word] = 1  # Initialize count

    write_choice = input("Write word count to file? (y/n): ").strip().lower()
    if write_choice == "y":
        with open("words.count", "w") as file:
            for word, count in word_dict.items():
                file.write(f"{word}:{count}\n")
        print("Word count saved to 'words.count'.\n")
    else:
        print("No file written.\n")

def display_menu():
    print("Words List Program for Project 1")
    print()
    print("Command Menu")
    print("list - list words")
    print("count - count the occurences of words in the list")
    print("write - write the word count file")
    print("exit - exit the program")
    print()

def main():
    display_menu()
    words = read_words()
    while True:
        command = input("Command: ")
        if command.lower() == "list":
            list_words(words)
        elif command.lower() == "count":
            count_words(word, count)
        elif command.lower() == "write":
            write_words_count(words)
        elif command.lower() == "exit":
            print("Goodbye!")
            break
        else:
            print("Invalid command. Please try again.\n")

if __name__ == "__main__":
    main()
