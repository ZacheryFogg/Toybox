from toybox import Toybox, Input
from toybox.envs.atari.base import ToyboxBaseEnv
from toybox.envs.atari.constants import *
import sys


class PacmanEnv(ToyboxBaseEnv):

    def __init__(self, frameskip=(2, 5), repeat_action_probability=0., grayscale=True, alpha=False):
        super().__init__(Toybox('pacman', grayscale), 'pacman',
            frameskip, repeat_action_probability,
            grayscale=grayscale,
            alpha=alpha)
