import socket

# Streaming socket configuration
socket_object = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Server that takes the host name with port number
socket_object.bind((socket.gethostname(), 5000))
# Listen to whoever is trying to connect
socket_object.listen()
# store the client socket object and the address of the client in the respective variables
client_object, address = socket_object.accept()

# Function that formats the keyboard input direction and speed into motor direction format
def set_direction(direction, speed):
    # convert the direction and speed into their respective format
    if direction == "w":
        # the format is motor 1, motor 2, motor 3, and motor 4 direction [f or r] and speed [0-255]
        print(f"[f {speed}] [f {speed}] [f {speed}] [f {speed}]\n")
    if direction == "s":
        print(f"[r {speed}] [r {speed}] [r {speed}] [r {speed}]\n")
    if direction == "d":
        print(f"[f {speed}] [f {speed}] [r {speed}] [r {speed}]\n")
    if direction == "a":
        print(f"[r {speed}] [r {speed}] [f {speed}] [f {speed}]\n")


while True:
    # Accept the speed value in string format first
    speed_data = client_object.recv(1024)
    # Convert the speed and store it into string variable with ut-8 format
    speed_string = str(speed_data, "utf-8")
    # Typecast the string into int
    speed_value = int(speed_string)
    # Accept the direction value and store it into direction variable
    direction = client_object.recv(1024)
    # Format it into ut-8 format
    direction = str(direction, "utf-8")
    # Linear relationship between keyboard input speed ( 0 to 5) and motor speed ( 0 - 255)
    speed_PWM = (speed_value / 5) * 255
    # Set the direction and speed of the robot by sending the direction and speed
    set_direction(direction, speed_PWM)
