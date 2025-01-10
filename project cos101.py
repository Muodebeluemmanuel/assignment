Igbo_dictionary = {"bia": 'come',
                   "eze": 'king',
                   "nri": 'food',
                   "isi": 'head',
                   "ire": 'tongue',
                   "onu": 'mouth',
                   "aka": 'hand',
                   "nkita": 'dog',
                   "agwa": 'beans',
                   "akpa": 'bag',
                   "nye": 'give/present',
                   "chineke": 'lord',
                   "ehi": 'cow',
                   "ewu": 'goat',
                   "ube": 'pear',
                   "imela": 'thank you',
                   "oyi": 'cold',
                   "ekpere": 'prayer',
                   "ego": 'money',
                   "chukwu": 'God'}

Spanish_dictionary ={"hola": 'hello',
                     "adios": 'goodbye',
                     "gracias":'thank you',
                     "por favor":'please',
                     "si": 'yes',
                     "no":'no',
                     "buenos dias":'good morning',
                     "buenas noches":'good night',
                     "lo siento":'I am sorry',
                     "familia":'family',
                     "amigo":'friend',
                     "luz":'light',
                     "agua":'water',
                     "comida":'food',
                     "casco":'helmet',
                     "zapatos":'shoes'}
Igala_dictionary={"Gba":'take',        
              "Oskapa" : 'Rice',
              "Oji" : 'Head',
              "Eju" : 'Face',
              "Efu" : 'Stomach',
              "Ehi" : 'Cook',
              "Adide" : 'Guard',
              "Ojika" : 'Shoulder',
              "Okwukwu" : 'Kneel',
              "Agba" : 'Jaw',
              "Ubi" : 'Back',
              "Imi" : 'Breath',
              "Imo" : 'Nose',
              "Unyi" : 'House',
              "Ule era" : 'Run',
              "Agba" : 'Thank you',
              "Omi" : 'Fish',
              "Eti" : 'Ear',
              "Oli" : 'Tree',
              "L'olu" : 'Sleep'}
Hausa_dictionary={"zo" : 'come'
                  "tafi" : 'go',
                  "abinchi" : 'food',
                  "shiga" : 'enter',
                  "gudu" : 'run',
                  "waya" : 'phone',
                  "ni" : 'me',
                  "su" : 'them',
                  "shi" : 'him',
                  "ita" : 'her',
                  "lemu" : 'orange',
                  "daba" : 'animal',
                  "kujera" : 'chair',
                  "takalmi" : 'chair',
                  "waje" : 'outside',
                  "kalmomi" :'alphabets',
                  "fanca" :'fan',
                  "kasa" : 'sand',
                  "allo" : 'board',
                  "shiga" : 'enter'}
   from tkinter import  TK, Entry, Button,Label,StringVar
   
    window=TK()
    window.geometry("688×255")
    window.title("Igala_dictionary")
    
    word.Stringvar()
    word_entry.Entry(window,textvariable=word,font.('ariel',19))
    word_entry.pack()
    
    result=StringVar()
    result_label=Label(window, textvariable=result)
    result_label.pack()
    
    def search (word):
        if word in Igala_dictionary:
            result.set(Igala_dictionary[word])
            print(Igala_dictionary[word])
        else:
            result.set("not found")
            
    search_btn=Button(window, text="search", command=lambda: search(word.get()))
    search_btn.pack
    
    exit_button=Button(window,text="exit",command=lambda: exit())
    exit_button.pack()
    
    word_entry=Entry(window, textvariable=word, font=('ariel', 19))
    window.mainloop()
    
from tkinter import Tk, Entry, Button, Label, StringVar,Menubutton,Menu

window = Tk()
window.geometry("600x250")
window.title("Igbo_dictionary")


mb= Menubutton(window,text="Select language")
mb.menu= Menu(mb)
mb["menu"]=mb.menu



def openNewWindow():
    word = StringVar()
    word_entry = Entry(window, textvariable=word, font=('ariel', 19))
    word_entry.pack()


    result = StringVar()
    result_label = Label(window, textvariable=result)
    result_label.pack()


    def search (word):
        if word in Igbo_dictionary:
            result.set(Igbo_dictionary[word])
            print(Igbo_dictionary[word])
        else:
            result.set("not found")


    search_btn = Button(window, text="search", command=lambda: search(word.get()))
    search_btn.pack()
word.Stringvar()
    word_entry.Entry(window,textvariable=word,font.('ariel',19))
    word_entry.pack()
    
    result=StringVar()
    result_label=Label(window, textvariable=result)
    result_label.pack()
    
    def search (word):
        if word in Igala_dictionary:
            result.set(Igala_dictionary[word])
            print(Igala_dictionary[word])
        else:
            result.set("not found")
            
    search_btn=Button(window, text="search", command=lambda: search(word.get()))
    search_btn.pack

def spanish():
     word = StringVar()
     word_entry = Entry(window, textvariable=word, font=('ariel', 19))
     word_entry.pack()


     result = StringVar()
     result_label = Label(window, textvariable=result)
     result_label.pack()


     def search (word):
        if word in Spanish_dictionary:
            result.set(Spanish_dictionary[word])
            print(Spanish_dictionary[word])
        else:
            result.set("not found")
            
     search_btn = Button(window, text="search", command=lambda: search(word.get()))
     search_btn.pack()
def Hausa():
     word = StringVar()
     word_entry = Entry(window, textvariable=word, font=('ariel', 19))
     word_entry.pack()


     result = StringVar()
     result_label = Label(window, textvariable=result)
     result_label.pack()


     def search (word):
        if word in Hausa_dictionary:
            result.set(Hausa_dictionary[word])
            print(Hausa_dictionary[word])
        else:
            result.set("not found")
            
     search_btn = Button(window, text="search", command=lambda: search(word.get()))
     search_btn.pack()

mb.menu.add_command(label="Igbo dictionary",command=(openNewWindow))
mb.pack()

menu2_btn=Button(window,text="spanish Language",command=(spanish))
menu2_btn.pack() 
menu3_btn=Button(window,text="Igala Language",command=(Hausa))
menu3_btn.pack() 


window.mainloop()

