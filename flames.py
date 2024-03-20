def toLowerCase(name):
    return name.replace(" ", "").lower()

def countLetters(name1, name2):
    nameCombined = name1 + name2
    countLetter = {}
    for letter in nameCombined:
        if letter in countLetter:
            countLetter[letter] += 1
        else:
            countLetter[letter] = 1
    return countLetter

def flameCount(countLetter):
    flameSequence = ['F', 'L', 'A', 'M', 'E', 'S']
    total = sum(countLetter.values())
    flames_count = len(flameSequence)
    return total % flames_count

def determine_relationship(countLetter, flames_count):
    flameSequence = ['F', 'L', 'A', 'M', 'E', 'S']
    while len(flameSequence) > 1:
        letter_index = flames_count - 1
        while letter_index >= len(flameSequence):
            letter_index -= len(flameSequence)
        flames_count = flames_count % len(flameSequence)
        letter = flameSequence.pop(letter_index)
        if letter in countLetter:
            countLetter[letter] -= 1
            if countLetter[letter] == 0:
                del countLetter[letter]
        flames_count += len(flameSequence)
    return flameSequence[0]

def main():
    name1 = input("Enter the first name: ")
    name2 = input("Enter the second name: ")
    
    name1 = toLowerCase(name1)
    name2 = toLowerCase(name2)
    
    countLetter = countLetters(name1, name2)
    flames_count = flameCount(countLetter)
    relationship = determine_relationship(countLetter, flames_count)
    
    if relationship == 'F':
        print("Friendship")
    elif relationship == 'L':
        print("Love")
    elif relationship == 'A':
        print("Affection")
    elif relationship == 'M':
        print("Marriage")
    elif relationship == 'E':
        print("Enmity")
    elif relationship == 'S':
        print("Siblings")
    else:
        print("Error: Invalid relationship")

if __name__ == "__main__":
    main()
