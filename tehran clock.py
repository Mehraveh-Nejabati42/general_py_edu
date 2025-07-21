import time, turtle
t=turtle.Turtle()
a=time.localtime()
saat=a.tm_hour
dagigeh=a.tm_min
sanieh=a.tm_sec
t.penup()
t.goto(-200,0)
t.pendown()
for h in range(saat,24):
    for m in range(dagigeh,60):
        for s in range(sanieh,60):
            clock=f"{h}:{m}:{s}"
            t.write(clock,font=('segoe print',60))
            time.sleep(1)
            t.clear()