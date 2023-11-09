# Robotics Homework Solutions 🤖

This repository contains my solutions to a series of robotics homework assignments. These assignments encompass various aspects of robotics, from sensor-based control to mapping, path following, and even human-robot interaction.

## Homework 1: Sonar-based Obstacle Rotation

**Solution**: [Homework 1 Solution](/HW1)

- In Homework 1, I worked with a wheeled robot equipped with sonar sensors. The robot had the capability to rotate in place and featured a sonar sensor array on top, providing distance measurements in four directions: front, back, left, and right. The goal of this assignment was to program the robot to always rotate towards the direction of the nearest obstacle. To achieve this, I used the robot's rotational capabilities and sonar sensor data. I leveraged the Robot Operating System (ROS) and related tools to develop a program that ensured the robot consistently rotated to position the closest obstacle directly behind it.

**Report**: A detailed report is provided in the Homework 1 folder for more information.

## Homework 2: Lidar-based Obstacle Avoidance and Mapping

**Solution**: [Homework 2 Solution](/HW2)

In Homework 2, I tackled two key challenges:

- **Lidar-based Obstacle Avoidance**: I developed a solution to find the distance of the closest obstacle using a lidar sensor and implemented a control system that prompts the robot to turn when it approaches an obstacle.

- **Mapping with TurtleBot**: I designed a solution that enables the TurtleBot to move and scan its environment to reconstruct a map. This process is crucial for building a robot's awareness of its surroundings.

**Report**: A detailed report is provided in the Homework 2 folder for more information.

## Homework 3: Geometric Path Following and Wall Following

**Solution**: [Homework 3 Solution](/HW3)

In Homework 3, I addressed the following tasks:

- **PID Controller for Geometric Path Following**: I defined and fine-tuned a PID controller to control the robot's movement along a geometric path. The PID controller ensures that the robot follows the desired path accurately.

- **Wall Following Algorithm with LaserScan Sensor**: I implemented a wall following algorithm, which utilizes data from the LaserScan sensor to assist the robot in navigating alongside walls. This algorithm is particularly useful for initial movements in unknown environments.

**Report**: A detailed report is provided in the Homework 3 folder for more information.

## Homework 4: Humanoid Robot Control and Maze Navigation

**Solution**: [Homework 4 Solution](/HW4)

In Homework 4, I worked on an exciting challenge:

- **Humanoid Robot Control**: I controlled a TurtleBot3 robot with PID controller to follow humanoid robot which moved by keyboard . The objective was for the Burger robot to follow the humanoid robot.

**Report**: A detailed report is provided in the Homework 4 folder for more information.

## Final Projects: VFH Algorithm and Traffic Sign Detection

**Solution**: [Final Projects Solution](/FinalProjects)

The final projects were diverse and innovative:

- **VFH Algorithm for Maze Navigation**: My [team mate](https://github.com/aliasad059) and I implemented the VFH (Vector Field Histogram) algorithm from scratch to navigate the TurtleBot3 through a complex maze while avoiding obstacles. The VFH algorithm helps the robot make intelligent decisions based on its environment.

- **Traffic Sign Detection with YOLO**: My [team mate](https://github.com/aliasad059) and I integrated the YOLO (You Only Look Once) object detection algorithm to identify traffic signs and then control the robot to react to the signs accurately when it reaches them (eg. stop, lower speed, turn).

**Report**: Detailed reports for each final project are provided in the Final Projects folder for more information.

**Used Packages**: ROS, Gazebo, YOLO

## How to Use This Repository

Explore each homework or project solution by navigating to the respective directory. Inside each directory, you'll find my code, documentation, and additional resources relevant to the specific task.

## Contact

If you have any questions, or feedback, or wish to discuss any of my solutions, please don't hesitate to contact me:

- [Hosna Hoseini](mailto:hosna.hoseini@gmail.com)

Thank you for exploring my robotics homework solutions and final projects!

