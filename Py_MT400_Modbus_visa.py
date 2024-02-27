import visa 
 
# VISA resource name (replace with your actual COM port) 
resource_name = "COM9" 
 
# Modbus settings 
baudrate = 57600 
data_bits = 8 
parity = visa.constants.PARITY_NONE 
stop_bits = 1 
 
# Function definitions 
def start(): 
    """Sends the start command to the Atlas Copco MT400.""" 
    write_buffer = "\x02\x20G0A7\x03\n" 
    instrument.write(write_buffer) 
    visa.wait_async_operation_complete(instrument) 
    visa.delay(500)  # Delay in milliseconds 
 
def get_plf_busy(): 
    """Reads the PLF busy status from the Atlas Copco MT400.""" 
    write_buffer = "\x02\x20TOD3\x03\n" 
    instrument.write(write_buffer) 
    visa.wait_async_operation_complete(instrument) 
    visa.delay(100)  # Delay in milliseconds 
    read_buffer = instrument.read(1) 
    return read_buffer 
 
def get_result(): 
    """Reads the result from the Atlas Copco MT400.""" 
    write_buffer = "\x02\x20TRD6\x03\n" 
    instrument.write(write_buffer) 
    visa.wait_async_operation_complete(instrument) 
    visa.delay(200)  # Delay in milliseconds 
    read_buffer = instrument.read( instrument.ask("*TRB?").strip() )  # Read based on response length 
    return read_buffer 
 
# Open VISA resource 
instrument = visa.ResourceManager().open_resource(resource_name) 
 
# Configure VISA parameters 
instrument.baudrate = baudrate 
instrument.data_bits = data_bits 
instrument.parity = parity 
instrument.stop_bits = stop_bits 
 
# Example usage 
start() 
is_busy = get_plf_busy() 
print("PLF Busy:", is_busy) 
 
# Get result only if PLF is not busy 
if is_busy != b"\x00": 
    print("PLF is busy, cannot get result.") 
else: 
    result = get_result() 
    print("Result:", result) 
 
# Close VISA resource 
instrument.close() 