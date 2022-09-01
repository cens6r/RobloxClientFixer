import os, ctypes, sys

from libs.utils import Utils
from libs.logger import Logger

if Utils.is_admin:
    pass
else:
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)

# Theme inspired by: https://github.com/Endermanch
print("""\n
# Roblox Client Fixer
#
# Author: https://github.com/cens6r
# Written in python 3!
#
#⠀  ⢀⣀⣀⡀⠀⠀⠀⣀⣀⡀⠀⠀⠀
#   ⠸⣿⣿⠃⠀⠀⠀⢿⣿⡟⠀⠀⠀
#⠀⠀  ⠉⠁⠀⠀⠀⠀⠀⠉⠀⠀⠀⠀
#
#                       Fastest fixer out there!
#
# ⣆⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣴⠇
# ⠙⢿⣷⣶⣤⣤⣤⣤⣤⣶⣾⣿⠿⠁⠀
#   ⠈⠻⠿⣿⣿⣿⣿⠿⠛⠁⠀⠀⠀
#
# ----------------------------------------------------------------
\n""")

Logger.warning("Only use this program if reinstalling roblox and waiting 1 hour does not work for you.\n")

Logger.info("""\n
#
# Please select a method
#
# [1] - DNS Flush (CMD METHOD)
# [2] - Remove Temp Files
\n""")

def getMethod():
    method = int(input("Select Method(1, 2): "))

    if method == 1 or method == 2:
        return method
    else:
        Logger.warning("Please select a valid method. (1, 2)")
        getMethod()

method = getMethod()

if method == 1:
    if Utils.flush_dns():
        Logger.success("Successfully flushed DNS! Restart your computer for changes to take effect.")
else:
    Utils.delete_dir(os.getenv('APPDATA'), "Temp")
    Logger.success("Successfully deleted %temp%! You may have to restart your computer for changes to take effect.")
