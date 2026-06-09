import base
from pybricks.tools import wait, StopWatch
from pybricks.parameters import Stop

def spin_turn_small(kat_stopnie, predkosc_max=260, predkosc_min=40, Kp=9.0, Kd=1.2, tolerance=0.6, kick_ms=60, timeout_ms=900, pauza=0):
    print(f"⚡ Spin small: {kat_stopnie}°")
    kat_startowy = base.hub.imu.heading()
    zegar = StopWatch()
    zegar.reset()

    def blad_kata():
        kat_aktualny = base.hub.imu.heading()
        blad = kat_stopnie - (kat_aktualny - kat_startowy)
        if blad > 180: blad -= 360
        elif blad < -180: blad += 360
        return blad

    kier = 1 if kat_stopnie >= 0 else -1
    base.lewy.run(-kier * predkosc_max)
    base.prawy.run(kier * predkosc_max)
    wait(kick_ms)

    poprzedni_blad = blad_kata()

    while True:
        if zegar.time() > timeout_ms: break
        b = blad_kata()
        db = b - poprzedni_blad
        poprzedni_blad = b
        output = Kp * b + Kd * db

        if output > 0:
            output = max(predkosc_min, min(predkosc_max, output))
        else:
            output = min(-predkosc_min, max(-predkosc_max, output))

        base.lewy.run(-output)
        base.prawy.run(output)

        if abs(b) <= tolerance: break
        wait(10)

    base.lewy.stop()
    base.prawy.stop()
    wait(60)
    base.lewy.hold()
    base.prawy.hold()
    wait(pauza)


def jazda_prosto(dystans_mm, predkosc_max=600, dystans_hamowania=100, Kp=2.0, Ki=0.1, Kd=0.2, pauza=0):
    print(f"▶️ Jazda prosto: {dystans_mm} mm")
    kierunek = 1 if dystans_mm >= 0 else -1
    cel_mm = abs(dystans_mm)
    dystans_mm = cel_mm

    kat_start = base.hub.imu.heading()
    suma_bledow = 0
    poprzedni_blad = 0

    base.lewy.reset_angle(0)
    base.prawy.reset_angle(0)

    predkosc_biezaca = 0
    rampa_krok = 20

    while True:
        kat = base.hub.imu.heading()
        blad = kat - kat_start

        if blad > 180: blad -= 360
        elif blad < -180: blad += 360

        suma_bledow += blad
        zmiana_bledu = blad - poprzedni_blad

        korekta = Kp * blad + Ki * suma_bledow + Kd * zmiana_bledu
        korekta *= kierunek

        sredni_kat = (base.lewy.angle() + base.prawy.angle()) / 2
        dystans_przejechany = abs((sredni_kat / 360) * base.obwod_kola)
        pozostalo = dystans_mm - dystans_przejechany

        if pozostalo < dystans_hamowania:
            skala = pozostalo / dystans_hamowania
            predkosc_docelowa = max(predkosc_max * skala, 150)
        else:
            predkosc_docelowa = predkosc_max

        if predkosc_biezaca < predkosc_docelowa:
            predkosc_biezaca = min(predkosc_biezaca + rampa_krok, predkosc_docelowa)
        else:
            predkosc_biezaca = predkosc_docelowa

        v_lewy = kierunek * (predkosc_biezaca + korekta)
        v_prawy = kierunek * (predkosc_biezaca - korekta)

        base.lewy.run(v_lewy)
        base.prawy.run(v_prawy)

        if pozostalo <= 3: break
        poprzedni_blad = blad
        wait(20)

    base.lewy.stop()
    base.prawy.stop()
    wait(100)
    base.lewy.hold()
    base.prawy.hold()
    wait(pauza)


def spin_turn_v1(kat_stopnie, predkosc_max=400, Kp=3.0, Ki=0.1, pauza=0):
    print(f"🔁 Spin Turn v1: {kat_stopnie}°")
    kat_startowy = base.hub.imu.heading()
    zegar = StopWatch()
    suma_bledu = 0

    while True:
        kat_aktualny = base.hub.imu.heading()
        blad = kat_stopnie - (kat_aktualny - kat_startowy)
        if blad > 180: blad -= 360
        elif blad < -180: blad += 360

        dt = zegar.time() / 1000
        zegar.reset()

        P = Kp * blad
        suma_bledu += blad * dt
        I = Ki * suma_bledu

        output = P + I
        output = max(-predkosc_max, min(predkosc_max, output))

        base.lewy.run(-output)
        base.prawy.run(output)

        if abs(blad) < 1 and abs(output) < 50: break
        wait(10)

    base.lewy.brake()
    base.prawy.brake()
    print("✅ Spin Turn v1 zakończony.")
    wait(pauza)


