#Orest 2.07.26
import base
import robot_move
from pybricks.tools import wait

def run():
    #straight
    robot_move.jazda_prosto(dystans_mm=, predkosc_max=, pauza=)
    #inputing the data to the function: how many milimeters the robot has to go, the speed and the 
    #pause after
    robot_move.spin_turn_v2(kat_stopnie=,predkosc_max=,predkosc_min=,pauza=)
    #spin turn data: the angle we need the robot to move, max speed during that, minimum speed 
    #and the pause
    robot_move.smooth_turn(promien_mm=,kat_stopnie=,predkosc=,pauza=)
    #smooth turn data; radius, angle, speed and the pause
