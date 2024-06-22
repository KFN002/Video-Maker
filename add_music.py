import os
from moviepy.audio.AudioClip import concatenate_audioclips
from moviepy.editor import VideoFileClip, AudioFileClip
from data import output_name


def add_audio(video_path, audio_path, output_path):
    video_clip = VideoFileClip(video_path)
    audio_background = AudioFileClip(audio_path)

    if audio_background.duration < video_clip.duration:
        n_loops = int(video_clip.duration / audio_background.duration) + 1
        audio_background = concatenate_audioclips([audio_background] * n_loops)

    audio_background = audio_background.subclip(0, video_clip.duration)

    final_video = video_clip.set_audio(audio_background)

    final_video.write_videofile(output_path, codec='libx264')


'''
for audio in os.listdir("background_music"):
    video_output = f"{output_name}.avi"
    audio_file = f"background_music/{audio}"
    final_video_output = f"videos_done/video_{audio[:-4].lower().replace(' ', '_')}.avi"
    add_audio(video_output, audio_file, final_video_output)
'''

video_output = f"{output_name}.avi"
audio_file = f"background_music/два_korablya.mp3"
final_video_output = f"videos_done/video_два_korablya.avi"
add_audio(video_output, audio_file, final_video_output)
