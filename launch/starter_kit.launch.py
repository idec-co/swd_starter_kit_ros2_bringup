import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource


def generate_launch_description():
    # Directory path
    bringup_dir = get_package_share_directory('swd_starter_kit_ros2_bringup')
    swd_controller_dir = get_package_share_directory('swd_ros2_controllers')

    # Launch description
    return LaunchDescription([
        # Mortor (SWD)
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(
                [os.path.join(swd_controller_dir, 'launch', 'swd_diff_drive_controller.launch.py')]),
        ),
        # LiDAR (SE2L)
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(
                [os.path.join(bringup_dir, 'launch/lidar_idec_se2l.launch.py')]),
            launch_arguments={'prefix': 'laser'}.items(),
        ),
        # Game controller
        Node(
            package='joy',
            executable='joy_node',
        ),
        # Teleop
        Node(
            package='teleop_twist_joy',
            executable='teleop_node',
            # Configuration of the controller for Starter-Kit
            parameters=[{
                "joy_config": 'xbox',
                "enable_button": 5,
                "enable_turbo_button": 6,
                "axis_linear.x": 1,
                "axis_angular.yaw": 3,
                "scale_linear": 1.0,
                "scale_angular.yaw": 0.7,
                "scale_linear_turbo.x": 1.3,
                "scale_angular_turbo.yaw": 1.4,
            }]
        ),
    ])
