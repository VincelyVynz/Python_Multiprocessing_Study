from PIL import Image
import os, time


def gray_scale(images):
    for image in images:
        filename = os.path.basename(image)
        os.makedirs("output_images", exist_ok=True)
        with Image.open(image) as img:
            print(f"Converting {filename}")
            img = img.convert('L')
            img.save(f'output_images/{filename}')
            print(f"Saved {filename}")


def main():
    folder = input('Enter the images folder path : ')

    if os.path.isdir(folder):
        images = [os.path.join(folder, file) for file in os.listdir(folder) if file.lower().endswith(('.jpg', '.jpeg', '.png'))]
        start_time = time.perf_counter()
        gray_scale(images)
        end_time = time.perf_counter()
        print(f"Time taken to convert {len(images)} images: {end_time - start_time} seconds")
    else:
        print("Folder not found.")


if __name__ == '__main__':
    main()
