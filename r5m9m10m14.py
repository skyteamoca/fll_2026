import base
import robot_move
from pybricks.tools import wait

def run():
    # wait(100)
    # base.c_motor.run_angle(500, -1000, wait=False)
    # robot_move.jazda_prosto(280, predkosc_max=700, pauza=10)
    # robot_move.spin_turn_v1(-105, predkosc_max=500, pauza=10)
    # robot_move.jazda_prosto(250, predkosc_max=700, pauza=10)
    
    # # skręt do artefaktu
    # base.c_motor.run_angle(500, 1000, wait=False)
    # robot_move.spin_turn_v1(40, predkosc_max=800, pauza=10)
    
    # # wyciąganie artefaktu
    # robot_move.jazda_prosto(115, predkosc_max=800, pauza=100)
    # base.c_motor.run_angle(500, -1000)
    # wait(10)
    # base.prawy.run_time(600, 2500, wait=False)
    # base.lewy.run_time(545, 2500)
    # wait(10)
    # base.prawy.run_angle(-500, 115)
    # wait(10)
    # base.d_motor.run_angle(50, 200)
    # wait(10)
    # robot_move.jazda_prosto(-20, predkosc_max=200, pauza=10)
    # robot_move.spin_turn_small(10, 50)

    robot_move.jazda_prosto(460, predkosc_max=1100, dystans_hamowania=100, pauza=30)
    robot_move.spin_turn_v1(-125, predkosc_max=400,pauza=10)
    robot_move.jazda_prosto(276, predkosc_max=1100, pauza=10)#stragan
    robot_move.spin_turn_v1(33,predkosc_max=600)
    robot_move.nakladka_prawa(-360, 500)#wyjęcie beczki
    robot_move.spin_turn_v1(-45, predkosc_max=500)
    robot_move.jazda_prosto(120, predkosc_max=700)
    robot_move.spin_turn_v1(60, predkosc_max=600)
    robot_move.jazda_prosto(330, 1200)
    robot_move.spin_turn_small(, 17predkosc_max=600)
    robot_move.jazda_prosto(160, predkosc_max=600)
    robot_move.nakladka_prawa(300, predkosc=600)
    robot_move.jazda_prosto(-300, 700)

    #robot_move.spin_turn_v1(-50, predkosc_max=700)
    #robot_move.smooth_turn(20000, -20)
    #base.prawy.run_angle(-60, 180)
    #robot_move.jazda_prosto(400, 700)
