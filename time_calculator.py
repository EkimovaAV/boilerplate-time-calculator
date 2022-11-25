'''1 считывание времени
2 скложить,  минуты % 60
3 если след день (next day) или больше (n days later)
optional starting day of the week parameter должен выводить день в который мы перенеслись
polovina= pm or am
'''
def add_time(start, duration, day=None):
    polovina=start.split()[1]
    nedelya = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    time=start.split(':')
    hours=int(time[0])
    minutes=time[1][0:2]
    hours1=duration.split(':')[0]
    minutes1=duration.split(':')[1]
    sec= int(minutes)+int(minutes1)
    n=0
    if polovina == "PM":
        hours += 12
    chas=int(hours)+int(hours1)
    day_string=None
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
            day_string = "(next day)"
        if n>1:
            day_string= f"({n} days later)"
    if chas<12:
        polovina="AM"
        if chas == 0:
            chas = 12
    elif chas > 12:
        polovina = "PM"
        chas -= 12
    elif chas == 12:
        polovina = "PM"
    if day != None:
        new_day = day.lower().capitalize()
        day_index = nedelya.index(new_day)
        new_day = nedelya[(day_index + n) % len(nedelya)]
        if n!=0:
            return f"{chas}:{sec} {polovina}, {new_day} {day_string}"
        else:
            return f"{chas}:{sec} {polovina}, {new_day}"
    else:
      new_day = None
    new_time = f"{chas}:{sec} {polovina}"
    if new_day != None:
      new_time = new_time + ", " + new_day
    if day_string != None:
      new_time = new_time + " " + day_string
    return new_time
