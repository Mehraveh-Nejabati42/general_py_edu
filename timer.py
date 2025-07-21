import turtle,time
t=turtle.Turtle()
for h in range(0,24):
    for m in range(0,60):
        for s in range(0,60):
            clock=f"{h}:{m}:{s}"
            t.write(clock,font=('segoe print',60))
            time.sleep(1)
            t.clear()
