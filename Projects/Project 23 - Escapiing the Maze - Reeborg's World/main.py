def check():
    if at_goal()==False:
        if wall_on_right():
            if front_is_clear():
                move()
                check()
            else:
                turn_left()
                check()
        else:
            turn_left()
            turn_left()
            turn_left()
            move()
            check()
    else:
        done()

check()