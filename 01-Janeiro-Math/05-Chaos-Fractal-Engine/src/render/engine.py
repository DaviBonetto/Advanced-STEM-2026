import numpy as np
from ..math_core.fractal_equations import mandelbrot_kernel, julia_kernel
from ..colors.palettes import apply_palette
from .grid_generator import GridSystem

class FractalRenderer:
    def __init__(self):
        pass

    def render(self, fractal_type: str, width: int, height: int, max_iter: int, 
               cmap: str = 'inferno', **kwargs) -> np.ndarray:
        """
        Main rendering pipeline.
        
        Args:
            fractal_type (str): 'mandelbrot' or 'julia'.
            width (int): Image width.
            height (int): Image height.
            max_iter (int): Maximum iterations.
            cmap (str): Color palette name.
            **kwargs: Additional arguments (e.g., 'c_real', 'c_imag' for Julia).
            
        Returns:
            np.ndarray: RGB image (H, W, 3).
        """
        # 1. Coordinate System Setup
        # Adjust aspect ratio usually [-2, 1] for x and [-1.5, 1.5] for y for Mandelbrot
        ratio = width / height
        
        if fractal_type == 'mandelbrot':
            x_min, x_max = -2.0, 1.0
            y_min, y_max = -1.2, 1.2
            # Adjust x range to match aspect ratio if needed, but standard view is fixed typically
            # Let's simple center it
             
        elif fractal_type == 'julia':
            x_min, x_max = -1.5, 1.5
            y_min, y_max = -1.5, 1.5
        
        # Simple Aspect Ratio Correction
        view_width = x_max - x_min
        view_height = y_max - y_min
        
        if ratio > (view_width / view_height):
            # Image is wider than view, extend x
            desired_width = view_height * ratio
            center_x = (x_min + x_max) / 2
            x_min = center_x - desired_width / 2
            x_max = center_x + desired_width / 2
        else:
            # Image is taller than view, extend y
            desired_height = view_width / ratio
            center_y = (y_min + y_max) / 2
            y_min = center_y - desired_height / 2
            y_max = center_y + desired_height / 2

        print(f"Generating Grid: {width}x{height} in X[{x_min:.2f}, {x_max:.2f}] Y[{y_min:.2f}, {y_max:.2f}]...")
        complex_grid = GridSystem.generate_complex_plane(width, height, x_min, x_max, y_min, y_max)
        
        # 2. Mathematical Kernel
        print(f"Computing {fractal_type} set ({max_iter} iterations)...")
        if fractal_type == 'mandelbrot':
            iterations = mandelbrot_kernel(complex_grid, max_iter)
        elif fractal_type == 'julia':
            c_real = kwargs.get('c_real', -0.7)
            c_imag = kwargs.get('c_imag', 0.27015)
            c = complex(c_real, c_imag)
            print(f"Julia Constant: {c}")
            iterations = julia_kernel(complex_grid, c, max_iter)
        else:
            raise ValueError(f"Unknown fractal type: {fractal_type}")
            
        # 3. Color Mapping
        print(f"Applying Palette '{cmap}'...")
        image = apply_palette(iterations, max_iter, cmap)
        
        return image
