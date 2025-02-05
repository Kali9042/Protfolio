import tkinter as tk
from tkinter import colorchooser, filedialog, messagebox
from PIL import Image, ImageDraw, ImageTk
import os
import subprocess

class PaintApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Paint")
        
        self.color = "black"
        self.brush_size = 5
        self.image_path = None
        self.clipboard = None

        self.canvas = tk.Canvas(root, bg="white", width=800, height=600)
        self.canvas.pack(fill=tk.BOTH, expand=True)

        self.setup_menu()
        self.setup_buttons()
        self.setup_bindings()

        self.image = Image.new("RGB", (800, 600), "white")
        self.draw = ImageDraw.Draw(self.image)

    def setup_menu(self):
        menu = tk.Menu(self.root)
        self.root.config(menu=menu)

        file_menu = tk.Menu(menu, tearoff=0)
        menu.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="New", command=self.new_image)
        file_menu.add_command(label="Open", command=self.open_image)
        file_menu.add_command(label="Save", command=self.save_image)
        file_menu.add_command(label="Save As", command=self.save_as_image)
        file_menu.add_command(label="Print", command=self.print_image)
        file_menu.add_command(label="Share", command=self.share_image)
        file_menu.add_command(label="Exit", command=self.root.quit)

        edit_menu = tk.Menu(menu, tearoff=0)
        menu.add_cascade(label="Edit", menu=edit_menu)
        edit_menu.add_command(label="Cut", command=self.cut)
        edit_menu.add_command(label="Copy", command=self.copy)
        edit_menu.add_command(label="Paste", command=self.paste)

        brush_menu = tk.Menu(menu, tearoff=0)
        menu.add_cascade(label="Brush", menu=brush_menu)
        brush_menu.add_command(label="Choose Color", command=self.choose_color)
        brush_menu.add_command(label="Brush Size", command=self.choose_brush_size)

    def setup_buttons(self):
        button_frame = tk.Frame(self.root)
        button_frame.pack(side=tk.TOP, fill=tk.X)

        color_button = tk.Button(button_frame, text="Color", command=self.choose_color)
        color_button.pack(side=tk.LEFT, padx=5, pady=5)

        size_button = tk.Button(button_frame, text="Size", command=self.choose_brush_size)
        size_button.pack(side=tk.LEFT, padx=5, pady=5)

        clear_button = tk.Button(button_frame, text="Clear", command=self.clear_canvas)
        clear_button.pack(side=tk.LEFT, padx=5, pady=5)

        save_button = tk.Button(button_frame, text="Save", command=self.save_image)
        save_button.pack(side=tk.LEFT, padx=5, pady=5)

    def setup_bindings(self):
        self.canvas.bind('<B1-Motion>', self.paint)
        self.canvas.bind('<ButtonRelease-1>', self.reset)

    def choose_color(self):
        self.color = colorchooser.askcolor(color=self.color)[1]

    def choose_brush_size(self):
        size = tk.simpledialog.askinteger("Brush Size", "Enter brush size:", initialvalue=self.brush_size)
        if size:
            self.brush_size = size

    def paint(self, event):
        x, y = event.x, event.y
        self.canvas.create_oval(x - self.brush_size, y - self.brush_size, x + self.brush_size, y + self.brush_size,
                                fill=self.color, outline=self.color)
        self.draw.ellipse((x - self.brush_size, y - self.brush_size, x + self.brush_size, y + self.brush_size),
                          fill=self.color, outline=self.color)

    def reset(self, event):
        self.old_x, self.old_y = None, None

    def clear_canvas(self):
        self.canvas.delete("all")
        self.image = Image.new("RGB", (800, 600), "white")
        self.draw = ImageDraw.Draw(self.image)

    def new_image(self):
        self.clear_canvas()
        self.image_path = None

    def open_image(self):
        file_path = filedialog.askopenfilename(filetypes=[("PNG files", "*.png"), ("All files", "*.*")])
        if file_path:
            self.image = Image.open(file_path)
            self.draw = ImageDraw.Draw(self.image)
            self.image_path = file_path
            self.update_canvas()

    def save_image(self):
        if self.image_path:
            self.image.save(self.image_path)
        else:
            self.save_as_image()

    def save_as_image(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png"), ("All files", "*.*")])
        if file_path:
            self.image.save(file_path)
            self.image_path = file_path

    def print_image(self):
        if not self.image_path:
            self.save_as_image()
        if self.image_path:
            if os.name == 'nt':  # Windows
                os.startfile(self.image_path, "print")
            else:
                subprocess.run(["lp", self.image_path])
        else:
            messagebox.showerror("Error", "Save the image before printing.")

    def share_image(self):
        # Placeholder for sharing functionality. Customize as needed.
        messagebox.showinfo("Share", "This feature will allow sharing the image via email or social media.")

    def cut(self):
        self.copy()
        self.clear_canvas()

    def copy(self):
        self.clipboard = self.image.copy()

    def paste(self):
        if self.clipboard:
            self.image.paste(self.clipboard)
            self.update_canvas()

    def update_canvas(self):
        self.canvas.delete("all")
        self.tk_image = ImageTk.PhotoImage(self.image)
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.tk_image)

if __name__ == "__main__":
    root = tk.Tk()
    paint_app = PaintApp(root)
    root.mainloop()
