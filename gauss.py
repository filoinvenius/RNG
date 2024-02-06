import serial

# Set the serial port and baud rate
ser = serial.Serial('COM5', 9600)  # Replace 'COM3' with the appropriate port for your Arduino

# Open a file for writing
with open('data_gauss_05_fev_ii.txt', 'w') as file:
    try:
        while True:
            # Read a line from the serial port
            line = ser.readline().decode('utf-8').strip()
            
            # Print the line to the console
            print(line)
            
            # Write the line to the file
            file.write(line + '\n')

    except KeyboardInterrupt:
        # Close the serial port and the file when the user interrupts the program
        ser.close()
        file.close()
