#Matt
import base
import robot_move
from pybricks.tools import wait

def run():
    robot_move.jazda_prosto(700, predkosc_max=800, dystans_hamowania=125, pauza=50)
    robot_move.jazda_prosto(-210, predkosc_max=800, pauza=50)
    robot_move.nakladka_lewa(93, -200)
    robot_move.jazda_prosto(80, predkosc_max=750, pauza=50)
    robot_move.nakladka_lewa(100, 100)
    robot_move.jazda_prosto(80, predkosc_max=500, pauza=10)
    robot_move.spin_turn_small(-41, 260, pauza=10)
    robot_move.jazda_prosto(25, predkosc_max=800, pauza=10)
    robot_move.nakladka_prawa(-185, predkosc=600, pauza=10)
    robot_move.spin_turn_small(4, 100, pauza=50)
    robot_move.jazda_prosto(165, predkosc_max=500, pauza=10)
    robot_move.spin_turn_small(7, 100, pauza=10)
    robot_move.spin_turn_small(-10, 100, pauza=10)
    robot_move.smooth_turn(-550, 100, 500)
