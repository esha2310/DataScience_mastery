sensor_readings = [10.3, 10.7, 5, 6.9, 11.7, 12.7]
print("original data:", sensor_readings)
print("first reading:", sensor_readings[0])
print("first reading:", sensor_readings[2])
sensor_readings.append(13.5)
print("after adding new data:", sensor_readings)

max_value = max( sensor_readings)
min_value = min( sensor_readings)
total_value_count = len( sensor_readings)
print("maximum reading:", max_value)
print("minimum reading:", min_value)
print("total value count:", total_value_count)
