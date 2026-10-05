import os
from PIL import Image

src_path = r'C:\Users\NDIEZE\.gemini\antigravity\scratch\waasz-website\assets\waasz-logo.png'
assets_dir = r'C:\Users\NDIEZE\.gemini\antigravity\scratch\waasz-website\assets'
root_dir = r'C:\Users\NDIEZE\.gemini\antigravity\scratch\waasz-website'

img = Image.open(src_path).convert('RGBA')

def make_square_icon(src_img, size, padding_ratio=0.06):
    w, h = src_img.size
    target_h = int(size * (1 - 2 * padding_ratio))
    target_w = int(w * (target_h / h))
    if target_w > int(size * (1 - 2 * padding_ratio)):
        target_w = int(size * (1 - 2 * padding_ratio))
        target_h = int(h * (target_w / w))
    
    resized = src_img.resize((target_w, target_h), Image.Resampling.LANCZOS)
    canvas = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    offset = ((size - target_w) // 2, (size - target_h) // 2)
    canvas.paste(resized, offset, resized)
    return canvas

# 180x180 for Apple Touch Icon
icon_180 = make_square_icon(img, 180, padding_ratio=0.08)
icon_180.save(os.path.join(assets_dir, 'apple-touch-icon.png'))
icon_180.save(os.path.join(root_dir, 'apple-touch-icon.png'))

# 32x32 favicon
icon_32 = make_square_icon(img, 32, padding_ratio=0.04)
icon_32.save(os.path.join(assets_dir, 'favicon-32x32.png'))
icon_32.save(os.path.join(root_dir, 'favicon-32x32.png'))

# 16x16 favicon
icon_16 = make_square_icon(img, 16, padding_ratio=0.04)
icon_16.save(os.path.join(assets_dir, 'favicon-16x16.png'))
icon_16.save(os.path.join(root_dir, 'favicon-16x16.png'))

# 48x48
icon_48 = make_square_icon(img, 48, padding_ratio=0.04)

# favicon.ico
icon_48.save(os.path.join(root_dir, 'favicon.ico'), format='ICO', sizes=[(16,16), (32,32), (48,48)])
icon_48.save(os.path.join(assets_dir, 'favicon.ico'), format='ICO', sizes=[(16,16), (32,32), (48,48)])

# Vector logo SVG
svg_data = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="112 56 664 856" width="100%" height="100%">
  <path d="M121 222 A150 150 0 0 1 271 72 L393 72 L393 313 A112 112 0 0 0 505 425 L768 425 L768 600 Q768 678 700 716 L457 852 L375 696 L251 695 A130 130 0 0 1 121 565 Z" fill="#18181B"/>
  <path d="M447 299 L447 82 Q447 64 466 64 L762 358 Q770 377 745 377 L525 377 A78 78 0 0 1 447 299 Z" fill="#18181B"/>
  <path d="M375 696 L520 696 Q548 698 541 725 L540 726 L537 742 L530 758 L520 774 L508 790 L495 806 L481 822 L466 838 L450 854 L433 870 L414 886 L405 894 Q396 903 388 904 Q375 905 375 888 Z" fill="#C2410C"/>
</svg>"""

with open(os.path.join(assets_dir, 'waasz-logo.svg'), 'w', encoding='utf-8') as f:
    f.write(svg_data)
with open(os.path.join(root_dir, 'waasz-logo.svg'), 'w', encoding='utf-8') as f:
    f.write(svg_data)

print("All favicons and vector assets generated successfully!")
