from pybricks.hubs import PrimeHub
from pybricks.parameters import Direction, Port
from pybricks.pupdevices import Motor
from pybricks.robotics import DriveBase

# Inicjalizacja kontrolera głównego
hub = PrimeHub()

# Konfiguracja silników napędowych i akcesoriów
lewy = Motor(Port.A, Direction.COUNTERCLOCKWISE)
prawy = Motor(Port.B)
c_motor = Motor(Port.C)
d_motor = Motor(Port.D)

# Konstrukcja bazy jezdnej (kinematyka kół i rozstawu osi)
robot = DriveBase(lewy, prawy, wheel_diameter=49.5, axle_track=115)

# Stałe geometryczne koła wykorzystywane w algorytmach odometrii
srednica_kola = 49.5
obwod_kola = 3.14 * srednica_kola
