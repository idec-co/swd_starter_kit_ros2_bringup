cmake_minimum_required(VERSION 3.8)
project(swd_starter_kit_ros2_bringup)

find_package(ament_cmake REQUIRED)

install(DIRECTORY launch DESTINATION share/${PROJECT_NAME})

ament_package()
