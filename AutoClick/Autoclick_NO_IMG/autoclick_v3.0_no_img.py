"""Bibliotecas / Libraries"""
import threading
import time
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo, askokcancel
from tkinter.font import Font
import pyautogui as auto
from keyboard import add_hotkey, remove_hotkey


# Classe Back-End


class BackProcess:
    """Classe responsavél pelo Auto click / Class responsible for Auto click"""

    def __init__(self):

        # Flags de controle & tempo de ciclo & contador de ciclos
        # Control flags & cycle time & cycle counter

        self.loopstate = False
        self.time_delay = 0
        self.cycle = 0
        self.positions_target_list = []

    def set_position(self):
        """Captura de posição do mouse"""
        self.positions_target_list.append(auto.position())

    def autoclick_process(self):
        """Sistema do AutoClick / AutoClick System"""

        while self.loopstate:
            for target in self.positions_target_list:
                auto.PAUSE = (self.time_delay * 60)
                auto.click(target)
            self.cycle += 1
            time.sleep(1)

    def instance_config(self):
        """configuração da thread / thread configuration"""

        parallel_process = threading.Thread(
            target=self.autoclick_process,
            daemon=True
            )
        parallel_process.start()


class WindowsConfig(BackProcess):
    """Configurações da interface grafica / Graphical interface settings."""

    def __init__(self):
        super().__init__()

        # Configurações essenciais
        # Essential settings

        self._root = tk.Tk()
        self._root.title("AutoClick by Erick Ep.")
        self._root.geometry("500x300")
        self._root.resizable(False, False)
        self._root.protocol("WM_DELETE_WINDOW", self.close_interface)
        # self.icon = tk.PhotoImage(file="imagens/template.png")
        # self._root.iconphoto(True, self.icon)

        # Estilização
        # Styling
        self.font_config = Font(size=15, weight="bold")
        self.back_color = "#f5f5f5"
        self._root.config(bg=self.back_color)

        # Conteúdo
        # Content
        self.labelconteiner = tk.LabelFrame(
            self._root, text="Modo de uso",
            background=self.back_color
            )

        self.info_text = ttk.Label(
            self._root, text="",
            background=self.back_color
            )
        self.process_info = None
        self.button = None
        self.target_count = None

        # Atalho
        self.shotcut = add_hotkey("ctrl+del", self.toggle)
        self.set_position = add_hotkey("alt+'", callback=self.set_position)

    def toggle(self):
        """Controle de estado do loop / Loop state control"""

        self.loopstate = not self.loopstate

        time.sleep(0.1)
        if self.loopstate:
            self.button.config(text="parar")
            self.process_info.config(
                text="Status do processo: Executando",
                foreground="green"
                )
            self.instance_config()
        else:
            self.button.config(text="Iniciar")
            showinfo(
                "status",
                message=f"Processo pausado\nRepetição feitas: {self.cycle}"
                )
            self.process_info.config(
                text="Status do processo: Parado",
                foreground="red"
                )

    def close_interface(self):
        """Mecanismo de saída / exit mechanism"""

        if askokcancel("AutoClick by Erick Ep.", "deseja sair?"):
            remove_hotkey("ctrl+del")
            remove_hotkey("alt+'")
            self._root.destroy()

    def text_title(self):
        """Titulo / Title."""

        title = ttk.Label(
            self._root,
            text="AutoClick (NO IMAGE)\n",
            font=self.font_config,
            background=self.back_color,
        )

        title.pack(anchor="w")

    def text_manager(self):
        """Gerenciador de textos / text manager"""

        usage_info = ttk.Label(
            self.labelconteiner,
            text="Antes de iniciar, é preciso selecionar o tempo por ciclo."
            "\nO que é tempo de ciclo? Simples,"
            "é o tempo que permanencia em cada pagina.\n"
            "Ou seja, cada ciclo representa uma pagina.\n\n"
            "Para configurar as posições use: Alt + '\n\n"
            "Para pausar via atalho é: Ctrl + Del\n",
            background=self.back_color
        )

        version = ttk.Label(
            self.labelconteiner, text="v3.2 - (prototipo)",
            foreground="#636336",
            background=self.back_color
        )

        texts_list = [
            usage_info,
            version
        ]

        for index, text_target in enumerate(texts_list):
            text_target.grid(column=0, row=index, sticky="w")
        self.labelconteiner.pack(fill="both")

    def time_insert(self):
        """entrada de dados"""

        insert = ttk.Entry(self._root)
        insert.pack(side="left", pady=1, anchor="n")

        def send_data():
            try:
                time_data = float(insert.get())
                self.time_delay = time_data
                self.info_text.config(
                    text=f"Tempo configurado: {self.time_delay} Min/C",
                    foreground="green"
                    )
                self.button.config(state="enable")
                self.process_info.config(
                    text="Status do processo: Preparado",
                    foreground="#b59322"
                    )
            except ValueError:
                self.info_text.config(text="Tempo invalido", foreground="red")

        send_data_button = ttk.Button(
            self._root,
            text="Confirmar",
            padding=0.2,
            command=send_data
            )
        send_data_button.pack(side="left", anchor="n")
        self.info_text.pack(side="top", anchor="w")

    def button_config(self):
        """Configuções do botão"""

        self.button = ttk.Button(
            self._root, text="Iniciar",
            state="disable",
            command=self.toggle
            )
        self.button.pack(side="bottom")

    def status_process(self):
        """indicador de estado"""

        self.process_info = ttk.Label(
            self._root,
            text="Status do processo: Não programado",
            background=self.back_color,
            foreground="black"
            )

        self.process_info.pack(side="left", anchor="n")

    def run(self):
        """Método de unificação de execução / Execution unification method"""

        self.text_title()
        self.text_manager()
        self.time_insert()
        self.button_config()
        self.status_process()
        self._root.mainloop()


main = WindowsConfig()
main.run()
