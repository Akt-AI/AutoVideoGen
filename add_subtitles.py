import os
import subprocess
import re

def create_srt_from_markdown(markdown_file):
    srt_lines = []
    with open(markdown_file, 'r') as f:
        lines = f.readlines()
    
    index = 1
    for line in lines:
        match = re.match(r'# (\d{2}:\d{2}:\d{2})', line)
        if match:
            start_time = match.group(1)
            subtitle = next((l.strip() for l in lines if l.strip() and l != line), "")
            if subtitle:
                srt_lines.append(f"{index}\n{start_time},000 --> {start_time},500\n{subtitle}\n")
                index += 1
    
    return ''.join(srt_lines) if srt_lines else None

def save_srt(srt_content, output_file):
    with open(output_file, "w") as srt_file:
        srt_file.write(srt_content)

def add_subtitles_to_video(video_file, srt_file, output_file):
    cmd = [
        'ffmpeg', '-i', video_file, '-vf', f'subtitles={srt_file}',
        '-c:a', 'copy', output_file
    ]
    subprocess.run(cmd)

# Create subtitles from Markdown
markdown_file = "test.md"
srt_content = create_srt_from_markdown(markdown_file)

if srt_content is None:
    raise ValueError("No subtitles were generated. Please check the markdown file format.")

# Save the SRT file
srt_file_path = "subtitles.srt"
save_srt(srt_content, srt_file_path)

# Define the video file and output path
video_file_path = "merged_video_with_audio.mp4"  # Replace with your video path
output_file_path = "output_video_with_subtitles.mp4"

# Add subtitles to the video
add_subtitles_to_video(video_file_path, srt_file_path, output_file_path)

print("Video processing complete. Output saved as:", output_file_path)
