# OpenTronsTerminalCalibration
Lightweight python script to calibrate position of equipment in an OpenTrons robot, rather than relying on the GUI app.

Set the equipment in `equipment.py`. You can import this into your main `protocol.py` (or other scripts) and use the equipment normally. To calibrate run `python calibrate.py` and use the keyboard commands to jog the robot into the correct positions, then press S to save each position.
