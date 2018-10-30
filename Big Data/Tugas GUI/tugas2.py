import tkinter as tk
import matplotlib.pyplot as plt
import pandas as pd 
from matplotlib import cm
from tkinter import filedialog
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def upload_file_csv():
    csv_path = filedialog.askopenfilename(initialdir = "",title = "Pilih file",filetypes = (("File CSV","*.csv"),("semua jenis file","*.*")))
    print(csv_path)
    lokasiFile.set(csv_path)
    data=pd.read_csv(csv_path,sep=';',index_col=False)
    print(data)
    
    ax.cla()
    colors = cm.hsv(data['value'] / float(max(data['value'])))
    ax.bar(data['no'],data['value'],0.35, color=colors)
    ax.grid()
    ax.set(ylabel='Value',xlabel='Data')
    
    canvasGrafik.draw()

halamanUtama = tk.Tk()
canvas = tk.Canvas(halamanUtama, width=900, height=700)
canvas.pack()

fig,ax = plt.subplots()

canvasGrafik = FigureCanvasTkAgg(fig, master=canvas)
canvasGrafik.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

lokasiFile = tk.StringVar()
lokasiFileWidget = tk.Entry(halamanUtama, textvariable=lokasiFile,width=30,state='readonly')
lokasiFileWidget.pack()

button = tk.Button(halamanUtama, text="Upload File",command=upload_file_csv)
button.pack()

halamanUtama.mainloop()