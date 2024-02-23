import tkinter as tk
from tkinter import filedialog # For masters task
from tkinter import * #added this import
from tkinter import ttk #added this import
from typing import Callable, Union, Optional
from a3_support import *
from model import *
from constants import *
from summarychart import *
from infobar import *
from farmview import *
from itemview import *

# Implement your classes here


# class InfoBar(AbstractGrid):
#     """InfoBar inherits from AbstractGrid. It displays information to the user
#     about the number of days elapsed in the game, as well as the
#     player’s money and energy.
#
#     Attributes:
#         master: the window in which the InfoBar is placed in.
#         dimensions: the number of rows by columns the InfoBar consists of.
#         size: the pixel size of InfoBar.
#     """
#     def __init__(self, master: tk.Tk | tk.Frame) -> None:
#         """ Sets up this InfoBar to be an AbstractGrid with the appropriate
#         number of rows and columns, and the appropriate width and height.
#
#         Args:
#             master: the window where the InfoBar is packed.
#         """
#         dimensions = (2, 3)
#         size = (700, 90)
#         super().__init__(master, dimensions, size)
#
#     def redraw(self, day: int, money: int, energy: int) -> None:
#         """ Clears the InfoBar and redraws it to display the
#         provided day, money, and energy.
#
#         Args:
#             day: int representing the amount of days elapsed
#             money: int representing the amount of money the player has
#             energy: int representing the amount of energy the player has
#         """
#         self.clear()
#         InfoBar.annotate_position(self, (0, 0), "Day:", HEADING_FONT)
#         InfoBar.annotate_position(self, (0, 1), "Money:", HEADING_FONT)
#         InfoBar.annotate_position(self, (0, 2), "Energy:", HEADING_FONT)
#         InfoBar.annotate_position(self, (1, 0), f"{day}")
#         InfoBar.annotate_position(self, (1, 1), f"${money}")
#         InfoBar.annotate_position(self, (1, 2), f"{energy}")


# class FarmView(AbstractGrid):
#     """FarmView inherits from AbstractGrid. The FarmView is a grid displaying
#     the farm map, player, and plants.
#
#     Attributes:
#         master: the window in which the FarmView is placed in
#         dimensions: the number of rows by columns the FarmView consists of
#         size: the pixel size of the FarmView.
#     """
#     def __init__(self, master: tk.Tk | tk.Frame, dimensions: tuple[int, int],
#                  size: tuple[int, int], **kwargs) -> None:
#         """Sets up the FarmView to be an AbstractGrid with the appropriate
#         dimensions and size, and creates an instance attribute of an empty
#         dictionary to be used as an image cache.
#
#         Args:
#             master: the window in which the FarmView is placed in
#             dimensions: the number of rows by columns the FarmView consists of
#             size: the pixel size of the FarmView.
#         """
#         super().__init__(master, dimensions, size)
#         self.dimensions = dimensions
#         self.cache = {}
#
#         # size of cell
#         self.ground_size = FarmView.get_cell_size(self)
#
#     def redraw(
#             self,
#             ground: list[str],
#             plants: dict[tuple[int,int], 'Plant'],
#             player_position: tuple[int, int],
#             player_direction: str
#     ) -> None:
#
#         self.ground = ground
#         self.clear()
#
#         # drawing the ground
#         # store ground blocks as images
#         grass = get_image("images/grass.png",
#                           self.ground_size,
#                           self.cache)
#
#         soil = get_image("images/soil.png",
#                          self.ground_size,
#                          self.cache)
#
#         untilled_soil = get_image("images/untilled_soil.png",
#                                   self.ground_size,
#                                   self.cache)
#
#         #interate through the map file
#         #uses enumerate to find the list of letters and what row it belongs on
#         for row, letter_list in enumerate(ground):
#             #uses enumerate to find the letter and its respective position
#             for pos_letter, letter in enumerate(letter_list):
#                 position = self.get_midpoint((row, pos_letter))
#
#                 if letter == "G":
#                     self.create_image(position[0], position[1], image=grass)
#
#                 if letter == "S":
#                     self.create_image(position[0], position[1], image=soil)
#
#                 if letter == "U":
#                     self.create_image(position[0], position[1],
#                                       image=untilled_soil)
#
#         #drawing the plants
#         for pos, plant in plants.items():
#             plant_pos = self.get_midpoint(pos)
#             plant_image = get_image(
#                 f"images/{get_plant_image_name(plant)}",
#                 self.ground_size,
#                 self.cache)
#
#             self.create_image(plant_pos, image=plant_image)
#
#         #drawing the player
#         #uses the pixel position of the player to annotate them
#         #in the middle of each block
#         x, y = self.get_midpoint(player_position)
#
#         if player_direction == "s":
#             player_s = get_image("images/player_s.png",
#                                  self.ground_size, self.cache)
#             self.create_image(x, y, image=player_s)
#
#         if player_direction == "w":
#             player_w = get_image("images/player_w.png",
#                                  self.ground_size, self.cache)
#             self.create_image(x, y, image=player_w)
#
#         if player_direction == "d":
#             player_d = get_image("images/player_d.png",
#                                  self.ground_size, self.cache)
#             self.create_image(x, y, image=player_d)
#
#         if player_direction == "a":
#             player_a = get_image("images/player_a.png",
#                                  self.ground_size, self.cache)
#             self.create_image(x, y, image=player_a)


