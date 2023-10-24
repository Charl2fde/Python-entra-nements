import tkinter as tk

def valider_inscription():
    pseudo = pseudo_entry.get()
    mdp = mdp_entry.get()
    email = email_entry.get()
    print(f"Pseudo : {pseudo}")
    print(f"Mot de passe : {mdp}")
    print(f"Email : {email}")

app = tk.Tk()
app.title("Inscription")

pseudo_label = tk.Label(app, text="Pseudo")
pseudo_label.pack()
pseudo_entry = tk.Entry(app)
pseudo_entry.pack()

mdp_label = tk.Label(app, text="Mot de passe")
mdp_label.pack()
mdp_entry = tk.Entry(app, show="*")  
mdp_entry.pack()

email_label = tk.Label(app, text="Email")
email_label.pack()
email_entry = tk.Entry(app)
email_entry.pack()

valider_button = tk.Button(app, text="Valider", command=valider_inscription)
valider_button.pack()

app.mainloop()

