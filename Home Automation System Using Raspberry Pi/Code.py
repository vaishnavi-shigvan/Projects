import bluetooth
# Importing the GPIO library to use the GPIO pins of Raspberry pi
import RPi.GPIO as GPIO

led_pin1 = 40     # Initializing pin 40 for led
led_pin2=11
led_pin3=13
led_pin4=15
GPIO.setmode(GPIO.BOARD)  # Using BCM numbering

GPIO.setup(led_pin1, GPIO.OUT)   # Declaring the pin 40 as output pin
GPIO.setup(led_pin2,GPIO.OUT)
host = ""
port = 1        # Raspberry Pi uses port 1 for Bluetooth Communication
# Creaitng Socket Bluetooth RFCOMM communication
server = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
print('Bluetooth Socket Created')
try:
        server.bind((host, port))
        print("Bluetooth Binding Completed")
except:
        print("Bluetooth Binding Failed")
server.listen(1) # One connection at a time
# Server accepts the clients request and assigns a mac address.
client, address = server.accept()
print("Connected To", address)
print("Client:", client)
try:
        while True:
                # Receivng the data.
                data = int(client.recv(1024)) # 1024 is the buffer size.
                print(data)

                if data == 1:
                        print("Turning LED1 ON")
                        GPIO.output(led_pin1, False)
                        send_data = "Light On "
                elif data == -1:
                        print("Turning LED1 OFF")
                        GPIO.output(led_pin1, True)
                        send_data = "Light Off "
                if data == 2:
                        print("Turning LED2 ON")
                        GPIO.output(led_pin2, False)
                        send_data = "Light On "
                elif data == -2:
                        print("Turning LED2 OFF")
                        GPIO.output(led_pin2, True)
                        send_data = "Light Off "
                if data == 3:
                        print("Turning LED3 ON")
                        GPIO.output(led_pin3, False)
                        send_data = "Light On "
                elif data == -3:
                        print("Turning LED3 OFF")
                        GPIO.output(led_pin3, True)
                        send_data = "Light Off"
                if data == 4:
                        print("Turning LED4 ON")
                        GPIO.output(led_pin4, False)
                        send_data = "Light On "
                elif data == -4:
                        print("Turning LED4 OFF")
                        GPIO.output(led_pin4, True)
                        send_data = "Light Off"
                else:
                        send_data = "Type 1 or 0 "
                # Sending the data.
                client.send(send_data)
except:
        # Making all the output pins LOW
        GPIO.cleanup()
        # Closing the client and server connection
        client.close()
        server.close()
