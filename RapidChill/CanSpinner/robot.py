import wpilib
from wpilib import TimedRobot
from ctre import WPI_TalonSRX as Talon

##################################################################################################################################################################################
### STEP 8, part 1(temp. separate): Spin motor #2 180 fast clockwise --> Stop/switch direction --> spin counterclockwise until Temp. sensor target reached --> Stop motor #2   ###
##################################################################################################################################################################################

class MyRobot(wpilib.TimedRobot):

    # initialize variables used in multiple functions
    # EDIT ID 2 ON THE TALON BELOW!
    def robotInit(self):
        self.spinnermotor = wpilib.Talon(2)
        self.timer = wpilib.Timer()

    def autonomousInit(self):
        """This function is run once each time the robot enters autonomous mode."""
        self.timer.reset()
        self.timer.start()

    def autonomousPeriodic(self):
        """This function is called periodically during autonomous.
        TUNE time and speed UNTIL 180 clock / 180 counter, w/o wires tangling up too much"""


        while True: # during code integration/final --> will run until temp sensor shows optimal cooling for slush
            # Drive for two seconds
            if self.timer.get() < 2.0: # TUNE TIME ROTATING - current: 2 seconds !!
                self.spinnermotor.set(0.05)  # TUNE SPEED !! - currently on 0.5% motor output (-1.0 to 1.0; 0 is no output, negative is other direction)
            else:
                self.timer.reset()
                if self.timer.get() < 2.0:
                    self.spinnermotor.set(-0.05)  # Stop robot
                    self.timer.reset()
                    
if __name__ == "__main__":
    wpilib.run(MyRobot)