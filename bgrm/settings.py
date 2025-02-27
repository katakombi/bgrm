# Author: Dylan Turner
# Description: Keep app settings in one place

import argparse
from dataclasses import dataclass
from argparse import ArgumentParser

@dataclass
class AppSettings:
    winTitle : str
    winStartX : int
    winStartY : int
    camera : int
    screenWidth : int
    screenHeight : int
    viewScale : float
    quitKey : int
    rmThresh : float
    fillColor : tuple[float, float, float]
    bgImg : str
    blur : bool
    disableWin : bool

    @staticmethod
    def fromArguments():
        parser = ArgumentParser()
        parser.add_argument(
            '-t', '--title', type = str, default = 'Feeds',
            help = 'Window title'
        )
        parser.add_argument(
            '-x', '--start_x', type = int, default = 1000,
            help = 'Window horizontal start position'
        )
        parser.add_argument(
            '-y', '--start_y', type = int, default = 300,
            help = 'Window vertical start position'
        )
        parser.add_argument(
            '-c', '--camera', type = int, default = 0,
            help = 'ID of camera device to use for input'
        )
        parser.add_argument(
            '-w', '--width', type = int, default = 1280,
            help = 'Width of camera input'
        )
        parser.add_argument(
            '-H', '--height', type = int, default = 960,
            help = 'Height of camera input'
        )
        parser.add_argument(
            '-s', '--scale', type = float, default = 0.5,
            help = 'Scale of window to display'
        )
        parser.add_argument(
            '-T', '--thresh', type = float, default = 0.4,
            help = 'Background removal threshold'
        )
        parser.add_argument(
            '-b', '--bg', type = str, default = '',
            help = 'Background image'
        )
        parser.add_argument(
            '--blur', help = 'Blur background (overrides --bg)',
            action='store_true'
        )
        parser.add_argument(
            '--disable_window', help = 'Disable feedback window',
            action='store_true'
        )
        args = parser.parse_args()

        return AppSettings(
            args.title, args.start_x, args.start_y, args.camera,
            args.width, args.height, args.scale, ord('q'),
            args.thresh, (0, 0, 0), args.bg, args.blur, args.disable_window
        )

