import tkinter as tk
from tkinter import filedialog # For masters task
from tkinter import * #added this import
from tkinter import ttk #added this import
from typing import Callable, Union, Optional
from a3_support import *
from model import *
from constants import *

class ItemView(tk.Frame):
    """ItemView should inherit from tk.Frame. The ItemView is a frame
    displaying relevant information and buttons for a single item.

    Attributes:
        master: the frame in which the ItemView window is packed in.
        item_name: a str representing the name of the item.
        amount: an int representing the amount of the item.
        select_command: callback for select item command in controller.
        buy_command: callback for the buy item command in controller.
        sell_command: callback for the sell item command in controller.
    """

    def __init__(
            self,
            master: tk.Frame,
            item_name: str,
            amount: int,
            select_command: Optional[Callable[[str], None]] = None,
            buy_command: Optional[Callable[[str], None]] = None,
            sell_command: Optional[Callable[[str], None]] = None
    ) -> None:
        """Sets up ItemView to operate as a tk.Frame, and creates all
           internal widgets. Sets the commands for the buy and sell buttons
           to the buy command and sell command each called with the appropriate
           item name respectively. Binds the select command to be called with
           the appropriate item name when either the ItemView frame or
           label is left-clicked.

           Args:
               master: the frame in which the ItemView window is packed in.
               item_name: a str representing the name of the item.
               amount: an int representing the amount of the item.
               select_command: calls back to select item command in controller.
               buy_command: calls back to the buy item command in controller.
               sell_command: calls back to the sell item command in controller.
           """

        super().__init__(master,
                         width=INVENTORY_WIDTH,
                         height=83,
                         bd=2,
                         relief="raised")

        self.item_name = item_name
        self.pack_propagate(False)

        #allows the frame to have a fixed height and width
        self.pack()

        # Binds mouse click press to calling function
        self.bind("<Button-1>", lambda evt: select_command(self.item_name))

        #changes the colour of the frames
        # according to the amount of items present
        if amount <= 0:
            bg = INVENTORY_EMPTY_COLOUR
            self.configure(bg=bg)

        else:
            bg = INVENTORY_COLOUR
            self.configure(bg=bg)

        self.item_details = tk.Frame(self, bg=bg)
        self.item_details.pack(side=tk.LEFT)

        self.label = tk.Label(
            self.item_details,
            text=f"{item_name}: {amount}",
            bg=bg,
        )
        self.label.pack(fill=tk.X)
        #binds the select command to the label
        self.label.bind("<Button-1>",
                        lambda evt: select_command(self.item_name))

        self.sell_price = tk.Label(self.item_details,
                                   text=
                                   f"Sell price: ${SELL_PRICES[item_name]}",
                                   bg=bg)

        self.sell_price.pack(fill=tk.X)
        #binds the select command to the label
        self.sell_price.bind("<Button-1>",
                             lambda evt: select_command(self.item_name))

        self.button_frames = tk.Frame(self, bg=bg)
        self.button_frames.pack(side=tk.RIGHT, expand=True)

        if item_name in BUY_PRICES:
            self.buy_price = tk.Label(self.item_details,
                                      text=
                                      f"Buy price: ${BUY_PRICES[item_name]}",
                                      bg=bg)

            self.buy_price.pack(fill=tk.X)
            #binds the select command to the label
            self.buy_price.bind("<Button-1>",
                                lambda evt: select_command(self.item_name))

            buy_frame = tk.Button(self.button_frames,
                                  text="Buy",
                                  command=lambda: buy_command(self.item_name))
            buy_frame.pack(side=tk.LEFT, ipadx=8, padx=10)

        else:
            self.buy_price = tk.Label(self.item_details,
                                      text=f"Buy price: $N/A", bg=bg)
            self.buy_price.pack(fill=tk.X)
            #binds the select command to the label
            self.buy_price.bind("<Button-1>",
                                lambda evt: select_command(self.item_name))


        sell_frame = tk.Button(self.button_frames,
                               text="Sell",
                               command=lambda: sell_command(self.item_name))
        sell_frame.pack(side=tk.LEFT, ipadx=8, padx=5)


    def update(self, amount: int, selected: bool = False) -> None:
        """Updates the text on the label, and the colour of this
        ItemView appropriately.

        Args:
            amount: integer representing the item amount
            selected: bool indicating if an item is selected. automatically set
            as False.
        """

        self.label.configure(text=f"{self.item_name}: {amount}")

        #updates the itemview to the selected colour
        if selected and amount > 0:
            self.configure(bg=INVENTORY_SELECTED_COLOUR)
            self.label.configure(bg=INVENTORY_SELECTED_COLOUR)
            self.sell_price.configure(bg=INVENTORY_SELECTED_COLOUR)
            self.buy_price.configure(bg=INVENTORY_SELECTED_COLOUR)
            self.item_details.configure(bg=INVENTORY_SELECTED_COLOUR)
            self.button_frames.configure(bg=INVENTORY_SELECTED_COLOUR)

        #updates the itemview to grey if amount is 0
        elif amount == 0:
            self.configure(bg=INVENTORY_EMPTY_COLOUR)
            self.label.configure(bg=INVENTORY_EMPTY_COLOUR)
            self.sell_price.configure(bg=INVENTORY_EMPTY_COLOUR)
            self.buy_price.configure(bg=INVENTORY_EMPTY_COLOUR)
            self.item_details.configure(bg=INVENTORY_EMPTY_COLOUR)
            self.button_frames.configure(bg=INVENTORY_EMPTY_COLOUR)

        #updates the itemview to normal inventory colour
        else:
            self.configure(bg=INVENTORY_COLOUR)
            self.label.configure(bg=INVENTORY_COLOUR)
            self.sell_price.configure(bg=INVENTORY_COLOUR)
            self.buy_price.configure(bg=INVENTORY_COLOUR)
            self.item_details.configure(bg=INVENTORY_COLOUR)
            self.button_frames.configure(bg=INVENTORY_COLOUR)