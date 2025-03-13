from irrecvdata import irGetCMD
from machine import UART, Pin

uart0 = UART(0, baudrate=115200, tx=Pin(0), rx=Pin(1))

recvPin = irGetCMD(8)
while True:
    try:
        irValue = recvPin.ir_read()
        if irValue:
            print(irValue)
            uart0.write(irValue)
    except Exception as e:
        print(e)
        pass