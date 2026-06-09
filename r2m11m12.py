import base
import robot_move
from pybricks.tools import wait

def run():
    # podjazd do łódki
    robot_move.jazda_prosto(505, predkosc_max=600, dystans_hamowania=50, pauza=10)
    robot_move.jazda_prosto(-140, predkosc_max=700, pauza=10)
    
    # podniesienie łódki
    robot_move.jazda_prosto(280, predkosc_max=400, dystans_hamowania=10, pauza=10)
    base.lewy.run_time(-350, 500, wait=False)
    base.prawy.run_time(-600, 500)
    wait(10)
    
    # drugie uderzenie artefaktu
    robot_move.jazda_prosto(120, predkosc_max=1000, dystans_hamowania=10, pauza=10)
    robot_move.nakladka_prawa(115, predkosc=700, pauza=10)
    base.d_motor.run_target(700, 75, wait=False)
    robot_move.jazda_prosto(-700, predkosc_max=1000, pauza=0)
    robot_move.nakladka_prawa(60, 1000)
