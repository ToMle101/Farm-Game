import tkinter as tk
from tkinter import filedialog # For masters task
from tkinter import * #added this import
from tkinter import ttk #added this import
from typing import Callable, Union, Optional
from a3_support import *
from model import *
from constants import *

class FarmView(AbstractGrid):
    """FarmView inherits from AbstractGrid. The FarmView is a grid displaying
    the farm map, player, and plants.

    Attributes:
        master: the window in which the FarmView is placed in
        dimensions: the number of rows by columns the FarmView consists of
        size: the pixel size of the FarmView.
    """
    def __init__(self, master: tk.Tk | tk.Frame, dimensions: tuple[int, int],
                 size: tuple[int, int], **kwargs) -> None:
        """Sets up the FarmView to be an AbstractGrid with the appropriate
        dimensions and size, and creates an instance attribute of an empty
        dictionary to be used as an image cache.

        Args:
            master: the window in which the FarmView is placed in
            dimensions: the number of rows by columns the FarmView consists of
            size: the pixel size of the FarmView.
        """
        super().__init__(master, dimensions, size)
        self.dimensions = dimensions
        self.cache = {}

        # size of cell
        self.ground_size = FarmView.get_cell_size(self)

    def redraw(
            self,
            ground: list[str],
            plants: dict[tuple[int,int], 'Plant'],
            player_position: tuple[int, int],
            player_direction: str
    ) -> None:

        self.ground = ground
        self.clear()

        # drawing the ground
        # store ground blocks as images
        grass = get_image("images/grass.png",
                          self.ground_size,
                          self.cache)

        soil = get_image("images/soil.png",
                         self.ground_size,
                         self.cache)

        untilled_soil = get_image("images/untilled_soil.png",
                                  self.ground_size,
                                  self.cache)

        #interate through the map file
        #uses enumerate to find the list of letters and what row it belongs on
        for row, letter_list in enumerate(ground):
            #uses enumerate to find the letter and its respective position
            for pos_letter, letter in enumerate(letter_list):
                position = self.get_midpoint((row, pos_letter))

                if letter == "G":
                    self.create_image(position[0], position[1], image=grass)

                if letter == "S":
                    self.create_image(position[0], position[1], image=soil)

                if letter == "U":
                    self.create_image(position[0], position[1],
                                      image=untilled_soil)

        #drawing the plants
        for pos, plant in plants.items():
            plant_pos = self.get_midpoint(pos)
            plant_image = get_image(
                f"images/{get_plant_image_name(plant)}",
                self.ground_size,
                self.cache)

            self.create_image(plant_pos, image=plant_image)

        #drawing the player
        #uses the pixel position of the player to annotate them
        #in the middle of each block
        x, y = self.get_midpoint(player_position)

        if player_direction == "s":
            player_s = get_image("images/player_s.png",
                                 self.ground_size, self.cache)
            self.create_image(x, y, image=player_s)

        if player_direction == "w":
            player_w = get_image("images/player_w.png",
                                 self.ground_size, self.cache)
            self.create_image(x, y, image=player_w)

        if player_direction == "d":
            player_d = get_image("images/player_d.png",
                                 self.ground_size, self.cache)
            self.create_image(x, y, image=player_d)

        if player_direction == "a":
            player_a = get_image("images/player_a.png",
                                 self.ground_size, self.cache)
            self.create_image(x, y, image=player_a)