import wpilib
from wpilib import TimedRobot

###################################################################################
### STEP 10 test turn on/off 3 fans surrounding the can at the end of polycool  ###
###################################################################################

class MyRobot(wpilib.TimedRobot):

    # EDIT DIO ports on rio like below!!!!!!!!!!!!!!!!!!!!!!!!!!!
    def robotInit(self):
        self.fan1 = wpilib.DigitalOutput(3)
        self.fan2 = wpilib.DigitalOutput(4)
        self.fan3 = wpilib.DigitalOutput(5)

        self.timer = wpilib.Timer()

    def autonomousInit(self):
        """This function is run once each time the robot enters autonomous mode."""
        self.timer.reset()
        self.timer.start()

    def autonomousPeriodic(self):
        """This function is called periodically during autonomous.
        TUNE time and speed UNTIL 180 clock / 180 counter, w/o wires tangling up too much"""

        if self.timer.get() < 10.0: #test for fans by turning on all for 10 secs then all off
            self.fan1.set(True)
            self.fan2.set(True)
            self.fan3.set(True)
        else:
            self.fan1.set(False)
            self.fan2.set(False)
            self.fan3.set(False)
                    
if __name__ == "__main__":
    wpilib.run(MyRobot)