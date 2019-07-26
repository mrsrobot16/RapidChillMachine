import wpilib
from wpilib import TimedRobot
from ctre import WPI_TalonSRX as Talon

#########################################
### STEP 6: +45 degree angler code !! ###
#########################################

class MyRobot(wpilib.TimedRobot):

    # initialize variables used in multiple functions
    # EDIT ID 1 ON THE TALON BELOW!
    def robotInit(self):
        self.turntablemotor = wpilib.Talon(1)
        self.timer = wpilib.Timer()

    def autonomousInit(self):
        """This function is run once each time the robot enters autonomous mode."""
        self.timer.reset()
        self.timer.start()

    def autonomousPeriodic(self):
        """This function is called periodically during autonomous."""

        # TUNE to Drive until 45 DEGREE ANGLE!
        if self.timer.get() < 1.0: # TUNE TIME ROTATING - current: 1 second !!
            self.turntablemotor.set(0.05)  # TUNE SPEED !! - currently on 0.5% motor output (-1.0 to 1.0; 0 is no output, negative is other direction)
        else:
            self.turntablemotor.set(0)  # Stop robot

if __name__ == "__main__":
    wpilib.run(MyRobot)