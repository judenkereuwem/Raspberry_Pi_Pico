# Import necessary modules
from machine import Pin
import bluetooth
from ble_simple_peripheral import BLESimplePeripheral

# Create a Bluetooth Low Energy (BLE) object
ble = bluetooth.BLE()

# Create an instance of the BLESimplePeripheral class with the BLE object
sp = BLESimplePeripheral(ble)

# Create a Pin object for the onboard LED, configure it as an output
led = Pin("LED", Pin.OUT)


# Define a callback function to handle received data
def on_rx(data):
    print("Data received: ", data)  # Print the received data
    #global led_state  # Access the global variable led_state
    if data == b'H\r\n':
        led.on()
    elif data == b'L\r\n':
        led.off()

# Start an infinite loop
while True:
    if sp.is_connected():  # Check if a BLE connection is established
        sp.on_write(on_rx)  # Set the callback function for data reception