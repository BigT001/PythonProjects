def word_replace():

    My_str = "This is a program that replaces word with another"

    word_to_replace = input("Enter word to replace: ")
    new_word = input("Enter new word: ")

    print(My_str.replace(word_to_replace, new_word))

word_replace()