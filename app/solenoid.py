import pyfirmata

try:
    sel = pyfirmata.Arduino('/dev/ttyACM0')
    # board = pyfirmata.Arduino('YOUR_PORT_HERE')
    print("Communication Successfully started")

    def solenoid(p):
        if str(p) == '1' :
            sel.digital[7].write(1)
        else:
            sel.digital[7].write(0)
            

except Exception as e:
    print(e)

solenoid(1)