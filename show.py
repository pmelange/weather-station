#!/usr/bin/python3
import interrupt_client, MCP342X, wind_direction, HTU21D, bmp085, tgs2600, ds18b20_therm

pressure = bmp085.BMP085()
cabinet_temp = ds18b20_therm.DS18B20("28-0517a25effff")
roof_temp = ds18b20_therm.DS18B20("28-39ff691f64ff")
air_qual = tgs2600.TGS2600(adc_channel = 0)
humidity = HTU21D.HTU21D()
wind_dir = wind_direction.wind_direction(adc_channel = 0, config_file="wind_direction.json")
interrupts = interrupt_client.interrupt_client(port = 49501)

#wind_average = wind_dir.get_value(10) #ten seconds

print("Roof Temp:     ", roof_temp.read_temp())
print("Cabinet Temp:  ", cabinet_temp.read_temp())
print("Humidity Temp: ", humidity.read_temperature())
print("Pressure Temp: ", pressure.get_temperature())
print("Air Quail:     ", air_qual.get_value())
print("Pressure:      ", pressure.get_pressure())
print("Humidity:      ", humidity.read_humidity())
print("Wind:          ", interrupts.get_wind())
print("Gust:          ", interrupts.get_wind_gust())
print("Rain:          ", interrupts.get_rain())

#interrupts.reset()
