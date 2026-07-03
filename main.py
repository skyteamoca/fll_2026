import base
import r1m1m2, r2m11m12, r3m3m4m13, r4m5m6m7m9a, r5m9m10m14, judge_session,rflaga
from pybricks.parameters import Button
from pybricks.tools import wait

# Lista przypisująca wybrane misje z modułu missions.py do pozycji w menu
lista_misji = [
    r1m1m2.run,         # 1
    r2m11m12.run,       # 2
    r3m3m4m13.run,      # 3
    r4m5m6m7m9a.run,    # 4
    r5m9m10m14.run,     # 5
    judge_session.run,  # 6
    rflaga.run
]

def main():
    print("\n🚦 START SYSTEMU MENU\n")
    base.hub.system.set_stop_button(None)
    aktualny_indeks = 0
    ilosc_misji = len(lista_misji)

    while True:
        base.hub.display.char(str(aktualny_indeks + 1))
        wcisniete = base.hub.buttons.pressed()

        if not wcisniete:
            wait(10)
            continue

        if Button.LEFT in wcisniete:
            aktualny_indeks = (aktualny_indeks + 1) % ilosc_misji
            while base.hub.buttons.pressed(): wait(10)

        elif Button.RIGHT in wcisniete:
            aktualny_indeks = (aktualny_indeks - 1) % ilosc_misji
            while base.hub.buttons.pressed(): wait(10)

        elif Button.BLUETOOTH in wcisniete:
            base.hub.display.off()
            break

        elif Button.CENTER in wcisniete:
            while base.hub.buttons.pressed(): wait(10)
            base.hub.system.set_stop_button(Button.CENTER)
            base.hub.display.char("R")
            print(f"\n▶️ URUCHAMIAM MISJĘ: {aktualny_indeks + 1}")

            try:
                lista_misji[aktualny_indeks]()
                base.hub.speaker.beep(frequency=1000, duration=100)
            except SystemExit:
                print(f"🛑 PRZERWANO MISJĘ {aktualny_indeks + 1}!")
                base.lewy.stop(); base.prawy.stop(); base.c_motor.stop(); base.d_motor.stop()
                base.hub.speaker.beep(frequency=500, duration=500)

            base.lewy.stop()
            base.prawy.stop()
            base.c_motor.stop()
            base.d_motor.stop()

            aktualny_indeks = (aktualny_indeks + 1) % ilosc_misji
            base.hub.system.set_stop_button(None)
            while base.hub.buttons.pressed(): wait(10)

# Automatyczne odpalenie programu po włączeniu pliku main.py
main()
