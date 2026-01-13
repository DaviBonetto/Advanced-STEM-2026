import argparse
import sys
import time

# Ensure src is in pythonpath
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from src.render.engine import FractalRenderer
from src.utils.file_io import save_image

def parse_resolution(res_str):
    try:
        w, h = map(int, res_str.lower().split('x'))
        return w, h
    except ValueError:
        raise argparse.ArgumentTypeError("Resolution must be in format WIDTHxHEIGHT (e.g., 800x600)")

def main():
    parser = argparse.ArgumentParser(description="Chaos Fractal Engine - Advanced Science 2026")
    
    parser.add_argument('--type', type=str, choices=['mandelbrot', 'julia'], default='mandelbrot',
                        help='Type of fractal to generate')
    
    parser.add_argument('--res', type=parse_resolution, default='800x800',
                        help='Resolution in WIDTHxHEIGHT (default: 800x800)')
    
    parser.add_argument('--iter', type=int, default=100,
                        help='Maximum number of iterations (default: 100)')
    
    parser.add_argument('--cmap', type=str, choices=['inferno', 'electric_blue', 'psychodelic', 'grayscale'], default='inferno',
                        help='Color palette (default: inferno)')
    
    parser.add_argument('--output', type=str, default='fractal.png',
                        help='Output filename')
    
    # Julia set specific params
    parser.add_argument('--cx', type=float, default=-0.7, help='Julia set Re(c)')
    parser.add_argument('--cy', type=float, default=0.27015, help='Julia set Im(c)')

    args = parser.parse_args()
    
    width, height = args.res
    
    print("="*60)
    print(f"CHAOS FRACTAL ENGINE | Mode: {args.type.upper()}")
    print("="*60)
    
    renderer = FractalRenderer()
    
    start_time = time.time()
    
    try:
        image = renderer.render(
            fractal_type=args.type,
            width=width,
            height=height,
            max_iter=args.iter,
            cmap=args.cmap,
            c_real=args.cx,
            c_imag=args.cy
        )
        
        save_image(image, args.output)
        
        elapsed = time.time() - start_time
        print(f"Done! Total time: {elapsed:.4f}s")
        print(f"Output saved to: output/{args.output}")
        
    except Exception as e:
        print(f"CRITICAL ERROR: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()
