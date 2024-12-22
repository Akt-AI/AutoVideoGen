```markdown
# Video Merging and Resizing Script

This script allows you to merge multiple video clips into a single video, resize them to a specified resolution, and overlay background audio. It is ideal for creating a single cohesive video from multiple video files while maintaining high-quality output.

---

## Features

- **Video Resizing**: Resize all input videos to 1080p resolution using high-quality LANCZOS resampling.
- **Video Merging**: Combine multiple video clips into a single video seamlessly.
- **Audio Overlay**: Add a background audio track to the merged video.
- **Output Optimization**: Exports the final video in MP4 format with H.264 video and AAC audio codecs.

---

## Requirements

- Python 3.6 or higher
- Libraries:
  - `moviepy`
  - `Pillow`
  - `numpy`
  - `os`

Install the required libraries using:
```bash
pip install moviepy pillow numpy
```

---

## How to Use

### Step 1: Prepare Input Files
1. Place your video files in a directory named `video` (or update the `video_directory` variable in the script to your directory).
2. Ensure the audio file for the background sound is named `background_audio.wav` and placed in the `audio` directory (or update the `audio_file` variable in the script).

### Step 2: Run the Script
Execute the script:
```bash
python merge_videos.py
```

### Step 3: Output
- The script generates a merged video with the name `merged_video_with_audio.mp4` in the current directory.

---

## Script Workflow

1. **Resize Videos**: 
   - Each video is resized to a resolution of 1920x1080 (1080p).
   - The resizing is performed frame-by-frame using high-quality LANCZOS filtering.

2. **Merge Videos**:
   - All resized videos are concatenated in the order they appear in the directory.

3. **Add Background Audio**:
   - A specified audio file is added as the background audio for the merged video.

4. **Export Final Video**:
   - The merged video with audio is saved in MP4 format with `libx264` codec for high compatibility.

---

## Customization

- **Change Resolution**:
  Modify the `newsize` parameter in the `custom_resize` function to your desired resolution (e.g., `(1280, 720)` for 720p).

- **Input Directory**:
  Update the `video_directory` variable to specify the folder containing your video files.

- **Audio File**:
  Update the `audio_file` variable to use a different audio file.

---

## Example Directory Structure
```
project/
├── merge_videos.py
├── video/
│   ├── video1.mp4
│   ├── video2.mp4
│   └── video3.mp4
├── audio/
│   └── background_audio.wav
```

---

## Notes

- Ensure all video files are in a compatible format for `moviepy` (e.g., `.mp4`, `.mov`).
- For longer videos, the process may take significant time depending on your system performance.

---

## License

This project is open-source and available under the MIT License.
