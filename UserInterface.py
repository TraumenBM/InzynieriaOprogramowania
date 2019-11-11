# -*- coding: utf-8 -*-
import os
import re
from tkinter import *
from tkinter import filedialog
# from Tkinter import *
# import tkFileDialog as filedialog
import FileReader as filereader

#klasa interfejs użytkownika
class IU:
    def __init__(self): #konstruktor
        root = Tk()
        OpenFileButton = Button(root, text = "wczytaj pliki", command = self.openfiles)
        ExitButton = Button(root, text = "koniec", command = self.exit)
        OpenFileButton.pack()
        ExitButton.pack()
        root.mainloop()

    def openfiles(self): #metoda
        osSpecificFiles = []
        #konwertowanie ścieżek do plików na format specyficzny dla danego systemu operacyjnego
        root = filedialog.askdirectory(
            initialdir = ".",
            title = "Wybierz folder",
        )
        for path, subdirs, files in os.walk(root):
            for name in files:
                osSpecificFiles.append(os.path.join(path, name))

        #zamienianie ścieżek na specyficzne dla danego systemu operacyjnego
        for file in files:
            fileName = re.sub(r'[\\|/]', os.path.sep, file, 0)
            osSpecificFiles.append(fileName)
        fr = filereader.FileReader() #inicjowanie klasy fileReader
        fr.readFiles(osSpecificFiles)

    def exit(self) :
        sys.exit()
