<h1>Car HUD Project</h1>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Car HUD Project - README</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f4f4f9;
            margin: 0;
            padding: 20px;
            color: #333;
        }
        h1, h2 {
            color: #4CAF50;
        }
        code {
            background-color: #f1f1f1;
            padding: 5px;
            border-radius: 4px;
        }
        pre {
            background-color: #333;
            color: #f1f1f1;
            padding: 15px;
            border-radius: 5px;
            overflow-x: auto;
        }
        .section {
            margin-bottom: 30px;
        }
        .important {
            color: red;
            font-weight: bold;
        }
        .installation, .usage {
            background-color: #e7f5e7;
            padding: 10px;
            border-radius: 5px;
        }
    </style>
</head>
<body>

    <h1>Car HUD Project</h1>

    <p>This project involves creating a Car Heads-Up Display (HUD) using a PocketBeagle, a GPS module, and a 7-segment display. The system provides real-time speed, heading, and a custom timer that reacts to the vehicle's speed.</p>

    <div class="section">
        <h2>Project Features</h2>
        <ul>
            <li>Displays current speed on a 7-segment display.</li>
            <li>Displays current heading (latitude or longitude).</li>
            <li>Starts a timer upon reaching a speed of 60 mph.</li>
            <li>Adjusts the display brightness using a potentiometer.</li>
            <li>Runs automatically on boot with the PocketBeagle.</li>
        </ul>
    </div>

    <div class="section installation">
        <h2>Installation</h2>
        <p>To get this project running on your PocketBeagle, follow these steps:</p>
        <ol>
            <li><strong>Install Required Libraries:</strong>
                <pre><code>pip install gpsd ht16k33 button potentiometer</code></pre>
            </li>
            <li><strong>Clone the Project Repository:</strong>
                <pre><code>git clone <repository-url> /home/debian/ENGI301/project1/</code></pre>
            </li>
            <li><strong>Set Up Systemd Service:</strong> 
                Create a systemd service to run the script on boot. Follow the instructions below:
                <pre><code>sudo nano /etc/systemd/system/gps_timer.service</code></pre>
                Paste the following content into the file:
                <pre><code>[Unit]
Description=Run GPS Timer Script at Boot
After=network.target

[Service]
ExecStart=/home/debian/start_gps_timer.sh
Restart=always
User=debian
WorkingDirectory=/home/debian

[Install]
WantedBy=multi-user.target</code></pre>
                Save the file and enable the service:
                <pre><code>sudo systemctl daemon-reload
sudo systemctl enable gps_timer.service</code></pre>
            </li>
        </ol>
    </div>

    <div class="section usage">
        <h2>Usage</h2>
        <p>Once the system is booted, the script will automatically start and provide the following features:</p>
        <ul>
            <li>Press button 1 to cycle between different display modes: Speed, Heading, or Timer.</li>
            <li>Press button 2 to reset the display to 00:00 or start a countdown timer.</li>
            <li>Adjust the display brightness using the potentiometer.</li>
            <li>The timer starts after the countdown and stops once a speed of 60 mph is reached.</li>
        </ul>
    </div>

    <div class="section">
        <h2>System Setup</h2>
        <p>Ensure the following components are correctly wired:</p>
        <ul>
            <li>PocketBeagle board</li>
            <li>GPS module connected to the PocketBeagle</li>
            <li>7-segment display connected via I2C</li>
            <li>Button and potentiometer connected to appropriate GPIO pins</li>
        </ul>
    </div>

    <div class="section">
        <h2>Troubleshooting</h2>
        <p>If you encounter issues during setup or execution, consider the following:</p>
        <ul>
            <li>Ensure the GPS module is receiving a valid signal and sending data.</li>
            <li>Check that the I2C bus is properly enabled on the PocketBeagle.</li>
            <li>If the display does not update, ensure the wiring is correct and power is supplied.</li>
            <li>If the script doesn't run on boot, verify the systemd service configuration and check logs with <code>journalctl -u gps_timer.service</code>.</li>
        </ul>
    </div>

    <div class="section">
        <h2>License</h2>
        <p>This project is licensed under the MIT License - see the <a href="LICENSE">LICENSE</a> file for details.</p>
    </div>

</body>
</html>
