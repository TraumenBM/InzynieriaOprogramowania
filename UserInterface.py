import os
from tkinter import *
from tkinter import filedialog
#from Tkinter import *
#import tkFileDialog as filedialog
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
        files = filedialog.askopenfilenames(
            initialdir = ".",
            title = "Wybierz pliki",
            filetypes = (
                ("Pliki kodu", "*.php *.cpp *.py"),
                ("Pliki tekstowe", "*.txt"),
                ("Wszystkie pliki", "*.*")
            )
        )

        #zamienianie ścieżek na specyficzne dla danego systemu operacyjnego
        for file in files:
            fileName = file.replace('/', os.path.sep)
            osSpecificFiles.append(fileName)
        fr = filereader.FileReader() #inicjowanie klasy fileReader
        fr.readFiles(osSpecificFiles)

    def exit(self) :
        sys.exit()
