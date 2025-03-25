#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor, InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile, Image

class Feladatok():

    def __init__(self):
        # EV3 agy
        self.ev3 = EV3Brick()
        # Motorok
        self.jm = Motor(Port.B)
        self.bm = Motor(Port.C)
        self.km = Motor(Port.A)
        # Szenzorok
        self.cs = ColorSensor(Port.S3)
        self.ts = TouchSensor(Port.S1)
        self.gs = GyroSensor(Port.S2)
        self.us = UltrasonicSensor(Port.S4)
        # Dupla motorkezelő
        self.robot = DriveBase(self.jm, self.bm, 55, 115)
        # Stopperóra
        self.ido = StopWatch()

    def csipog(self):
        self.ev3.speaker.beep()

    def hanyvonal(self, db, seb, hatar):
        for _ in range(db):
            self.robot.drive(seb, 0)
            fekete = False
            self.ido.reset()
            while not (fekete and self.cs.reflection() >= hatar):
                if self.cs.reflection() < hatar:
                    if not fekete:
                        self.ido.reset()
                        fekete = True
                wait(10)
            szelesseg = self.ido.time() / 10
            print("Vonal szélesség:", szelesseg, "mm")
            self.robot.stop(Stop.BRAKE)


    def scanner1b(self):
        hatar = (7+55)/2
        self.hanyvonal(4, 100, hatar)