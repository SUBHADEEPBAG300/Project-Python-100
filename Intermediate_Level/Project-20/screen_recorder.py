import cv2
import numpy as np
import pyautogui
import time
import os

# ==============================
# Screen Recorder Class
# ==============================
class ScreenRecorder:
    def __init__(self, output_file="recordings/output.mp4", fps=20.0, resolution=None):
        # recordings ফোল্ডার অটো-ক্রিয়েট হবে
        os.makedirs(os.path.dirname(output_file), exist_ok=True)

        self.output_file = output_file
        self.fps = fps
        self.resolution = resolution or pyautogui.size()  # Default: full screen
        self.is_recording = False

        # Define codec and create VideoWriter object
        fourcc = cv2.VideoWriter_fourcc(*"mp4v")
        self.out = cv2.VideoWriter(self.output_file, fourcc, self.fps, self.resolution)

    def start_recording(self, duration=10):
        """Record the screen for a given duration (seconds)."""
        self.is_recording = True
        print(f"🎥 Recording started... Saving to {self.output_file}")

        start_time = time.time()
        while self.is_recording and (time.time() - start_time) < duration:
            # Capture screen
            img = pyautogui.screenshot()
            frame = np.array(img)
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            # Write frame
            self.out.write(frame)

            # Optional: show live preview
            cv2.imshow("Recording", frame)
            if cv2.waitKey(1) == ord("q"):
                break

        self.stop_recording()

    def stop_recording(self):
        """Stop recording and release resources."""
        self.is_recording = False
        self.out.release()
        cv2.destroyAllWindows()
        print("✅ Recording stopped and saved.")

# ==============================
# Video Processing Functions
# ==============================
def extract_frames(video_path, output_folder="frames"):
    """Extract frames from a video and save as images."""
    os.makedirs(output_folder, exist_ok=True)
    cap = cv2.VideoCapture(video_path)
    count = 0

    while True:
        ret, frame = cap.read()
        if not ret:
            break
        cv2.imwrite(f"{output_folder}/frame_{count}.jpg", frame)
        count += 1

    cap.release()
    print(f"📸 Extracted {count} frames to {output_folder}/")

def convert_format(video_path, output_path="recordings/output.avi"):
    """Convert video format (e.g., mp4 → avi)."""
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    cap = cv2.VideoCapture(video_path)
    fourcc = cv2.VideoWriter_fourcc(*"XVID")
    fps = cap.get(cv2.CAP_PROP_FPS)
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))

    while True:
        ret, frame = cap.read()
        if not ret:
            break
        out.write(frame)

    cap.release()
    out.release()
    print(f"🔄 Converted {video_path} → {output_path}")

# ==============================
# Main Execution
# ==============================
if __name__ == "__main__":
    # Record screen for 10 seconds
    recorder = ScreenRecorder(output_file="recordings/output.mp4", fps=20.0)
    recorder.start_recording(duration=10) 

    # Extract frames
    extract_frames("recordings/output.mp4", output_folder="frames")

    # Convert format
    convert_format("recordings/output.mp4", output_path="recordings/output.avi")