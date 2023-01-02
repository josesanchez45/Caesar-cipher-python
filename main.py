import art

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def ceasar(userChoice, plainText, shiftAmount):
    endText = ""
    if userChoice== "decode":
        shiftAmount *= -1
    for char in plainText:
        if char in alphabet:
            position = alphabet.index(char)
            newPosition = position + shiftAmount
            endText += alphabet[newPosition]
        else:
            endText += char
    print(f"Your {userChoice}d message is {endText}")


print(art.logo)
shouldContinue = True
while shouldContinue:
  
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    if(shift < len(alphabet)):
        shift = shift % 26

    ceasar(userChoice=direction, plainText=text, shiftAmount=shift)
    
    yesOrNo = input("Would you like to try again? Yes or No?").lower()
    if yesOrNo == "no":
        shouldContinue = False
        print("Thank you for using this cipher.")