# class ItemView(tk.Frame):
#     """ItemView should inherit from tk.Frame. The ItemView is a frame
#     displaying relevant information and buttons for a single item.
#
#     Attributes:
#         master: the frame in which the ItemView window is packed in.
#         item_name: a str representing the name of the item.
#         amount: an int representing the amount of the item.
#         select_command: callback for select item command in controller.
#         buy_command: callback for the buy item command in controller.
#         sell_command: callback for the sell item command in controller.
#     """
#
#     def __init__(
#             self,
#             master: tk.Frame,
#             item_name: str,
#             amount: int,
#             select_command: Optional[Callable[[str], None]] = None,
#             buy_command: Optional[Callable[[str], None]] = None,
#             sell_command: Optional[Callable[[str], None]] = None
#     ) -> None:
#         """Sets up ItemView to operate as a tk.Frame, and creates all
#            internal widgets. Sets the commands for the buy and sell buttons
#            to the buy command and sell command each called with the appropriate
#            item name respectively. Binds the select command to be called with
#            the appropriate item name when either the ItemView frame or
#            label is left-clicked.
#
#            Args:
#                master: the frame in which the ItemView window is packed in.
#                item_name: a str representing the name of the item.
#                amount: an int representing the amount of the item.
#                select_command: calls back to select item command in controller.
#                buy_command: calls back to the buy item command in controller.
#                sell_command: calls back to the sell item command in controller.
#            """
#
#         super().__init__(master,
#                          width=INVENTORY_WIDTH,
#                          height=83,
#                          bd=2,
#                          relief="raised")
#
#         self.item_name = item_name
#         self.pack_propagate(False)
#
#         #allows the frame to have a fixed height and width
#         self.pack()
#
#         # Binds mouse click press to calling function
#         self.bind("<Button-1>", lambda evt: select_command(self.item_name))
#
#         #changes the colour of the frames
#         # according to the amount of items present
#         if amount <= 0:
#             bg = INVENTORY_EMPTY_COLOUR
#             self.configure(bg=bg)
#
#         else:
#             bg = INVENTORY_COLOUR
#             self.configure(bg=bg)
#
#         self.item_details = tk.Frame(self, bg=bg)
#         self.item_details.pack(side=tk.LEFT)
#
#         self.label = tk.Label(
#             self.item_details,
#             text=f"{item_name}: {amount}",
#             bg=bg,
#         )
#         self.label.pack(fill=tk.X)
#         #binds the select command to the label
#         self.label.bind("<Button-1>",
#                         lambda evt: select_command(self.item_name))
#
#         self.sell_price = tk.Label(self.item_details,
#                                    text=
#                                    f"Sell price: ${SELL_PRICES[item_name]}",
#                                    bg=bg)
#
#         self.sell_price.pack(fill=tk.X)
#         #binds the select command to the label
#         self.sell_price.bind("<Button-1>",
#                              lambda evt: select_command(self.item_name))
#
#         self.button_frames = tk.Frame(self, bg=bg)
#         self.button_frames.pack(side=tk.RIGHT, expand=True)
#
#         if item_name in BUY_PRICES:
#             self.buy_price = tk.Label(self.item_details,
#                                       text=
#                                       f"Buy price: ${BUY_PRICES[item_name]}",
#                                       bg=bg)
#
#             self.buy_price.pack(fill=tk.X)
#             #binds the select command to the label
#             self.buy_price.bind("<Button-1>",
#                                 lambda evt: select_command(self.item_name))
#
#             buy_frame = tk.Button(self.button_frames,
#                                   text="Buy",
#                                   command=lambda: buy_command(self.item_name))
#             buy_frame.pack(side=tk.LEFT, ipadx=8, padx=10)
#
#         else:
#             self.buy_price = tk.Label(self.item_details,
#                                       text=f"Buy price: $N/A", bg=bg)
#             self.buy_price.pack(fill=tk.X)
#             #binds the select command to the label
#             self.buy_price.bind("<Button-1>",
#                                 lambda evt: select_command(self.item_name))
#
#
#         sell_frame = tk.Button(self.button_frames,
#                                text="Sell",
#                                command=lambda: sell_command(self.item_name))
#         sell_frame.pack(side=tk.LEFT, ipadx=8, padx=5)
#
#
#     def update(self, amount: int, selected: bool = False) -> None:
#         """Updates the text on the label, and the colour of this
#         ItemView appropriately.
#
#         Args:
#             amount: integer representing the item amount
#             selected: bool indicating if an item is selected. automatically set
#             as False.
#         """
#
#         self.label.configure(text=f"{self.item_name}: {amount}")
#
#         #updates the itemview to the selected colour
#         if selected and amount > 0:
#             self.configure(bg=INVENTORY_SELECTED_COLOUR)
#             self.label.configure(bg=INVENTORY_SELECTED_COLOUR)
#             self.sell_price.configure(bg=INVENTORY_SELECTED_COLOUR)
#             self.buy_price.configure(bg=INVENTORY_SELECTED_COLOUR)
#             self.item_details.configure(bg=INVENTORY_SELECTED_COLOUR)
#             self.button_frames.configure(bg=INVENTORY_SELECTED_COLOUR)
#
#         #updates the itemview to grey if amount is 0
#         elif amount == 0:
#             self.configure(bg=INVENTORY_EMPTY_COLOUR)
#             self.label.configure(bg=INVENTORY_EMPTY_COLOUR)
#             self.sell_price.configure(bg=INVENTORY_EMPTY_COLOUR)
#             self.buy_price.configure(bg=INVENTORY_EMPTY_COLOUR)
#             self.item_details.configure(bg=INVENTORY_EMPTY_COLOUR)
#             self.button_frames.configure(bg=INVENTORY_EMPTY_COLOUR)
#
#         #updates the itemview to normal inventory colour
#         else:
#             self.configure(bg=INVENTORY_COLOUR)
#             self.label.configure(bg=INVENTORY_COLOUR)
#             self.sell_price.configure(bg=INVENTORY_COLOUR)
#             self.buy_price.configure(bg=INVENTORY_COLOUR)
#             self.item_details.configure(bg=INVENTORY_COLOUR)
#             self.button_frames.configure(bg=INVENTORY_COLOUR)

