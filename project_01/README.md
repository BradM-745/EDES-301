# Car HUD Project for PocketBeagle

## Overview

This project implements a car heads-up display (HUD) using a **PocketBeagle** board, GPS module, 7-segment display, buttons, and a potentiometer. The system reads GPS data (such as speed and heading), displays it on the 7-segment display, and allows user interaction through buttons for various functions like starting a timer or adjusting display brightness.

## Components

- **PocketBeagle Board**
- **GPS Module** (connected via UART)
- **7-Segment Display** (connected via HT16K33 I2C module)
- **Two Buttons** (for user input)
- **Potentiometer** (for controlling the display brightness)
- **Power Supply** (for the components)

## Pinout

### **1. GPS Module (UART)**

- **GPS TX** → **P2.11 (UART4 RX)**
- **GPS RX** → **P2.13 (UART4 TX)**
- **GPS VCC** → **3.3V or 5V**
- **GPS GND** → **Ground**

### **2. 7-Segment Display (via HT16K33)**

- **HT16K33 SDA** → **P2.9 (I2C SDA)**
- **HT16K33 SCL** → **P2.11 (I2C SCL)**
- **HT16K33 VCC** → **3.3V**
- **HT16K33 GND** → **Ground**

### **3. Buttons (GPIO Pins 34-35 on P1)**

- **Button 1 (Mode Cycling)**:
  - One side to **Ground**
  - Other side to **GPIO pin 34 (P1.34)** on PocketBeagle

- **Button 2 (Timer and Reset)**:
  - One side to **Ground**
  - Other side to **GPIO pin 35 (P1.35)** on PocketBeagle

### **4. Potentiometer (Brightness Control)**

- **Potentiometer Pin 1 (Ground)** → **Ground**
- **Potentiometer Pin 2 (Wiper, Middle Pin)** → **GPIO pin 17 (P1.17)**
- **Potentiometer Pin 3 (VCC)** → **1.8V (via P1.18)**

---

### Final Pinout Summary

| **Component**        | **Pin on PocketBeagle (P1, P2)**  | **Connection**         |
|----------------------|-----------------------------------|------------------------|
| **GPS TX**           | **P2.11 (UART4 RX)**              | GPS TX                 |
| **GPS RX**           | **P2.13 (UART4 TX)**              | GPS RX                 |
| **GPS VCC**          | **3.3V or 5V**                    | Power to GPS           |
| **GPS GND**          | **Ground**                        | Ground for GPS         |
| **HT16K33 SDA**      | **P2.9 (I2C SDA)**                | HT16K33 SDA            |
| **HT16K33 SCL**      | **P2.11 (I2C SCL)**               | HT16K33 SCL            |
| **HT16K33 VCC**      | **3.3V**                          | Power to HT16K33       |
| **HT16K33 GND**      | **Ground**                        | Ground for HT16K33     |
| **Button 1**         | **P1.34 (GPIO)**                  | Mode cycling button    |
| **Button 2**         | **P1.35 (GPIO)**                  | Timer reset button     |
| **Potentiometer**    | **P1.17 (Wiper)**                 | Brightness control     |
| **Potentiometer VCC**| **P1.18 (1.8V)**                  | Power to Potentiometer |
| **Potentiometer GND**| **Ground**                        | Ground for Potentiometer|

---

## How to Run the Project

###Clone the repository to your PocketBeagle device:

```bash
git clone https://github.com/yourusername/car-hud-project.git
cd car-hud-project
```
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
