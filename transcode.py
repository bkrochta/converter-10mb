import os
import sys
import subprocess

# Define the target size in bytes (10 MB)
TARGET_SIZE_BYTES = 10 * 1024 * 1024
AUDIO_BIT_RATE = 96000


def calculate_audio_size(duration: float) -> float:
    return duration * AUDIO_BIT_RATE


def calculate_bitrate(target_size: int, duration: float) -> int:
    # Both are in Bytes
    video_target_size = target_size - calculate_audio_size(duration)
    # Convert to bits per second
    bitrate = (video_target_size * 8) / duration

    return int(bitrate)


def transcode_video(input_path: str, output_path: str):
    try:
        # Get video duration using ffprobe
        result = subprocess.run(
            [
                "ffprobe",
                "-v",
                "error",
                "-show_entries",
                "format=duration",
                "-of",
                "default=noprint_wrappers=1:nokey=1",
                input_path,
            ],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
        )

        duration = float(result.stdout.strip())

        target_bitrate = calculate_bitrate(TARGET_SIZE_BYTES, duration)

        # Run ffmpeg to transcode video
        subprocess.run(
            [
                "ffmpeg",
                "-i",
                input_path,
                "-b:v",
                str(target_bitrate),
                "-bufsize",
                str(target_bitrate * 2),
                "-maxrate",
                str(target_bitrate),
                "-ab",
                str(AUDIO_BIT_RATE),
                "-preset",
                "slow",
                output_path,
            ],
            check=True,
        )

        print(f"Transcoding completed. Output saved to: {output_path}")

    except Exception as e:
        print(f"Error: {e}")


def main():
    if len(sys.argv) != 2:
        print("Usage: python transcode.py <input_video_path>")
        sys.exit(1)

    input_video_path = str(sys.argv[1])
    base, ext = os.path.splitext(input_video_path)
    output_video_path = f"{base}_10mb{ext}"

    if not os.path.exists(input_video_path):
        print(f"Error: Input file '{input_video_path}' does not exist.")
        sys.exit(1)

    transcode_video(input_video_path, output_video_path)


# Main entry point
if __name__ == "__main__":
    main()
