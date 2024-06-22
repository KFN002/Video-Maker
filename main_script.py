import cv2
import os
from os.path import join
import numpy as np
from data import pic_path, fps, resolution, output_name

width, height = resolution

image_files = [f for f in os.listdir(pic_path) if
               f.endswith('.jpg') or f.endswith('.png') or f.endswith('.webp') or f.endswith('.JPG') or f.endswith(
                   '.jfif')]
image_files.sort()
image_files.remove('_.png')
image_files.insert(0, '_.png')

video_output = f'{output_name}.avi'
fourcc = cv2.VideoWriter_fourcc(*'XVID')
video_writer = cv2.VideoWriter(video_output, fourcc, fps, (width, height))


def resize_and_center(img, target_width, target_height):
    h, w = img.shape[:2]
    aspect_ratio = w / h

    if aspect_ratio > target_width / target_height:
        new_w = target_width
        new_h = int(new_w / aspect_ratio)
    else:
        new_h = target_height
        new_w = int(new_h * aspect_ratio)

    resized = cv2.resize(img, (new_w, new_h))

    delta_w = target_width - new_w
    delta_h = target_height - new_h
    top, bottom = delta_h // 2, delta_h - (delta_h // 2)
    left, right = delta_w // 2, delta_w - (delta_w // 2)
    resized_with_border = cv2.copyMakeBorder(resized, top, bottom, left, right, cv2.BORDER_CONSTANT, value=(0, 0, 0))

    return resized_with_border


def add_fade_transition(img1, img2, fade_duration):
    for alpha in np.linspace(0, 1, fade_duration):
        blended = cv2.addWeighted(img1, 1 - alpha, img2, alpha, 0)
        yield blended.astype(np.uint8)


frame_duration = int(fps)
transition_duration = int(fps // 2)
first_image_duration = int(fps * 3)

for i in range(len(image_files) - 1):
    img1_path = join(pic_path, image_files[i])
    img2_path = join(pic_path, image_files[i + 1])

    img1 = cv2.imread(img1_path)
    img2 = cv2.imread(img2_path)

    img1_resized = resize_and_center(img1, width, height)
    img2_resized = resize_and_center(img2, width, height)

    if i == 0:
        for _ in range(first_image_duration):
            video_writer.write(img1_resized)
    else:
        for _ in range(frame_duration):
            video_writer.write(img1_resized)

    for frame in add_fade_transition(img1_resized, img2_resized, transition_duration):
        video_writer.write(frame)

last_image_path = join(pic_path, image_files[-1])
last_image = cv2.imread(last_image_path)
last_image_resized = resize_and_center(last_image, width, height)
for _ in range(frame_duration):
    video_writer.write(last_image_resized)

video_writer.release()
