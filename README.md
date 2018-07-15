# BasicPiBot
Here's a basic framework for setting up your first Raspberry Pi-based robot using Python 2.7. This example shows how easy it can be to setup a drivable a robot controlled with an XBox 360 controller.  To do this, the RPi needs some supporting electronics. 

## Electronics

Hardware | Recommendations
-------- | ---------------
Raspberry Pi | I suggest a Pi 3, mostly for the ease of USB connection, but any Pi will do.
Pololu Maestro Servo Controller | There are 6, 12, 18 and 24 channel versions.  Any will do, but the 12 channel version is a sweet spot (here's a [link](https://www.pololu.com/category/102/maestro-usb-servo-controllers)).  These will drive servo and motor controllers, as well as provide digital I/O and analog inputs.  Check out their documentation for full details.
XBox 360 Controller | Wired or wireless.  Wired is good for bench testing, but to let your robot roam free, you'll want to get a wireless reciever, which is a USB dongle.  I prefer the Microsoft original hardware, if you can find it, but a knock-off should work fine.
PWM-based motor contoller | A pair of motor controllers that work using standard RC signals.  These are readily available from many sources, including Amazon.  For large bots, I find that [Sparks](http://www.revrobotics.com/rev-11-1200/) provide a good balance of power and price.

## Software
This repository contains two files.  The drive.py module is a class that takes joystick inputs, blends them together and powers the drive motors.  The basicbot.py module is the PiBot framework.  It instantiates the hardware and runs a robot loop to give interactive control.  There are two other repositories that contain Python modules and instructions that are core to a PiBot:

- [Maestro](https://github.com/FRC4564/Maestro) provides a Python class to communicate with the Maestro hardware over USB serial.
- [Xbox](https://github.com/FRC4564/Xbox) provides setup instuctions for installing a XBox driver and has sample code showing how to read the controller from Python.

## Setup
Once you have completed the Maestro and Xbox setup on your Raspberry Pi, create a folder in you home directory to hold the BasicPiBot code.  Download the 2 files from this repositiory (drive.py and basicbot.py) and place in your folder.  Additionally copy the maestro.py and xbox.py files, from those repositories, into this folder, as well.

Channels 0 and 1 of the Maestro are assumed to be connected to the left and right motor controllers for your robot drive train. 

## Driving the robot
Run the basicbot.py code.  You'll need to run as sudo to allow xboxdrv access to the USB ports.

    sudo python basicbot.py

If the hardware (maestro and xbox) are detected, you'll see the text

    Robot loop started

Now the left stick of the XBox controller will drive and steer the robot.  Pressing the Back button on the controller will end the robot loop.  The basicbot.py code is well documented and is meant to give you a framework to build in more robot functionality.

Check out these other repositiories to see some more advanced PiBots.  A crowd favorite is [Wall-E](https://github.com/FRC4564/WallE) and another fun bot is [Sasha](https://github.com/FRC4564/Sashapi) which was a competition frisbee shooter augmented with t-shirt cannons.
