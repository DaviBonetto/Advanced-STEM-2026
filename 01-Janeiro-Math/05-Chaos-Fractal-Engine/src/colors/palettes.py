import numpy as np

def apply_palette(iteration_map: np.ndarray, max_iter: int, palette_name: str = 'inferno') -> np.ndarray:
    """
    Maps an array of iteration counts to an RGB image using the specified palette.
    
    Args:
        iteration_map (np.ndarray): 2D array of iteration counts.
        max_iter (int): The maximum iteration count used in generation.
        palette_name (str): Name of the palette to use ('inferno', 'electric_blue', 'psychodelic', 'grayscale').
        
    Returns:
        np.ndarray: 3D array (H, W, 3) of uint8 representing the RGB image.
    """
    # Normalize iterations from 0 to 1
    # We use a power law or log scale often for smoother gradients, but linear is fine for basic
    norm_iter = iteration_map / max_iter
    
    # Create empty RGB image (High, Width, 3 channels)
    h, w = iteration_map.shape
    image = np.zeros((h, w, 3), dtype=np.uint8)
    
    # Mask of points strictly inside the set (converged)
    inside_mask = iteration_map == max_iter
    
    if palette_name == 'inferno':
        # Simulated matplotlib 'inferno' (Black -> Red -> Yellow -> White)
        # R = 255 * (t^0.5)
        # G = 255 * (t^2)
        # B = 255 * (t^4)
        pass 
        # Vectorized implementation of a custom fire-like palette
        t = np.sqrt(norm_iter)
        
        image[:, :, 0] = (255 * t).astype(np.uint8)                    # Red
        image[:, :, 1] = (255 * (t**3)).astype(np.uint8)               # Green
        image[:, :, 2] = (255 * (t**6)).astype(np.uint8)               # Blue
        
    elif palette_name == 'electric_blue':
        # Black -> Blue -> Cyan -> White
        # Cyclic based on modulus can create banding "electric" effects
        # Use simple sine waves for "electric" feel
        
        # t is 0..1
        t = norm_iter
        
        # Frequency multiplier for bands
        freq = 5.0
        
        image[:, :, 0] = (255 * (0.5 + 0.5 * np.sin(freq * np.pi * t + 0.0))).astype(np.uint8) # R
        image[:, :, 1] = (255 * (0.5 + 0.5 * np.sin(freq * np.pi * t + 2.0))).astype(np.uint8) # G
        image[:, :, 2] = (255 * (0.5 + 0.5 * np.sin(freq * np.pi * t + 4.0))).astype(np.uint8) # B
        
        # Override visual for 'outside' set points that are close to 0 iterations (dark)
        # But specifically make the "inside" points black
        
    elif palette_name == 'psychodelic':
        # HSV-like rainbow conversion style manually calculated
        freq = 10.0
        image[:, :, 0] = (255 * ((np.sin(freq * norm_iter + 0) + 1) / 2)).astype(np.uint8)
        image[:, :, 1] = (255 * ((np.sin(freq * norm_iter + 2) + 1) / 2)).astype(np.uint8)
        image[:, :, 2] = (255 * ((np.sin(freq * norm_iter + 4) + 1) / 2)).astype(np.uint8)
        
    else: # grayscale
        val = (norm_iter * 255).astype(np.uint8)
        image[:, :, 0] = val
        image[:, :, 1] = val
        image[:, :, 2] = val

    # Set converged points to Black (0, 0, 0)
    image[inside_mask] = [0, 0, 0]
    
    return image
