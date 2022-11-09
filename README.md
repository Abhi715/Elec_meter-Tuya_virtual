# Elec_meter-Tuya_virtual

This is a small project collect the data from electrical meter using modbus and use he virtual devices on Tuya. 

No hardware is used, instead of real devices virtual devices and simulator is used for this project and the script is written in python and use the Visual Studio Code.

1. Diagslave Modbus simulator is used that is free command line based Modbus slave simulator for testing.
2. Virtual Serial Port Driver software is used to create the virtual COM ports.


Version-
Python 3.8.0
pymodbus 3.0.2
pip3 22.3.1
VS Code 1.73.0


Getting Started

-------------------------------------------------------------------------------------------------------------------------------------------------------

Install all the required modules,

To install the pymodbus
-> pip3 install pymodbus

install the tuya connector
-> pip3 install tuya_connector_python

install the pep8
-> pip3 install autopep8

Open the virtual serial port driver software and continue the trial version, here we will get the option virtual ports to pair (i used COM1 and COM2) and click on create. the connection can be break by clicking the break.

Open the diagslave modbus software usign the command prompt,
1. follow the path where the .exe file of the software is stored.
2. go to the win folder
3. use the command: diagslave -b 9600 -p none -m rtu COM1
Serial server has been started and the message "Server started up successfully" will show on command prompt and it can be stopped by Ctrl+C

For Tuya
1. First need to create the tuya account, Go to the sign up page and create an account.
2. After that, you will be asked to choose if you are an individual developer or an organization; click on Set Now and choose I am an Individual Developer.
3. Next click Cloud > Development from the left navigation bar and then select the TRIAL EDITION option.
4. On the next page select TRIAL EDITION and click Buy Now. Don't worry, you don't have to add a credit card, the process is completely free, and select Submit Order on the next page. Again, don't worry this is completely free. After that, you can see that your trial edition plan is running.
5. Now go back to the IoT platform by clicking on the IoT Platform button at the top right of the page and then click Cloud > Development
6. Now we need to create a cloud project. Click Create Cloud Project on the right side of the page. On the dialog box, fill in the form and click Create.
7. For Industry select Smart Home, for Development Method select Custom, and for Availability Zone select the server address corresponding to your area. For me it's India Data Center.
8. On the Authorize API Services page, you can see that there are some APIs services selected by default (on the right) but we also need to add other APIs.  Select them and click Authorize.
9. After that, you will see the Project Configuration page to create an asset and a user
10. Then add the virtual devices, Under the Devices section, hover the mouse on Add Device, and click Add Virtual Device.
11. then for the Asset Path just select the asset that you created before and click OK, for me I named it AB Asset.

then install the pip3 install tuya_connector_python

we need to collect some device and project information,
1. the ACCESS_ID and ACCESS_KEY keys by navigating to Cloud > Development > My Cloud Project
2. the DEVICE_ID by navigating to Cloud > Development > My Cloud Project > Devices



