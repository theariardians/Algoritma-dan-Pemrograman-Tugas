#Nama   : Ari Ardiansyah
#NIM    : 210741031

from tkinter import *
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    
class BalikKata:
    def __init__(self, induk, judul):
        self.induk = induk
         
        self.induk.title(judul)
        self.induk.protocol("WM_DELETE_WINDOW", self.tutup)
        self.induk.resizable(False, False)
         
        self.aturKomponen()
         
        self.entInput.focus_set()
         
    def aturKomponen(self):
        # atur frame utama
        mainFrame = Frame(self.induk)
        mainFrame.pack(fill=BOTH, expand=YES)
         
        ## atur frame data
        fr_data = Frame(mainFrame, bd=10)
        fr_data.pack(fill=BOTH, expand=YES)
         
        # atur komponen input teks
        self.entInput = Entry(fr_data, fg="blue")
        self.entInput.pack(side=LEFT, expand=YES)
         
        # atur tombol Reverse String
        self.btnBalik = Button(fr_data, text='REVERSE STRING',
                command=self.balikKata)
        self.btnBalik.pack(side=LEFT, expand=YES, padx=5)
         
        # atur komponen output teks
        self.entOutput = Entry(fr_data, fg="red")
        self.entOutput.pack(side=LEFT, expand=YES)
         
                 
    def balikKata(self, event=None):
        kata = self.entInput.get()
         
        balikan = ''.join(reversed(kata))
         
        self.entOutput.delete(0, END)
        self.entOutput.insert(END, balikan)
         
    def tutup(self, event=None):
        self.induk.destroy()
         
if __name__ == '__main__':
    root = Tk()
     
    app = BalikKata(root, "Reverse String")
     
    root.mainloop()