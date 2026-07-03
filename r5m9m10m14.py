#Greg&Matt 03.07
import base
import robot_move
from pybricks.tools import wait

def run():

    robot_move.jazda_prosto(460, predkosc_max=1100, dystans_hamowania=100, pauza=30)
    robot_move.spin_turn_v1(-125, predkosc_max=400,pauza=50)
    robot_move.jazda_prosto(260, predkosc_max=1100, pauza=10)#stragan
    robot_move.spin_turn_v1(33,predkosc_max=400)
    robot_move.jazda_prosto(-10, 1000)
    #zabranie beczki

    robot_move.nakladka_prawa(-360, 500)#wyjęcie beczki
    robot_move.spin_turn_v1(-35, 400, pauza=10)
    robot_move.jazda_prosto(120, predkosc_max=900)
    robot_move.spin_turn_v1(37, predkosc_max=400, pauza=10)
    robot_move.jazda_prosto(380, 1200, pauza=10)
    #turn_seal
    robot_move.spin_turn_v1(38, predkosc_max=400, pauza=10)
    robot_move.jazda_prosto(90, predkosc_max=1100, pauza=10)
    #puszczenie beczki
    robot_move.spin_turn_v1(-5, 400)
    #wyjęcie nakładki z beczki
    robot_move.nakladka_prawa(300, predkosc=800)
    #podjazd do przodu i opuszczenie nakładki z artefaktami
    robot_move.jazda_prosto(100, 300, pauza=50)
    robot_move.nakladka_lewa(90, 200)
