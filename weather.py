# Import 
from tkinter import *

def search():
    pass


app = Tk()
app.title('Weather App')
app.geometry('700x350')

city_text = StringVar()
city_entry = Entry(app, textvariable=city_text)
city_entry.pack()

search_btn =Button(app, text='Search Weather', width=12, command=search)
search_btn.pack()

location_lbl = Label(app, text='location', font=('bold', 20))
location_lbl.pack()

image = Label(app, bitmap='')
image.pack()

temp_lbl = Label(app, text='temperate')

app.mainloop()