"""Modulos/bibliotécas necessarias""" 

#importações inteiras:
import threading
import time
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
import pyautogui as auto
from keyboard import add_hotkey



class BackProcess:
    """Configuração de execução do auto click"""

    def __init__(self):
        self.loopstate = True
        self.instance_process = None
        self.time_delay = None

        # Imagens
        self.imagem_target_1 = "C:/Users/erick/Desktop/projeto/LeiaSP_bot/next.png"
        self.imagem_target_2 = "C:/Users/erick/Desktop/projeto/LeiaSP_bot/confirmation.png"


    def toggle(self):
        """Alternancia de estado True/False"""

        self.loopstate = not self.loopstate


    def autoclick_process(self):
        """Processo principal"""

        while self.loopstate:
            try:
                auto.PAUSE = 0.5
                if auto.locateOnScreen(self.imagem_target_2, confidence=0.7):
                    set_postion_target_2 = auto.locateOnScreen(self.imagem_target_2, confidence=0.7)
                    auto.moveTo(set_postion_target_2)
                    #auto.click()

                else:
                    set_postion_target_1 = auto.locateOnScreen(self.imagem_target_1, confidence=0.7)
                    auto.moveTo(set_postion_target_1)
                    #auto.click()

            except auto.ImageNotFoundException:
                # Não vou precisar tratar essa exceção, apenas quero eu a ignore.
                pass
            time.sleep(self.time_delay)

    def instance_config(self):
        """Processo de instanciamento da thread de execução do auto click"""

        self.instance_process = threading.Thread(group=None, target=self.autoclick_process)
        self.instance_process.start()


class WindowsConfig(BackProcess):
    """Configurações da janela do programa"""

    def __init__(self):
        super().__init__()
        self.root = tk.Tk()
        self.title = self.root.title("AutoClick by VeilCruss")
        self.icon = tk.PhotoImage(file="C:/Users/erick/Desktop/projeto/LeiaSP_bot/template.png")
        self.root.iconphoto(True, self.icon)
        self.size = self.root.geometry("500x300")
        self.size_lock = self.root.resizable(False, False)

        #Conteúdo

        self.labelconteiner = None
        self.button_start = None
        self.button_stop = None
        self.insert_time = None
        self.loop_status = None
        self.time_set_status = None

        #Atalho
        self.shotcut = add_hotkey("ctrl+del", self.action_shotcut)

    def labelframe_config(self):
        """Todos as configurações e necessarias """

        self.labelconteiner = ttk.Labelframe(self.root, text="Modo de uso")
        usage_info = ttk.Label(
            self.labelconteiner,
            text=
            "Antes de iniciar, é preciso selecionar o tempo por ciclo." \
            "\nO que é tempo de ciclo? Simples, é o tempo que permanencia em cada pagina.\n" \
            "Ou seja, cada ciclo representa uma pagina.\n\n\nPara pausar via atalho é: Ctrl + Del"
            )

        version = ttk.Label(
            self.labelconteiner,
            text="v3.1 - (prototipo)",
            foreground= "#646443"
            )

        #As proximas linhas abaixo se trata de instanciamento "dinamico" dos texto na janela
        text_list = [
            usage_info,
            version
        ]

        for line_index, selected_text in enumerate(text_list):
            selected_text.grid(column= 0, row= line_index, sticky="w")

        self.labelconteiner.pack(fill="both")

    def status_display(self):
        """Estados"""

        self.loop_status = ttk.Label(self.root, text="Estado do loop: PARADO", foreground="red")
        self.loop_status.pack(anchor="w")


    def action_start(self):
        """Chama o método que instancia a thread de execução do back-end do autoclick"""

        self.button_stop.config(state="enable")
        self.instance_config()
        self.button_start.config(state="disable")
            # Garante que o botão "iniciar" não fica ativo
            # E consequentemente não chame outra instanciamento

    def action_stop(self):
        """Troca o estado da flag responsavel por controlar o loop infinito da thread"""

        # Método que alterna o estado booleano da flag (loopstate)
        if self.loopstate:
            self.toggle()
            self.loop_status.config(text="Estado do loop: PARADO", foreground="red")
            self.button_stop.config(text="Trocar Estado")
        elif not self.loopstate:
            self.toggle()
            self.button_start.config(state="enable")
            self.loop_status.config(text="Estado do loop: PRONTO", foreground="green")
            self.button_stop.config(state="disable")
            self.button_stop.config(text="Parar")


    def button_1(self):
        """Configurações dos botões"""

        button_frame = ttk.Frame(self.root, borderwidth=4)
        button_frame.pack(side="bottom")

        #botão de iniciar
        self.button_start = ttk.Button(
            button_frame, state="disable",
            text="Iniciar",
            command=self.action_start
            )
        self.button_start.pack(side="right", padx=10)

        #botão de parar
        self.button_stop = ttk.Button(
            button_frame,
            state="disable",
            text="Parar",
            command=self.action_stop
            )
        self.button_stop.pack(side="left")

    def time_set(self):
        """Entrada de tempo de ciclo"""

        self.insert_time = ttk.Entry(self.root)
        self.insert_time.pack(side="left", pady=1, anchor="ne")

        def time_set_config():
            try:
                get_time = float(self.insert_time.get())
                if isinstance(get_time, float):
                    self.time_delay = get_time

                    message_time_info.config(
                        text=f"Tempo de ciclo configurado: {self.time_delay} Minutos/Pg",
                        foreground="green"
                    )

                    if not self.loopstate:
                        self.toggle()
                        self.button_start.config(state="enable")
                        self.button_stop.config(state="enable")
                    else:
                        self.button_start.config(state="enable")
                    self.loop_status.config(text="Estado do loop: PRONTO", foreground="green")

            except ValueError:
                message_time_info.config(
                    text="Entrada invalida, " \
                    "é necessario ser um numero.",
                    foreground="red"
                )

        enter = ttk.Button(self.root, text="confirmar", padding=0.2 ,command=time_set_config)
        enter.pack(side="left", anchor="n")
        message_time_info = ttk.Label(self.root, text="")
        message_time_info.pack(anchor="w")

    def action_shotcut(self):
        """atalho"""

        self.toggle()

        if not self.loopstate:
            massage_info = showinfo(
                title="AutoClick info",
                message="Processo pausado",
                default="ok"
            )

            if massage_info == "ok":
                self.button_start.config(state="enable")
                self.toggle()
                self.button_stop.config(state="disable")

    def run(self):
        """Simplificação de instanciamento"""
        self.labelframe_config()
        self.time_set()
        self.button_1()
        self.status_display()
        self.root.mainloop()

WindowsConfig().run()
