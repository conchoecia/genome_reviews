from PIL import Image
import os

# --- CONFIGURATION ---
CROP_HEIGHT = 44  # number of pixels to remove from the top
INPUT_FOLDER = '.'  # current directory
OUTPUT_FOLDER = 'trimmed'

# --- CREATE OUTPUT DIRECTORY ---
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

# --- PROCESS IMAGES ---
for filename in os.listdir(INPUT_FOLDER):
    if filename.lower().endswith('.png'):
        input_path = os.path.join(INPUT_FOLDER, filename)
        output_path = os.path.join(OUTPUT_FOLDER, filename)

        with Image.open(input_path) as img:
            width, height = img.size
            cropped_img = img.crop((0, CROP_HEIGHT, width, height))  # (left, top, right, bottom)
            cropped_img.save(output_path)

print(f"Done. Trimmed images saved in ./{OUTPUT_FOLDER}")