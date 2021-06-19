subcipher = {
    "A" : "N",
    "B" : "O",
    "C" : "P",
    "D" : "Q",
    "E" : "R",
    "F" : "S",
    "G" : "T",
    "H" : "U",
    "I" : "V",
    "J" : "W",
    "K" : "X",
    "L" : "Y",
    "M" : "Z",
    "N" : "A",
    "O" : "B",
    "P" : "C",
    "Q" : "D",
    "R" : "E",
    "S" : "F",
    "T" : "G",
    "U" : "H",
    "V" : "I",
    "W" : "J",
    "X" : "K",
    "Y" : "L",
    "Z" : "M",
    " " : " "
}

def ciphersucc(subci):
    for each in subci:
        print(subcipher.get(each,"?"), end="")


logo = (f"""

        |||||      ||||||||||      |||||||||||    |||||||||       ||     ||    |||||||||     |||||||||||||||||      |||||||||          |||||||||   
        ||   ||    ||            |||              ||       ||      ||   ||     ||      ||           ||            ||        ||         ||       ||
        ||    ||   ||           ||                ||       ||       || ||      ||       ||          ||           ||          ||        ||       ||
        ||    ||   ||          |||                |||||||||||        ||        ||      ||           ||          ||            ||       |||||||||| 
        ||    ||   ||||||      ||                 ||       ||        ||        |||||||||            ||         ||              ||      ||       ||
        ||   ||    ||           ||                ||        ||       ||        ||                   ||          ||            ||       ||        ||    
        ||  ||     ||            |||              ||         ||      ||        ||                   ||           ||          ||        ||         ||
        ||||       ||||||||||       |||||||||||   ||          ||     ||        ||                   ||             ||||||||||          ||          || 

""")

choice = ''
print(logo)
print()
print()
decrypter = input("Type 'Cipher' for human verification: ").lower()
print()
print()
while True:
    if decrypter == "cipher":
        print()
        print()
        ciphermsg = input("Please enter your cipher code here: ").upper()
        print()
        print("Result: ")
        print()
        ciphersucc(ciphermsg)
        print()
        choice = input("What would you like to do next? [menu/exit]: ")
        if choice == "exit":
            print("See you later!")
            exit()
        elif choice == "menu":
            print()
            print(ciphermsg)
        else:
            print("Error! Redirecting you to menu!")
            print()
            print()
            print(logo)
            print(decrypter)
    elif decrypter == "exit":
        exit()
    else:
        print("Your value was incorrect.")
        print()
        print()
        print(decrypter)