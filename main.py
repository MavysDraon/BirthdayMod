import tkinter as tk
from stardewvalley.game import Game
from smapi.modinfo import ModInfo
from smapi.scripting import ScriptContext
from smapi.utils import get_mod_path
from smapi.config import ModConfig

def main():
    # Create the main window.
    root = tk.Tk()

    # Create the date picker.
    date_picker = DatePicker(root)
    date_picker.pack()

    # Start the main loop.
    root.mainloop()

if __name__ == "__main__":
    main()
