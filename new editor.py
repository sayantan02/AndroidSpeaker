import androidhelper
import datetime
import time
import os

red= '\033[1;31m'
end= '\033[0m'
grn= '\033[1;32m'
ylo= '\033[1;33m'
blue='\033[1;34m'
cyan='\033[1;36m'
pink='\033[1;35m'


def countdown_timer():
    times = 10
    os.system('clear')
    #times = int(input("Enter times of count down: "))
    i = 1    
    #while(i !=""):
    for i in range(times):
        droid = androidhelper.Android()
        print(str(times-i),cyan+"\t","time remain"+end)
        timer = (str(times-i))
        droid.ttsSpeak(timer)
        time.sleep(1)
        i = (i-1)
countdown_timer()

print(time.strftime(grn+"your time: %H.%M.%S.00"+end))

def time_compare(hr,min,sec,msec):
    droid = androidhelper.Android()
    now_time = datetime.datetime.now()
    print('present time is :',now_time)
    cusertime = now_time.replace(hour=hr,minute=min,second=sec,microsecond=msec)
    print(red+"made by your current time,your current time is : "+end,cusertime)
    morning0 = now_time.replace(hour=0,minute=0,second=1,microsecond=1)
    morning3 = now_time.replace(hour=3,minute=0,second=0,microsecond=0)
    morning6 = now_time.replace(hour=6,minute=0,second=0,microsecond=0)
    noon12 = now_time.replace(hour=12,minute=0,second=1,microsecond=1)
    evening5 = now_time.replace(hour=16,minute=0,second=0,microsecond=0)
    night8 = now_time.replace(hour=20,minute=0,second=0,microsecond=0)
    try:
        if morning3 <= cusertime < morning6:
            print("oohh sayantan it's soo early morning.   what is the work now ?")
            droid.ttsSpeak("oh sayantan it's so early morning.   what is the work now ?")
        elif morning6 <= cusertime < noon12:
            print('good morning sayantan')
            droid.ttsSpeak('good morning sayantan')
        elif noon12 <= cusertime < evening5:
            print('good afternoon sayantan')
            droid.ttsSpeak("good afternoon sayantan")
        elif evening5 <= cusertime < night8:
            print('good evening sayantan')
            droid.ttsSpeak('good evening sayantan !')
        elif morning0 <= cusertime < morning3:
            print(ylo+"hey sayantan ! what r you doing at deep night ?, I suggest you to go and get a sleep"+end)
            droid.ttsSpeak("hey sayantan ! what r you doing at deep night ?, I suggest you to go and get a sleep")
        else:
            print('I can see my bed, I want to sleep')
            droid.ttsSpeak('I can see my bed, I want to sleep')
    except exception as e:
      print('Error found')
    
def testtime():

    droid = androidhelper.Android()
    droid.makeToast("Current Time recived")
    user_time = (time.strftime("%H:%M:%S:00"))
    #user_time = input("Enter the time value \n\n")
    hr,min,sec,msec = str(user_time).split(':')
    print(hr,min,sec,msec,type(user_time))
    print('_'*40)
    time_compare(hr=int(hr),min=int(min),sec = int(sec),msec=int(msec))
testtime()