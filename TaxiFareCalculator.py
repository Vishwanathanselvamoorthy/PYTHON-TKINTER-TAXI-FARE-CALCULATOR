import tkinter as tk

basePay = 50
kmPerHr = 10

currency_symbol = "RS. "

def total():
    
    try:
        travelKms = int(entry.get())
        
        KmsPay = kmPerHr * travelKms
        
        EstimatedPay = basePay + KmsPay
        
        base_pay_label.config(text=f"Base Pay: {currency_symbol}{basePay}")
        
        distance_cost_label.config(text=f"Distance Cost: {currency_symbol}{KmsPay}")
        
        total_label.config(text=f"Total: {currency_symbol}{EstimatedPay}", font=("Helvetica", 30, 'bold'), fg='#2ecc71')
        
        
    except ValueError:
        
        total_label.config(text="PLEASE ENTER THE VALID NUMBER OF KMS !", font=('Times', 20, 'bold'), fg='#C0392B')
        

def reset():
    
    entry.delete(0, tk.END)
    
    base_pay_label.config(text="")
    
    distance_cost_label.config(text="")
    
    total_label.config(text="", font=('Times', 30, 'bold'))
    
    

app = tk.Tk()

app.title("Taxi Pay")

app.configure(bg='#FF5733')  # Using a shade of red



headingLabel = tk.Label(app, text="TAXI   FARE   CALCULATOR", font=("Helvetica", 60, 'bold'), bg='#FF5733', foreground="White")

headingLabel.pack(pady=20)

tk.Label(app, text="ENTER THE KMS TAXI TRAVELLED:", font=("Helvetica", 40, 'bold'), bg='#FF5733').pack(pady=10)


entry = tk.Entry(app, font=('Times', 30, 'bold'),width=40,borderwidth=15,border=15)

entry.pack(pady=40)

entry.insert(0,"KMs: ")



calculateButton = tk.Button(app, text="CALCULATE", command=total, font=('Times', 30, 'bold'),border=10,borderwidth=10)

calculateButton.pack(pady=10)



base_pay_label = tk.Label(app, bg='#FF5733', font=('Times', 20, 'bold'))

base_pay_label.pack(pady=5)



distance_cost_label = tk.Label(app, bg='#FF5733', font=('Times', 20, 'bold'))

distance_cost_label.pack(pady=5)



total_label = tk.Label(app, bg='#FF5733')

total_label.pack(pady=10)



resetButton = tk.Button(app, text="RESET", command=reset, font=('Times', 20, 'bold'),border=5,borderwidth=5)

resetButton.pack(pady=10)



app.mainloop()











