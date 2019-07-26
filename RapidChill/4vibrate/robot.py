import wpilib
from wpilib import TimedRobot

###################################################################################
### STEP 10 test turn on/off 3 fans surrounding the can at the end of polycool  ###
###################################################################################

class MyRobot(wpilib.TimedRobot):

    # EDIT DIO ports on rio like below!!!!!!!!!!!!!!!!!!!!!!!!!!!
    def robotInit(self):
        self.vib1 = wpilib.DigitalOutput(6)
        self.vib2 = wpilib.DigitalOutput(7)
        self.vib3 = wpilib.DigitalOutput(8)
        self.vib4 = wpilib.DigitalOutput(9)

        self.timer = wpilib.Timer()

    def autonomousInit(self):
        """This function is run once each time the robot enters autonomous mode."""
        self.timer.reset()
        self.timer.start()

    def autonomousPeriodic(self):
        """This function is called periodically during autonomous.
        TUNE time and speed UNTIL 180 clock / 180 counter, w/o wires tangling up too much"""

        if self.timer.get() < 10.0: #test for vibrating motors by turning on all for 10 secs then all off
            self.vib1.set(True)
            self.vib2.set(True)
            self.vib3.set(True)
            self.vib4.set(True)
        else:
            self.vib1.set(False)
            self.vib2.set(False)
            self.vib3.set(False)
            self.vib4.set(False)
                    
if __name__ == "__main__":
    wpilib.run(MyRobot)