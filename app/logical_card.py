import serial

def cek_card():
    try :
        arduino = serial.Serial(port='/dev/ttyACM0', baudrate=9600, timeout=.1)
        while True:
            data = arduino.readline()
            data = data.decode('utf-8')
            if 'Card UID' in data:
                data = data.replace("\r\n","")
                return data

    except:
        return "alat error"

