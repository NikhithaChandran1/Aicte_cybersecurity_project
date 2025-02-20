import cv2

def decrypt_image(image_path):
    """Decrypts a message from an image."""
    img = cv2.imread(image_path)
    if img is None:
        print("Error: Encrypted image not found!")
        return

    try:
        with open("password.txt", "r") as f:
            saved_password = f.read().strip()
    except FileNotFoundError:
        print("Error: Password file not found!")
        return

    entered_password = input("Enter passcode for decryption: ")
    
    if entered_password != saved_password:
        print("YOU ARE NOT AUTHORIZED!")
        return
    
    message = ""
    n, m, z = 0, 1, 0  # Start from (0,1) since (0,0) stores length

    # Read the stored message length
    message_length = img[0, 0, 0]

    for _ in range(message_length):
        message += chr(img[n % img.shape[0], m % img.shape[1], z])
        n += 1
        m += 1
        z = (z + 1) % 3  # Rotate RGB channels

    print("Decrypted message:", message)

# Run the decryption process
if __name__ == "__main__":
    image_path = input("Enter the encrypted image path: ")
    decrypt_image(image_path)
