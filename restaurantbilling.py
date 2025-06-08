from tkinter import *
import random
from datetime import datetime
from PIL import Image, ImageTk
import requests
from io import BytesIO

# Root window setup
root = Tk()
root.geometry("1200x650+100+20")
root.title("Restaurant Management System")

# Frames
f = Frame(root, bd=10, relief=GROOVE)
f.pack(side=TOP)

f1 = Frame(root, bd=5, height=400, width=300, relief=RAISED)
f1.pack(side=LEFT, fill="both", expand=1)

f2 = Frame(root, bd=5, height=400, width=300, relief=RAISED, bg="light yellow")
f2.pack(side=RIGHT, fill="both", expand=1)

# Load image from URL
response = requests.get("https://as2.ftcdn.net/v2/jpg/03/88/83/57/1000_F_388835719_U5apiVhloXpwIo3yVEdgh2ZMW5zJ1XIM.jpg")
image = Image.open(BytesIO(response.content))
tk_image = ImageTk.PhotoImage(image.resize((300, 120)))

lbl_info = Label(f, font=('arial', 30, 'bold'), text="Restaurant Billing System", image=tk_image, compound='left', fg="white", bg="brown", padx=20)
lbl_info.grid(row=0, column=0)

# Date and Time
now = datetime.now()
localtime = now.strftime("%d/%m/%Y %H:%M:%S")

# Variables
rand = StringVar()
Dosa = StringVar()
Pongal = StringVar()
Vadai = StringVar()
Poori = StringVar()
Total = StringVar()
Service_Charge = StringVar()
Idly = StringVar()
tax = StringVar()
cost = StringVar()
date = StringVar()
Coffee = StringVar()
Tea = StringVar()

# Food Entry Fields
items = [("Idly Rs.20", Idly), ("Dosa Rs.30", Dosa), ("Pongal Rs.50", Pongal),
         ("Vadai Rs.20", Vadai), ("Poori Rs.20", Poori), ("Tea Rs.10", Tea), ("Coffee Rs.10", Coffee)]

for i, (label_text, var) in enumerate(items):
    Label(f1, font=('arial', 20, 'bold'), text=label_text, width=12, fg="blue4", bd=10).grid(row=i+1, column=0)
    Entry(f1, font=('arial', 20, 'bold'), textvariable=var, bd=6, width=8, bg="misty rose").grid(row=i+1, column=1)

# Billing Display
fields = [("Bill No", rand), ("Date", date), ("Cost", cost),
          ("Service", Service_Charge), ("Tax", tax), ("Total", Total)]

for i, (label_text, var) in enumerate(fields):
    Label(f2, font=('arial', 18, 'bold'), text=label_text, fg="blue", pady=5, bg="light yellow").grid(row=i, column=0, sticky='w')
    Entry(f2, font=('arial', 16, 'bold'), textvariable=var, bd=6, insertwidth=2, bg="misty rose", justify='right').grid(row=i, column=1)

# Generate Bill Function
def generate_bill():
    bill_no = str(random.randint(15000, 50000))
    rand.set(bill_no)
    date.set(localtime)

    try:
        qd = int(Dosa.get() or 0)
        qp = int(Pongal.get() or 0)
        qv = int(Vadai.get() or 0)
        qpoori = int(Poori.get() or 0)
        qc = int(Coffee.get() or 0)
        qi = int(Idly.get() or 0)
        qt = int(Tea.get() or 0)
    except ValueError:
        cost.set("Invalid input")
        return

    # Prices
    costofdosa = qd * 30
    costofpongal = qp * 50
    costofvadai = qv * 20
    costofpoori = qpoori * 20
    costofidly = qi * 20
    costofcoffee = qc * 10
    costoftea = qt * 10

    Totalcost = costofdosa + costofpongal + costofvadai + costofpoori + costofidly + costofcoffee + costoftea
    payTax = round(Totalcost * 0.18, 2)
    ser_charge = round(Totalcost * 0.01, 2)
    overall = round(Totalcost + payTax + ser_charge, 2)

    cost.set(f"Rs. {Totalcost:.2f}")
    tax.set(f"Rs. {payTax:.2f}")
    Service_Charge.set(f"Rs. {ser_charge:.2f}")
    Total.set(f"Rs. {overall:.2f}")

# Reset Function
def reset():
    for var in [Dosa, Pongal, Poori, Idly, Vadai, Coffee, Tea, date, rand, tax, cost, Service_Charge, Total]:
        var.set("")

# Exit Function
def qexit():
    root.destroy()

# Buttons
btn_Total = Button(f1, bd=5, fg="black", font=('arial', 16, 'bold'), width=14, text="CALCULATE", bg="green", command=generate_bill)
btn_Total.grid(row=9, column=0, padx=10, pady=10)

btn_reset = Button(f1, bd=5, fg="black", font=('arial', 16, 'bold'), width=10, text="RESET", bg="green", command=reset)
btn_reset.grid(row=9, column=1, padx=10, pady=10)

btn_exit = Button(f1, bd=5, fg="black", font=('arial', 16, 'bold'), width=10, text="EXIT", bg="green", command=qexit)
btn_exit.grid(row=9, column=2, padx=10, pady=10)

# Start the GUI loop
root.mainloop()
