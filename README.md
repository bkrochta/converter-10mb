# converter-10mb

Command line script to convert videos to less than 10mb to send on Discord

## Getting Started

This script is expected to be run on Windows.

### Prerequisites

- `ffmpeg`
- `python3`

Install the dependencies with the following command on Windows in a PowerShell terminal:

```bash
winget install python3 ffmpeg
```

Restart the terminal after installation before running the script

### Installation

In the directory you want to download the script, run the following command:

```bash
git clone https://github.com/bkrochta/converter-10mb.git
cd converter-10mb
```

## Usage

Run the following command in the terminal:

```bash
python transcode.py <input_video_path>
```

An example command:

```bash
python transcode.py ../Videos/clip.mp4
```

The converted file will be placed in the same directory as the input video file with `_10mb` appended.
