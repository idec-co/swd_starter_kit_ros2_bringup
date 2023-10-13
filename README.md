swd_starter_kit_ros2_bringup
===============
# Overview
This package provides the joystick control of the ez-Wheel [Safety Wheel Drive](https://jp.idec.com/solutions/safety-wheel-drive) (SWD®).

# Pre-requisites
- Ubuntu 20.04
- ROS2 Foxy

# Dependent Packages
- Install the motor driver, please refer to [swd_ros2_controllers](https://github.com/ezWheelSAS/swd_ros2_controllers).
- Install other dependent ROS2 packages:
```
sudo apt install ros-foxy-joy ros-foxy-teleop-twist-joy ros-foxy-urg-node ros-foxy-tf2-ros
```

# Usage
### SWD® Starter Kit

Bring up ROS2 packages:
```
ros2 launch swd_starter_kit_ros2_bringup starter_kit.launch.py
```
