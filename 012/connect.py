import sys
import serial

def connect(path='/dev/ttyACM'): #default path is for linux
    for i in range(0, 10):
        try:
            s = serial.Serial('{0}{1}'.format(path,i))
            print('Connected')
            return s
        
        except:
            continue
        
    print('No Device Found')

def connect_any():
    p = sys.platform
    if "lin" in p:
        s = connect()
        print('Well done for usuing Linux.')
    elif "win" in p:
        s = connect('COM')
        print('Boooo! Windows.')
    #elif "dar" in p:
        #print('mac')
    
    return s
