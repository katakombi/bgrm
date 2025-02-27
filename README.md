# Background Remover

## The Need

It's been good long while since Microsoft first released a Teams version for Linux and yet, one of Teams' coolest features doesn't exist in said Linux version: removable backgrounds. As someone who uses Linux for their daily driver, this annoys me.

Well, I'm an engineer, so of course, I found a solution.

Using OpenCV and a v4l2loopback device (basically a virtual webcam you can write data to), I threw together a Python application that takes your normal webcam input, removes and replaces the background, and outputs that to the created video device. Problem solved :)

## How to Use

1. Setup
   - First time you set up you need to do the following
   - Create the proper virtual environment with `./scripts/setup-venv.sh`
   - Patch the v4l2 library `./scripts/patch-v4l2-py-mod.sh`

2. Run
   - After setting up, you can run the application
   - Run with `sudo ./bgrm.sh <options>` (use `--help` to see all options)
   - Example: `sudo ./bgrm.sh -b ~/Pictures/Wallpapers/ni-skyline-wallpaper.png -w 320 -H 240 -s 2.0`

Note, this will work anywhere WebCams are used.

# Dependencies

 - python >= 3.9
 - pip
 - v4l2loopback-dkms

## Current State

As a package, this project has become relatively stable for me (considering it started as a little baby script just barely functioning), so I'm pretty much done use-case-wise. This was always a personal project intended for my own use, and it has reached the point where I can easily use it for daily use, so major features are probably done at this point.

So where to go now? The plan from here on out is just to help others to get the software running and possibly package it for other systems. If you'd like other features, then you're absolutely welcome to fork the project and make your own additions (I'll consider pull requests into this repo as well), but for now, I'm shifting gears to maintenance.
