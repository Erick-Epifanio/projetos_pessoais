from termcolor import colored
from prettytable import PrettyTable
import subprocess
tabela = PrettyTable()

#tabela.field_names = [colored('função','yellow'),colored('descrição','yellow')]
#tabela.add_row(['Portscan','identificar portas de redes abertas'])

class table():
				def __init__(self):
								self.tabela = PrettyTable()
								self.line()
				def line(self):
								self.tabela.field_names = [colored('função','yellow'),colored('descrição','yellow')]
								self.tabela.add_row(['Portscan','identificar portas de redes abertas'])
								
				def exibir(self):
												print(self.tabela)
												
				def startup(self):
												self.exibir()
												
if __name__ == "__main__":
				script = table()
				script.exibir()