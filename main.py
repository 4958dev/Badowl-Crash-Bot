import disnake
from disnake.ext import commands

import os
from os import walk

import pathlib
from pathlib import Path

from config import Token

bot = commands.InteractionBot(intents=disnake.Intents.all())


src_root = Path(pathlib.Path.cwd(), "src", "extensions")
loadlist = ["__command__", "__event__"]


def loadable(file):
    if file.endswith(".py"):
        for ext in loadlist:
            if file.startswith(ext):
                return True
    else:
        return


for dirpath, dirnames, filenames in walk(src_root):
    for filename in os.listdir(dirpath):
        if loadable(filename):
            path = Path(dirpath, filename)
            strpath = str(path)
            strpath = strpath.replace(str(Path(pathlib.Path.cwd())), "")
            for char in [r"\\", r"\ "[0], "/", "//"]:
                if char in strpath:
                    ext = strpath.replace(char, ".")
                    ext = ext.replace(ext[0], "", 1)
            bot.load_extension(ext[:-3])
            print(f"extension {filename[:-3]} loaded!")


bot.run(Token)
