from statemachine import StateMachine

def timerrood(time, car):    
    if car > 0:
        time = time - car
        
    if time <= 0:
        newState = "groen"
        time = 30
    else:
        newState = "rood"
        time = time - 1
    
    

    return (newState, time, car)


def timergroen(time,car):
    if time <= 0:
        newState = "rood"
        time = 30
    else:
        newState = "groen"
        time = time - 1

    if (car > 0):
        car = car - 1

    return (newState, time, car)



if __name__== "__main__":
    m = StateMachine()
    m.add_state("rood", timerrood, end_state=1)
    m.add_state("groen", timergroen)
    m.set_start("rood")
    m.run(30, 0)
    

# https://www.python-course.eu/finite_state_machine.php