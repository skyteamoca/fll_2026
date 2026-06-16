import base
import robot_move
from pybricks.tools import wait

def run():
    wait(10)
    base.c_motor.run_angle(-1000, 200, wait=False)
    robot_move.jazda_prosto(692, predkosc_max=800)
    wait(10)
    robot_move.spin_turn_v1(-20, predkosc_max=200, Kp=7, pauza=100)
    #wyrzucenie głazów
    robot_move.spin_turn_v1(63, predkosc_max=200, Kp=7)
    wait(50)
    robot_move.spin_turn_small(-3, predkosc_max=500)
    wait(50)
    base.c_motor.run_angle(-1000, 175)#200
    wait(10)
    robot_move.jazda_prosto(16, predkosc_max=100)
    wait(10)
    #podniesienie dźwigu
    base.c_motor.run_angle(350, 350)#375
    wait(10)
    robot_move.jazda_prosto(-80, predkosc_max=500)
    wait(10)
    
    #wypchanie kamieni
    robot_move.spin_turn_v1(-129, predkosc_max=500)
    wait(100)
    base.prawy.run_time(-480, 1150, wait=False)
    base.lewy.run_time(-415, 1150)
    wait(50)
    #Silos
    #robot_move.nakladka_lewa(-90, 500)
    robot_move.nakladka_lewa(90, 2000)
    robot_move.nakladka_lewa(-90, 400)
    robot_move.nakladka_lewa(90, 2000)
    robot_move.nakladka_lewa(-90, 400)
    robot_move.nakladka_lewa(90, 2000)
    robot_move.nakladka_lewa(-90, 400)
    #robot_move.smooth_turn(300, 180, 500, pauza=10)

    #Podjazd do wagonika
    # base.prawy.run_time(500, 1000, wait=False)
    # base.lewy.run_time(180, 1000)
    # robot_move.jazda_prosto(575, predkosc_max=600)
    # wait(100)
    # robot_move.spin_turn_v1(125, predkosc_max=500)
    # wait(100)
    # base.d_motor.run_angle(40, -142)
    # robot_move.jazda_prosto(-50, predkosc_max=600) 
