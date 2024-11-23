from string import ascii_lowercase


def read_file():
    content = None
    with open("books/frankenstein.txt") as file:
        content = file.read()
    return content


def word_count(content):
    count = 0
    lines = content.splitlines()
    for line in lines:
        for word in line.split(" "):
            if word != "":
                count += 1
    return count


def character_count(content):
    frequency = {}
    for char in content:
        char = char.lower()
        if char in ascii_lowercase:
            if char not in frequency:
                frequency[char] = 0
            frequency[char] += 1
    frequency_sorted = sorted(frequency.items(), key=lambda item: item[1], reverse=True)
    return frequency_sorted


def main():
    content = read_file()
    words = word_count(content)
    characters = character_count(content)
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{words} words found in the document")
    for char, count in characters:
        print(f"The '{char}' character was found {count} times")
    print("--- End report ---")

if __name__ == "__main__":
    main()