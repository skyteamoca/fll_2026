import base
import robot_move
from pybricks.tools import wait

def misja_m1m2():
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


def misja_m3m4m13():
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


def misja_m8():
    wait(100)
    robot_move.jazda_prosto(420, predkosc_max=800)
    wait(50)
    for _ in range(2):
        base.c_motor.run_angle(1000, 130)
        wait(50)
        base.c_motor.run_angle(-1000, 130)
        wait(50)
    robot_move.jazda_prosto(-450, predkosc_max=800)


def misja_m5m6m7m9a():
    wait(10)
    base.c_motor.run_angle(-1000, 200, wait=False)
    robot_move.jazda_prosto(675, predkosc_max=800)
    wait(10)
    robot_move.spin_turn_v1(50, predkosc_max=800, Kp=7)
    wait(10)
    robot_move.spin_turn_small(-13, predkosc_max=500)
    wait(10)
    base.c_motor.run_angle(-1000, 200)
    wait(10)
    robot_move.jazda_prosto(32, predkosc_max=100)
    wait(10)
    
    # podniesienie dźwigu
    base.c_motor.run_angle(350, 375)
    wait(10)
    robot_move.jazda_prosto(-80, predkosc_max=500)
    wait(10)
    
    # skręt do stołu
    robot_move.spin_turn_v1(-130, predkosc_max=500)
    wait(100)
    base.prawy.run_time(-500, 1100, wait=False)
    base.lewy.run_time(-430, 1100)
    wait(50)
    base.prawy.run_time(500, 1000, wait=False)
    base.lewy.run_time(340, 1000)
    robot_move.jazda_prosto(410, predkosc_max=600)
    robot_move.spin_turn_v1(75, predkosc_max=500)
    wait(100)
    base.d_motor.run_angle(40, -142)
    robot_move.jazda_prosto(-50, predkosc_max=600)


def misja_m11m12():
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


def misja_m9m10m14():
    wait(100)
    base.c_motor.run_angle(500, -1000, wait=False)
    robot_move.jazda_prosto(280, predkosc_max=700, pauza=10)
    robot_move.spin_turn_v1(-105, predkosc_max=500, pauza=10)
    robot_move.jazda_prosto(250, predkosc_max=700, pauza=10)
    
    # skręt do artefaktu
    base.c_motor.run_angle(500, 1000, wait=False)
    robot_move.spin_turn_v1(40, predkosc_max=800, pauza=10)
    
    # wyciąganie artefaktu
    robot_move.jazda_prosto(115, predkosc_max=800, pauza=100)
    base.c_motor.run_angle(500, -1000)
    wait(10)
    base.prawy.run_time(600, 2500, wait=False)
    base.lewy.run_time(545, 2500)
    wait(10)
    base.prawy.run_angle(-500, 115)
    wait(10)
    base.d_motor.run_angle(50, 200)
    wait(10)
    robot_move.jazda_prosto(-20, predkosc_max=200, pauza=10)
    robot_move.spin_turn_small(10, 50)