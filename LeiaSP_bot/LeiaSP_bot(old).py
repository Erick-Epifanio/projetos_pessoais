import pyautogui as auto
import keyboard
import time
import sys


program_runtime = True
Loop_process = False
delay = time.time()

class Central_Process:
    def __init__(self, img_base, timer):
        self.basic_image = img_base
        self.timer = timer

    def Body_Process(self):
        auto.PAUSE = self.timer * 60 # minutos
        basic_image_center = auto.center(self.basic_image)
        try:
            if auto.locateOnScreen("confirmation.png", confidence= 0.7):
                img_2 = auto.locateOnScreen("confirmation.png", confidence= 0.7)
                x,y = auto.center(img_2)
                auto.click()
        except auto.ImageNotFoundException:
            # não quero que o erro apareça, aqui estou passando a proxima tentativa de scanner da tela
            # é uma verificação continua se a tela que trava a leitura do livra se vai aparecer
            # # caso não apareça apenas ignore e tente de novo
            pass
        
        finally:
            auto.click(basic_image_center)
    
    def Run_Process(self):
        self.Body_Process()


def toggle():
    global Loop_process
    Loop_process = not Loop_process
    return


keyboard.add_hotkey("ctrl + del", toggle)
print("Ctrl + C para encerrar o programa\nCtrl + del para pausar o processo\n")
print("Digite o tempo de leitura PARA CADA FOLHA. O tempo padrão caso não digite nada é 1 minuto, e caso queria mudar o tempo, reinicie o programa\n\n")

while True:
    try:
        entry = input("Digite a duração em minutos (ou Enter para 1): ").strip()
        
        if entry:
            timer = float(entry)
            if timer <= 0:
                print("ERRO: O tempo deve ser um valor positivo.")
                continue
        else:
            timer = 1.0

        print(f"Tempo definido para {timer} minutos.")
        break 

    except ValueError:
        print("ERRO - Valor inválido. Digite um número ou Enter para o padrão (1).")
        continue

while program_runtime:
    try:
        time.sleep(1)
        print("Pressione Enter para iniciar")
        keyboard.wait('enter')
        toggle()
        print("\niniciando...")

        while Loop_process:
            try:
                img_1 = auto.locateOnScreen("next.png", confidence= 0.7)
                Master = Central_Process(img_1, timer)
                Master.Run_Process()

            except auto.ImageNotFoundException:
                continue
            time.sleep(0.1)

    except ValueError:
        continue

    except KeyboardInterrupt:
        print("saindo...")
        sys.exit()
