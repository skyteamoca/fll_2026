import base
import robot_move
from pybricks.tools import wait

def misja_m8():
    wait(100)
    robot_move.jazda_prosto(420, predkosc_max=800)
    wait(50)
    for _ in range(2):
        base.c_motor.run_angle(1000, 130)
        wait(50)
        base.c_motor.run_angle(-1000, 130)
        wait(50)
    robot_move.jazda_prosto(-450, predkosc_max=800)
