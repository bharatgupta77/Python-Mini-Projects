import time


def countdown(time_sec):
    while time_sec >= 0:
        # divmod function is use to give quotient and remainder of 2 no. passed in parameter.
        mins, secs = divmod(time_sec, 60)
        # fomating the mins and second
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        print(timeformat, end='\r')
        time.sleep(1)
        time_sec -= 1


t = int(input("Enter the time in seconds: "))
countdown(t)
print("Times Over")
