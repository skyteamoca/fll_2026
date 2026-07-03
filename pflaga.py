#Oksana 24.06.2026r.
import base
import robot_move
from pybricks.tools import wait

def run():
    # base.d_motor.run_until_stalled(speed=200, duty_limit=55)
    # #move forward for mission 1
    base.c_motor.run_angle(270,200,wait=False)
    robot_move.jazda_prosto(500, predkosc_max=800, dystans_hamowania=125, pauza=50)
    robot_move.smooth_turn(240,45,800,pauza=50)
    robot_move.jazda_prosto(300, predkosc_max=800, dystans_hamowania=50, pauza=50)
    base.c_motor.run_angle(230,-1100,wait=False)
    robot_move.spin_turn_v1(32,1000)
    base.d_motor.run_angle(-1100,100)

