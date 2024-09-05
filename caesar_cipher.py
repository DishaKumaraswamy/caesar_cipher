import art

print(art.logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(og_text, shift_num, user_choice):
    cipher_text = ""

    if user_choice == "decode":
        shift_num *=-1
                
    for i in og_text :
        if i not in alphabet:
            cipher_text += i

            
        else :
            shifted = alphabet.index(i) + shift_num
            shifted %= len(alphabet)
            cipher_text += alphabet[shifted]

    print(f"Here is the {user_choice} text: {cipher_text}")

cont = True

while cont:
    choice = input("Type 'encode' to encrypt or Type 'decode' to decrypt:\n").lower()
    text = input("Type your message here \n").lower()
    shift = int(input("Type the shift number :\n"))
    caesar(text, shift, choice)
    restart = input("Should you wish to continue type 'Yes'. Type 'No' otherwise.\n").lower()
    if restart == "no" :
        cont = False
        print(art.farewell)
