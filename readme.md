# Autobuilder

This program was _initially born_ with the intention of being able to directly compile the source code written in _C_ and run it immediately after saving the file, just to simplify those two _boring_ commands.

## How is the project structured?

The project, for now, is structured in three parts:

- Current folder:
    - Inside the current folder we find the main files to start the whole program.

- Lib folder:
    - Inside this folder we find the main heart of the program. There are all the managers for the management of the GUI in bash and for the threads, who will have to check continuously every saving of the selected file when the program is launched.
- Facades folder

    - Inside this folder, however, we find all the Autobuild GUI configurations. In fact, thanks to the **bash_manager.py** library you can customize the whole GUI to your liking.

## How do facades work?

There are two very important files within this folder:

- **config.json**
    - Within this file we can find a list, which contains all the facades of AutoBuild, like the example below:
    ```
    {
        "facades" : [
            "main.json"
        ]
    }
    ```
    To add a facade, simply insert it after the last facade after the comma.

- **main.json**
    - _**Disclaimer:**_ The file name doesn't have to be called that way, you can call it whatever you want!  
    
    ```
    {
        "window" : {
            "title" : "Example Title",
            "body" : {
                "2" : "Foo",
                "3" : "Example var 1 &v&var1&v&",
            },
            "footer" : ""
        }
    }
    ```
    - In this file the things we can customize are:  
        - **title:** Corresponds to the window title  
        - **body:** Corresponds to the central body of the window. Here we can customize the terminal line by line. The number, such as _"2"_ corresponds to the line number, while the assigned value corresponds to what you want to print on the screen. When writing the guide, you can print variables present in **bash_manager.py**, enclosed with **&v&**  
        - **footer:** Corresponds to the last line of the terminal. In the future, the ability to update the _footer_ whenever you want will be implemented, perhaps during an update or operation. 

## Technical information

The program requires a version of **Python3** installed. The version I use is **3.8.4 64-bit**. I Program with Visual Studio Code connected to WSL (Windows Subsystem for Linux). The distro is Ubuntu 20.04 

Libraries used:

- **curses** (creation of the GUI)
- **termios** (terminal reset)
- **json** (facades management)
- **threading** (thread management)

## Disclaimer

In case of problems with the program, before reporting it via the **Issue** tab on GitHub, try to replicate my own programming environment, so as not to create unnecessary "Issues".
