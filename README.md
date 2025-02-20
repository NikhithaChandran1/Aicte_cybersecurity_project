# Aicte_cybersecurity_project
This is apart of the AICTE IBM Skillsbuild Internship on Cybersecurity done by Nikhitha Konnikkara Chandran.


Image Steganography using OpenCV

This project implements a simple image-based steganography system using Python and OpenCV. It allows you to hide a secret message inside an image and later retrieve it using a password.

🚀 How It Works

-The encrypt.py script takes an input image and a secret message and hides the message inside the image.

-The decrypt.py script extracts the hidden message from the encrypted image, but only if the correct password is provided.

📜 Prerequisites

Make sure you have the following installed:

1.Python 3.x (I have used Python 3.13)

2.OpenCV (pip install opencv-python)

📂 Project Structure

│── encrypt.py  # Script to encrypt message in an image
│── decrypt.py  # Script to decrypt message from an image
│── password.txt  # Stores the password (auto-generated)
│── README.md  # This file

🔐 Encryption Process

1.Place an image (e.g., Waterfall.jpg) in the same folder as encrypt.py.

2.Run the encryption script:

-python encrypt.py

3.Enter the image path and the secret message when prompted.

4.Enter a passcode to protect your message.

5.The encrypted image (encryptedImage.png) will be generated.

6.The password is stored in password.txt.

🔓 Decryption Process

1.Run the decryption script:

-python decrypt.py

2.Enter the encrypted image path (encryptedImage.png).

3.Enter the passcode used during encryption.

4.If the password matches, the hidden message is displayed. Otherwise, access is denied.

🛠️ Troubleshooting

Image not found? Ensure the correct image path is provided.

Decrypted message is corrupted? Make sure to use .png instead of .jpg to avoid compression issues.

Wrong passcode? The message cannot be decrypted without the correct password.


💡 Future Improvements

-Use better encryption techniques for increased security.

-Implement GUI-based message hiding and retrieval.



