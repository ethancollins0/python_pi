from flask import Flask, jsonify
import RPi.GPIO as GPIO
import time

app = Flask(__name__)

GPIO setup
GPIO.setmode(GPIO.BCM)
GPIO.setup(channel, GPIO.OUT)

set a 'channel' or pin
channel = 21

# POST route to start water
@app.route("/start_water", methods=['POST'])
def index():
    try:
        GPIO.output(channel, GPIO.HIGH)
    except KeyboardInterrupt:
        GPIO.cleanup()
    return jsonify({"start": "watering"})


# POST route to stop water pump
@app.route("/stop_water", methods=['GET'])
def handle():
    try:
        GPIO.output(channel, GPIO.LOW)
    except KeyboardInterrupt:
        GPIO.cleanup()
    return jsonify({"stop": "watering"})


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
