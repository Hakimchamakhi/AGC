from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import mysql.connector
import configparser
import os

# Read database configuration from config.ini
config = configparser.ConfigParser()
config.read(os.path.join(os.path.dirname(__file__), 'config.ini'))

DB_HOST = config.get('database', 'host')
DB_NAME = config.get('database', 'database')
DB_USER = config.get('database', 'user')
DB_PASS = config.get('database', 'password')

def update(rows):
	trv.delete(*trv.get_children())
	for i in rows:
		trv.insert('', 'end', values=i)

def search():
	q2 = q.get()
	query = "SELECT num_rtb, nom_client, nom_adv, tribunal, num_chkaya, dossier_jd, date, place_re, dernier_re FROM tbl_chkaya WHERE num_rtb LIKE '%"+q2+"%' OR nom_client LIKE '%"+q2+"%' OR nom_adv LIKE '%"+q2+"%' OR tribunal LIKE '%"+q2+"%' OR dossier_jd LIKE '%"+q2+"%' OR date LIKE '%"+q2+"%' OR num_chkaya LIKE '%"+q2+"%' "
	cursor.execute(query)
	rows = cursor.fetchall()
	update(rows)

def clear():
	query="SELECT num_rtb, nom_client, nom_adv, tribunal, num_chkaya, dossier_jd, date, place_re, dernier_re FROM tbl_chkaya ORDER BY num_rtb DESC"
	cursor.execute(query)
	rows = cursor.fetchall()
	update(rows)

def clearchamps():
    t1.set("")
    t2.set("")
    t3.set("")
    t4.set("")
    t5.set("")
    t6.set("")
    t7.set("")
    t8.set("")
    t9.set("")

def getrow(event):
	rowid = trv.identify_row(event.y)
	item = trv.item(trv.focus())
	t1.set(item['values'][0])
	t2.set(item['values'][1])
	t3.set(item['values'][2])
	t4.set(item['values'][3])
	t5.set(item['values'][4])
	t6.set(item['values'][5])
	t7.set(item['values'][6])
	t8.set(item['values'][7])
	t9.set(item['values'][8])

def update_customer():
	num_rtb = t1.get()
	nom_client = t2.get()
	nom_adv = t3.get()
	tribunal = t4.get()
	num_chkaya = t5.get()
	dossier_jd = t6.get()
	date = t7.get()
	place_re = t8.get()
	dernier_re = t9.get()

	if messagebox.askyesno("Confirmation", "Confirmation de mettre à jour client"):
		query = "UPDATE tbl_chkaya SET  num_rtb = %s, nom_client = %s, nom_adv = %s, tribunal = %s, num_chkaya = %s, dossier_jd = %s, date = %s, place_re = %s, dernier_re = %s where num_rtb= %s"
		cursor.execute(query,( num_rtb, nom_client, nom_adv, tribunal, num_chkaya, dossier_jd, date, place_re, dernier_re, num_rtb ))
		mydb.commit()
		clear()
	else:
		return True

def add_new():
	num_rtb = t1.get()
	nom_client = t2.get()
	nom_adv = t3.get()
	tribunal = t4.get()
	num_chkaya = t5.get()
	dossier_jd = t6.get()
	date = t7.get()
	place_re = t8.get()
	dernier_re = t9.get()
	cursor.execute("SELECT * FROM tbl_chkaya WHERE num_rtb = '"+num_rtb+"'")
	test = cursor.rowcount
	if (test == 1):
		messagebox.showerror("Erreur", "Ce dossier déja exist")
	else:
		query = "INSERT INTO tbl_chkaya Values(%s, %s, %s, %s, %s, %s, %s, %s, %s )"
		cursor.execute(query, (num_rtb, nom_client, nom_adv, tribunal, num_chkaya, dossier_jd, date, place_re, dernier_re))
		messagebox.showinfo("Message", "Ce dossier a été ajouté")
		mydb.commit()
		clear()
 
    

def delete_customer():
	refd = t1.get()    
	if messagebox.askyesno("Confirmation", "Confirmation de suppression de client"):
		query = "DELETE From tbl_chkaya WHERE num_rtb='"+refd+"'"
		cursor.execute(query)
		mydb.commit()
		clear()
	else:
		return True
    

mydb = mysql.connector.connect(host=DB_HOST, database=DB_NAME, user=DB_USER, passwd=DB_PASS)
cursor = mydb.cursor(buffered=True)

root = Tk()
q = StringVar()
t1 = StringVar()
t2 = StringVar()
t3 = StringVar()
t4 = StringVar()
t5 = StringVar()
t6 = StringVar()
t7 = StringVar()
t8 = StringVar()
t9 = StringVar()

wrapper1 = LabelFrame(root, text="Liste des clients")
wrapper2 = LabelFrame(root, text="Rechercher un client")
wrapper3 = LabelFrame(root, text="Mettre à jour un client")

wrapper1.pack(fill="both", expand="yes", side=TOP, padx=20, pady=10)
wrapper2.pack(fill="both", expand="yes", side=LEFT, padx=20, pady=10)
wrapper3.pack(fill="both", expand="yes", side=RIGHT, padx=20, pady=10)

style = ttk.Style()
style.configure("mystyle.Treeview", highlightthickness=0, bd=0, font=('Calibri', 10)) # Modify the font of the body
style.configure("mystyle.Treeview.Heading", font=('Calibri', 11,'bold')) # Modify the font of the headings

trv = ttk.Treeview(wrapper1, columns=(1,2,3,4,5,6,7,8,9), show="headings", style="mystyle.Treeview")
trv.pack(fill="both", expand="yes", side=LEFT)



