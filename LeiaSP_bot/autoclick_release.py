"""Modulos que vou usar até então"""

from sys import exit  # pylint: disable=redefined-builtin
import time
import keyboard
import pyautogui as auto


class AutoClick:
    """Objetos que serão necessarios"""

    def __init__(self):
        self.asset_next = "next.png"  # PNG principal a ser detectado
        self.asset_confirm = "confirmation.png"  # PNG secundario (confirmação)
        self.loop_process = True  # controle de processo (RUN/STOP)
        self.controlkey = keyboard.add_hotkey("ctrl + del", self.toggle)
        self.delayofstage = None
        self.uniquecheck = True
        self.count = 0

    def toggle(self):
        """Alternancia booleana"""

        self.loop_process = not self.loop_process

    def delaycheck(self):
        """Verifico & trato o tempo de atraso de cada ciclo antes de iniciar o processo geral"""

        while True:
            try:
                self.delayofstage = (
                    float(input("Digite o tempo em minutos de ciclo: ") or 1) * 60
                )
                break

            except ValueError:
                print("ERRO -- valor invalido")
                continue

    def bodyprogramming(self):
        """Escopo geral do programa"""

        auto.PAUSE = 0.1

        try:
            imgfist = auto.locateOnScreen(self.asset_next, confidence=0.7)
            nextlocate = auto.center(imgfist)
            auto.moveTo(nextlocate)
            auto.click()
            self.count += 1
            print(f"Fim de ciclo: {self.count}")

            if auto.locateOnScreen(self.asset_confirm, confidence=0.7):
                confirmlocate = auto.locateOnScreen(self.asset_confirm, confidence=0.7)
                auto.click(confirmlocate.x, confirmlocate.y)

        except auto.ImageNotFoundException:
            # Não vou implementar nada nesse bloco
            # é apenas uma tentativa invalida de detecção de imagem
            # Apenas segue o jogo
            pass

            # Vou esperar acontecer uma excessão para implementar contramedidas se for necessario

    def run_body(self):
        """Loop do bodyprogramming"""

        try:
            self.delaycheck()

            while True:
            # Loop geral, controla a permarsistencia Runtime
                if self.loop_process:
                    self.bodyprogramming()
                else:
                    print("Terminando processo atual\nStatus do processo: PAUSADO")
                    keyboard.wait("ctrl+del")

                if self.uniquecheck:
                    self.uniquecheck = not self.uniquecheck
                else:
                    time.sleep(self.delayofstage)

        except KeyboardInterrupt:
            print("\nSaindo....")
            time.sleep(1)
            exit()


Master = AutoClick()
Master.run_body()

# Refiz esse programa, pois a versão anterior não levava o PEP8 em conta...
