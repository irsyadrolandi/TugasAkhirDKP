#List Modul yang digunakan dalam Tugas ini : 
# Modul 1 : Variabel
# Modul 2 : if-else
# Modul 3 : For
# Modul 4 : Function
# Modul 7 : Stack
# Modul 8 : GUI


import random
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Progressbar
from tkinter.messagebox import *
from turtle import window_width
import time

Nilai = []
window = Tk()
root = Tk()
root.title("Aplikasi Penghitung Nilai Akhir")
#Membuat Tampilan
n_hadir = Entry(root, width=10, borderwidth=5)
n_tugas = Entry(root, width=10, borderwidth= 5)
n_uts = Entry(root, width=10, borderwidth= 5)
n_uas = Entry(root, width=10, borderwidth= 5)
#membuat label
judul = Label(root,text="Silahkan isi data-data berikut ! ",bg="light blue")
isi = Label(root,text="Isian",bg="pink")
hadir = Label(root,text="Nilai Kehadiran : ")
tugas = Label(root,text="Nilai Tugas : ")
uts = Label(root,text="Nilai UTS : ")
uas = Label(root,text="Nilai UAS : ")
pemberitahuan = Label(root,text="Hasil Nilai Anda Dibawah Ini")
#menampilkan
judul.grid(column=0,row=0) 
isi.grid(column=1,row=0)
hadir.grid(column=0,row=1)
n_hadir.grid(column=1,row=1)
tugas.grid(column=0,row=2)
n_tugas.grid(column=1,row=2)
uts.grid(column=0,row=3)
n_uts.grid(column=1,row=3)
uas.grid(column=0,row=4)
n_uas.grid(column=1,row=4)
pemberitahuan.grid(column=0, row=5)
#Tampilan tombol
def mulai(): #function tombol
    a = int(n_hadir.get())
    b = int(n_tugas.get())
    c = int(n_uts.get())
    d = int(n_uas.get())
    has = (a + b + c + d)/4
    if has > 85 : 
        n_hasil.insert(0,str(has))
        messagebox.showinfo("Nilai Konversi","Nilai Anda adalah A (PERTAHANKAN) ")
    elif(has < 80 and has < 85):
        n_hasil.insert(0,str(has))
        messagebox.showinfo("Nilai Konversi","Nilai Anda adalah B (PERTAHANKAN DAN TINGKATKAN)")
    elif(has < 75 and has < 80):
        n_hasil.insert(0,str(has))
        messagebox.showinfo("Nilai Konversi","Nilai Anda adalah C (TINGKATKAN TERUS)")
    elif(has < 70 and has < 75):
        n_hasil.insert(0,str(has))
        messagebox.showinfo("Nilai Konversi","Nilai Anda adalah D (TINGKATKAN LAGI)")
    else :
        n_hasil.insert(0,str(has))
        messagebox.showinfo("Nilai Konversi","Nilai Anda adalah E (TINGKATKAN YA)")

#Tampilan hasil
hasil = Label(root,text="Nilai Anda Adalah : ")
n_hasil = Entry(root,width=10,borderwidth=5)
hasil.grid(column=0, row = 6)
n_hasil.grid(column=1,row=6)

olah = Button(root,text="klik",bg="light blue",command=mulai)
olah.grid(columnspan=2,rowspan=2)

#Stack
window.title("Data Nilai Siswa")
def stackPush():
    data = userInput.get()
    Nilai.append(data)
    userInput.set("")
def stackPop():
    Nilai.pop()


labelNilai = Label(window,text = "Masukkan Nilai Rata Rata yang sudah dihitung : \n").pack(side=TOP)
userInput = StringVar()
entry = Entry(window,textvariable=userInput).pack(side=TOP)

def tampilData():
    global showNama
    showNama.configure(state="normal")
    showNama.delete(1.0,"end")
    showNama.insert("end", "Nama Dan Nilai  : \n")
    showNama.insert("end", '\n'.join(Nilai))
    showNama.configure(state="disabled")

#buttons
buttonSubmit = Button(window, text="Submit",bg="light green", command=lambda: [stackPush(), tampilData()]).pack(pady=5)
buttonPop = Button(window, text= "Delete",bg="light blue", command=lambda: [stackPop(), tampilData()]).pack(pady=5)

#tampil Nilai Rata Rata
showNama = Text(window, width=25, height= 8)
showNama.insert("end", "Nama Dan Nilai  : ")
showNama.insert("end", '\n'.join(Nilai))
showNama.configure(state="disabled")
showNama.pack(pady=5)

#loading bar dan random function Bonus
def randomFunction():
    global showWinner
    pb['value'] = 0
    for i in range(100):
        window.update_idletasks()
        pb['value'] += 1
        time.sleep(1/100)
    showWinner.configure(state="normal")
    if Nilai:
        winner = random.choice(Nilai)
        Nilai.remove(winner)
        showWinner.insert("end","Selamat kepada ")
        showWinner.insert("end", winner)
        showWinner.insert("end", '\n')
    else:
        messagebox.showwarning("Perhatian!", "Tidak ada yang dapat bonus")
    showWinner.configure(state="disabled")

buttonGenerate = Button(window, text="Cari Pemenang",bg="light blue", command=lambda: [randomFunction(), tampilData()]).pack()
showWinner = Text(window, width=20, height= 3)
showWinner.insert("end", "YANG MENDAPAT BONUS LIMA POIN ADALAH : \n")
showWinner.configure(state="disabled")
showWinner.pack(pady=5)

pb = Progressbar(
    window,
    orient = HORIZONTAL,
    length = 250,
    mode = 'determinate'
    )
pb.pack(side= BOTTOM, pady=35)

window.mainloop()
root.mainloop()
