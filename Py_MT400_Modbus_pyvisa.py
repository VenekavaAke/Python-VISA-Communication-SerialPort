# Import the pyvisa library 
import pyvisa 

# Create a resource manager object 
rm = pyvisa.ResourceManager() 

# Open the serial port with the specified parameters 
ser = rm.open_resource( 
    resource_name='ASRL9::INSTR', # The VISA resource name 
    baud_rate=57600, # The baud rate 
    data_bits=8, # The number of data bits 
    parity=pyvisa.constants.Parity.none, # The parity mode 
    stop_bits=pyvisa.constants.StopBits.one, # The number of stop bits 
    read_termination='\n' # The read termination character 
) 

# Define the Open Protocol commands as bytes 
open_cmd = b'\x020G0A7\x03\n' # Open communication 
busy_cmd = b'\x020TOD3\x03\n' # Get busy status 
result_cmd = b'\x020TRD6\x03\n' # Get result data 

# Define the function to start communication 
def start(): 
    # Write the open command to the serial port 
    ser.write(open_cmd) 

    # Wait for 500 ms 
    ser.wait_for_srq(0.5) 

    # Read the response from the serial port 
    response = ser.read_bytes(100) # Read up to 100 bytes 

    print(response) # Print the response 

# Define the function to get the PLF busy status 
def get_plf_busy(): 
    # Write the busy command to the serial port 
    ser.write(busy_cmd) 

    # Wait for 100 ms 
    ser.wait_for_srq(0.1) 

    # Read the response from the serial port 
    response = ser.read_bytes(100) # Read up to 100 bytes 

    print(response) # Print the response 

# Define the function to get the result data 
def get_result(): 

    # Write the result command to the serial port 
    ser.write(result_cmd) 

    # Wait for 200 ms 
    ser.wait_for_srq(0.2) 
    
    # Read the response from the serial port 
    response = ser.read_bytes(100) # Read up to 100 bytes 

    print(response) # Print the response 

# Call the functions 
start() 
get_plf_busy() 
get_result() 

# Close the serial port 
ser.close() 