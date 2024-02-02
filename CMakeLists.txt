cmake_minimum_required(VERSION 3.10)

project(GitTuto)

add_executable(GitTuto 
    src/main.cpp
    src/abstractappliance.hpp
    src/abstractcharacter.hpp
    src/power.hpp src/power.cpp
)
