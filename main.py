import machine
import time

def calc_temperature(voltage):
    # y = mx + b, where y is temperature and x is voltage
    m = 104.1667 # Or same as k
    b = -54.1667
    temperature = m * voltage + b
    return temperature

# Initialize ADC on GP26 (ADC0)
adc = machine.ADC(26)

while True:
    # Read 16-bit ADC value on pin 26
    adc_value = adc.read_u16()
    
    # Convert ADC value back to voltage
    voltage = adc_value * (3.3 / 65535)
    
    # Calculate temperature from voltage
    temperature = calc_temperature(voltage)
    
    # Print the temperature
    print("Temperature: ", temperature)
    
    # Wait for a short period before reading again
    time.sleep(1)
