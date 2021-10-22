import pygame
import socket

# initialize pygame
pygame.init()

# Streaming socket configuration
socket_object = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# client that connects to the host name with port number
socket_object.connect((socket.gethostname(), 5000))

# Initialize screen to execute pygame commands
screen = pygame.display.set_mode((800, 600))
# speed variable initialized to zero
speed = 0

if __name__ == '__main__':
    print("Welcome to the robot control simulator! \n")
    print("Please select the speed for the robot between 0 and 5: ")

    looping = True
    while looping:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                looping = False
            # numbers 0 to 5 to set the speeds
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_0:
                    speed = 0
                    print(f"speed set to {speed}")
                if event.key == pygame.K_1:
                    speed = 1
                    print(f"speed set to {speed}")
                if event.key == pygame.K_2:
                    speed = 2
                    print(f"speed set to {speed}")
                if event.key == pygame.K_3:
                    speed = 3
                    print(f"speed set to {speed}")
                if event.key == pygame.K_4:
                    speed = 4
                    print(f"speed set to {speed}")
                if event.key == pygame.K_5:
                    speed = 5
                    print(f"speed set to {speed}")
                # w, a, s , and d for direction setting
                # both speed and direction once one of the direction keys are pressed
                if event.key == pygame.K_a:
                    # First the speed value is sent since the server is expecting speed value first
                    # It is sent in byte format and the integer is converted into string with utf-8 format
                    socket_object.sendall(bytes(str(speed), "utf-8"))
                    # The next value the server is expecting is the direction value, which is sent next
                    socket_object.sendall(bytes("a", "utf-8"))
                if event.key == pygame.K_d:
                    socket_object.sendall(bytes(str(speed), "utf-8"))
                    socket_object.sendall(bytes("d", "utf-8"))
                if event.key == pygame.K_w:
                    socket_object.sendall(bytes(str(speed), "utf-8"))
                    socket_object.sendall(bytes("w", "utf-8"))
                if event.key == pygame.K_s:
                    socket_object.sendall(bytes(str(speed), "utf-8"))
                    socket_object.sendall(bytes("s", "utf-8"))
