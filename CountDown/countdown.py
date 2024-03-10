import time

def countdown(t):
    while t:
        #divmod(a,b) --> (a//b, a%b)
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        # 'r' carriage return, enxt line printed will overwite the previous one
        print(timer, end = '\r')
        #time.sleep() add delay in the execution of a program
        time.sleep(1)
        t -= 1
    print('count down complete!')
    
t = input('enter the time in sec: ')
    
countdown(int(t))
        
