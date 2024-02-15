# git-tuto-playground
A simple repository for git demonstration purposes.

To have a little playground, imagine we are in the repository of a game development. <br/>
In this game, you are an installer, and your goal is to install some appliances in a limited amount of time. <br/>
<br/>
Features:
- Create some characters: installers, customers etc..
- Drive to customer's home
- Install your appliance
- Interact with customers
- You can have superpower that helps you install more appliances and quicked etc...

## How to build (in wsl)
Create a build directory and navigate in it:<br/>
```shell
mkdir build
cd build
```

In the build directory, launch cmake, and build within make:<br/>
```shell
cmake ..
make
```

>Note: cmake shall be installed on the system, and added in the path environment variable
