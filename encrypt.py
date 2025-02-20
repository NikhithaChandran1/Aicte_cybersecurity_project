import cv2
import os

def encrypt_image(image_path, secret_msg, password, output_path="encryptedImage.png"):
    """Encrypts a message into an image."""
    img = cv2.imread(image_path)
    if img is None:
        print("Error: Image not found!")
        return
    
    # Store message length in the first pixel
    img[0, 0, 0] = len(secret_msg)

    n, m, z = 0, 1, 0  # Start from (0,1) to avoid overwriting the length

    for char in secret_msg:
        img[n % img.shape[0], m % img.shape[1], z] = ord(char)  # Store ASCII value
        n += 1
        m += 1
        z = (z + 1) % 3  # Rotate RGB channels

    cv2.imwrite(output_path, img)  # Save as PNG to prevent corruption
    print(f"Message encrypted and saved as {output_path}")

    with open("password.txt", "w") as f:
        f.write(password)  # Save password

    os.system(f"start {output_path}")  # Open encrypted image (Windows)

# Run the encryption process
if __name__ == "__main__":
    image_path = input("Enter the image path: ")
    message = input("Enter secret message: ")
    password = input("Enter a passcode: ")
    encrypt_image(image_path, message, password)
