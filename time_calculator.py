'''1 считывание времени
2 скложить,  минуты % 60
3 если след день (next day) или больше (n days later)
optional starting day of the week parameter должен выводить день в который мы перенеслись
polovina= pm or am
'''
def add_time(start, duration):
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
    if chas >=24:
        n = chas // 24
        chas%= 24
        return f"{chas}:{sec} {polovina} ({n} days later)"
    if chas> 15:
        chas-=chas-12
    if chas >=12:


        polovina='PM'



    new_time=f"{chas}:{sec} {polovina}"
    return new_time
