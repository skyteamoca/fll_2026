from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch
from pybricks.hubs import PrimeHub
from pybricks.parameters import Direction, Port
from pybricks.pupdevices import Motor
from pybricks.robotics import DriveBase

# Inicjalizacja kontrolera głównego
hub = PrimeHub()

# Konfiguracja silników napędowych i akcesoriów
lewy = Motor(Port.A, Direction.COUNTERCLOCKWISE)
prawy = Motor(Port.E)
L_motor = Motor(Port.B)
P_motor = Motor(Port.F)

# Konstrukcja bazy jezdnej (kinematyka kół i rozstawu osi)
robot = DriveBase(lewy, prawy, wheel_diameter=49.5, axle_track=127)

# Stałe geometryczne koła wykorzystywane w algorytmach odometrii
srednica_kola = 49.5
obwod_kola = 3.14 * srednica_kola
