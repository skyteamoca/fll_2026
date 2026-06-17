#Oksana, 17.06.2026r
import base
import robot_move
from pybricks.tools import wait

def run():
    base.d_motor.run_until_stalled(speed=200, duty_limit=55)
    #move forward for mission 1
    robot_move.jazda_prosto(700, predkosc_max=800, dystans_hamowania=125, pauza=50)
    robot_move.jazda_prosto(-210, predkosc_max=800, pauza=50)
    #about to catch the artifact in m1
    robot_move.nakladka_lewa(91, -200)
    robot_move.jazda_prosto(80, predkosc_max=750, pauza=50)
    #lifts the artifact
    robot_move.nakladka_lewa(100, 100)
    #going for mission 2
    robot_move.jazda_prosto(80, predkosc_max=500, pauza=10)
    robot_move.spin_turn_small(-40.5, 260, pauza=10)
    robot_move.jazda_prosto(25, predkosc_max=800, pauza=10)
    #catching the artfact in m2
    robot_move.nakladka_prawa(-185, predkosc=600, pauza=10)
    #base.c_motor.run_until_stalled(speed=-600, duty_limit=70)
    robot_move.spin_turn_small(4, 100, pauza=50)
    robot_move.jazda_prosto(167, predkosc_max=500, pauza=10)
    robot_move.spin_turn_small(7, 100, pauza=10)
    robot_move.spin_turn_small(-10, 100, pauza=10)
    #going back to the base
    robot_move.smooth_turn(-550, 100, 500)
