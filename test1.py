import RPi.GPIO as GPIO
import time

#讀取腳位
DATA_PIN = 19
#設定BCM(GPIO引腳號)
GREEN_PIN = 21
GPIO.setmode(GPIO.BCM)
GPIO.setup(GREEN_PIN,GPIO.OUT)
#開啟下拉電阻
GPIO.setup(DATA_PIN,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
#下拉電阻是把電阻接地, 所以電路段開時會得到LOW 閉合得到HIGH
#上拉反過來, 把電阻接再3.3V ,所以電路斷開時會得到3.3V , 閉合 得到0
try:
    while True:
        button_status = GPIO.input(DATA_PIN)
        print(f'按鈕信號={button_status}')
        
        if button_status:
            GPIO.output(GREEN_PIN,1)
        else:
            GPIO.output(GREEN_PIN,0)
        time.sleep(0.1)

except KeyboardInterrupt:
    print('釋放腳位')
    GPIO.output(GREEN_PIN,0)
    GPIO.cleanup()