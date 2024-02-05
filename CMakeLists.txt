cmake_minimum_required(VERSION 3.10)

project(GitTuto)

add_executable(${PROJECT_NAME}
    src/main.cpp
    src/abstractappliance.hpp
    src/abstractcharacter.hpp
    src/power.hpp src/power.cpp
)

install(TARGETS ${PROJECT_NAME}
    RUNTIME DESTINATION bin
    LIBRARY DESTINATION lib
)
