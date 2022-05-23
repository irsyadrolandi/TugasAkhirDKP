#List Modul yang digunakan dalam Tugas ini : 
# Modul 1 : Variabel
# Modul 2 : if-else
# Modul 4 : Function
# Modul 8 : GUI

from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Aplikasi Penghitung Nilai Akhir")
#Membuat Tampilan
n_hadir = Entry(root, width=10, borderwidth=5)
n_tugas = Entry(root, width=10, borderwidth= 5)
n_uts = Entry(root, width=10, borderwidth= 5)
n_uas = Entry(root, width=10, borderwidth= 5)
#membuat label
judul = Label(root,text="Silahkan isi data-data berikut ! ",bg="blue")
isi = Label(root,text="Isian",bg="green")
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
#membuat tampilan tombol
def mulai(): #fungsi tombol
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
        messagebox.showinfo("Nilai Konversi","Nilai Anda adalah C (TINGKATKAN)")
    elif(has < 70 and has < 75):
        n_hasil.insert(0,str(has))
        messagebox.showinfo("Nilai Konversi","Nilai Anda adalah D (TINGKATKAN)")
    else :
        n_hasil.insert(0,str(has))
        messagebox.showinfo("Nilai Konversi","Nilai Anda adalah E (TINGKATKAN)")

#membuat tampilan hasil
hasil = Label(root,text="Nilai Anda Adalah : ")
n_hasil = Entry(root,width=10,borderwidth=5)
hasil.grid(column=0, row = 6)
n_hasil.grid(column=1,row=6)

olah = Button(root,text="klik",bg="green",command=mulai)
olah.grid(columnspan=2,rowspan=2)

root.mainloop()
