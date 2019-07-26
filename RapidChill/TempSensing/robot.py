import wpilib
from wpilib import TimedRobot

###################################################################################
### STEP 8, part 2 testing thermocouple for when to stop spinning in polycool   ###
###################################################################################

class MyRobot(wpilib.TimedRobot):

    # EDIT port 2 ON THE Analog section on rio and BELOW!
    def robotInit(self):
        self.thermocouple = wpilib.DigitalInput(2)

        self.timer = wpilib.Timer()

    def autonomousInit(self):
        """This function is run once each time the robot enters autonomous mode."""
        self.timer.reset()
        self.timer.start()

    def autonomousPeriodic(self):
        """This function is called periodically during autonomous.
        TUNE time and speed UNTIL 180 clock / 180 counter, w/o wires tangling up too much"""

        while True:
            if self.timer.get() > 2.0: #loop to grap temp reading every 2 seconds
                print(int(self.thermocouple.get())) #check output!!!
                #TODO: conversion into temp goes here, don't know what thermocouple "Type" we purchased (value-specific stuff)
                
                
                
                
                self.timer.reset()
                    
if __name__ == "__main__":
    wpilib.run(MyRobot)