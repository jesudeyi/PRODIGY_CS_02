from PIL import Image
import numpy as np
import random

import tkinter as tk
from tkinter import filedialog

def load_image(image_path):

    image = Image.open(image_path)
    return np.array(image)

def save_image(image_array, output_path):
    image = Image.fromarray(image_array)
    image.save(output_path)

def permute_pixels(image_array, key):
    flat_image = image_array.flatten()

    random.seed(key)
    permutation = list(range(len(flat_image)))
    random.shuffle(permutation)

    permuted_image = flat_image[permutation]
    permuted_image = permuted_image.reshape(image_array.shape)
    
    return permuted_image

def encrypt_image(image_path, output_path, key):
    # Step 1: Load the image
    image_array = load_image(image_path)

    # Step 2: Permute the pixel positions
    encrypted_image = permute_pixels(image_array, key)

    # Step 3: Save the encrypted image
    save_image(encrypted_image.astype(np.uint8), output_path)
    print(f"Image encrypted and saved as {output_path}")

def unpermute_pixels(image_array, key):
    flat_image = image_array.flatten()

    random.seed(key)
    permutation = list(range(len(flat_image)))
    random.shuffle(permutation)

    inverse_permutation = np.argsort(permutation)

    unpermuted_image = flat_image[inverse_permutation]
    
    unpermuted_image = unpermuted_image.reshape(image_array.shape)
    return unpermuted_image



def decrypt_image(image_path, output_path, key):
    # Step 1: Load the encrypted image
    image_array = load_image(image_path)

    # Step 2: Reverse the pixel permutation
    unpermuted_image = unpermute_pixels(image_array, key)

    # Step 3: Save the decrypted image
    save_image(unpermuted_image.astype(np.uint8), output_path)
    print(f"Image decrypted and saved as {output_path}")



try: 
    # Welcome instructions
    print("Which operation do you wish to perform?")
    print("1. Encrypting an image")
    print("2. Decrypting an image") 
    choice = int(input("Enter an option: "))  

    # Encryption
    if choice == 1:
        root = tk.Tk()
        file = filedialog.askopenfile(mode='rb', filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])
        file_path_without_extension = file.name[:-4]

        if file:            
            key = (input("Add an encryption key/passphrase: "))
            output_path = file_path_without_extension + "(Encrypted_image).png"
            encrypt_image(file, output_path, key)
            print("encrypted image saved to ", output_path)

        # Decryption   
    elif choice == 2:
        root = tk.Tk()
        file = filedialog.askopenfile(mode='rb', filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])
        file_path_without_extension = file.name[:-4]

        if file:            
            key = (input("The correct key/passphrase for decryption: "))
            output_path = file_path_without_extension + "(Decrypted_image).png"
            decrypt_image(file, output_path, key)
            print("Decrypted image saved to ", output_path)
            

        
    else:
        print("Input an valid option 1 or 2")
except ValueError:  
    print("That's not a valid number!")



