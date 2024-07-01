from PIL import Image
import argparse

# Encryption function
def encrypt_image(image_path, key):
    img = Image.open(image_path)
    width, height = img.size
    pixels = img.load()

    encrypted_pixels = []
    for y in range(height):
        row = []
        for x in range(width):
            r, g, b = pixels[x, y]
            # Encrypt each channel value using XOR with key
            r_encrypted = r ^ key
            g_encrypted = g ^ key
            b_encrypted = b ^ key
            row.append((r_encrypted, g_encrypted, b_encrypted))
        encrypted_pixels.append(row)

    encrypted_img = Image.new(img.mode, (width, height))
    for y in range(height):
        for x in range(width):
            encrypted_img.putpixel((x, y), encrypted_pixels[y][x])

    encrypted_img.save("encrypted_image.png")
    print(f"Image encrypted and saved as 'encrypted_image.png'.")

# Decryption function
def decrypt_image(encrypted_image_path, key):
    img = Image.open(encrypted_image_path)
    width, height = img.size
    pixels = img.load()

    decrypted_pixels = []
    for y in range(height):
        row = []
        for x in range(width):
            r_encrypted, g_encrypted, b_encrypted = pixels[x, y]
            # Decrypt each channel value using XOR with key
            r_decrypted = r_encrypted ^ key
            g_decrypted = g_encrypted ^ key
            b_decrypted = b_encrypted ^ key
            row.append((r_decrypted, g_decrypted, b_decrypted))
        decrypted_pixels.append(row)

    decrypted_img = Image.new(img.mode, (width, height))
    for y in range(height):
        for x in range(width):
            decrypted_img.putpixel((x, y), decrypted_pixels[y][x])

    decrypted_img.save("decrypted_image.png")
    print(f"Image decrypted and saved as 'decrypted_image.png'.")

# Command-line interface
def main():
    parser = argparse.ArgumentParser(description="Image Encryption and Decryption Tool")
    parser.add_argument('action', choices=['encrypt', 'decrypt'], help="Action to perform: encrypt or decrypt")
    parser.add_argument('image_path', help="Path to the image file")
    parser.add_argument('key', type=int, help="Encryption/Decryption key (integer)")
    
    args = parser.parse_args()

    if args.action == 'encrypt':
        encrypt_image(args.image_path, args.key)
    elif args.action == 'decrypt':
        decrypt_image(args.image_path, args.key)

if __name__ == "__main__":
    main()
