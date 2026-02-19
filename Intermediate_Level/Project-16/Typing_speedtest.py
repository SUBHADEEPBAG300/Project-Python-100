import tkinter as tk
import time
import random

PARAGRAPHS = [
    "Python is a high level programming language widely used in software development data analysis and artificial intelligence. It is known for its simplicity readability and powerful libraries. Python helps developers build applications faster and more efficiently.",

    "Typing speed and accuracy are essential skills for computer science students and professionals. Regular practice improves performance and reduces errors. Efficient typing saves time and increases productivity in daily work."
]

TEST_DURATION = 60

class TypingSpeedTest:
    def __init__(self, root):
        self.root = root
        self.root.title("Typing Speed Test")
        self.root.geometry("950x700")
        self.root.resizable(False, False)

        self.text = random.choice(PARAGRAPHS)
        self.start_time = None
        self.remaining_time = TEST_DURATION
        self.running = False

        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.root, text="Typing Speed Test", font=("Arial", 22, "bold")).pack(pady=10)

        self.timer_label = tk.Label(self.root, text=f"Time Left: {TEST_DURATION}s",
                                    font=("Arial", 16), fg="red")
        self.timer_label.pack()

        self.paragraph_box = tk.Text(self.root, height=7, font=("Arial", 14),
                                     wrap="word", bg="#f0f0f0")
        self.paragraph_box.pack(pady=15, padx=20)
        self.paragraph_box.insert(tk.END, self.text)
        self.paragraph_box.config(state="disabled")

        self.paragraph_box.tag_configure("cursor_mark", background="yellow")

        self.input_box = tk.Text(self.root, height=6, font=("Arial", 14), state="disabled")
        self.input_box.pack(pady=10, padx=20)
        self.input_box.bind("<KeyRelease>", self.check_typing)

        self.input_box.tag_configure("correct", foreground="green")
        self.input_box.tag_configure("wrong", foreground="red")

        self.speed_label = tk.Label(self.root, text="Live Speed: 0 WPM", font=("Arial", 14))
        self.speed_label.pack()

        btn_frame = tk.Frame(self.root)
        btn_frame.pack(pady=10)

        tk.Button(btn_frame, text="Start Test", width=12,
                  command=self.start_test).grid(row=0, column=0, padx=10)
        tk.Button(btn_frame, text="Reset", width=12,
                  command=self.reset_test).grid(row=0, column=1, padx=10)

        self.result_label = tk.Label(self.root, font=("Arial", 14), justify="left")
        self.result_label.pack(pady=15)

    def start_test(self):
        if self.running:
            return

        self.start_time = time.time()
        self.remaining_time = TEST_DURATION
        self.running = True

        self.input_box.config(state="normal")
        self.input_box.delete("1.0", tk.END)

        self.paragraph_box.config(state="normal")
        self.paragraph_box.tag_remove("cursor_mark", "1.0", tk.END)
        self.paragraph_box.tag_add("cursor_mark", "1.0", "1.0+1c")
        self.paragraph_box.config(state="disabled")

        self.result_label.config(text="")
        self.update_timer()

    def update_timer(self):
        if self.remaining_time > 0 and self.running:
            self.timer_label.config(text=f"Time Left: {self.remaining_time}s")
            self.remaining_time -= 1
            self.root.after(1000, self.update_timer)
        else:
            self.finish_test()

    def check_typing(self, event=None):
        if not self.running:
            return

        typed = self.input_box.get("1.0", tk.END)[:-1]

        self.input_box.tag_remove("correct", "1.0", tk.END)
        self.input_box.tag_remove("wrong", "1.0", tk.END)

        correct = 0
        for i in range(len(typed)):
            idx = f"1.0+{i}c"
            if i < len(self.text) and typed[i] == self.text[i]:
                self.input_box.tag_add("correct", idx, f"{idx}+1c")
                correct += 1
            else:
                self.input_box.tag_add("wrong", idx, f"{idx}+1c")

        self.paragraph_box.config(state="normal")
        self.paragraph_box.tag_remove("cursor_mark", "1.0", tk.END)

        pos = len(typed)
        if pos < len(self.text):
            self.paragraph_box.tag_add("cursor_mark",
                                       f"1.0+{pos}c",
                                       f"1.0+{pos+1}c")

        self.paragraph_box.config(state="disabled")

        elapsed = time.time() - self.start_time
        if elapsed > 0:
            wpm = (len(typed.split()) / elapsed) * 60
            self.speed_label.config(text=f"Live Speed: {int(wpm)} WPM")

    def finish_test(self):
        self.running = False
        self.input_box.config(state="disabled")

        typed = self.input_box.get("1.0", tk.END)[:-1]

        correct = 0
        for i in range(min(len(typed), len(self.text))):
            if typed[i] == self.text[i]:
                correct += 1

        total = len(typed)
        errors = max(total - correct, 0)
        accuracy = (correct / total) * 100 if total > 0 else 0

        elapsed = time.time() - self.start_time
        wpm = (len(typed.split()) / elapsed) * 60 if elapsed > 0 else 0

        self.result_label.config(
            text=f"Final Result:\n"
                 f"WPM: {int(wpm)}\n"
                 f"Accuracy: {accuracy:.2f}%\n"
                 f"Errors: {errors}"
        )

    def reset_test(self):
        self.running = False
        self.start_time = None
        self.remaining_time = TEST_DURATION
        self.text = random.choice(PARAGRAPHS)

        self.paragraph_box.config(state="normal")
        self.paragraph_box.delete("1.0", tk.END)
        self.paragraph_box.insert(tk.END, self.text)
        self.paragraph_box.tag_remove("cursor_mark", "1.0", tk.END)
        self.paragraph_box.config(state="disabled")

        self.timer_label.config(text=f"Time Left: {TEST_DURATION}s")
        self.speed_label.config(text="Live Speed: 0 WPM")
        self.result_label.config(text="")

        self.input_box.config(state="normal")
        self.input_box.delete("1.0", tk.END)
        self.input_box.config(state="disabled")

if __name__ == "__main__":
    root = tk.Tk()
    TypingSpeedTest(root)
    root.mainloop()