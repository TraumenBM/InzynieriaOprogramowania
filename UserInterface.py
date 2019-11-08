from Tkinter import *
import tkFileDialog as filedialog
import FileReader as filereader

class IU:
    def __init__(self):
        root = Tk()
        OpenFileButton = Button(root, text = "wczytaj plik", command = self.openfiles)
        ExitButton = Button(root, text = "koniec", command = self.exit)
        OpenFileButton.pack()
        ExitButton.pack()
        root.mainloop()

    def openfiles(self):
        files = filedialog.askopenfilenames(
            initialdir = "/var/www/InzynieriaOprogramowania",
            title = "Wybierz pliki",
            filetypes = (
                ("Pliki kodu", "*.php *.cpp *.py"),
                ("Pliki tekstowe", "*.txt"),
                ("Wszystkie pliki", "*.*")
            )
        )
        fr = filereader.FileReader()
        fr.readFiles(files)

    def exit(self) :
        sys.exit()
