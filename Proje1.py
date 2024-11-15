from tkinter import *
from tkinter import ttk

root = Tk()
root.geometry("800x800")
root.title("Proje 1")

label = Label(root, text="Metin Girişi",font=("constantia",17))
label.pack()

e = Entry(root, width=80)
e.pack()

# 1. İSTER:
def letters():
    letters = []
    label = e.get()
    for i in label:
        letters.append(i)
        letters.append("\n")
    final_str = "".join(letters)    
    myLabel = Label(root, text= final_str)
    myLabel.pack()

# 2. İSTER:
def strs():
    label = e.get()
    words = label.split()
    reversed_words = []
    for word in words:
        reversed_words.append(word[::-1])
    reversed_sentence = " ".join(reversed_words)
    normal = Label(root, text= "Cümlenin orjinali:  " + label)
    reverse = Label(root, text="Tamamen tersi alınmış hali:  " + label[::-1])
    reversed_letters = Label(root, text="Kelime kelime tersi alınmış hali:  " + reversed_sentence)
    normal.pack()
    reverse.pack()
    reversed_letters.pack()

# 3. İSTER:
def aLetter():   
    new_list = []
    label = e.get()
    for i in label:
        if(i == "a"):
            i = "A"
            new_list.append(i)
        else:
            new_list.append(i)
    final_str = "".join(new_list) 
    letter = Label(root, text= final_str)
    letter.pack()

# 4. İSTER: 
def like_list():
    words = []
    label = e.get().split()
    words.append("[")
    for i in label:
        words.append("'" + i + "'" + ",")
    words.append("]")
    final_letter = "".join(words)
    letter = Label(root,text=final_letter)
    letter.pack()

# 5. İSTER:
def join():
    letters = []
    label = e.get()
    for i in label:
        if(i == " "):
            continue
        else:
            letters.append(i)
    final_str = "".join(letters)
    letter = Label(root, text=final_str)
    letter.pack()

# 6. İSTER:
def vowels():
    vowel = ["a","e","ı","i","o","ö","u","ü"]
    label = e.get()
    count = 0
    for i in label:
        if( i in vowel):
            count += 1
    vowel_count = Label(root, text="Metindeki ünlü harf sayısı:  "+ str(count))
    vowel_count.pack()



def selected(event=None):  
    
    option = clicked.get()  
    if option == "Harfleri Alt Alta Yazdırma":
        letters()
    elif option == "Ters Metin ve Ters Kelimeli Metin":
        strs()
    elif option == "'a' Harflerini Büyüğe Çevirme":
        aLetter()
    elif option == "Kelimeleri Ayrı Ayrı Yazma":
        like_list()
    elif option == "Ayrı Olan Kelimeleri Birleştirme":
        join()
    elif option == "Ünlü Harf Sayısı Bulma":
        vowels()

options = [
    "Harfleri Alt Alta Yazdırma",
    "Ters Metin ve Ters Kelimeli Metin",
    "'a' Harflerini Büyüğe Çevirme",
    "Kelimeleri Ayrı Ayrı Yazma",
    "Ayrı Olan Kelimeleri Birleştirme",
    "Ünlü Harf Sayısı Bulma",
]

clicked = StringVar()
clicked.set(options[0]) 

myCombo = ttk.Combobox(root,value=options, textvariable=clicked) 
myCombo.current(0)
myCombo.pack()

myButton = Button(root, text="Çalıştır", command=lambda: selected())  
myButton.pack()

root.mainloop()
