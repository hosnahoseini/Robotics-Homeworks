# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.16

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:


#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:


# Remove some rules from gmake that .SUFFIXES does not remove.
SUFFIXES =

.SUFFIXES: .hpux_make_needs_suffix_list


# Suppress display of executed commands.
$(VERBOSE).SILENT:


# A target that is always out of date.
cmake_force:

.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /usr/bin/cmake

# The command to remove a file.
RM = /usr/bin/cmake -E remove -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /home/hosna/Desktop/catkin_ws/src

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/hosna/Desktop/catkin_ws/build

# Utility rule file for hw0_geneus.

# Include the progress variables for this target.
include hw0/CMakeFiles/hw0_geneus.dir/progress.make

hw0_geneus: hw0/CMakeFiles/hw0_geneus.dir/build.make

.PHONY : hw0_geneus

# Rule to build all files generated by this target.
hw0/CMakeFiles/hw0_geneus.dir/build: hw0_geneus

.PHONY : hw0/CMakeFiles/hw0_geneus.dir/build

hw0/CMakeFiles/hw0_geneus.dir/clean:
	cd /home/hosna/Desktop/catkin_ws/build/hw0 && $(CMAKE_COMMAND) -P CMakeFiles/hw0_geneus.dir/cmake_clean.cmake
.PHONY : hw0/CMakeFiles/hw0_geneus.dir/clean

hw0/CMakeFiles/hw0_geneus.dir/depend:
	cd /home/hosna/Desktop/catkin_ws/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/hosna/Desktop/catkin_ws/src /home/hosna/Desktop/catkin_ws/src/hw0 /home/hosna/Desktop/catkin_ws/build /home/hosna/Desktop/catkin_ws/build/hw0 /home/hosna/Desktop/catkin_ws/build/hw0/CMakeFiles/hw0_geneus.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : hw0/CMakeFiles/hw0_geneus.dir/depend

