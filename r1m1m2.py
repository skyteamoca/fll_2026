#Oksana 24.06.2026r.
import base
import robot_move
from pybricks.tools import wait

def run():
    base.d_motor.run_until_stalled(speed=200, duty_limit=55)
    #move forward for mission 1
    robot_move.jazda_prosto(700, predkosc_max=800, dystans_hamowania=125, pauza=50)
    robot_move.jazda_prosto(-210, predkosc_max=800, pauza=50)
    #about to catch the artifact in m1
    robot_move.nakladka_lewa(87, -200)
    robot_move.jazda_prosto(90, predkosc_max=750, pauza=50)
    #lifts the artifact
    robot_move.nakladka_lewa(87, 100)
    #going for mission 2
    robot_move.jazda_prosto(110, predkosc_max=500, pauza=10)
    robot_move.spin_turn_small(-40, 260, pauza=10)
    robot_move.jazda_prosto(160, predkosc_max=800, pauza=10)
    robot_move.spin_turn_small(8, 500, pauza=10)
    robot_move.spin_turn_small(-8, 500, pauza=10 )
    robot_move.jazda_prosto(-50, 500, pauza=50)
    # # catching the artfact in m2
    robot_move.nakladka_prawa(-140, predkosc=600, pauza=10)
    # #going back to the base
    robot_move.smooth_turn(-550, 100, 500)
