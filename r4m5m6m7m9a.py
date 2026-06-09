import base
import robot_move
from pybricks.tools import wait

def run():
    wait(10)
    base.c_motor.run_angle(-1000, 200, wait=False)
    robot_move.jazda_prosto(675, predkosc_max=800)
    wait(10)
    robot_move.spin_turn_v1(50, predkosc_max=800, Kp=7)
    wait(10)
    robot_move.spin_turn_small(-13, predkosc_max=500)
    wait(10)
    base.c_motor.run_angle(-1000, 200)
    wait(10)
    robot_move.jazda_prosto(32, predkosc_max=100)
    wait(10)
