from PIL import Image, ImageEnhance, ImageFilter
import numpy as np
from scipy import ndimage

def enhance_image_smooth(src_path, dst_path):
    orig = Image.open(src_path).convert('RGB')
    w, h = orig.size
    
    # 2.5x upscale (1192 x 532) - matches exact display needs (container is ~500px wide, 185px high)
    target_w = int(w * 2.5)
    target_h = int(h * 2.5)
    
    # Resize with high quality Lanczos
    resampled = orig.resize((target_w, target_h), Image.Resampling.LANCZOS)
    
    # Light median filter or gentle bilateral to remove compression speckles
    # We can do a gentle cross-channel bilateral approximation using gaussian on RGB
    arr = np.array(resampled, dtype=np.float32)
    
    # Apply subtle guided smoothing
    smoothed = np.zeros_like(arr)
    for i in range(3):
        smoothed[:, :, i] = ndimage.gaussian_filter(arr[:, :, i], sigma=0.75)
    
    # Edge detection
    lum = 0.299 * arr[:, :, 0] + 0.587 * arr[:, :, 1] + 0.114 * arr[:, :, 2]
    dx = ndimage.sobel(lum, axis=1)
    dy = ndimage.sobel(lum, axis=0)
    mag = np.hypot(dx, dy)
    weight = np.clip(mag / 40.0, 0.0, 1.0)[:, :, np.newaxis]
    
    # Recombine: smooth flat areas, keep crisp transitions
    blended = arr * weight + smoothed * (1.0 - weight)
    clean_img = Image.fromarray(np.clip(blended, 0, 255).astype(np.uint8))
    
    # Very gentle, clean unsharp mask without crunchy edges
    crisp = clean_img.filter(ImageFilter.UnsharpMask(radius=1.2, percent=85, threshold=3))
    
    # Enhance vibrance and contrast gently
    contrast = ImageEnhance.Contrast(crisp).enhance(1.08)
    color = ImageEnhance.Color(contrast).enhance(1.06)
    
    color.save(dst_path, format='PNG', optimize=True)
    print(f"Saved smooth enhanced image: {dst_path} ({target_w}x{target_h})")

enhance_image_smooth('media/museo_historia_natural.png', 'media/museo_historia_natural_hd.png')
