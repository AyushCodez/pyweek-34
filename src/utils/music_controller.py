# Copyright (c) 2021 Ayush Gupta, Kartikey Pandey, Pranjal Rastogi, Sohan Varier, Shreyansh Kumar
# Author: Pranjal Rastogi

if __name__ == "__main__":
    import sys
    print("\n\nDo not run this file!\nRun root/run_game.py instead!\n\n")
    sys.exit()


from pygame import mixer
import os


# let channel 0 be for Backgrounds
# let channel 1 be for effects
# let channel 2 be for more effects
# let channel 3 be for even more effects

channel_bg = mixer.Channel(0)
channel_fx1 = mixer.Channel(1)
channel_fx2 = mixer.Channel(2)
channel_fx3 = mixer.Channel(3)
channel_fx4 = mixer.Channel(4)


BG_war = mixer.Sound('assets/music/war_screen.ogg')
BG_map = mixer.Sound('assets/music/map_screen.ogg')
BG_home = mixer.Sound('assets/music/home_screen.ogg')


def update_volume():
    volume_bg = 30
    volume_fx = 20
    channel_bg.set_volume(volume_bg)
    channel_fx1.set_volume(volume_fx)
    channel_fx2.set_volume(volume_fx)
    channel_fx3.set_volume(volume_fx)
    channel_fx4.set_volume(volume_fx)


def play_home_bg():
    channel_bg.stop()
    channel_bg.play(BG_home, loops=-1)

def play_war_bg():
    channel_bg.stop()
    channel_bg.play(BG_war, loops=-1)


def play_map_bg():
    channel_bg.stop()
    channel_bg.play(BG_map, loops=-1)




def stop_fx1():
    channel_fx1.stop()


def stop_fx2():
    channel_fx2.stop()


def stop_fx3():
    channel_fx3.stop()


def stop_fx4():
    channel_fx4.stop()


def stop_bg():
    channel_bg.stop()
