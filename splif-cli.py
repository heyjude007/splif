# Splif GIF Splitter
# Coded by Judith Greaney 2023
# Version 0.1.0

# import Pillow library
from PIL import Image
#imports GIF file and extracts frames, saves to destination
# Imports GIF file and extracts frames, saves to destination
def frameExtract(gifpath, dest):
    img = Image.open(gifpath)
    try:
        frame = 0
        while True:
            currentframe = img.copy()
            currentframe = currentframe.convert('RGB') # Converts the frame to RGB, otherwise the code exits with an error
            currentframe.save(f"{dest}/frame{img.tell()}.jpg")
            frame += 1
            img.seek(frame)
    except EOFError:
        pass
    finally:
        img.close()

print("Splif GIF Splitter v0.1.0")
print("Coded by Judith Greaney 2023")
gifpath = input("Enter the path to your gif here:").strip('\'"')
dest = input("Where would you like to output to?:").strip('\'"')
frameExtract(gifpath, dest)
