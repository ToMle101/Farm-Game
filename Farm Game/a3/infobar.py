import tkinter as tk
from tkinter import filedialog # For masters task
from tkinter import * #added this import
from tkinter import ttk #added this import
from typing import Callable, Union, Optional
from a3_support import *
from model import *
from constants import *



class InfoBar(AbstractGrid):
    """InfoBar inherits from AbstractGrid. It displays information to the user
    about the number of days elapsed in the game, as well as the
    player’s money and energy.

    Attributes:
        master: the window in which the InfoBar is placed in.
        dimensions: the number of rows by columns the InfoBar consists of.
        size: the pixel size of InfoBar.
    """
    def __init__(self, master: tk.Tk | tk.Frame) -> None:
        """ Sets up this InfoBar to be an AbstractGrid with the appropriate
        number of rows and columns, and the appropriate width and height.

        Args:
            master: the window where the InfoBar is packed.
        """
        dimensions = (2, 3)
        size = (700, 90)
        super().__init__(master, dimensions, size)

    def redraw(self, day: int, money: int, energy: int) -> None:
        """ Clears the InfoBar and redraws it to display the
        provided day, money, and energy.

        Args:
            day: int representing the amount of days elapsed
            money: int representing the amount of money the player has
            energy: int representing the amount of energy the player has
        """
        self.clear()
        InfoBar.annotate_position(self, (0, 0), "Day:", HEADING_FONT)
        InfoBar.annotate_position(self, (0, 1), "Money:", HEADING_FONT)
        InfoBar.annotate_position(self, (0, 2), "Energy:", HEADING_FONT)
        InfoBar.annotate_position(self, (1, 0), f"{day}")
        InfoBar.annotate_position(self, (1, 1), f"${money}")
        InfoBar.annotate_position(self, (1, 2), f"{energy}")