def spin_turn_v2(kat_stopnie, predkosc_max=400, predkosc_min=100, pauza=0):
    print(f"🔁 Spin Turn v2 (rampa): {kat_stopnie}°")
    kat_startowy = base.hub.imu.heading()
    kat_koncowy = (kat_startowy + kat_stopnie) % 360

    def oblicz_blad_kata(kat_aktualny, kat_cel):
        kat_pozostaly = kat_cel - kat_aktualny
        if kat_pozostaly > 180: kat_pozostaly -= 360
        elif kat_pozostaly < -180: kat_pozostaly += 360
        return kat_pozostaly

    predkosc_robota = 0

    while True:
        kat_aktualny = base.hub.imu.heading()
        kat_pozostaly = oblicz_blad_kata(kat_aktualny, kat_koncowy)
        kat_bezwzgledny = abs(kat_pozostaly)

        if kat_bezwzgledny > 45:
            predkosc_chwilowa = predkosc_max
        else:
            predkosc_chwilowa = predkosc_min + ((predkosc_max - predkosc_min) * (kat_bezwzgledny / 45))

        predkosc_chwilowa = max(predkosc_min, min(predkosc_max, predkosc_chwilowa))
        predkosc_chwilowa *= 1 if kat_pozostaly > 0 else -1
        predkosc_robota = 0.7 * predkosc_robota + 0.3 * predkosc_chwilowa

        base.lewy.run(-predkosc_robota)
        base.prawy.run(predkosc_robota)

        if abs(kat_pozostaly) < 1 and abs(predkosc_robota) < 50: break
        wait(20)

    base.lewy.stop()
    base.prawy.stop()
    wait(100)
    base.lewy.hold()
    base.prawy.hold()

    kat_koncowy_rzeczywisty = base.hub.imu.heading()
    blad_koncowy = oblicz_blad_kata(kat_koncowy_rzeczywisty, kat_koncowy)
    print(f"📐 Kąt końcowy: {kat_koncowy_rzeczywisty:.1f}° | Błąd: {blad_koncowy:+.1f}°")
    wait(pauza)


def pivot_turn(akcja, kat_docelowy, v_max=600, Kp=8, dt=20, v_min=20, pauza=0):
    kat_docelowy = abs(kat_docelowy)
    kat_start = base.hub.imu.heading()
    silnik = base.lewy if akcja.startswith("lewy") else base.prawy
    kierunek = 1 if akcja.endswith("przod") else -1
    kierunek_IMU = 1 if akcja.endswith("przod") else -1

    base.lewy.brake()
    base.prawy.brake()
    wait(50)
    print("🧭 START PIVOT TURN")

    while True:
        kat = base.hub.imu.heading()
        blad = kat_docelowy - kierunek_IMU * (kat - kat_start)
        if blad <= 0: break
        v = min(int(Kp * blad), v_max)
        v = max(v, v_min)
        silnik.run(kierunek * v)
        wait(dt)

    base.lewy.brake()
    base.prawy.brake()
    kat_koncowy = base.hub.imu.heading()
    print(f"✅ KONIEC PIVOT TURN | Zmiana: {(kat_koncowy - kat_start):+.1f}°")
    wait(pauza)


def smooth_turn(promien_mm, kat_stopnie, predkosc=None, pauza=0):
    print(f"🔄 Smooth turn: promień={promien_mm}mm, kąt={kat_stopnie}°")
    if predkosc is not None:
        aktualne_ustawienia = base.robot.settings()
        base.robot.settings(straight_speed=predkosc)

    base.robot.curve(promien_mm, kat_stopnie, then=Stop.HOLD, wait=True)

    if predkosc is not None:
        base.robot.settings(*aktualne_ustawienia)
    wait(pauza)


def nakladka_lewa(stopnie, predkosc=500, pauza=0):
    base.d_motor.run_angle(predkosc, stopnie)
    base.d_motor.brake()
    wait(pauza)


def nakladka_prawa(stopnie, predkosc=500, pauza=0):
    base.c_motor.run_angle(predkosc, stopnie)
    base.c_motor.brake()
    wait(pauza)