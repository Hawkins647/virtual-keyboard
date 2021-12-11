import tkinter as tk
import string


# define colours and fonts
background_colour = "#519872"
frame_colour = "#01200f"
letter_font = ("Calibri Bold", 20)

# define global variables
alphabet = string.ascii_lowercase
symbols = ["+", "=", "/", "*"]


class OnScreenKeyboard:

    def __init__(self, root):
        self.root = root
        root.title("Virtual Keyboard")
        root.config(bg=background_colour)
        root.geometry("800x400")
        self.main_frame = tk.Frame(root, bg=frame_colour)
        self.main_frame.pack(padx=10, pady=10)
        self.alternate_frame = tk.Frame(root, bg=background_colour)
        self.alternate_frame.pack()
        self.create_buttons()

    def create_buttons(self):
        # create numerical buttons
        for i in range(0, 10):
            tk.Button(self.main_frame, text=i, font=letter_font, width=4).grid(row=0, column=i, padx=5, pady=3)
        # create letter buttons
        for i in range(0, 10):
            tk.Button(self.main_frame, text=alphabet[i], font=letter_font, width=4).grid(row=1, column=i, padx=5, pady=3)
        for i in range(0, 10):
            tk.Button(self.main_frame, text=alphabet[i + 10], font=letter_font, width=4).grid(row=2, column=i, padx=5, pady=3)
        for i in range(0, 6):
            tk.Button(self.main_frame, text=alphabet[i + 20], font=letter_font, width=4).grid(row=3, column=i, padx=5, pady=3)
        # create symbol buttons
        for i in range(0, 4):
            tk.Button(self.main_frame, text=symbols[i], font=letter_font, width=4).grid(row=3, column=i + 6, padx=5, pady=3)
        tk.Button(self.alternate_frame, text="⎵", font=letter_font, width=20).grid(row=0, column=0, padx=50)
        tk.Button(self.alternate_frame, text="ENTER", font=letter_font, width=20).grid(row=0, column=1, padx=50)
        tk.Button(root, text="Alternate keyboard", font=letter_font).pack(pady=10)


if __name__ == "__main__":
    root = tk.Tk()
    window = OnScreenKeyboard(root)
    root.mainloop()