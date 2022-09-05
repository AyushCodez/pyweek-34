# Copyright (c) 2021 Ayush Gupta, Pranjal Rastogi
# -----------------------------------------------
# run_game.py
#
# Runs the game while checking for version
# -----------------------------------------------

import sys
# The major, minor version numbers required
MIN_VER = (3, 8)
if sys.version_info[:2] < MIN_VER:
    sys.exit(
        "This game requires Python {}.{}.".format(*MIN_VER)
    )

# run game
from main import main
main()
