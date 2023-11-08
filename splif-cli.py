# Splif GIF Splitter
# Coded by Judith Greaney 2023
# Version 0.1.2

# import Pillow library
from PIL import Image
#imports GIF file and extracts frames, saves to destination
def frameExtract(gifpath, dest, ext, complvl):
    img = Image.open(gifpath)
    try:
        frame = 0
        while True:
            currentframe = img.copy()
            currentframe = currentframe.convert('RGB') # Converts the frame to RGB, otherwise the code exits with an error
            currentframe.save(f"{dest}/frame{img.tell()}.{ext}", optimize=True, quality=100 - complvl)
            frame += 1
            img.seek(frame)
    except EOFError:
        pass
    finally:
        img.close()
        exit()

print("Splif GIF Splitter v0.1.2")
print("Coded by Judith Greaney 2023")
gifpath = input("Enter the path to your gif here:").strip('\'"')
dest = input("Where would you like to output to?:").strip('\'"')
while True:
    try:
        compression = int(input("What level of compression would you like? (0 is no compression, 100 is max compression, a.k.a artifact city): "))
        if compression < 0 or compression > 100:
            print("Input must be a number between 0 and 100")
        else:
            break
    except ValueError as e:
        print("Please enter a valid number between 0 and 100.")
ext = input("What type of file would you like?")
frameExtract(gifpath, dest, ext, compression)
