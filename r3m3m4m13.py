#Orest 24.06.2026r
import base
import robot_move
from pybricks.tools import wait

def run():
    wait(100)
    base.d_motor.run_angle(250, -230, wait=False)
    robot_move.jazda_prosto(755, predkosc_max=800, dystans_hamowania=200, pauza=200)
    base.c_motor.run_angle(300, 200)
    wait(50)
    base.c_motor.run_angle(-300, 200, wait=False)
    robot_move.jazda_prosto(148, predkosc_max=800, dystans_hamowania=100, pauza=200)
    robot_move.spin_turn_v1(88, 200, 50, pauza=10)
    wait(100)
    #opuszczenie nakładki do oporu
    base.d_motor.run_until_stalled(speed=200, duty_limit=40)
    base.d_motor.run_angle(200, -20)
    #base.d_motor.run_angle(150, 230) #opuszczenie nakłądki do artefaktu
    base.c_motor.run_angle(450, 350)
    wait(10)
    robot_move.jazda_prosto(154, predkosc_max=200, pauza=10)
    
    # podniesienie artefaktu
    base.d_motor.run_angle(150, -43)
    wait(50)
    
    # podniesienie wózka
    base.c_motor.run_angle(700, -285)
    wait(1000)
    robot_move.jazda_prosto(-144, predkosc_max=300, pauza=10)
    
    # Skręt do foki
    robot_move.spin_turn_small(39.5, 500, pauza=10)
    wait(10)
    base.d_motor.run_angle(250, -90, wait=False)
    base.c_motor.run_angle(400, 300, wait=False)
    
    # podjazd do foki
    robot_move.jazda_prosto(380, predkosc_max=900, pauza=10)
    
    # podnoszenie foki
    base.c_motor.run_angle(1000, -300)
    wait(100)
    robot_move.jazda_prosto(-148, predkosc_max=1000, pauza=10)
    robot_move.spin_turn_v1(-32, predkosc_max=500, Kp=4.0, Ki=0.1)
    base.c_motor.run_angle(700, -250, wait=False)
    robot_move.jazda_prosto(560, predkosc_max=1000, pauza=10)
    
    # skręt do wiaderka
    #test
    # robot_move.spin_turn_v1(7, predkosc_max=300, pauza=10)
    base.c_motor.run_angle(800, 520)
    wait(100)
    base.c_motor.run_angle(-300, 300)
    wait(100)
    robot_move.spin_turn_small(-30, 500, pauza=30)
    robot_move.smooth_turn(245, -60, 500, pauza=10)
    robot_move.jazda_prosto(200, predkosc_max=1000, pauza=10)
    robot_move.jazda_prosto(-200, 1000, pauza=10)
    robot_move.spin_turn_v1(-40, predkosc_max=300, pauza=10)
    robot_move.smooth_turn(500, -100, 500, pauza=10)
