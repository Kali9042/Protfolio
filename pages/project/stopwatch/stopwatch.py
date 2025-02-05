import tkinter as tk

class Stopwatch:
    def __init__(self, root):
        self.root = root
        self.root.title("Stopwatch")
        self.running = False
        self.time = 0
        self.label = tk.Label(root, text="00:00:00", font=("Helvetica", 48))
        self.label.pack()
        self.start_button = tk.Button(root, text="Start", command=self.start)
        self.start_button.pack(side="left")
        self.stop_button = tk.Button(root, text="Stop", command=self.stop)
        self.stop_button.pack(side="left")
        self.reset_button = tk.Button(root, text="Reset", command=self.reset)
        self.reset_button.pack(side="left")
    
    def update(self):
        if self.running:
            self.time += 1
            self.label.config(text=self.format_time(self.time))
            self.root.after(1000, self.update)
    
    def format_time(self, time):
        minutes, seconds = divmod(time, 60)
        hours, minutes = divmod(minutes, 60)
        return f"{hours:02}:{minutes:02}:{seconds:02}"
    
    def start(self):
        if not self.running:
            self.running = True
            self.update()
    
    def stop(self):
        if self.running:
            self.running = False
    
    def reset(self):
        self.time = 0
        self.label.config(text="00:00:00")
        self.stop()

if __name__ == "__main__":
    root = tk.Tk()
    stopwatch = Stopwatch(root)
    root.mainloop()
