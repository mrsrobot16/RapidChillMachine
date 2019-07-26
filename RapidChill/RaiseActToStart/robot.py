import wpilib
from wpilib.doublesolenoid import DoubleSolenoid
from wpilib import TimedRobot

######################################################################################
### STEPS 5 & 9: Raise vertical actuator to starting position while holding can !! ###
######################################################################################

class MyRobot(wpilib.TimedRobot):
    
    def robotInit(self):
        self.ActuatorOne = wpilib.DoubleSolenoid(0,1)
        self.ActuatorTwo = wpilib.DoubleSolenoid(2,3)
        self.ActuatorOne.set(DoubleSolenoid.Value.kOff)
        self.ActuatorTwo.set(DoubleSolenoid.Value.kOff)
        self.timer = wpilib.Timer()

    def autonomousInit(self):
        self.timer.reset()
        self.timer.start()
            
    def autonomousPeriodic(self):
        if self.timer.get() < 1.0: # TUNE TIME Lowering till hit top of can - current: 1 second !!
            self.ActuatorOne.set(wpilib.DoubleSolenoid.Value.kReverse)
            self.ActuatorTwo.set(wpilib.DoubleSolenoid.Value.kReverse)
        else:
            self.ActuatorOne.set(DoubleSolenoid.Value.kOff)  # Stop actuators once hit top of can
            self.ActuatorTwo.set(DoubleSolenoid.Value.kOff)

if __name__ == "__main__":
    wpilib.run(MyRobot)