# R3-SoftwareTask2-AhmadAlnoor
Repository that includes 2 python code that communicate with each other using socket. The input.py sends user input direction and speed entered using keyboard and converts it into motor direction (forward or reverse) and speed (0 to 255)

In this project, the objective was to create two files (input.py and server.py) to control a 4 wheel rover. The input.py recieved input from the user using keyword and it was sent over to the server.py over the network to control the rover using Python programming language.
The files and their implementation are mentioned below

input.py implementation:
input.py file is the file that takes the user input from the keyboard and sends it over the network to the server.py. The input.py accepts values from 0 to 5 to control the speed of the rove and accepts W, S, A, and D keys to control the rovers direction.
In order to accept user input, "pygame" library was imported into the file so that its library could be used to decode which keys are pressed.
Also, for network connection, "socket" was also imported.

Before we get into the code, the pygame library and the network connection must be initalized:
In order to use pygames library, "pygame.init()" must be called to initalize all the libraries.
Next, in order to set up a network between input.py and server.py, socket library's socket.socket function was called to initialize the iPv4 and TCP connections
