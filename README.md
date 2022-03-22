Source code for testArm. This directory is currently using ROS 1 (Noetic) tentatively
# Dependencies
1.Also ensure that you have the following(Install with ```sudo apt-get install```): 
     - ros-noetic-moveit
     - ros-noetic-ros-control 
     - ros-noetic-ros-controllers

# Setup 
1.Create catkin workspace using steps from http://wiki.ros.org/catkin/Tutorials/create_a_workspace
     - ```cd catkin ws```
     - ```cd src```
2.create and setup package ```catkin_create_pkg arm_description``` 
     - ```cd arm_description```
     - ```mkdir urdf ```
     - ```cd urdf```
     - ```vi custom_arm.urdf.```  Paste in urdf

3.Create launch and controls files using moveit setup assistant ```roslaunch moveit_setup_assistant setup_assistant.launch```
     -create config and find urdf
     -set to highest sampling density -> generate collision matrix
     -add a virtual fixed joint with parent frame to world (child_link=base_link)
     -add group::: 
          -group name: manipulator , 
          -kinematic solver: kdl kinematics, 
          -kin. param file : !!UNKNOWN!!, 
          -Group Planner :RRT
          -Add joints - ALL JOINTS and save
     -add pose to see arm movement
     -endeffector
          select endeffector joints and links
          apply default controllers to wrist joint and hand joint
     -generate urdf and copy and paste into urdf
     -All except endeffector joints for passive joints 
     -Skip to author info and fill out
     -Make the file inside of the src directory ex ```<home_directory>/catkin_ws/src/arm_moveit_config```
     -configure file
   
# Launch 
1. Source project at root directory using ```. devel/setup.sh``` when first opening the shell. If you don't want to do this everytime, refer to #4
2. To launch, ```roslaunch arm_moveit_config demo.launch```
3. To launch, ```roslaunch arm_moveit_config gazebo.launch```

# Guidelines for this repository
1.All files except urdf was completed using moveit setup assistant 
