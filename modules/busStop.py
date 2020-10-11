import requests
from . import tts_module as tts
#import RPi.GPIO as GPIO
bus_stop_name = []
bus_stop_id = []
ind = 0
curr_stop = ""
def selectStation(bus_num, curr_stn):
    global bus_stop_name
    global curr_stop
    global ind
    url = 'http://114.70.21.89:1337/api/route-station/' + str(bus_num)
    response = requests.get(url)
    res = response.json()
    for i in res:
        bus_stop_name.append(i['stn_name'])
        bus_stop_id.append(i['stn_id'])
    print(curr_stn)
    curr_stop = curr_stn
    ind = bus_stop_name.index(curr_stn)
    curr_stop = bus_stop_name[ind]
    #print(ind)

def move_right():
    global ind
    global curr_stop
    if ind < len(bus_stop_name) - 1:
        ind += 1
    else:
        print("종착지입니다.")
        ind = 0
    curr_stop = bus_stop_name[ind]
    print(curr_stop)
    tts.tts_input(curr_stop+"입니다아.")

def move_left():
    global ind
    global curr_stop
    if ind > 0:
        ind -= 1
    else:
        print("종착지입니다.")
        ind = len(bus_stop_name) - 1
    curr_stop = bus_stop_name[ind]
    print(curr_stop)
    tts.tts_input(curr_stop+"입니다아.")
'''
if __name__ == '__main__':
    selectStation(143, '신동중학교')
    #setup()
    print(curr_stop)
    print(bus_stop_name)
    print(len(bus_stop_name))
    move_right()
    print(ind)
    move_left()

'''
