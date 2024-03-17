def main():
    #print("Hi")
    file_path = "books/frankenstein.txt"
    with open(file_path) as f:
        file_contents = f.read()
        word_count = count_words(file_contents)
        letter_count = count_letters(file_contents)
        print_report(file_path, word_count, letter_count)

def count_words(text):
    words = text.split()
    #print("Number of words: "+  str(len(words)))
    return len(words)

def count_letters(text):
    letters = {
        "a":0,
        "b":0,
        "c":0,
        "d":0,
        "e":0,
        "f":0,
        "g":0,
        "h":0,
        "i":0,
        "j":0,
        "k":0,
        "l":0,
        "m":0,
        "n":0,
        "o":0,
        "p":0,
        "q":0,
        "r":0,
        "s":0,
        "t":0,
        "u":0,
        "v":0,
        "w":0,
        "x":0,
        "y":0,
        "z":0
    }

    text = text.lower()
    for letter in letters:
        count = text.count(letter)
        letters[letter] = count
    
   #print("Amount of each letter:")
    #print(letters)
    return letters

def bubble_sort(array):
    n = len(array)


    for i in range(n):

        # Create a flag that will allow the function to

        # terminate early if there's nothing left to sort

        already_sorted = True


        # Start looking at each item of the list one by one,

        # comparing it with its adjacent value. With each

        # iteration, the portion of the array that you look at

        # shrinks because the remaining items have already been

        # sorted.

        for j in range(n - i - 1):

            if array[j][1] < array[j + 1][1]:

                # If the item you're looking at is greater than its

                # adjacent value, then swap them

                array[j], array[j + 1] = array[j + 1], array[j]


                # Since you had to swap two elements,

                # set the `already_sorted` flag to `False` so the

                # algorithm doesn't finish prematurely

                already_sorted = False


        # If there were no swaps during the last iteration,

        # the array is already sorted, and you can terminate

        if already_sorted:

            break


    return array

def print_report(file_path, word_count, letter_count):
    print("--- Begin report of " + file_path + " ---")
    print(str(word_count) + " words found in the document\n\n")

    #convert dictionary to containing sets and then sort the list in descending order
    letterArr = []
    for item in letter_count:
        #print(item, letter_count[item])
        letter_set = [item, letter_count[item]]
        letterArr.append(letter_set)
    letterArr = bubble_sort(letterArr)
    for letter in letterArr:
        print(f"The '{letter[0]}' character was found {letter[1]} times")
    print("--- End report ---")

main()