from moviepy.editor import VideoFileClip
import os


def convert_avi_to_mp4(avi_file, mp4_file):
    try:
        clip = VideoFileClip(avi_file)

        clip.write_videofile(mp4_file, codec='libx264')

        print(f"Successfully converted {avi_file} to {mp4_file}")

    except Exception as e:
        print(f"Error converting {avi_file} to {mp4_file}: {e}")


if __name__ == "__main__":
    for video in os.listdir("videos_done"):
        avi_file = f'videos_done/{video}'
        mp4_file = f'videos_mp4/{video[:-4]}.mp4'

        convert_avi_to_mp4(avi_file, mp4_file)

