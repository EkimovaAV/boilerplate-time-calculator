'''1 считывание времени
2 скложить,  минуты % 60
3 если след день (next day) или больше (n days later)
optional starting day of the week parameter должен выводить день в который мы перенеслись
polovina= pm or am
'''
def add_time(start, duration, d=None):
    polovina=start.split()[1]


    time=start.split(':')
    hours=time[0]
    minutes=time[1][0:2]
    hours1=duration.split(':')[0]
    minutes1=duration.split(':')[1]
    sec= int(minutes)+int(minutes1)
    chas=int(hours)+int(hours1)
    if sec > 60:
        chas+=sec//60
        sec%=60
    if sec<10:
        sec='0'+str(sec)
        #00
    if chas >=24:
        n = chas // 24
        chas%= 12
        if n==1:
            return f"{chas}:{sec} {polovina} (next day)"
        return f"{chas}:{sec} {polovina} ({n} days later)"
        chas-=chas-12
    if chas >= 12:
        if polovina=='PM':
            polovina='AM'
        else:
            polovina='PM'
    if chas>12:
        chas-=12


    new_time=f"{chas}:{sec} {polovina}"
    return new_time
