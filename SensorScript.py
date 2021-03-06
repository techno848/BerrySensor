# assembler for all the script data
def assembler(dt, my_list, user_id):

    # converting received values to float
    humidity = float(my_list[0])
    humidity_decimal = float(my_list[1])/10

    temperature = float(my_list[2])
    temperature_decimal = float(my_list[3])/10

    # adding the decimal bits
    humidity = humidity + humidity_decimal
    temperature = temperature + temperature_decimal

    # formatting data to be sent to the bluetooth device
    format_string = '{} SensorID={}, temperature={}, humidity={} \n'.format(dt.now, user_id, temperature, humidity)


    return format_string
