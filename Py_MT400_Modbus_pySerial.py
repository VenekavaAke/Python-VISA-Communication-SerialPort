# Import the pySerial library 
import serial 

# Create a serial object with the specified parameters 
ser = serial.Serial( 
    port='COM3', # The port name 
    baudrate=57600, # The baud rate 
    bytesize=serial.EIGHTBITS, # The number of data bits 
    parity=serial.PARITY_NONE, # The parity mode 
    stopbits=serial.STOPBITS_ONE, # The number of stop bits 
    timeout=1 # The read timeout in seconds 
) 

# Define the Open Protocol commands as bytes 
open_cmd = b'\x020G0A7\x03\n' # Open communication 
busy_cmd = b'\x020TOD3\x03\n' # Get busy status 
result_cmd = b'\x020TRD6\x03\n' # Get result data 

# Write the open command to the serial port 
ser.write(open_cmd) 

# Read the response from the serial port 
response = ser.read(100) # Read up to 100 bytes 

print(response) # Print the response 

# Write the busy command to the serial port 
ser.write(busy_cmd) 

# Read the response from the serial port 
response = ser.read(100) # Read up to 100 bytes 

print(response) # Print the response 

# Write the result command to the serial port 
ser.write(result_cmd) 

# Read the response from the serial port 
response = ser.read(100) # Read up to 100 bytes 

print(response) # Print the response 

# Close the serial port 
ser.close() 