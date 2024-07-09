import tkinter as tk
from tkinter import colorchooser

class CircleDrawer:
    def __init__(self, root):
        self.root = root
        self.root.title("Circle Drawer")
        
        self.canvas = tk.Canvas(root, width=800, height=600, bg="white")
        self.canvas.pack()

        self.label = tk.Label(root, text="Click to draw circles!")
        self.label.pack()

        self.size_label = tk.Label(root, text="Circle Size:")
        self.size_label.pack()

        self.size_var = tk.IntVar(value=50)
        self.size_entry = tk.Entry(root, textvariable=self.size_var)
        self.size_entry.pack()

        self.color_button = tk.Button(root, text="Choose Color", command=self.choose_color)
        self.color_button.pack()

        self.clear_button = tk.Button(root, text="Clear", command=self.clear_canvas)
        self.clear_button.pack()

        self.canvas.bind("<Button-1>", self.draw_circle)

        self.current_color = "black"

    def draw_circle(self, event):
        x, y = event.x, event.y
        r = self.size_var.get()
        self.canvas.create_oval(x - r, y - r, x + r, y + r, outline=self.current_color, width=2)

    def clear_canvas(self):
        self.canvas.delete("all")

    def choose_color(self):
        color = colorchooser.askcolor()[1]
        if color:
            self.current_color = color

if __name__ == "__main__":
    root = tk.Tk()
    app = CircleDrawer(root)
    root.mainloop()
