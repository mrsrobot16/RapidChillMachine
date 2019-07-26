import wpilib

################################################################################################
### STEP 4 & 13: Activate suction compressor – air out to hold can, then wait, then deactivate !! ###
################################################################################################

class MyRobot(wpilib.TimedRobot):
    
    def robotInit(self):
        self.compressor = wpilib.Compressor(0) #change ID 0 to that on PCM
        self.compressor.setClosedLoopControl(True)
        self.compressor.start()
        self.timer = wpilib.Timer()

    def autonomousInit(self):
        """This function is run once each time the robot enters autonomous mode."""
        self.timer.reset()
        self.timer.start()

    def autonomousPeriodic(self):
        """This function is called periodically during autonomous."""

        # hold can for 4 seconds
        if self.timer.get() > 4.0: # TUNE TIME COMPRESSING - current: 4 seconds !!
            self.compressor.setClosedLoopControl(False)
            self.compressor.stop()
            
if __name__ == "__main__":
    wpilib.run(MyRobot)