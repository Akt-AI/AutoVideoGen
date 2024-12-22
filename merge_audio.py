from moviepy.editor import AudioFileClip, concatenate_audioclips
import os

# Directory containing the audio files
audio_directory = "audio"  # Change this to your audio files directory

# List of audio file paths to merge
audio_files = os.listdir(audio_directory)
print(audio_files)

# Create full paths for the audio files
audio_paths = [os.path.join(audio_directory, audio) for audio in audio_files]

# Load the audio clips
audio_clips = [AudioFileClip(audio) for audio in audio_paths]

# Concatenate the audio clips
merged_audio = concatenate_audioclips(audio_clips)

# Output the final merged audio
merged_audio.write_audiofile("merged_audio.mp3", codec="libmp3lame")

# Close the audio clips to free resources
for audio in audio_clips:
    audio.close()
merged_audio.close()

