# R3-SoftwareTask2-AhmadAlnoor
Repository that includes 2 python code that communicate with each other using socket. The input.py sends user input direction and speed entered using keyboard and converts it into motor direction (forward or reverse) and speed (0 to 255)

In this project, the objective was to create two files (input.py and server.py) to control a 4 wheel rover. The input.py recieved input from the user using keyword and it was sent over to the server.py over the network to control the rover using Python programming language.
The files and their implementation are mentioned below

input.py implementation:
input.py file is the file that takes the user input from the keyboard and sends it over the network to the server.py. The input.py accepts values from 0 to 5 to control the speed of the rove and accepts W, S, A, and D keys to control the rovers direction.
In order to accept user input, "pygame" library was imported into the file so that its library could be used to decode which keys are pressed.
Also, for network connection, "socket" was also imported.

Before we get into the code, the pygame library and the network connection must be initalized:
In order to use pygames library, "pygame.init()" must be called to initalize pygame for execution.
Next, in order to set up a network between input.py and server.py, socket library's socket.socket function is called to initialize the iPv4 and TCP connections. Furthermore, the client (input.py) must connect to the server (server.py). To establish the connection, connect() function was used to establish connection using the host connection name and a port number. For this project. "socket.gethostname()" function was called to connect to the host computers network and port number 5000 was chosen at random since the lower ports are already in use by other programs on the computer. 

To use pygame, a small display screen of 800x600 was also initialized. The screen is an interface that must be clicked in order for the program to accept input. It is a black screen that displays nothing. The commands that the code executes get displayed in the terminal instead.

A speed variable is also initialzed to zero so that the robot is initally at rest and the speed must be manually changed.

Now to the code:
In the  "if __name__ == '__main__':", the first two lines are a welcome message and an introduction message to let the user know what the program is about.
After the message, input.py goes into an infinite loop which starts to handle events. Events are triggered every time a key is pressed. In this infinite while loop, the program executes the events for all the 9 possible inputs the user can enter. 
    
    "for event in pygame.event.get():" is a for loop that calls pygame.event.get() to see if any event has been triggered (if any button is pressed).
    The first if-condition in the for-loop looks for if the display screen has been close. If it has, the loop condition becomes false and input.py exits
    The second if-condition in the for-loop checks if a button-pressed type of event has been triggered. (pygame.KEYDOWN). If a button is pressed, then it checks for which 1 of the 9 buttons has been pressed. 
    if 0 has been pressed, then set the "speed" variable to 0
    if 1 has been pressed, then set the "speed" variable to 1
    if 2 has been pressed, then set the "speed" variable to 2
    if 3 has been pressed, then set the "speed" variable to 3
    if 4 has been pressed, then set the "speed" variable to 4
    if 5 has been pressed, then set the "speed" variable to 5
  For the W,A,S,and D keys, the if-condition is different. When they are pressed, instead of setting a variable, we send the speed and the respective direction to the server.py. The reason why we must send it when W,A,S, and D are pressed is because we have all the information to direct the rover. If W,A,S,and D are pressed before setting the rover speed, the speed by default is set to zero hence, we still have enough information to direct the rover. Except, when speed = 0, no matter which direction is pressed, the robot doesn't move. Therefore,
  if A has been pressed, send the speed information first over the network (in a string format) followed by the character "A"
Similarly, for S,W,and D, the speed variable is also sent first followed by character "S", "W", and "D" when their respective keys are pressed.


In serve.py the socket library is also used to establish the network connection between the client and the server. In server.py, the main difference is that instead of connecting, it hosts the server. It does that by hosting the server on the gethostname() and port number 5000 (the same gethostname() and port number input.py is trying to connect). After it hosts the server, it listens to whoever is trying to connect to the server. Once it recieves a client, the server.py creates a client_object variable for it so that it can communicate with the client. The server also stores the clients address in the address variable. Next we enter the infinite while loop. In the while loop, the server recieves the first bytes of data the client sends. It accepts it in 1024-bits. Since the first bits of data the client is going to be sending is the speed data, the server stores it into speed_data variable. The data is then convered into a string by calling the str() function. Finally, the speed value is converted to int by calling the int() function and storing it into speed_value variable. The speed value is then converted into PWM value by using the equation

(speed_value * 255)/5 
which basically takes the value from 0 - 5 and converts it into PWM value 0 - 255

The next data the serve recieves from the client is the direction data. It follows the same convertion steps  as the speed variable except that it is not converted to an int.
Lastly, the direction value and the PWM speed value is formated in such a way that it prints out which direction the motors are spinning and at what PWM speed they are spinning at.
The set_direction function is called to format the speed and direction as follows:
When the "W" key is pressed, all 4 motors are spinning forward with their PWM speed. For example, if "W" is pressed and the speed = 1 then the formating will be
[f 51] [f 51] [f 51] [f 51] where each block represents a motor, f represents forward direction, and 51 represents the speed value converted into its PWM value.
Similarly, when "S" is pressed, instead of printing "f", "r" is printed to show that all motors are spinning in reverse and the rover is going backwards.
[r 51] [r 51] [r 51] [r 51] if speed = 1
When "A" is pressed, the first two motors spin in reverse, while the last 2 spin the forward directin to turn the rover to the left.
[r 51] [r 51] [f 51] [f 51] if speed = 1
When "D" is presses, the first two motors spin forward, while the last 2 spin in reverse direction to turn the rover to the right.
[f 51] [f 51] [r 51] [r 51] if speed = 1

The server.py continues to listen to the client and continues to format the direction and the PWM speed until the client completly closes its application.
