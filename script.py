import tkinter
from tkinter import filedialog
from hashlib import md5


tkinter.Tk().withdraw() #Statement para não mostrar uma janela ao fundo
open_file = open(filedialog.askopenfilename(), 'r', encoding = 'ISO-8859-1') #Solitação do arquivo para cálculo de hash
file_content = open_file.read().translate({ord(ch):None for ch in '\r\n'}) #Leitura do arquivo e remoção de quebra de linha

m = md5() #Novo objeto MD5
m.update(file_content[:-43].encode('ISO-8859-1')) #Criação do hash utilizando o encoder ISO-8859-1

print('Aplicação criada por Paulo Henrique Vasconcellos, da Unimed Araruama\n\n')
print('Seu novo hash é: ', m.hexdigest(),'\nAltere o registro 998 (Posição 12 a 43) e valide o arquivo.\n\n')
input('Pressione \"ENTER\" para sair.')
