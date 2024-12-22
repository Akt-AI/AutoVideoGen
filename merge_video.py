from moviepy.editor import VideoFileClip, concatenate_videoclips
import os
from PIL import Image
import numpy as np

def custom_resize(clip, newsize):
    """Resize clip to newsize while maintaining aspect ratio."""
    # Resize frame by frame
    def resize_frame(frame):
        pil_image = Image.fromarray(frame)
        resized_image = pil_image.resize(newsize, Image.LANCZOS)
        return np.array(resized_image)

    return clip.fl_image(resize_frame)

# Directory containing the video files
video_directory = "video"

# List of video file paths to merge
video_files = os.listdir(video_directory)
print(video_files)

# Create full paths for the video files
video_paths = [os.path.join(video_directory, video) for video in video_files]

# Load and resize the video clips
clips = []
for video in video_paths:
    clip = VideoFileClip(video)
    resized_clip = custom_resize(clip, newsize=(1920, 1080))  # Resize to 1080p
    clips.append(resized_clip)

# Concatenate the clips
merged_clip = concatenate_videoclips(clips)

# Output the final merged video
merged_clip.write_videofile("merged_video.mp4", codec="libx264", audio_codec="aac")

# Close the clips to free resources
for clip in clips:
    clip.close()

