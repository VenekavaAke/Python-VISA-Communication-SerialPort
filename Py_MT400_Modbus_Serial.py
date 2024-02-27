import serial 
 
# Configure serial port parameters 
port = "COM9" 
baudrate = 57600 
bytesize = serial.EIGHTBITS 
parity = serial.PARITY_NONE 
stopbits = serial.STOPBITS_ONE 
 
# Function to send a Modbus RTU command and receive the response 
def send_modbus_command(command): 
  # Open serial port 
  with serial.Serial(port, baudrate, bytesize=bytesize, parity=parity, stopbits=stopbits) as ser: 
    # Send command 
    ser.write(command) 
 
    # Set timeout and read response 
    ser.timeout = 1  # Set a 1 second timeout 
    response = ser.readall() 
 
  return response 
 
# Function to start communication 
def start(): 
  command = "\x02\x00\x07\x00\x03\n"  # Start function (0x02, function code 0x07, register address 0x00, data count 0x03) 
  response = send_modbus_command(command) 
  # Process response (if needed) 
 
# Function to get PLF Busy status 
def get_plf_busy(): 
  command = "\x02\x03\x00\x00\x01\n"  # Get PLF Busy status (0x02, function code 0x03, register address 0x00, data count 0x01) 
  response = send_modbus_command(command) 
  # Process response (if needed) 
  # Check if byte at index 3 is 0x00 (not busy) or 0x01 (busy) 
  if response[3] == 0x00: 
    return False 
  else: 
    return True 
 
# Function to get results 
def get_result(): 
  command = "\x02\x01\x00\x00\x06\n"  # Get result (0x02, function code 0x01, register address 0x00, data count 0x06) 
  response = send_modbus_command(command) 
  # Process response (if needed) 
  # Extract relevant data from response bytes 
 
# Example usage 
start() 
 
if not get_plf_busy(): 
  print("PLF is not busy") 
  get_result() 
else: 
  print("PLF is busy") 
