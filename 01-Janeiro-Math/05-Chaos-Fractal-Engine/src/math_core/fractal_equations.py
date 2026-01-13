import numpy as np

def mandelbrot_kernel(c_grid: np.ndarray, max_iter: int = 100) -> np.ndarray:
    """
    Computes the Mandelbrot set for a grid of complex numbers C.
    Formula: Z = Z^2 + C, starting with Z = 0.
    
    Args:
        c_grid (np.ndarray): 2D array of complex coordinates.
        max_iter (int): Maximum number of iterations.
        
    Returns:
        np.ndarray: 2D integer array where each value is the iteration count 
                    at which the point diverged (or max_iter if bounded).
    """
    # Z starts at 0 for Mandelbrot
    z = np.zeros_like(c_grid, dtype=np.complex128)
    
    # Array to store the iteration number when divergence happens
    divergence_map = np.zeros(c_grid.shape, dtype=int)
    
    # Mask to track points that haven't diverged yet
    mask = np.ones(c_grid.shape, dtype=bool)
    
    for i in range(max_iter):
        if not np.any(mask):
            break
            
        # Only update points that are still within bounds
        # Z_{n+1} = Z_n^2 + C
        z[mask] = z[mask]**2 + c_grid[mask]
        
        # Check for divergence: |Z| > 2 (squared check |Z|^2 > 4 is faster)
        # However, np.abs handles complex magnitude correctly.
        diverged = np.abs(z) > 2.0
        
        # Identify points that JUST diverged in this iteration
        newly_diverged = mask & diverged
        
        # Record iteration number
        divergence_map[newly_diverged] = i
        
        # Update mask: stop processing diverged points
        mask[diverged] = False
        
    # For points that never diverged, set them to max_iter
    divergence_map[mask] = max_iter
    
    return divergence_map

def julia_kernel(z_grid: np.ndarray, c: complex, max_iter: int = 100) -> np.ndarray:
    """
    Computes the Julia set for a grid of starting Z values and a constant C.
    Formula: Z = Z^2 + C.
    
    Args:
        z_grid (np.ndarray): 2D array of initial Z values (the complex plane).
        c (complex): The constant parameter for the Julia set.
        max_iter (int): Maximum number of iterations.
        
    Returns:
        np.ndarray: 2D integer array of iteration counts.
    """
    # Copy z_grid to avoid modifying input
    z = z_grid.copy().astype(np.complex128)
    
    divergence_map = np.zeros(z_grid.shape, dtype=int)
    mask = np.ones(z_grid.shape, dtype=bool)
    
    for i in range(max_iter):
        if not np.any(mask):
            break
            
        # Z_{n+1} = Z_n^2 + C
        z[mask] = z[mask]**2 + c
        
        diverged = np.abs(z) > 2.0
        newly_diverged = mask & diverged
        
        divergence_map[newly_diverged] = i
        mask[diverged] = False
    
    divergence_map[mask] = max_iter
    
    return divergence_map
