# Copyright (c) 2021 Ayush Gupta, Pranjal Rastogi
# -----------------------------------------------
# main.py
#
# Main game code
# -----------------------------------------------

if __name__ == "__main__":
    import sys
    print("Do not run this file!\nRun run_game.py instead!\n")
    sys.exit()

from models.game import Game


def main():
    game = Game()
    game.on_execute()
    