# Image Encryption and Decryption Tool

This Python tool encrypts and decrypts images using a pixel permutation standard. It allows users to secure their images with a key, ensuring that the original pixel arrangement is obscured.

## Features

- **Encrypt Images**: Randomly permute the pixels of an image using a provided key.
- **Decrypt Images**: Reverse the pixel permutation to restore the original image using the same key.
- **Supports common image formats**: PNG, JPG, JPEG.

## Prerequisites

Make sure you have Python installed on your machine. This tool requires the following Python packages:

- `PIL` (Pillow)
- `numpy`
- `tkinter`

You can install the required packages using pip:

```bash
pip install pillow numpy
