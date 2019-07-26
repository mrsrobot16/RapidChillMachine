import wpilib
from wpilib.doublesolenoid import DoubleSolenoid
from wpilib import TimedRobot

#######################################################################
### STEP 7: Lower/push out vertical actuator into Poly-cool bath - comes AFTER 45angler !! ###
#######################################################################

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
        if self.timer.get() < 4.0: # TUNE TIME Lowering till hit top of can - current: 4 second !!
            self.ActuatorOne.set(wpilib.DoubleSolenoid.Value.kForward)
            self.ActuatorTwo.set(wpilib.DoubleSolenoid.Value.kForward)
        else:
            self.ActuatorOne.set(DoubleSolenoid.Value.kOff)  # Stop actuators once hit top of can
            self.ActuatorTwo.set(DoubleSolenoid.Value.kOff)

if __name__ == "__main__":
    wpilib.run(MyRobot)