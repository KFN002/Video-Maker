import os
from PIL import Image, ImageFilter


def upscale_image(img):
    width, height = img.size
    large_img = img.resize((width * 4, height * 4), Image.BICUBIC)
    blurred_img = large_img.filter(ImageFilter.BLUR)

    return blurred_img


def process_images(source_dir, dest_dir):
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)

    for root, _, files in os.walk(source_dir):
        for file_name in files:
            if file_name.lower().endswith(('.png', '.jpg', '.jpeg', '.webp')):
                file_path = os.path.join(root, file_name)
                try:
                    img = Image.open(file_path).convert("RGB")
                    img_hr = upscale_image(img)

                    dest_file_path = os.path.join(dest_dir, file_name)
                    img_hr.save(dest_file_path)

                    print(f"Processed and saved: {dest_file_path}")

                except Exception as e:
                    print(f"Error processing {file_path}: {e}")


def main():
    source_directory = "C:/Users/fedot/Desktop/class"
    destination_directory = "C:/Users/fedot/Desktop/class2"

    process_images(source_directory, destination_directory)


if __name__ == "__main__":
    main()
