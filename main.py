#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor, InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
import Feladatok

# főprogram
oraifeladat = Feladatok.Feladatok()
#oraifeladat.scanner1b()
oraifeladat.szinMeres()
oraifeladat.szineket_logol(sebesseg=100, idotartam=3500)

# asztal 53, fekete 7