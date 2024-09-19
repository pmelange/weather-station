#!/usr/bin/python3
import interrupt_client, MCP342X, wind_direction, HTU21D, bmp085, tgs2600, ds18b20_therm
import database 

pressure = bmp085.BMP085()
cabinet_temp = ds18b20_therm.DS18B20("28-0517a25effff")
roof_temp = ds18b20_therm.DS18B20("28-39ff691f64ff")
air_qual = tgs2600.TGS2600(adc_channel = 0)
humidity = HTU21D.HTU21D()
wind_dir = wind_direction.wind_direction(adc_channel = 0, config_file="wind_direction.json")
interrupts = interrupt_client.interrupt_client(port = 49501)

sch8_db = database.sch8_weather_database()


roof_temp_val = roof_temp.read_temp()
cabinet_temp_val = cabinet_temp.read_temp()
air_qual_val = air_qual.get_value()
pressure_val = pressure.get_pressure()
humidity_val = humidity.read_humidity()
wind_average_val = wind_dir.get_value(10) #ten seconds
wind_dir_val = interrupts.get_wind()
wind_gust_val = interrupts.get_wind_gust()
rain_val = interrupts.get_rain()

print("Inserting...")

sch8_db.insert(roof_temp_val, cabinet_temp_val, air_qual_val, pressure_val, humidity_val, wind_average_val, wind_dir_val, wind_gust_val, rain_val)

print("done")

interrupts.reset()
