import RPi.GPIO as GPIO
import time

#讀取腳位
DATA_PIN = 19
#設定BCM(GPIO引腳號)
GREEN_PIN = 21
GPIO.setmode(GPIO.BCM)

#開啟下拉電阻

#下拉電阻是把電阻接地, 所以電路段開時會得到LOW 閉合得到HIGH
#上拉反過來, 把電阻接再3.3V ,所以電路斷開時會得到3.3V , 閉合 得到0

def get_data():
    #設定信號腳位, 並回傳接收狀況, 並且設定下拉電阻
    GPIO.setup(DATA_PIN,GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
    
    return GPIO.input(DATA_PIN)
    
    
def show_led(single):
    
    '當按鈕按下時,點燈'
    GPIO.setup(GREEN_PIN,GPIO.OUT)
    GPIO.output(GREEN_PIN,single)

def close_led():
    GPIO.setup(GREEN_PIN,GPIO.OUT)
    GPIO.output(GREEN_PIN,0)


def dis():
    #釋放GPIO資源
    GPIO.output(GREEN_PIN,0)
    GPIO.cleanup()
    

try:
    led_mode = False
    while True:
        Single_status = get_data()
        print(f'按鈕信號={Single_status}')
        if Single_status: #被按下
            led_mode = not led_mode
            #翻轉前次狀態 0 > 1 , 1 > 0
            show_led(led_mode)
        print(f'目前led_mode={led_mode}')
            


        
            
        
        time.sleep(0.2)
        
        

except KeyboardInterrupt:
    print('釋放GPIO腳位')
    dis()
    