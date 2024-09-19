#!/usr/bin/python3
import ds18b20_therm

#roof_temp = ds18b20_therm.DS18B20("28-0517a22496ff")
cabinet_temp = ds18b20_therm.DS18B20("28-0517a25effff")
roof_temp = ds18b20_therm.DS18B20("28-39ff691f64ff")

print("Roof Temp:     ", roof_temp.read_temp())
print("Cabinet Temp: ", cabinet_temp.read_temp())
#print("Attic Temp:    ", attic_temp.read_temp())


