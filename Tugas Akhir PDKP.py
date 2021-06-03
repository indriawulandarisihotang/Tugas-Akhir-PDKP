from tkinter import * 
from tkinter import ttk
from tkinter import messagebox 

def submit():
    perkenalan = ""
    hargaatk = 0
    totalharga = 0
    if len(stringnama.get()) == 0:
        messagebox.showerror("Error","BELUM MENGISI NAMA PEMBELI")
        return
    if radio.get()== 0:
        messagebox.showerror("Error","BELUM MEMILIH UKURAN PESANAN")
        return
    if len(stringjumlah.get()) == 0:
        messagebox.showerror("Error","BELUM MEMILIH JUMLAH PESANAN")
        return
    if len(stringwarna.get()) == 0:
        messagebox.showerror("Error","BELUM MEMILIH WARNA PESANAN")
        return
    if len(stringnama.get()) == 0:
        messagebox.showerror("Error","BELUM MEMILIH NAMA ATK")
        return
    if len(stringtunai.get()) == 0:
        messagebox.showerror("Error","BELUM MENGISI TUNAI")
        return
    
    pesan = "Terimakasih telah membeli ATK di Toko kami" + "!!!"
    messagebox.showinfo("Greeting", pesan)
    
  
top = Tk()  
top.geometry("500x500")
top.title("Wonderland Stationary")
top.configure(bg="Pink")
top.title("start building your own PC")

#creating label  
lbJudul = Label (top, text = " Pembelian Alat Tulis \t:",bg="Pink").place (x=60,y=10)
lbnama = Label(top, text = "Nama Pembeli\t:",bg="Pink").place(x = 8,y = 40)    
lbukuran = Label(text = "Ukuran\t:",bg="Pink").place(x = 8, y=80)
lbjumlah = Label(text = "Jumlah\t:",bg="Pink").place(x=8, y=150)
lbwarna = Label(text = "Warna\t:",bg="Pink").place(x = 8,y = 190)
lbatk = Label(text = "Nama ATK\t:",bg="Pink").place(x = 8,y = 230)
lbtunai = Label(text = "Tunai\t:",bg="Pink").place(x = 8,y = 330)

#create input  
stringnama = StringVar()
inama = Entry(top,width = 45, textvariable=stringnama).place(x = 110, y = 40)  

#create radio
radio = IntVar()
R1 = Radiobutton(top, text="Besar", variable=radio, value=1).place(x=105, y=80)  
R2 = Radiobutton(top, text="Sedang", variable=radio, value=2).place(x=105, y=100)  
R3 = Radiobutton(top, text="Kecil", variable=radio, value=3).place(x=105, y=120)  

#create input
stringjumlah = StringVar()
ijumlah = Entry(top,width = 45, textvariable=stringjumlah).place(x=110, y=150)

#create input
stringwarna = StringVar()
iwarna = Entry(top,width = 45, textvariable=stringwarna).place(x = 110, y = 190)

#create radio
harga = IntVar()
R1 = Radiobutton(top, text="Pensil (Rp 3.000)", variable=harga, value=1).place(x=110, y=230)  
R2 = Radiobutton(top, text="Pulpen (Rp 3.000)", variable=harga, value=2).place(x=110, y=250)  
R3 = Radiobutton(top, text="Buku (Rp 5.000)",variable=harga, value=3).place(x=110, y=270)
R4 = Radiobutton(top, text="Penggaris (Rp 6.000)", variable=harga, value=4).place(x=110, y=290)
R5 = Radiobutton(top, text="Lem Kertas (Rp 3.000)", variable=harga, value=5).place(x=280, y=230)  
R6 = Radiobutton(top, text="Penghapus (Rp 2.000", variable=harga, value=6).place(x=280, y=250)  
R7 = Radiobutton(top, text="Rautan (Rp 1.000)",variable=harga, value=7).place(x=280, y=270)
R8 = Radiobutton(top, text="Tip Ex (Rp 5.000)", variable=harga, value=8).place(x=280, y=290)

#create input
stringtunai = StringVar()
itunai = Entry(top,width = 45, textvariable=stringtunai).place(x = 110, y = 330)

#create button
btn1 = Button(top, command = submit, text="SUBMIT").place(x=250,y=450)

top.mainloop()