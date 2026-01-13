import numpy as np
from PIL import Image
import os

def save_image(image_array: np.ndarray, filename: str, output_dir: str = 'output'):
    """
    Saves a numpy RGB array as an image file.
    
    Args:
        image_array (np.ndarray): (H, W, 3) uint8 array.
        filename (str): Output filename (e.g., 'mandelbrot.png').
        output_dir (str): Directory where the image will be saved.
    """
    # Ensure directory exists
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        print(f"Created output directory: {output_dir}")
        
    filepath = os.path.join(output_dir, filename)
    
    # Convert Array to Image
    try:
        img = Image.fromarray(image_array, 'RGB')
        img.save(filepath)
        print(f"Image saved successfully: {filepath}")
    except Exception as e:
        print(f"Error saving image: {e}")
