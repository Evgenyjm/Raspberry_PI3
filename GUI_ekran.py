from tkinter import *
import tkinter as tk
from tkinter import ttk, messagebox, Radiobutton, Scale  
import RPi.GPIO as GPIO
from time import sleep
import time
import picamera

camera = picamera.PiCamera()
choices = ['off', 'auto', 'sunlight','cloudy','shade','tungsten','fluorescent','incandescent','flash','horizon']
effects = ['none','negative','solarize','sketch','denoise','emboss','oilpaint','hatch','gpen','pastel','watercolor','film','blur','saturation','colorswap','washedout','posterise','colorpoint','colorbalance','cartoon','deinterlace1','deinterlace2']

def CameraON():
    camera.preview_fullscreen=False
    camera.preview_window=(0, 0, 200, 150)
    camera.resolution=(300,200)
    camera.start_preview()
    
def CameraOFF():
    camera.stop_preview()

def UpdateBrightness(value):
    camera.brightness = int(value)
    
def UpdateContrast(value):
    camera.contrast = int(value)
    
def UpdateSaturation(value):
    camera.saturation = int(value)

def SetAWB(var):
    camera.awb_mode = var

def SetEFFECTS(var):
    camera.image_effect = var

def Zoom(var):
    x = float("0."+var)
    camera.zoom = (0.5,0.5,x,x)
    
  
def get_val_motion(event):
    s1 = scal.get()
    print("Motion Number",str(s1))
    sld = s1/15
    pwm.ChangeDutyCycle(float(sld))
def left_motor():  
    for i in range(0,24):
        GPIO.output(36, GPIO.HIGH)
        GPIO.output(38, GPIO.LOW)
        GPIO.output(40, GPIO.LOW)
        GPIO.output(37, GPIO.HIGH)
        time.sleep(delay)
        # Шаг 2.
        GPIO.output(36, GPIO.HIGH)
        GPIO.output(38, GPIO.HIGH)
        GPIO.output(40, GPIO.LOW)
        GPIO.output(37, GPIO.LOW)
        time.sleep(delay)
        # Шаг 3.
        GPIO.output(36, GPIO.LOW)
        GPIO.output(38, GPIO.HIGH)
        GPIO.output(40, GPIO.HIGH)
        GPIO.output(37, GPIO.LOW)
        time.sleep(delay)
        # Шаг 4.
        GPIO.output(36, GPIO.LOW)
        GPIO.output(38, GPIO.LOW)
        GPIO.output(40, GPIO.HIGH)
        GPIO.output(37, GPIO.HIGH)
        time.sleep(delay)
def right_motor():  
    for i in range(0,24):
        GPIO.output(36, GPIO.LOW)
        GPIO.output(38, GPIO.LOW)
        GPIO.output(40, GPIO.HIGH)
        GPIO.output(37, GPIO.HIGH)
        time.sleep(delay)
        # Шаг 2.
        GPIO.output(36, GPIO.LOW)
        GPIO.output(38, GPIO.HIGH)
        GPIO.output(40, GPIO.HIGH)
        GPIO.output(37, GPIO.LOW)
        time.sleep(delay)
        # Шаг 3.
        GPIO.output(36, GPIO.HIGH)
        GPIO.output(38, GPIO.HIGH)
        GPIO.output(40, GPIO.LOW)
        GPIO.output(37, GPIO.LOW)
        time.sleep(delay)
        # Шаг 4.
        GPIO.output(36, GPIO.HIGH)
        GPIO.output(38, GPIO.LOW)
        GPIO.output(40, GPIO.LOW)
        GPIO.output(37, GPIO.HIGH)
        time.sleep(delay)  
def but_onoff(event, button):
    if button == "OFF":
        but["text"] = "ON"
        but['bg'] = '#FFFFFF'
        but['fg'] = '#C72828'
        but['activeforeground'] = "red"
        GPIO.setup(33, GPIO.HIGH)
    else:
        but["text"] = "OFF"
        but['bg'] = '#C72828'
        but['fg'] = '#FFFFFF'
        but['activeforeground'] = "red"
        GPIO.setup(33, GPIO.LOW)
def on_closing():
    if messagebox.askokcancel("Вихід", "Закрити програму?"):
        window.destroy()
        camera.stop_preview()
        camera.close()
