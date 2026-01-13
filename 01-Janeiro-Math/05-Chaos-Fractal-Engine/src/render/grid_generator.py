import numpy as np

class GridSystem:
    @staticmethod
    def generate_complex_plane(width: int, height: int, x_min: float, x_max: float, y_min: float, y_max: float) -> np.ndarray:
        """
        Generates a 2D grid of complex numbers mapping pixels to the complex plane.
        
        Args:
            width (int): Image width in pixels.
            height (int): Image height in pixels.
            x_min (float): Real part minimum.
            x_max (float): Real part maximum.
            y_min (float): Imaginary part minimum.
            y_max (float): Imaginary part maximum.
            
        Returns:
            np.ndarray: 2D array (height, width) of complex128 numbers.
        """
        # Create linearly spaced arrays for Real (x) and Imaginary (y) axes
        real_vals = np.linspace(x_min, x_max, width)
        imag_vals = np.linspace(y_min, y_max, height)
        
        # Create 2D coordinate matrices
        # We use 'xy' indexing for meshgrid so Re maps to x-axis (columns) and Im maps to y-axis (rows)
        # Note: image convention is (row, col), so usually y is the first dimension physically
        # sparse=False ensures we get full 2D arrays
        xx, yy = np.meshgrid(real_vals, imag_vals)
        
        # Combine into complex numbers: Z = x + iy
        complex_grid = xx + 1j * yy
        
        return complex_grid.astype(np.complex128)
