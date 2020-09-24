import glob
from PIL import Image
import sys

def convert(type1, type2):
    print(f"Converting .{type1}\nfiles to .{type2} files...")

    for file in glob.iglob(f"Images/*.{str(type1)}"):
        img = Image.open(file)
        rgb_img = img.convert("RGB")
        file = file.replace("Images", "")
        rgb_img.save(f"Converted_Images/{file.replace(type1, type2)}", quality=95)

    print(f"Finished converting\n.{type1} files\nto .{type2} files")


convert(sys.argv[1], sys.argv[2])
