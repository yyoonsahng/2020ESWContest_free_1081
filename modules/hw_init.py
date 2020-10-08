# -*- coding: utf-8 -*-
"""
Created on Thu Aug 20 01:33:57 2020
@author: tarah
"""
#37.5663° N, 126.9779° E

import RPi.GPIO as GPIO
#import tts
#import stt

SWITCH_PREV=21 #이전
SWITCH_NEXT=25 #다음
SWITCH_SAVE=20 #저장
SWITCH_DONE=26 #확인

SWITCH_TTS=13
br = [17, 18, 27, 22, 23, 24]


def init(switch_prev_callback, switch_next_callback,  switch_save_callback, switch_done_callback, switch_tts_callback):
    GPIO.setmode(GPIO.BCM)
    for i in range(0, 6):
        GPIO.setup(br[i], GPIO.OUT)
    GPIO.setup(16, GPIO.OUT)
    GPIO.output(16, GPIO.HIGH)
    # initialize pins
    GPIO.setup(SWITCH_PREV, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(SWITCH_NEXT, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(SWITCH_SAVE, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(SWITCH_DONE, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    GPIO.setup(SWITCH_TTS, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    # add eventHandler
    GPIO.add_event_detect(SWITCH_PREV, GPIO.RISING, callback=switch_prev_callback, bouncetime = 200)
    GPIO.add_event_detect(SWITCH_NEXT, GPIO.RISING, callback=switch_next_callback, bouncetime = 200)
    GPIO.add_event_detect(SWITCH_SAVE, GPIO.RISING, callback=switch_save_callback, bouncetime = 500)
    GPIO.add_event_detect(SWITCH_DONE, GPIO.RISING, callback=switch_done_callback, bouncetime = 200)

    GPIO.add_event_detect(SWITCH_TTS, GPIO.RISING, callback=switch_tts_callback, bouncetime = 200)
def destroy():
    GPIO.cleanup()
    
def gps():
    pos_x="127.0701692006"
    pos_y="37.5385662456"
    
    return pos_x,pos_y