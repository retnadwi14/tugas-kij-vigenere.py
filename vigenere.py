def encrypt_vigenere(plaintext, key):
    encrypted_bits = []
    key_bits = [ord(char) for char in key]

    for i, char in enumerate(plaintext):
        char_bits = ord(char)
        key_index = i % len(key)
        encrypted_bits.append(char_bits ^ key_bits[key_index])

    return bytes(encrypted_bits)

def decrypt_vigenere(ciphertext, key):
    decrypted_bits = []
    key_bits = [ord(char) for char in key]

    for i, char in enumerate(ciphertext):
        char_bits = char
        key_index = i % len(key)
        decrypted_bits.append(char_bits ^ key_bits[key_index])

    return bytes(decrypted_bits).decode('utf-8')

if __name__ == "__main__":
    while True:
        print("\nOptions:")
        print("1. Custom input")
        print("2. Default input")
        print("3. Exit")
        choice = input("Choose an option (1, 2, or 3): ")

        if choice == '1':
            plaintext = input("Enter the plaintext: ")
            key = input("Enter the key: ")
        elif choice == '2':
            plaintext = "HelloWorldThisIsAVeryLongText"
            key = "SecretKey12345"
        elif choice == '3':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please choose 1, 2, or 3.")
            continue

        # Encryption
        encrypted_text = encrypt_vigenere(plaintext, key)
        print("\nResults:")
        print(f"Plaintext: {plaintext}")
        print(f"Key: {key}")
        print(f"Encrypted Text: {encrypted_text}")

        # Decryption
        decrypted_text = decrypt_vigenere(encrypted_text, key)
        print(f"Decrypted Text: {decrypted_text}")

        restart = input("\nDo you want to go back to the main menu? (yes/no): ")
        if restart.lower() != 'yes':
            print("Exiting the program.")
            break
