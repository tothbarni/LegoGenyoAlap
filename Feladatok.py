#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor, InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile, Image

class Feladatok():
    def __init__(self):
        self.ev3 = EV3Brick()
        self.jm = Motor(Port.B)
        self.bm = Motor(Port.C)
        self.km = Motor(Port.A)
        self.cs = ColorSensor(Port.S3)
        self.ts = TouchSensor(Port.S1)
        self.gs = GyroSensor(Port.S2)
        self.us = UltrasonicSensor(Port.S4)
        self.robot = DriveBase(self.jm, self.bm, 55, 115)
        self.ido = StopWatch()

class Feladatok():
    def __init__(self):
        self.ev3 = EV3Brick()
        self.jm = Motor(Port.B)
        self.bm = Motor(Port.C)
        self.cs = ColorSensor(Port.S3)
        self.robot = DriveBase(self.jm, self.bm, 55, 115)
        self.ido = StopWatch()
    
    def szineket_logol(self, sebesseg, idotartam):
        data = DataLog('ido_ms', 'reflexio', name='/home/robot/szenzor_adatok')
        self.ido.reset()
        self.robot.drive(sebesseg, 0)
        
        while self.ido.time() < idotartam:
            reflexio = self.cs.reflection()
            data.log(self.ido.time(), reflexio)
            wait(10)
        self.robot.stop()
        return data

    def szinMeres(self):
        self.ev3.screen.clear()
        while True:
            vErtek = self.cs.reflection()
            print(vErtek)
            self.ev3.screen.print(vErtek)
            break