#Orest 30.06.26
import base
import robot_move
from pybricks.tools import wait

def run():
    robot_move.jazda_prosto(900, predkosc_max=1000,dystans_hamowania=0,pauza=50)
    robot_move.jazda_prosto(-200, predkosc_max=1000)
