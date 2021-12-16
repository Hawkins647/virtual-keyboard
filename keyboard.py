import tkinter as tk
import pyautogui

"""TODO:
Create checkbox to give window priority on top of other windows
"""

# define colours and fonts
background_colour = "#519872"
frame_colour = "#01200f"
letter_font = ("Calibri Bold", 20)


class OnScreenKeyboard:

    def __init__(self, root):
        self.root = root
        root.title("Virtual Keyboard")
        # give window priority
        root.wm_attributes("-topmost", 1)
        root.config(bg=background_colour)
        root.geometry("800x400")
        self.main_frame = tk.Frame(root, bg=frame_colour)
        self.main_frame.pack(padx=10, pady=10)
        self.alternate_frame = tk.Frame(root, bg=background_colour)
        self.alternate_frame.pack()
        self.create_buttons()

    def create_buttons(self):
        # create numerical buttons
        button_0 = tk.Button(self.main_frame, text="0", font=letter_font, width=4, command=lambda: self.type("0")).grid(row=0, column=0, padx=5, pady=3)
        button_1 = tk.Button(self.main_frame, text="1", font=letter_font, width=4, command=lambda: self.type("1")).grid(row=0, column=1, padx=5, pady=3)
        button_2 = tk.Button(self.main_frame, text="2", font=letter_font, width=4, command=lambda: self.type("2")).grid(row=0, column=2, padx=5, pady=3)
        button_3 = tk.Button(self.main_frame, text="3", font=letter_font, width=4, command=lambda: self.type("3")).grid(row=0, column=3, padx=5, pady=3)
        button_4 = tk.Button(self.main_frame, text="4", font=letter_font, width=4, command=lambda: self.type("4")).grid(row=0, column=4, padx=5, pady=3)
        button_5 = tk.Button(self.main_frame, text="5", font=letter_font, width=4, command=lambda: self.type("5")).grid(row=0, column=5, padx=5, pady=3)
        button_6 = tk.Button(self.main_frame, text="6", font=letter_font, width=4, command=lambda: self.type("6")).grid(row=0, column=6, padx=5, pady=3)
        button_7 = tk.Button(self.main_frame, text="7", font=letter_font, width=4, command=lambda: self.type("7")).grid(row=0, column=7, padx=5, pady=3)
        button_8 = tk.Button(self.main_frame, text="8", font=letter_font, width=4, command=lambda: self.type("8")).grid(row=0, column=8, padx=5, pady=3)
        button_9 = tk.Button(self.main_frame, text="9", font=letter_font, width=4, command=lambda: self.type("9")).grid(row=0, column=9, padx=5, pady=3)
        # create letter buttons
        button_a = tk.Button(self.main_frame, text="a", font=letter_font, width=4, command=lambda: self.type("a")).grid(row=1, column=0, padx=5, pady=3)
        button_b = tk.Button(self.main_frame, text="b", font=letter_font, width=4, command=lambda: self.type("b")).grid(row=1, column=1, padx=5, pady=3)
        button_c = tk.Button(self.main_frame, text="c", font=letter_font, width=4, command=lambda: self.type("c")).grid(row=1, column=2, padx=5, pady=3)
        button_d = tk.Button(self.main_frame, text="d", font=letter_font, width=4, command=lambda: self.type("d")).grid(row=1, column=3, padx=5, pady=3)
        button_e = tk.Button(self.main_frame, text="e", font=letter_font, width=4, command=lambda: self.type("e")).grid(row=1, column=4, padx=5, pady=3)
        button_f = tk.Button(self.main_frame, text="f", font=letter_font, width=4, command=lambda: self.type("f")).grid(row=1, column=5, padx=5, pady=3)
        button_g = tk.Button(self.main_frame, text="g", font=letter_font, width=4, command=lambda: self.type("g")).grid(row=1, column=6, padx=5, pady=3)
        button_h = tk.Button(self.main_frame, text="h", font=letter_font, width=4, command=lambda: self.type("h")).grid(row=1, column=7, padx=5, pady=3)
        button_i = tk.Button(self.main_frame, text="i", font=letter_font, width=4, command=lambda: self.type("i")).grid(row=1, column=8, padx=5, pady=3)
        button_j = tk.Button(self.main_frame, text="j", font=letter_font, width=4, command=lambda: self.type("j")).grid(row=1, column=9, padx=5, pady=3)
        button_k = tk.Button(self.main_frame, text="k", font=letter_font, width=4, command=lambda: self.type("k")).grid(row=2, column=0, padx=5, pady=3)
        button_l = tk.Button(self.main_frame, text="l", font=letter_font, width=4, command=lambda: self.type("l")).grid(row=2, column=1, padx=5, pady=3)
        button_m = tk.Button(self.main_frame, text="m", font=letter_font, width=4, command=lambda: self.type("m")).grid(row=2, column=2, padx=5, pady=3)
        button_n = tk.Button(self.main_frame, text="n", font=letter_font, width=4, command=lambda: self.type("n")).grid(row=2, column=3, padx=5, pady=3)
        button_o = tk.Button(self.main_frame, text="o", font=letter_font, width=4, command=lambda: self.type("o")).grid(row=2, column=4, padx=5, pady=3)
        button_p = tk.Button(self.main_frame, text="p", font=letter_font, width=4, command=lambda: self.type("p")).grid(row=2, column=5, padx=5, pady=3)
        button_q = tk.Button(self.main_frame, text="q", font=letter_font, width=4, command=lambda: self.type("q")).grid(row=2, column=6, padx=5, pady=3)
        button_r = tk.Button(self.main_frame, text="r", font=letter_font, width=4, command=lambda: self.type("r")).grid(row=2, column=7, padx=5, pady=3)
        button_s = tk.Button(self.main_frame, text="s", font=letter_font, width=4, command=lambda: self.type("s")).grid(row=2, column=8, padx=5, pady=3)
        button_t = tk.Button(self.main_frame, text="t", font=letter_font, width=4, command=lambda: self.type("t")).grid(row=2, column=9, padx=5, pady=3)
        button_u = tk.Button(self.main_frame, text="u", font=letter_font, width=4, command=lambda: self.type("u")).grid(row=3, column=0, padx=5, pady=3)
        button_v = tk.Button(self.main_frame, text="v", font=letter_font, width=4, command=lambda: self.type("v")).grid(row=3, column=1, padx=5, pady=3)
        button_w = tk.Button(self.main_frame, text="w", font=letter_font, width=4, command=lambda: self.type("w")).grid(row=3, column=2, padx=5, pady=3)
        button_x = tk.Button(self.main_frame, text="x", font=letter_font, width=4, command=lambda: self.type("x")).grid(row=3, column=3, padx=5, pady=3)
        button_y = tk.Button(self.main_frame, text="y", font=letter_font, width=4, command=lambda: self.type("y")).grid(row=3, column=4, padx=5, pady=3)
        button_z = tk.Button(self.main_frame, text="z", font=letter_font, width=4, command=lambda: self.type("z")).grid(row=3, column=5, padx=5, pady=3)
        # create special character buttons
        button_slash = tk.Button(self.main_frame, text="/", font=letter_font, width=4, command=lambda: self.type("/")).grid(row=3, column=6, padx=5, pady=3)
        button_asterisk = tk.Button(self.main_frame, text="*", font=letter_font, width=4, command=lambda: self.type("*")).grid(row=3, column=7, padx=5, pady=3)
        button_minus = tk.Button(self.main_frame, text="-", font=letter_font, width=4, command=lambda: self.type("-")).grid(row=3, column=8, padx=5, pady=3)
        button_plus = tk.Button(self.main_frame, text="+", font=letter_font, width=4, command=lambda: self.type("+")).grid(row=3, column=9, padx=5, pady=3)
        tk.Button(self.alternate_frame, text="⎵", font=letter_font, width=20).grid(row=0, column=0, padx=50)
        tk.Button(self.alternate_frame, text="ENTER", font=letter_font, width=20).grid(row=0, column=1, padx=50)

    def type(self, character):
        """Type a character using the pyautogui typewrite() function"""
        pyautogui.typewrite(character)
        print(character)


if __name__ == "__main__":
    root = tk.Tk()
    window = OnScreenKeyboard(root)
    root.mainloop()

