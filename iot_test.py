import sys
import pymodbus
from datetime import datetime, time
import random
from pymodbus.pdu import ModbusRequest
from pymodbus.client import ModbusSerialClient as ModbusClient
import time
import json
import logging
from tuya_connector import TuyaOpenAPI, TUYA_LOGGER

# date and time function


def current_time():
    """return the current time nad date"""
    now = datetime.now().isoformat()
    return now


# initiate modbus client to connect modbus RTU/serial server
client = ModbusClient(method='rtu', port='COM2',
                      timeout=2, stopbits=1, bytesize=8, parity='N', baudrate=9600)


# infinite while loop
while True:
    # connect the client to server
    client.connect()

    # generate the random data to write to the modbus register
    data = random.randint(10, 200)
    """generate the integer data in the range of 20 to 200"""

    # write_register(register_address, value_to_write, slave_ID)
    write_register = client.write_register(40001, data, unit=1)

    # read_holding_registers(starting_address, no_of_registers_to_read, slave_ID)
    read_registers = client.read_holding_registers(
        address=40001, count=1, unit=1)

    # store the date, time and data read from the modbus (integer) in dictionary
    modbus_data = {
        # calling the date and time function
        "date_time": current_time(),

        # store integer data get from modbus
        "data": read_registers.registers
    }

    # convert into json
    print(json.dumps(modbus_data))

    # access ID and key for project authorization on TUYA
    ACCESS_ID = 'mjehqreqspyrrut9nagv'
    ACCESS_SECRET = '9f2c2ec4fe274625959d1bc11aea386e'

    # Select an endpoint base on your project availability zone, I am using India data center
    # For more info, refer to: https://developer.tuya.com/en/docs/iot/api-request?id=Ka4a8uuo1j4t4
    ENDPOINT = "https://openapi.tuyain.com"

    # Enable debug log
    TUYA_LOGGER.setLevel(logging.DEBUG)

    # Initialization of tuya openapi and connect all the parameters in string
    openapi = TuyaOpenAPI(ENDPOINT, ACCESS_ID, ACCESS_SECRET)

    # initialize the connection
    openapi.connect()

    # Device_ID of virtual devices on Tuya (using three virtual device)
    # device id for switch
    SWITCH_DEVICE_ID = 'vdevo166782136188789'

    # device id for led
    LED_DEVICE_ID = 'vdevo166782120811251'

    # device ID for electric meter
    METER_DEVICE_ID = 'vdevo166792460706753'

    # get the virtual device information by passing the individual device ID
    """store the virtual device information in dictionary"""
    switch_info = openapi.get(
        "/v1.0/iot-03/devices/{}".format(SWITCH_DEVICE_ID))
    led_info = openapi.get(
        "/v1.0/iot-03/devices/{}".format(LED_DEVICE_ID))
    meter_info = openapi.get(
        "/v1.0/iot-03/devices/{}".format(METER_DEVICE_ID))

    # to send the command to switch virtual device
    Switch_command = {'commands': [{'code': 'switch_led', 'value': True}]}

    # send the commands to the individual virtual device by passing the device id and command
    switch_request = openapi.post(
        '/v1.0/iot-03/devices/vdevo166782120811251/commands', Switch_command)

    # to send the command to led virtual device
    led_command = {'commands': [{'code': 'switch_1', 'value': True}, {
        'code': 'bright_value_v2', 'value': 50}, {'code': 'countdown_1', 'value': 10000}]}

    # send the commands to the individual virtual device by passing the device id and command
    led_request = openapi.post(
        '/v1.0/iot-03/devices/vdevo166782136188789/commands', led_command)

    # to send the command to meter virtual device
    meter_command = {'commands': [{'code': 'switch', 'value': True}]}

    # send the commands to the individual virtual device by passing the device id and command
    meter_request = openapi.post(
        '/v1.0/iot-03/devices/vdevo166792460706753/commands', meter_command)

    # Get the status of a every single device
    # getting the switch (virtual device) status by passing the device id
    Switch_status = openapi.get(
        "/v1.0/iot-03/devices/{}/status".format(SWITCH_DEVICE_ID))

    # getting the led (virtual device) status by passing the device id
    Led_status = openapi.get(
        "/v1.0/iot-03/devices/{}/status".format(LED_DEVICE_ID))

    # getting the meter (virtual device) status by passing the device id
    Meter_status = openapi.get(
        "/v1.0/iot-03/devices/{}/status".format(METER_DEVICE_ID))

    # get the power consumed by swicth virtual devices result is in float
    switch_power = openapi.get(
        "/v1.0/iot-03/energy/electricity/device/nodes/statistics-sum?contain_childs=false&device_ids=vdevo166782136188789,&end_time=2022110820&energy_action=consume&start_time=2022110720&statistics_type=hour")

    # get the power consumed by led virtual devices result is in float
    led_power = openapi.get(
        "/v1.0/iot-03/energy/electricity/device/nodes/statistics-sum?contain_childs=false&device_ids=vdevo166782120811251,&end_time=2022110820&energy_action=consume&start_time=2022110720&statistics_type=hour")

    # get the power consumed by meter virtual devices result is in float
    electricMeter_power = openapi.get(
        "/v1.0/iot-03/energy/electricity/device/nodes/statistics-sum?contain_childs=false&device_ids=vdevo166792460706753,&end_time=2022110820&energy_action=consume&start_time=2022110720&statistics_type=hour")

    # convert to json and print
    # print(json.dumps(response))

    # delay for10 seconds
    time.sleep(10)