trv.heading(1, text="العدد الرتبي")
trv.heading(2, text="المنوب")
trv.heading(3, text="الضد")
trv.heading(4, text="المحكمة")
trv.heading(5, text="عدد الشكاية")
trv.heading(6, text="المحضر")
trv.heading(7, text="التاريخ")
trv.heading(8, text="مكان البحث")
trv.heading(9, text="آخر إجراء")
trv.column(1, width=130, minwidth=100)
trv.column(2, width=150, minwidth=100)
trv.column(3, width=130, minwidth=100)
trv.column(4, width=130, minwidth=100)
trv.column(5, width=150, minwidth=100)
trv.column(6, width=150, minwidth=100)
trv.column(7, width=150, minwidth=100)
trv.column(8, width=150, minwidth=100)
trv.column(9, width=150, minwidth=100)

trv.bind('<Double 1>', getrow)

#vertical scrollbar
yscrollbar = ttk.Scrollbar(trv, orient="vertical", command=trv.yview)
yscrollbar.pack(side=RIGHT, fill="y")

trv.configure(yscrollcommand=yscrollbar.set)


query = "SELECT num_rtb, nom_client, nom_adv, tribunal, num_chkaya, dossier_jd, date, place_re, dernier_re FROM tbl_chkaya ORDER BY num_rtb DESC"
cursor.execute(query)
rows = cursor.fetchall()
update(rows)


#search section
lbl = Label(wrapper2, text="Recherche")
lbl.pack(side=tk.LEFT, padx=10)
ent = Entry(wrapper2, bd=2, width=30, textvariable=q)
ent.pack(side=tk.LEFT, padx=6)
btn = Button(wrapper2, bd=3, bg="#D3D3D3", activebackground="#D3D3D3", width=13, text="Recherche", command=search)
btn.pack(side=tk.LEFT, padx=6)
cbtn = Button(wrapper2, bd=3, bg="#D3D3D3", activebackground="#D3D3D3", width=13, text="Initialiser", command=clear)
cbtn.pack(side=tk.LEFT, padx=6)

#User ADD MODIFY DELETE Section
lbl1 = Label(wrapper3, text="العدد الرتبي")
lbl1.grid(row=0, column=0, padx=5, pady=3)
ent1 = Entry(wrapper3, bd=2, width=30, textvariable=t1)
ent1.grid(row=0, column=1, padx=5, pady=3)

lbl2 = Label(wrapper3, text="المنوب")
lbl2.grid(row=1, column=0, padx=5, pady=3)
ent2 = Entry(wrapper3, bd=2, width=30, textvariable=t2)
ent2.grid(row=1, column=1, padx=5, pady=3)

lbl3 = Label(wrapper3, text="الضد")
lbl3.grid(row=2, column=0, padx=5, pady=3)
ent3 = Entry(wrapper3, bd=2, width=30, textvariable=t3)
ent3.grid(row=2, column=1, padx=5, pady=3)

lbl4 = Label(wrapper3, text="المحكمة")
lbl4.grid(row=3, column=0, padx=5, pady=3)
ent4 = Entry(wrapper3, bd=2, width=30, textvariable=t4)
ent4.grid(row=3, column=1, padx=5, pady=3)

lbl5 = Label(wrapper3, text="عدد الشكاية")
lbl5.grid(row=4, column=0, padx=5, pady=3)
ent5 = Entry(wrapper3, bd=2, width=30, textvariable=t5)
ent5.grid(row=4, column=1, padx=5, pady=3)

lbl6 = Label(wrapper3, text="المحضر")
lbl6.grid(row=5, column=0, padx=5, pady=3)
ent6 = Entry(wrapper3, bd=2, width=30, textvariable=t6)
ent6.grid(row=5, column=1, padx=5, pady=3)

lbl7 = Label(wrapper3, text="التاريخ")
lbl7.grid(row=6, column=0, padx=5, pady=3)
ent7 = Entry(wrapper3, bd=2, width=30, textvariable=t7)
ent7.grid(row=6, column=1, padx=5, pady=3)

lbl8 = Label(wrapper3, text="مكان البحث")
lbl8.grid(row=7, column=0, padx=5, pady=3)
ent8 = Entry(wrapper3, bd=2, width=30, textvariable=t8)
ent8.grid(row=7, column=1, padx=5, pady=3)

lbl9 = Label(wrapper3, text="آخر إجراء")
lbl9.grid(row=8, column=0, padx=5, pady=3)
ent9 = Entry(wrapper3, bd=2, width=30, textvariable=t9)
ent9.grid(row=8, column=1, padx=5, pady=3)

up_btn = Button(wrapper3, bd=3, bg="#D3D3D3", activebackground="#D3D3D3", width=13, text="Mettre à jour", command=update_customer)
add_btn = Button(wrapper3, bd=3, bg="#D3D3D3", activebackground="#D3D3D3", width=13, text="Ajouter", command=add_new)
delete_btn = Button(wrapper3, bd=3, bg="#D3D3D3", activebackground="#D3D3D3", width=13, text="Supprimer", command=delete_customer)
clear_btn = Button(wrapper3, bd=3, bg="#D3D3D3", activebackground="#D3D3D3", width=13, text="Vider les champs", command=clearchamps)

add_btn.grid(row=0, column=4, padx=5, pady=3)
up_btn.grid(row=2, column=4, padx=5, pady=3)
delete_btn.grid(row=4, column=4, padx=5, pady=3)
clear_btn.grid(row=6, column=4, padx=5, pady=3)


root.title("قائمة الشكايات")
root.geometry("1300x650")
root.minsize(1080,600)
root.state('zoomed')
root.iconphoto(False, tk.PhotoImage(file='AGC.png'))
root.mainloop()