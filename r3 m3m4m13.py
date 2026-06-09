import base
import robot_move
from pybricks.tools import wait

def run():
    wait(100)
    base.d_motor.run_angle(250, -230, wait=False)
    robot_move.jazda_prosto(755, predkosc_max=800, dystans_hamowania=200, pauza=200)
    base.c_motor.run_angle(300, 200)
    robot_move.jazda_prosto(155, predkosc_max=800, dystans_hamowania=100, pauza=200)
    robot_move.spin_turn_v1(89, 200, 50, pauza=10)
    wait(100)
    base.d_motor.run_angle(150, 230)
    base.c_motor.run_angle(450, 150)
    wait(10)
    robot_move.jazda_prosto(154, predkosc_max=200, pauza=10)
    
    # podniesienie artefaktu
    base.d_motor.run_angle(150, -43)
    wait(50)
    
    # podniesienie wózka
    base.c_motor.run_angle(120, -285)
    wait(1000)
    robot_move.jazda_prosto(-144, predkosc_max=300, pauza=10)
    
    # Skręt do foki
    robot_move.spin_turn_small(39, 500, pauza=10)
    wait(10)
    base.d_motor.run_angle(250, -90, wait=False)
    base.c_motor.run_angle(400, 300, wait=False)
    
    # podjazd do foki
    robot_move.jazda_prosto(365, predkosc_max=900, pauza=10)
    
    # podnoszenie foki
    base.c_motor.run_angle(400, -300)
    wait(100)
    robot_move.jazda_prosto(-118, predkosc_max=1000, pauza=10)
    robot_move.spin_turn_v1(-42, predkosc_max=500, Kp=4.0, Ki=0.1)
    base.c_motor.run_angle(700, -250, wait=False)
    robot_move.jazda_prosto(550, predkosc_max=1000, pauza=10)
    
    # skręt do wiaderka
    robot_move.spin_turn_v1(33, predkosc_max=300, pauza=10)
    base.c_motor.run_angle(800, 520)
    wait(100)
    base.c_motor.run_angle(-300, 300)
    wait(100)
    robot_move.spin_turn_small(-20, 500, pauza=30)
    robot_move.smooth_turn(400, -80, 500, pauza=10)
    robot_move.jazda_prosto(-200, predkosc_max=1000, pauza=10)
    robot_move.spin_turn_v1(-40, predkosc_max=300, pauza=10)
    robot_move.smooth_turn(580, -400, 1000, pauza=10)
