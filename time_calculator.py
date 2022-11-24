'''1 считывание времени
2 скложить,  минуты % 60
3 если след день (next day) или больше (n days later)
optional starting day of the week parameter должен выводить день в который мы перенеслись
den= pm or am
'''
def add_time(start, duration):
    den=start.split()[1]
    start=''

    time=start.split(':')
    hours=time[0]
    minutes=start[3:4]
    hours1=duration.split(':')[0]
    minutes1=duration[3:4]
    new_time=int(hours)+int(hours1),':', int(minutes)+int(minutes1)


    return new_time