GPIO.setmode(GPIO.BOARD)
GPIO.setup(35, GPIO.OUT)
pwm = GPIO.PWM (35, 50)
GPIO.setup(33, GPIO.OUT)
pwm.start (0)
in2 = 36
in1 = 37
in3 = 38
in4 = 40
delay = 0.002

GPIO.setup(36, GPIO.OUT)
GPIO.setup(37, GPIO.OUT)
GPIO.setup(38, GPIO.OUT)
GPIO.setup(40, GPIO.OUT)
window = Tk()  
window.title("Добро пожаловать")  
window.geometry('600x250')  
window.configure(bg='#ffffff')
window.protocol("WM_DELETE_WINDOW", on_closing)
tab_control = ttk.Notebook(window)
tab1 = ttk.Frame(tab_control)  
tab2 = ttk.Frame(tab_control)
tab3 = ttk.Frame(tab_control)
tab4 = ttk.Frame(tab_control) 
tab_control.add(tab1, text='Світлодіод')  
tab_control.add(tab2, text='Сервопривід')
tab_control.add(tab3, text='Двигун')
tab_control.add(tab4, text='Камера')
lbl1 = Label(tab1, text='Включити лампу', font=("Arial Bold", 20))
but = Button(tab1, text="OFF", width=15, height=5, bg="#C72828", fg="#000000", borderwidth="4", relief="solid", font=("Arial Bold", 15))
but.bind("<Button-1>", lambda event: but_onoff(event, but["text"]))
lbl1.pack(side="top",  expand=1) 
but.pack(side="bottom",  expand=1)

lbl2 = Label(tab2, text='Керування сервоприводом', font=("Arial Bold", 15))
lbl2.pack(side="top",  expand=1)
scal = Scale(tab2,orient=HORIZONTAL, from_=0, to=180, tickinterval=20)
scal.bind("<B1-Motion>",get_val_motion)
scal.pack(side="top",  expand=1, fill=X, padx=10)

lbl3 = Label(tab3, text='Керування двигуном', font=("Arial Bold", 15))
motor_1 = Button(tab3, text="Left", width=7, height=5, bg="#C72828", fg="#FFFFFF", borderwidth="1", relief="solid", padx=10, pady=10, font=("Arial Bold", 12), command=left_motor)
motor_2 = Button(tab3, text="Right", width=7, height=5, bg="#C72828", fg="#FFFFFF", borderwidth="1", relief="solid", padx=10, pady=10, font=("Arial Bold", 12), command=right_motor)
lbl3.pack(side="top",  expand=1)
motor_1.pack(side="left",  expand=1, pady=10)
motor_2.pack(side="left",  expand=1, pady=10)


on_cam = Button(tab4, text='Start Camera', padx=10, pady=10, bg="#C72828", fg="#FFFFFF", borderwidth="1", relief="solid", command=CameraON)
off_cam = Button(tab4, text='Kill Camera', padx=10, pady=10, bg="#C72828", fg="#FFFFFF", borderwidth="1", relief="solid", command=CameraOFF)
brg_scale = Scale(tab4, from_=30, to=100, orient=tk.HORIZONTAL, label = "Яскравість", command=UpdateBrightness)
cntrst_scale = Scale(tab4, from_=-100, to=100, orient=tk.HORIZONTAL, label = "Контраст", command=UpdateContrast)
saturation_scale = Scale(tab4, from_=-100, to=100, orient=tk.HORIZONTAL, label = "Насиченість", command=UpdateSaturation)
zoom_scale = Scale(tab4, from_=10, to=99, orient=tk.HORIZONTAL, label = "Zoom", command=Zoom)
on_cam.grid(row=1, column = 1)
off_cam.grid(row=1, column = 2)
brg_scale.grid(row=2,column=1)
cntrst_scale.grid(row=2,column=2)
saturation_scale.grid(row=2,column=3)
zoom_scale.grid(row=3,column=1)

AWB_Var = tk.StringVar(tab4)
AWB_Var.set(choices[0]) 
AWB_Option = tk.OptionMenu(tab4, AWB_Var, *choices, command=SetAWB).grid(row=3,column=2)

EFFECT_Var = tk.StringVar(tab4)
EFFECT_Var.set(effects[0]) 
EFFECT_Option = tk.OptionMenu(tab4, EFFECT_Var, *effects, command=SetEFFECTS).grid(row=3,column=3)

tab_control.pack(expand=1, fill='both')  
window.mainloop()