# Car HUD Project

This project involves creating a Car Heads-Up Display (HUD) using a PocketBeagle, a GPS module, and a 7-segment display. The system provides real-time speed, heading, and a custom timer that reacts to the vehicle's speed. I still have a lot of refinement to do before this project is fully complete, but please enjoy what I've done so far!

## Features
- Displays current speed on a 7-segment display.
- Displays current heading (latitude or longitude).
- Starts a timer upon reaching a speed of 60 mph.
- Adjusts the display brightness using a potentiometer.
- Runs automatically on boot with the PocketBeagle.

## Installation

To set up the project on your PocketBeagle:

1. **Install Required Libraries:**
    ```bash
    pip install gpsd ht16k33 button potentiometer
    ```

2. **Clone the Project Repository:**
    ```bash
    git clone <repository-url> /home/debian/ENGI301/project1/
    ```

3. **Set Up Systemd Service:**
   Create a systemd service to run the Python script on boot.

   Create the service file:
   ```bash
   sudo nano /etc/systemd/system/gps_timer.service
