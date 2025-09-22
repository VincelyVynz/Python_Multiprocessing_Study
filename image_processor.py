from PIL import Image
import os

def gray_scale(image):
    filename = os.path.basename(image)
    with Image.open(image) as img:
        img = img.convert('L')
        img.save(f'output_images/{filename}')



def main():
    image = input('Enter the image to be processed: ')
    if image:
        gray_scale(image)

if __name__ == '__main__':
    main()