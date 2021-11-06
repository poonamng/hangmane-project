import string
from words import choose_word
from images import IMAGES
def ifValid(user_input):
    if len(user_input) != 1:
        return False
    if not user_input.isalpha():
        return False
    return True

def is_word_guessed(secret_word, letters_guessed):
    if secret_word==get_guessed_word(secret_word, letters_guessed):
        return True
    return False

def get_guessed_word(secret_word,letters_guessed):
    index=0
    guessed_word=""
    while (index<len(secret_word)):
        if secret_word[index]in letters_guessed:
            guessed_word+=secret_word[index]
        else:
            guessed_word+="_"
            index+=1
        return guessed_word   

def get_available_letters(letter_gussed):
    import string
    # all_letters=string.ascii_lowercase
    letters_left=string.ascii_lowercase
    for i in letter_gussed:
        letters_left=letters_left.replace(i," ")
    return letters_left


def get_hint(secret_word,letters_gussed):
    import random
    letters_not_gussed=[]
    for i in secret_word:
        if i not in letters_gussed:
            if i not in letters_not_gussed:
                letters_not_gussed.append(i)
    return random.choice(letters_not_gussed)

#remaining_lives=8
#totallives=ramaing_lives=8
def hangman(secret_word):
    print("welcome to the game,Hangman!")
    print("I am thinking of a word that is "+str(len(secret_word))+"letters long.")
    print("")
    letters_gussed=[]
    level=input("enter the level in wich u want to play:\n(a for easy\n""(b)for meadium\n""(c) for hard level:")
    
    total_lives=remaining_lives=8
    image_selection_last_indices=[0,1,2,3,4,5,6,7]

    if level=="b":
        total_lives=remaining_lives=6
        image_selection=[0,2,3,5,6,7]
    elif level=="c":
        total_lives=remaining_lives=4
        image_selection=[1,3,5,7]
    elif level=="a":
        total_lives=remaining_lives=8
        image_selection=[0,1,2,3,4,5,6,7] 
    else:
        if level!="a":
            print("your choice is invalid")
    
    while remaining_lives>0:
        available_letters=get_available_letters(letters_gussed)
        print("Available Letters:"+available_letters)
        guess=input ("Please guess a letter:")
        letter= guess.lower()
        if letter=="hint":
            print("your hint for the secret word is",get_hint(secret_word,letters_gussed))
        # if (not ifValid(letter)):
        #    continue
        if (not ifValid(letter)):
            print("invalid input")
            continue
        if letter in secret_word:
            letters_gussed.append(letter)
            print("Good guss:"+get_guessed_word(secret_word,letters_gussed))
            print("")
            if is_word_guessed(secret_word,letters_gussed)==True:
                print("** congratulations, You win!**")
            print("")
            break
        else:
            print ("Oops! That letter is not in my word: " + get_guessed_word(secret_word, letters_gussed))
            letters_gussed.append(letter)
            print(IMAGES[image_selection[total_lives-remaining_lives]])
            remaining_lives -= 1
            print("remaining_lives:"+str(remaining_lives))       
            print("")
    else: 
        print("sorry, you run out of guess. the word was"+str(secret_word)+".")   
        
secret_word=choose_word()
hangman(secret_word)          
                            












