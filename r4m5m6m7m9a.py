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
    base.c_motor.run_angle(-1000, 175)#200
    wait(10)
    robot_move.jazda_prosto(32, predkosc_max=100)
    wait(10)
    #podniesienie dźwigu
    base.c_motor.run_angle(350, 350)#375
    wait(10)
    robot_move.jazda_prosto(-80, predkosc_max=500)
    wait(10)
    
    # skręt do stołu
    robot_move.spin_turn_v1(-130, predkosc_max=500)
    wait(100)
    base.prawy.run_time(-500, 1100, wait=False)
    base.lewy.run_time(-415, 1100)
    wait(50)
    base.prawy.run_time(500, 1000, wait=False)
    base.lewy.run_time(180, 1000)
    robot_move.jazda_prosto(575, predkosc_max=600)
    wait(100)
    robot_move.spin_turn_v1(125, predkosc_max=500)
    wait(100)
    base.d_motor.run_angle(40, -142)
    # robot_move.jazda_prosto(-50, predkosc_max=600) 
