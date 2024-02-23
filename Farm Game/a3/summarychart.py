import tkinter as tk
from tkinter import filedialog # For masters task
from tkinter import * #added this import
from tkinter import ttk #added this import
from typing import Callable, Union, Optional
from a3_support import *
from model import *
from constants import *

class SummaryChart(tk.Toplevel):
    def __init__(self, master) -> None:
        super().__init__(master)
        self.geometry("600x500")
        self.title("Summary Chart")
        self.configure(bg=INVENTORY_COLOUR)


        self.frame = tk.Frame(self)
        self.frame.pack(anchor=NW)
        self.create_highscore()
        self.create_total_earnings()
        self.create_total_crops_planted()

    def create_highscore(self):
        high_score = Label(self.frame, text="High Score:", font=('Calibri 20 bold'), bg=INVENTORY_COLOUR, fg=INVENTORY_SELECTED_COLOUR)
        high_score.pack()

    def create_total_earnings(self):
        total_earnings = Label(self.frame,text="Total Earnings:", font=("Calibri 20 bold"), bg=INVENTORY_COLOUR, fg=INVENTORY_SELECTED_COLOUR)
        total_earnings.pack()

    def create_total_crops_planted(self):
        total_crops_planted = Label(self.frame, text="Total Crops Planted:",
                               font=("Calibri 20 bold"), bg=INVENTORY_COLOUR,
                               fg=INVENTORY_SELECTED_COLOUR)
        total_crops_planted.pack()