#
# class SummaryChart(tk.Toplevel):
#     def __init__(self, master) -> None:
#         super().__init__(master)
#         self.geometry("600x500")
#         self.title("Summary Chart")
#         self.configure(bg=INVENTORY_COLOUR)
#
#         #highscore title:
#
#         self.highscore_frame = tk.Frame(self)
#         self.highscore_frame.pack()
#         self.create_highscore()
#
#     def create_highscore(self):
#         high_score = Label(self.highscore_frame, text="High Score", font=('Calibri 20 bold'), bg=INVENTORY_COLOUR, fg=INVENTORY_SELECTED_COLOUR)
#         high_score.pack(anchor=NW)


class FarmGame():
    """FarmGame is the controller class for the overall game.
    The controller is responsible for creating and maintaining instances of
    the model and view classes, event handling, and facilitating communication
    between the model and view classes.

    Attributes:
        master: the master window.
        map_file: str representing the path file.
    """
    def __init__(self, master: tk.Tk, map_file: str) -> None:
        """Initialises the FarmGame instances. sets up the title, banner,
        creates the FramModel instance, creates instances the instances for
        your view classes, and ensures they're a formatted correctly. Creates
        a button to enable users to increment days. Binds the key presses and
        redraws the views.

        Args:
            master: the master window.
            map_file: str representing the path file.

        """
        self._master = master
        master.title("Farm Game")

        self.header = get_image("images/header.png",
                                (FARM_WIDTH + INVENTORY_WIDTH, BANNER_HEIGHT))
        label = tk.Label(master, image=self.header)
        label.pack()

        self._model = FarmModel(map_file)
        # sets up empty dictionary with name of the item view and their
        # respective instances
        self.item_views: dict[str, ItemView] = {}
        self.plants = {"Potato Seed": PotatoPlant,
                       "Kale Seed": KalePlant, "Berry Seed": BerryPlant}

        # new day button
        new_day_button = tk.Button(
            master,
            text="Next day",
            command=self.next_day)
        new_day_button.pack(side=tk.BOTTOM)

        #summary button
        summary_button = tk.Button(master, text="Summary", command=self.open_summary)
        summary_button.pack(side=tk.BOTTOM)

        # sets up initial info bar
        self._info_bar = InfoBar(master=master)
        self._info_bar.pack(side=tk.BOTTOM)
        self._info_bar.redraw(day=self._model.get_days_elapsed(),
                              money=self._model.get_player().get_money(),
                              energy=self._model.get_player().get_energy())


        # sets up initial farm view
        self._farm_view = FarmView(master=master,
                                   dimensions=self._model.get_dimensions(),
                                   size=(FARM_WIDTH, FARM_WIDTH))
        self._farm_view.pack(side=tk.LEFT)
        self._farm_view.redraw(ground=self._model.get_map(),
                               plants=self._model.get_plants(),
                               player_position=(0, 0),
                               player_direction="s")


        # binds key presses to the window
        self._master.bind("<Key>", self.handle_keypress)

        # sets up the initial item view
        for item in ITEMS:
            if item in self._model.get_player().get_inventory():
                item_amount = self._model.get_player().get_inventory()[item]

            else:
                item_amount = 0

            self.item_views[item] = ItemView(
                master=master,
                item_name=item,
                amount=item_amount,
                select_command=self.select_item,
                buy_command=self.buy_item,
                sell_command=self.sell_item
            )

    def next_day(self):
        """Advances the game to the next day and triggers necessary redraws.
        This method is responsible for progressing the game to the next day by
        calling the 'new_day' method of the model.It then triggers the
        necessary updates and redrawing by calling the 'redraw' method.
        """
        self._model.new_day()
        self.redraw()

    def redraw(self) -> None:
        """Method redraws the FarmView and InfoBar based off the current state
        of the game. It does not take any arguments besides self.
        """
        # redraws the farm view
        self._farm_view.redraw(ground=self._model.get_map(),
                               plants=self._model.get_plants(),
                               player_position=
                               self._model.get_player_position(),
                               player_direction=
                               self._model.get_player_direction())

        # redraws the info bar
        self._info_bar.redraw(self._model.get_days_elapsed(),
                              self._model.get_player().get_money(),
                              self._model.get_player().get_energy())

    def open_summary(self):
        SummaryChart(self._master)

    def handle_keypress(self, event: tk.Event) -> None:
        """ An event handler to be called when
        a keypress event occurs.

        Args:
            event: the event to be handled
        """
        if event.keysym in "wasd":
            self._model.move_player(event.keysym)

        if event.keysym == "t":
            self._model.till_soil(self._model.get_player_position())

        if event.keysym == "u":
            self._model.untill_soil(self._model.get_player_position())

        if event.keysym == "p":
            player_x_position = self._model.get_player_position()[0]
            player_y_position = self._model.get_player_position()[1]
            tile_postion = \
                self._farm_view.ground[player_x_position][player_y_position]

            # checks if there is soil for the seed to be planted
            if tile_postion != "S":
                pass

            #checks if there is something selected
            elif self._model.get_player().get_selected_item() is None:
                pass

            # checks if there is anything in the inventory
            elif self._model.get_player().get_selected_item() \
                    not in self._model.get_player().get_inventory():
                pass

            #checks if there are already plants
            elif self._model.get_player_position() in\
                    self._model.get_plants().keys():
                pass

            # checks if the item is a seed and adds the plant
            elif self._model.get_player().get_selected_item() in SEEDS:
                plant = \
                    self.plants[self._model.get_player().get_selected_item()]()
                self._model.add_plant(self._model.get_player_position(), plant)

                self._model.get_player().remove_item\
                    ((self._model.get_player().get_selected_item(), 1))

                item_selected = self._model.get_player().get_selected_item()

                #checks if the amount of the item has depleted
                if item_selected not in self._model.get_player().\
                        get_inventory():
                    self.item_views[item_selected].\
                        update(amount=0, selected=True)

                else:
                    amount = \
                        self._model.get_player().get_inventory()[item_selected]
                    self.item_views[item_selected].\
                        update(amount=amount, selected=True)

        if event.keysym == "h":
            harvested_plant = \
                self._model.harvest_plant(self._model.get_player_position())
            if harvested_plant is not None:
                self._model.get_player().add_item(harvested_plant)

                amount = \
                    self._model.get_player().get_inventory()[harvested_plant[0]]
                self.item_views[harvested_plant[0]].\
                    update(amount=amount, selected=False)

        if event.keysym == "r":
            self._model.remove_plant(self._model.get_player_position())

        # if event.keysym == "m":
        #     """calls the command that opens the window"""

        self.redraw()

    def select_item(self, item_name: str) -> None:
        """The callback to be given to each ItemView for item selection.
        This method sets the selected item to be item name and then
        redraws the view.

        Args:
            item_name: string representing the item name that is selected.
        """
        item_currently_selected = self._model.get_player().get_selected_item()
        inventory = self._model.get_player().get_inventory()

        if item_currently_selected is not None and \
                item_currently_selected in inventory:
            self.item_views[item_currently_selected].update(
                amount=inventory[item_currently_selected],
                selected=False)

        if item_name in inventory:
            self._model.get_player().select_item(item_name=item_name)
            self.item_views[item_name].update(
                amount=inventory[item_name],
                selected=True)
        else:
            self.item_views[item_name].update(amount=0, selected=True)

    def buy_item(self, item_name: str) -> None:
        """The callback given to each ItemView for item selection. This
        method allows the player to attempt to buy the item with the given
        item_name then redraws the view.

        Args:
            item_name (str): The name of the item to buy.
        """
        self._model.get_player().buy(item_name, BUY_PRICES[item_name])
        inventory = self._model.get_player().get_inventory()

        if item_name in inventory:
            amount = self._model.get_player().get_inventory()[item_name]
            # determines the bool for selected.
            # Only make it selected if it is the current selected item and the
            # amount is greater than 1 because if the amount is 1,
            # it was previously 0, so it should not be selected
            selected = self._model.get_player().get_selected_item() \
                       == item_name and amount > 1
            self.item_views[item_name].update(amount=amount, selected=selected)

        self._info_bar.redraw(day=self._model.get_days_elapsed(),
                              money=self._model.get_player().get_money(),
                              energy=self._model.get_player().get_energy())

    def sell_item(self, item_name: str) -> None:
        """The callback given to each ItemView for item selection. This
        method allows the player to attempt to sell the item with the given
        item_name then redraws the view.

        Args:
            item_name (str): The name of the item to sell.

        """
        self._model.get_player().sell(item_name, SELL_PRICES[item_name])
        inventory = self._model.get_player().get_inventory()
        selected = self._model.get_player().get_selected_item() == item_name

        if item_name in inventory:
            amount = inventory[item_name]
            # determines the bool for selected
            self.item_views[item_name].update(amount=amount, selected=selected)

        else:
            # this is when there are no more items
            self.item_views[item_name].update(amount=0, selected=False)

        self._info_bar.redraw(day=self._model.get_days_elapsed(),
                              money=self._model.get_player().get_money(),
                              energy=self._model.get_player().get_energy())


def play_game(root: tk.Tk, map_file: str) -> None:
    """Starts and runs the Farm Game.

        This function initializes the Farm Game by creating an instance of
        the FarmGame class and passing the root window and the map file as
        parameters. It then starts the game by calling the mainloop()
        method of the root window.

        Args:
            root (tk.Tk): The root window object provided by the Tkinter
            library. map_file (str): The path to the file containing the game
            map.

        Returns:
            None
    """
    # Implement your play_game function here

    FarmGame(root, map_file)
    root.mainloop()


def main() -> None:
    """Constructs the root tk.TK instance and calls the play_game function"""
    # Implement your main function here

    root = tk.Tk()
    play_game(root, 'maps/map1.txt')


if __name__ == '__main__':
    main()


