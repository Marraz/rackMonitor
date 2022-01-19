import smbus2
import bme280
from flask import Flask, render_template

port = 1
address = 0x77
bus = smbus2.SMBus(port)

calibration_params = bme280.load_calibration_params(bus, address)

# the sample method will take a single reading and return a
# compensated_reading object
data = bme280.sample(bus, address, calibration_params)

# the compensated_reading class has the following attributes
print("id " + str(data.id))
print(data.timestamp)
print(data.temperature)
print(data.pressure)
print(data.humidity)

# there is a handy string representation too
print(data)


app = Flask(__name__)

@app.route('/')
def index():
	return tempsensor()
@app.route('/tempsensor')
def tempsensor():
	data = bme280.sample(bus, address, calibration_params)
	return render_template('tempsensor.html', temperature=data.temperature, pressure=data.pressure,humidity=data.humidity)

if __name__ == '__main__':
	app.run(debug=False, host='0.0.0.0')