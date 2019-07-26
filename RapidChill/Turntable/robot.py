import wpilib
from wpilib import TimedRobot
from ctre import WPI_TalonSRX as Talon

#################################
### STEP 2: TURNTABLE CODE !! ###
#################################

class MyRobot(wpilib.TimedRobot):

    # initialize variables used in multiple functions
    # EDIT ID 0 ON THE TALON BELOW!
    def robotInit(self):
        self.turntablemotor = wpilib.Talon(0)
        self.timer = wpilib.Timer()

    def autonomousInit(self):
        """This function is run once each time the robot enters autonomous mode."""
        self.timer.reset()
        self.timer.start()

    def autonomousPeriodic(self):
        """This function is called periodically during autonomous."""

        # Drive for two seconds
        if self.timer.get() < 2.0: # TUNE TIME ROTATING - current: 2 seconds !!
            self.turntablemotor.set(0.05)  # TUNE SPEED !! - currently on 0.5% motor output (-1.0 to 1.0; 0 is no output, negative is other direction)
        else:
            self.turntablemotor.set(0)  # Stop robot

if __name__ == "__main__":
    wpilib.run(MyRobot)