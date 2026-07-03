#Orest 3.07.26
import base
import robot_move
from pybricks.tools import wait

def run():
    #straight
    robot_move.jazda_prosto(dystans_mm=100, predkosc_max=100, pauza=50)
    #inputing the data to the function: how many milimeters the robot has to go, the speed and the 
    #pause after
    robot_move.spin_turn_v1(kat_stopnie=90,predkosc_max=100, pauza=50)
    #spin turn data: the angle we need the robot to move, max speed during that and the pause
    robot_move.smooth_turn(promien_mm=200,kat_stopnie=90,predkosc=200,pauza=50)
    #smooth turn data; radius, angle, speed and the pause
