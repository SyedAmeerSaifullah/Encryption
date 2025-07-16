import random
import string

def encryption():
    try:
        word=str(input("Enter the word to be encrypted:"))
    except :
        print("An error occured ")    
    count=0
    for index in word:
        count+=1
    #print(count)
    
    
    if count>=3:
        word=word[1:]+word[0]
        i=0
        while i<=2:
            temp=random.choice(string.ascii_letters)
            word=temp+word
            i+=1
        j=0
        while j<=2:
            temp=random.choice(string.ascii_letters)
            word=word+temp    
            j+=1
    else:
        word=word[len(word)-1]+word[0]
    return word    
    
def decryption():
    text=str(input("Enter the text to be decrypted :"))
    count=0
    for i in text:
        count+=1
    if count<3:
        text=text[1]+text[0]
    else:
        text=text[3:-3]
        lengthText=len(text)-1
        text=text[lengthText]+text[0:lengthText]      
    return text


print("Welcome to our encryption sysetem:")
while True:
    print("1. Encrypt a word :")
    print("2. Decode a secret :")
    print("3. Exit the program :")
  
    choice=int(input("Enter your choice :"))
    if choice==1:
        word=encryption()
        print("The encrypted text is",word)
    elif choice==2:
        text=decryption()
        print("The decoded text is",text)

    elif choice==3:
        print("Program exiting....")
        break
    if choice<1 or choice>3:
        raise ValueError("Invalid choice selected!")    