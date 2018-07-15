# This class provides a way to drive a robot which has a drive train equipped
# with separate motors powering the left and right sides of a robot.
# Two different drive methods exist:
#   Arcade Drive: combines 2-axes of a joystick to control steering and driving speed.
#   Tank Drive: uses two joysticks to control motor speeds left and right.
# A Pololu Maestro is used to send PWM signals to left and right motor controllers.


# When using motor controllers, the maestro's speed setting can be used to tune the 
# responsiveness of the robot.  Low values dampen acceleration, making for a more
# stable robot. High values increase responsiveness, but can lead to a tippy robot.
# Try values around 50 to 100.
RESPONSIVENESS = 60

# These are the motor controller limits, measured in Maestro units.  
# These default values typically work fine and align with maestro's default limits.
# Vaules should be adjusted so that center stops the motors and the min/max values
# limit speed range you want for your robot.
MIN_L = 4000
MIN_R = 4000
CENTER_L = 6000
CENTER_R = 6000
MAX_L = 8000
MAX_R = 8000


class DriveTrain:

    # Pass the maestro controller object and the maestro channel numbers being used
    # for the left and right motor controllers.  See maestro.py on how to instantiate maestro.
    def __init__(self, maestro, chLeft, chRight):
        self.maestro = maestro
        self.chLeft = chLeft
        self.chRight = chRight
        # Init motor accel/speed params
        self.maestro.setAccel(chLeft,0)
        self.maestro.setAccel(chRight,0)
        self.maestro.setSpeed(chLeft, RESPONSIVENESS)
        self.maestro.setSpeed(chRight, RESPONSIVENESS)
        # Motor min/center/max values
        self.minL = MIN_L
        self.minR = MIN_R
        self.centerL = CENTER_L
        self.centerR = CENTER_R
        self.maxL = MAX_L
        self.maxR = MAX_R

    # Mix steering and speed inputs (-1.0 to 1.0) into motor L/R powers (-1.0 to 1.0).
    def _arcadeMix(self, steer, drive):
        v = (1 - abs(steer)) * drive + drive
        w = (1 - abs(drive)) * steer + steer
        motorL = (v - w) / 2
        motorR = -(v + w) / 2  
        return (motorL, motorR)

    # Scale motor speeds (-1.0 to 1.0) to maestro servo min/center/max limits
    def _maestroScale(self, motorL, motorR):
        if (motorL >= 0) :
            l = int(self.centerL + (self.maxL - self.centerL) * motorL)
        else:
            l = int(self.centerL + (self.centerL - self.minL) * motorL)
        if (motorR >= 0) :
            r = int(self.centerR + (self.maxR - self.centerR) * motorR)
        else:
            r = int(self.centerR + (self.centerR - self.minR) * motorR)
        return (l, r)

    # Drive the robot motors given steering and speed parameters (arcade drive).
    # These typically come from X and Y axes of a joystick.
    # Valid inputs range between -1.0 and 1.0.
    # If steering or speed run in reverse direction, simple negative the respective input.
    def drive(self, steer, speed):
        (motorL, motorR) = self._arcadeMix(steer, speed)
        (maestroL, maestroR) = self._maestroScale(motorL, motorR)
        self.maestro.setTarget(self.chLeft, maestroL)
        self.maestro.setTarget(self.chRight, maestroR)

    # Drive the robot motors given left and right motor powers (tank drive).
    # These motor powers typically come from the Y axis of 2 analog joysticks.
    # Valid input range is between -1.0 and 1.0.
    def tankDrive(self, motorL, motorR):
        (maestroL, maestroR) = self._maestroScale(motorL, motorR)
        self.maestro.setTarget(self.chLeft, maestroL)
        self.maestro.setTarget(self.chRight, maestroR)

    # Set both motors to stopped (center) position
    def stop(self):
        self.maestro.setTarget(self.chLeft, self.centerL)
        self.maestro.setTarget(self.chRight, self.centerR)

    # Close should be used when shutting down Drive object
    def close(self):
        self.stop()
