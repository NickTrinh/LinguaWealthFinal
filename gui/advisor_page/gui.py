
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path
import os

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


class AdvisorPage:
    def __init__(self, start, stop, analyze, back):
        self.OUTPUT_PATH = Path(__file__).parent
        self.ASSETS_PATH = self.OUTPUT_PATH / str(os.path.dirname(os.path.abspath(__file__)) + r"\assets\frame0")
        self.start_stt = start
        self.stop_stt = stop
        self.analyze = analyze
        self.back = back

    def relative_to_assets(self, path: str) -> Path:
        return self.ASSETS_PATH / Path(path)
    
    def button_1_hover(self, e):
        self.button_1.config(
            image=self.button_image_hover_1
        )
    def button_1_leave(self, e):
        self.button_1.config(
            image=self.button_image_1
        )
    def button_2_hover(self, e):
        self.button_2.config(
            image=self.button_image_hover_2
        )
    def button_2_leave(self, e):
        self.button_2.config(
            image=self.button_image_2
        )
    def button_3_hover(self, e):
        self.button_3.config(
            image=self.button_image_hover_3
        )
    def button_3_leave(self, e):
        self.button_3.config(
            image=self.button_image_3
        )
    def button_4_hover(self, e):
        self.button_4.config(
            image=self.button_image_hover_4
        )
    def button_4_leave(self, e):
        self.button_4.config(
            image=self.button_image_4
        )

    def run(self):
        self.window = Tk()
        self.window.title("")

        self.window.geometry("900x600")
        self.window.configure(bg = "#FFFFFF")


        self.canvas = Canvas(
            self.window,
            bg = "#FFFFFF",
            height = 600,
            width = 900,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )

        self.canvas.place(x = 0, y = 0)
        self.button_image_1 = PhotoImage(
            file=self.relative_to_assets("button_1.png"))
        self.button_1 = Button(
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=self.start_stt,
            relief="flat"
        )
        self.button_1.place(
            x=119.0,
            y=398.0,
            width=288.0,
            height=74.0
        )

        self.button_image_hover_1 = PhotoImage(
            file=self.relative_to_assets("button_hover_1.png"))

        self.button_1.bind('<Enter>', self.button_1_hover)
        self.button_1.bind('<Leave>', self.button_1_leave)


        self.button_image_2 = PhotoImage(
            file=self.relative_to_assets("button_2.png"))
        self.button_2 = Button(
            image=self.button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=self.analyze,
            relief="flat"
        )
        self.button_2.place(
            x=119.0,
            y=488.0,
            width=288.0,
            height=74.0
        )

        self.button_image_hover_2 = PhotoImage(
            file=self.relative_to_assets("button_hover_2.png"))

        self.button_2.bind('<Enter>', self.button_2_hover)
        self.button_2.bind('<Leave>', self.button_2_leave)


        self.button_image_3 = PhotoImage(
            file=self.relative_to_assets("button_3.png"))
        self.button_3 = Button(
            image=self.button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_3 clicked"),
            relief="flat"
        )
        self.button_3.place(
            x=492.0,
            y=488.0,
            width=288.0,
            height=74.0
        )

        self.button_image_hover_3 = PhotoImage(
            file=self.relative_to_assets("button_hover_3.png"))

        self.button_3.bind('<Enter>', self.button_3_hover)
        self.button_3.bind('<Leave>', self.button_3_leave)


        self.button_image_4 = PhotoImage(
            file=self.relative_to_assets("button_4.png"))
        self.button_4 = Button(
            image=self.button_image_4,
            borderwidth=0,
            highlightthickness=0,
            command=self.stop_stt,
            relief="flat"
        )
        self.button_4.place(
            x=492.0,
            y=398.0,
            width=288.0,
            height=74.0
        )

        self.button_image_hover_4 = PhotoImage(
            file=self.relative_to_assets("button_hover_4.png"))

        self.button_4.bind('<Enter>', self.button_4_hover)
        self.button_4.bind('<Leave>', self.button_4_leave)


        self.canvas.create_rectangle(
            0.0,
            0.0,
            900.0,
            29.0,
            fill="#B40000",
            outline="")

        self.canvas.create_text(
            40.0,
            44.0,
            anchor="nw",
            text="Before you start…\n\n       Have your preferred video meeting app ready.\n\n       Make sure your camera is ready for use.\n\n       Click on the “Start” button to start. It will take a few seconds.\n\n       Say something to test out the app.\n\n       When you’re done, click the “Stop” button to stop.\n\n       Click on the “Analyze conversation” button to analyze.",
            fill="#000000",
            font=("Poppins Regular", 20 * -1)
        )

        self.canvas.create_text(
            264.0,
            0.0,
            anchor="nw",
            text="LINGUAWEALTH ADVISOR PAGE",
            fill="#FFFFFF",
            font=("Poppins Bold", 24 * -1, 'bold')
        )

        self.button_image_5 = PhotoImage(
            file=self.relative_to_assets("button_5.png"))
        self.button_5 = Button(
            image=self.button_image_5,
            borderwidth=0,
            highlightthickness=0,
            command=self.back,
            relief="flat"
        )
        self.button_5.place(
            x=0.0,
            y=0.0,
            width=125.0,
            height=29.0
        )

        self.image_image_1 = PhotoImage(
            file=self.relative_to_assets("image_1.png"))
        self.image_1 = self.canvas.create_image(
            50.0,
            102.0,
            image=self.image_image_1
        )

        self.image_image_2 = PhotoImage(
            file=self.relative_to_assets("image_2.png"))
        self.image_2 = self.canvas.create_image(
            50.0,
            240.0,
            image=self.image_image_2
        )

        self.image_image_3 = PhotoImage(
            file=self.relative_to_assets("image_3.png"))
        self.image_3 = self.canvas.create_image(
            50.0,
            286.0,
            image=self.image_image_3
        )

        self.image_image_4 = PhotoImage(
            file=self.relative_to_assets("image_4.png"))
        self.image_4 = self.canvas.create_image(
            50.0,
            332.0,
            image=self.image_image_4
        )

        self.image_image_5 = PhotoImage(
            file=self.relative_to_assets("image_5.png"))
        self.image_5 = self.canvas.create_image(
            50.0,
            194.0,
            image=self.image_image_5
        )

        self.image_image_6 = PhotoImage(
            file=self.relative_to_assets("image_6.png"))
        self.image_6 = self.canvas.create_image(
            50.0,
            148.0,
            image=self.image_image_6
        )
        self.window.resizable(False, False)
        self.window.mainloop()
        
    def terminate(self):
        self.window.destroy()