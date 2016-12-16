import tkinter
from tkinter import filedialog
from hashlib import md5


tkinter.Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
open_file = open(filedialog.askopenfilename(), 'r', encoding = 'ISO-8859-1')
file_content = open_file.read().translate({ord(ch):None for ch in '\r\n'})

m = md5()
m.update(file_content[:-43].encode('ISO-8859-1'))

print('Aplicação criada por Paulo Henrique Vasconcellos, da Unimed Araruama\n\n')
print('Seu novo hash é: ', m.hexdigest(),'\nAltere o registro 998 (Posição 12 a 43) e valide o arquivo.\n\n')
input('Pressione \"ENTER\" para sair.')
