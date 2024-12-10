#Basic Car HUD Project
#Brad Mahung - 2024
import gpsd
import time
import ht16k33 as HT16K33
import button as BUTTON  # Import the button library
import potentiometer as POT  # Import the potentiometer library

# Connect to the GPSD service
gpsd.connect()

# Initialize the HT16K33 7-segment display
display = HT16K33.HT16K33(address=0x70)  # Default I2C address (0x70) of the HT16K33

# Segment pattern for digits 0-9
digit_to_segments = {
    '0': 0x3F,  # 0b00111111
    '1': 0x06,  # 0b00000110
    '2': 0x5B,  # 0b01011011
    '3': 0x4F,  # 0b01001111
    '4': 0x66,  # 0b01100110
    '5': 0x6D,  # 0b01101101
    '6': 0x7D,  # 0b01111101
    '7': 0x07,  # 0b00000111
    '8': 0x7F,  # 0b01111111
    '9': 0x6F,  # 0b01101111
}

# Initialize button (assuming Button 3 on GPIO pin 22)
button3 = BUTTON.Button(22)  # Button 3 for the timer functionality

# Variables for the button states
button_state = 0  # 0: Display 00:00, 1: Countdown, 2: Timer running

# Initialize potentiometer for brightness control (using POT module)
potentiometer = POT.Potentiometer(1)  # Potentiometer connected to analog pin 1 (change based on your setup)

# Function to display a single digit on the 7-segment display
def display_digit(digit, position):
    """ Display a single digit at the given position on the 7-segment display. """
    # Map the digit to the corresponding 7-segment code
    display.set_digit(position, digit_to_segments[digit])

def display_time(time_str):
    """ Display time in MM:SS format on the 7-segment display. """
    for i, char in enumerate(time_str):
        if i < 5:  # Max 5 characters for MM:SS (2 digits for minutes, 2 for seconds, 1 for colon)
            display_digit(char, i)

def countdown():
    """ Perform a 3-second countdown and display on the 7-segment display. """
    for i in range(3, 0, -1):  # Countdown from 3 to 1
        print(f"Countdown: {i}")
        display_time(f"00:{i:02}")
        time.sleep(1)  # Wait for 1 second
    print("Countdown finished!")

def start_timer():
    """ Start a timer with 10ms accuracy and wait for speed to reach 60 mph (26.82 m/s). """
    print("Timer started, waiting for speed to reach 60 mph...")
    start_time = time.perf_counter()  # Use high-resolution timer

    while True:
        packet = gpsd.get_current()
        speed_mps = packet.speed  # Speed in meters per second
        
        if speed_mps is None:
            continue  # Skip if no GPS data available
        
        # Convert 60 mph to meters per second (1 mph ≈ 0.44704 m/s)
        target_speed_mps = 60 * 0.44704  # 60 mph in m/s

        if speed_mps >= target_speed_mps:
            # Once the target speed is reached, stop the timer
            elapsed_time = time.perf_counter() - start_time  # High-resolution elapsed time
            print(f"Speed reached 60 mph! Timer stopped.")
            print(f"Elapsed time: {elapsed_time:.2f} seconds")
            display_time(f"{int(elapsed_time):02}.{int((elapsed_time % 1) * 100):02}")  # Format to 00.00
            break

        # Display elapsed time in seconds and fractions (00.00 format)
        elapsed_time = time.perf_counter() - start_time
        display_time(f"{int(elapsed_time):02}.{int((elapsed_time % 1) * 100):02}")  # Format to 00.00

        time.sleep(0.01)  # Sleep for 10 milliseconds to check speed more frequently

def adjust_brightness():
    """ Adjust the display brightness based on the potentiometer value. """
    # Read the potentiometer value (assuming POT library provides a `read()` method)
    pot_value = potentiometer.read()  # Read the potentiometer value

    # Map the potentiometer value to the range 0-15 (brightness level of HT16K33)
    brightness_level = int(pot_value / 4096)  # Assuming the potentiometer value ranges from 0 to 4095 (12-bit ADC)

    # Set the display brightness (0-15 scale)
    display.set_brightness(brightness_level)
    print(f"Brightness set to {brightness_level}")

# Function to handle button press events
def button3_pressed():
    global button_state

    if button_state == 0:
        # First press: Set the screen to 00:00
        print("Button 3 pressed - Displaying 00:00")
        display_time("00:00")
        button_state = 1  # Move to countdown state

    elif button_state == 1:
        # Second press: Start countdown
        print("Button 3 pressed - Starting countdown")
        countdown()
        button_state = 2  # Move to timer state

    elif button_state == 2:
        # Third press: Start timer and wait for speed to reach 60 mph
        print("Button 3 pressed - Starting timer")
        start_timer()
        button_state = 0  # Reset to initial state (00:00)

# Assign the function to the button press event
button3.when_pressed = button3_pressed

if __name__ == "__main__":
    try:
        while True:
            adjust_brightness()  # Continuously adjust brightness based on potentiometer value
            time.sleep(0.1)  # Small delay to avoid overwhelming the system
    except KeyboardInterrupt:
        print("\nProgram interrupted.")
