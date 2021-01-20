

#  	appCamPanTilt.py
#  	Streaming video with Flask based on tutorial ==> https://blog.miguelgrinberg.com/post/video-streaming-with-flask
import os
from time import sleep
from flask import Flask, render_template, request, Response
import RPi.GPIO as GPIO
import time
# Raspberry Pi camera module (requires picamera package from Miguel Grinberg)
from camera_pi import Camera

app = Flask(__name__)

# Global variables definition and initialization
global slider
controlServo = 90
sliderr = 90
slider = 6
delay = 0.002


@app.route('/')
def index():
    """Video streaming home page."""
 
    templateData = {
      'controlServo'	: controlServo,
      #'sliderr'         : sliderr
      'sliderr'			: sliderr
      #'tiltServoAngle'	: tiltServoAngle
	}
    return render_template('index.html', **templateData)


def gen(camera):
    """Video streaming generator function."""
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')


@app.route('/video_feed')
def video_feed():
    """Video streaming route. Put this in the src attribute of an img tag."""
    return Response(gen(Camera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/bottombtn')
def bottombtn():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(16, GPIO.OUT)
    pwm = GPIO.PWM (16, 50)
    pwm.start (0)
    global slider
    if slider >= 0 and slider <= 12:
        slider +=1
        pwm.ChangeDutyCycle(float(slider))
        sleep(0.1)
    return "nothing"
@app.route('/topbtn')
def topbtn():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(16, GPIO.OUT)
    pwm = GPIO.PWM (16, 50)
    pwm.start (0)
    global slider
    if slider >= 0 and slider <= 12:
        slider -=1
        pwm.ChangeDutyCycle(float(slider))
        sleep(0.1)
    return "nothing"
@app.route('/leftsbtn')
def leftsbtn():
    GPIO.cleanup ()
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(12, GPIO.OUT)
    GPIO.setup(11, GPIO.OUT)
    GPIO.setup(13, GPIO.OUT)
    GPIO.setup(15, GPIO.OUT)
    for i in range(0,24):

        GPIO.output(11, GPIO.HIGH)
        GPIO.output(12, GPIO.LOW)
        GPIO.output(13, GPIO.LOW)
        GPIO.output(15, GPIO.HIGH)
        time.sleep(delay)
        # Шаг 2.
        GPIO.output(11, GPIO.HIGH)
        GPIO.output(12, GPIO.HIGH)
        GPIO.output(13, GPIO.LOW)
        GPIO.output(15, GPIO.LOW)
        time.sleep(delay)
        # Шаг 3.
        GPIO.output(11, GPIO.LOW)
        GPIO.output(12, GPIO.HIGH)
        GPIO.output(13, GPIO.HIGH)
        GPIO.output(15, GPIO.LOW)
        time.sleep(delay)
        # Шаг 4.
        GPIO.output(11, GPIO.LOW)
        GPIO.output(12, GPIO.LOW)
        GPIO.output(13, GPIO.HIGH)
        GPIO.output(15, GPIO.HIGH)
        time.sleep(delay)
    return "nothing"

@app.route('/rightsbtn')
def rightsbtn():
    GPIO.cleanup ()
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(12, GPIO.OUT)
    GPIO.setup(11, GPIO.OUT)
    GPIO.setup(13, GPIO.OUT)
    GPIO.setup(15, GPIO.OUT)
    for i in range(0,24):
        
        GPIO.output(11, GPIO.LOW)
        GPIO.output(12, GPIO.LOW)
        GPIO.output(13, GPIO.HIGH)
        GPIO.output(15, GPIO.HIGH)
        time.sleep(delay)
        # Шаг 2.
        GPIO.output(11, GPIO.LOW)
        GPIO.output(12, GPIO.HIGH)
        GPIO.output(13, GPIO.HIGH)
        GPIO.output(15, GPIO.LOW)
        time.sleep(delay)
        # Шаг 3.
        GPIO.output(11, GPIO.HIGH)
        GPIO.output(12, GPIO.HIGH)
        GPIO.output(13, GPIO.LOW)
        GPIO.output(15, GPIO.LOW)
        time.sleep(delay)
        # Шаг 4.
        GPIO.output(11, GPIO.HIGH)
        GPIO.output(12, GPIO.LOW)
        GPIO.output(13, GPIO.LOW)
        GPIO.output(15, GPIO.HIGH)
        time.sleep(delay)
    return "nothing"


if __name__ == '__main__':
    app.run(host='192.168.1.4', port =80, debug=True, threaded=True)
