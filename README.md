Simple Text Encryption & Decryption Program (Python CLI)
This is a simple Python-based text encryption and decryption system that encodes short words using random characters and string manipulation. It demonstrates basic logic building, string slicing, and usage of Python's random and string modules.

🚀 Features
🔒 Encrypts user-input text based on custom rules

🔓 Decrypts previously encrypted text to retrieve the original

🧠 Simple logic involving character shuffling and random characters

💬 Command-line menu interface

🛠️ Technologies Used
Python 3

random module

string module

String manipulation and slicing

▶️ How It Works
🔐 Encryption Logic:
If the word is 3 or more characters:

First letter is moved to the end

Three random letters are added to the beginning and end

If less than 3 characters:

The characters are rearranged simply

🔓 Decryption Logic:
Reverses the above logic based on the encrypted word’s length

📦 How to Run
Make sure Python 3 is installed.

Clone/download the repo.

Run the script:

bash
Copy
Edit
python encryptor.py
Choose from:

1 to encrypt a word

2 to decrypt a word

3 to exit

🧪 Sample Run
vbnet
Copy
Edit
Welcome to our encryption system:
1. Encrypt a word :
2. Decode a secret :
3. Exit the program :
Enter your choice :1
Enter the word to be encrypted: hello
The encrypted text is: MqZellohBfY

Enter your choice :2
Enter the text to be decrypted : MqZellohBfY
The decoded text is: hello
