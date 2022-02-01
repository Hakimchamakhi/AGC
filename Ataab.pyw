from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import mysql.connector


def update(rows):
	trv.delete(*trv.get_children())
	for i in rows:
		trv.insert('', 'end', values=i)

def search():
	q2 = q.get()
	query = "SELECT ID, client, case_num, value_charge, value_advance, advance_date FROM tbl_ataab WHERE case_num LIKE '%"+q2+"%' OR client LIKE '%"+q2+"%'"
	cursor.execute(query)
	rows = cursor.fetchall()
	update(rows)

def clear():
	query="SELECT ID, client, case_num, value_charge, value_advance, advance_date FROM tbl_ataab ORDER BY client, case_num"
	cursor.execute(query)
	rows = cursor.fetchall()
	update(rows)

def clearchamps():
    t1.set("")
    t2.set("")
    t3.set("")
    t4.set("")
    t5.set("")

def getrow(event):
	rowid = trv.identify_row(event.y)
	item = trv.item(trv.focus())
	t0.set(item['values'][0])
	t1.set(item['values'][1])
	t2.set(item['values'][2])
	t3.set(item['values'][3])
	t4.set(item['values'][4])
	t5.set(item['values'][5])


def update_customer():
	id_0 = t0.get()
	client = t1.get()
	case_num = t2.get()
	value_charge = t3.get()
	value_advance = t4.get()
	advance_date = t5.get()
	
	if messagebox.askyesno("Confirmation", "Confirmation de mettre à jour client"):
		query = "UPDATE tbl_ataab SET  client = %s, case_num = %s, value_charge = %s, value_advance = %s, advance_date = %s where ID= %s"
		cursor.execute(query,( client, case_num, value_charge, value_advance, advance_date, id_0))
		mydb.commit()
		clear()
	else:
		return True

def add_new():
	client = t1.get()
	case_num = t2.get()
	value_charge = t3.get()
	value_advance = t4.get()
	advance_date = t5.get() 
	query = "INSERT INTO tbl_ataab (client, case_num, value_charge, value_advance, advance_date) Values(%s, %s, %s, %s, %s )"
	cursor.execute(query, (client, case_num, value_charge, value_advance, advance_date))
	messagebox.showinfo("Message", "Ce dossier a été ajouté")
	mydb.commit()
	clear()
 
    

def delete_customer():
	refd = t0.get()    
	if messagebox.askyesno("Confirmation", "Confirmation de suppression de client"):
		query = "DELETE From tbl_ataab WHERE ID='"+refd+"'"
		cursor.execute(query)
		mydb.commit()
		clear()
	else:
		return True
    

mydb = mysql.connector.connect()
cursor = mydb.cursor(buffered=True)

root = Tk()
q = StringVar()
t1 = StringVar()
t2 = StringVar()
t3 = StringVar()
t4 = StringVar()
t5 = StringVar()
t0 = StringVar()


wrapper1 = LabelFrame(root, text="")
wrapper2 = LabelFrame(root, text="")
wrapper3 = LabelFrame(root, text="")

wrapper1.pack(fill="both", expand="yes", side=TOP, padx=20, pady=10)
wrapper2.pack(fill="both", expand="yes", side=LEFT, padx=20, pady=10)
wrapper3.pack(fill="both", expand="yes", side=RIGHT, padx=20, pady=10)

style = ttk.Style()
style.configure("mystyle.Treeview", highlightthickness=0, bd=0, font=('Calibri', 10)) # Modify the font of the body
style.configure("mystyle.Treeview.Heading", font=('Calibri', 11,'bold')) # Modify the font of the headings

trv = ttk.Treeview(wrapper1, columns=(1,2,3,4,5,6), show="headings", style="mystyle.Treeview")
trv.pack(fill="both", expand="yes", side=LEFT)

trv.heading(1, text="ID")
trv.heading(2, text="المنوب")
trv.heading(3, text="عدد القضية")
trv.heading(4, text="قيمة المستحقات")
trv.heading(5, text="قيمة التسبقة")
trv.heading(6, text="تاريخ التسبقة")

trv.column(1, width=180, minwidth=100)
trv.column(2, width=180, minwidth=100)
trv.column(3, width=180, minwidth=100)
trv.column(4, width=180, minwidth=100)
trv.column(5, width=180, minwidth=100)
trv.column(6, width=180, minwidth=100)


trv.bind('<Double 1>', getrow)

#vertical scrollbar
yscrollbar = ttk.Scrollbar(trv, orient="vertical", command=trv.yview)
yscrollbar.pack(side=RIGHT, fill="y")

trv.configure(yscrollcommand=yscrollbar.set)


query = "SELECT ID, client, case_num, value_charge, value_advance, advance_date FROM tbl_ataab ORDER BY client, case_num"
cursor.execute(query)
rows = cursor.fetchall()
update(rows)


#search section
lbl = Label(wrapper2, text="Recherche")
lbl.pack(side=tk.LEFT, padx=10)
ent = Entry(wrapper2, bd=2, width=30, textvariable=q)
ent.pack(side=tk.LEFT, padx=10)
btn = Button(wrapper2, bd=3, bg="#D3D3D3", activebackground="#D3D3D3", width=13, text="Recherche", command=search)
btn.pack(side=tk.LEFT, padx=10)
cbtn = Button(wrapper2, bd=3, bg="#D3D3D3", activebackground="#D3D3D3", width=13, text="Initialiser", command=clear)
cbtn.pack(side=tk.LEFT, padx=10)

#User ADD MODIFY DELETE Section
lbl1 = Label(wrapper3, text="المنوب")
lbl1.grid(row=0, column=0, padx=5, pady=3)
ent1 = Entry(wrapper3, bd=2, width=30, textvariable=t1)
ent1.grid(row=0, column=1, padx=5, pady=3)

lbl2 = Label(wrapper3, text="عدد القضية")
lbl2.grid(row=1, column=0, padx=5, pady=3)
ent2 = Entry(wrapper3, bd=2, width=30, textvariable=t2)
ent2.grid(row=1, column=1, padx=5, pady=3)

lbl3 = Label(wrapper3, text="قيمة المستحقات")
lbl3.grid(row=2, column=0, padx=5, pady=3)
ent3 = Entry(wrapper3, bd=2, width=30, textvariable=t3)
ent3.grid(row=2, column=1, padx=5, pady=3)

lbl4 = Label(wrapper3, text="قيمة التسبقة")
lbl4.grid(row=3, column=0, padx=5, pady=3)
ent4 = Entry(wrapper3, bd=2, width=30, textvariable=t4)
ent4.grid(row=3, column=1, padx=5, pady=3)

lbl5 = Label(wrapper3, text="تاريخ التسبقة")
lbl5.grid(row=4, column=0, padx=5, pady=3)
ent5 = Entry(wrapper3, bd=2, width=30, textvariable=t5)
ent5.grid(row=4, column=1, padx=5, pady=3)


up_btn = Button(wrapper3, bd=3, bg="#D3D3D3", activebackground="#D3D3D3", width=13, text="Mettre à jour", command=update_customer)
add_btn = Button(wrapper3, bd=3, bg="#D3D3D3", activebackground="#D3D3D3", width=13,text="Ajouter", command=add_new)
delete_btn = Button(wrapper3, bd=3, bg="#D3D3D3", activebackground="#D3D3D3", width=13,text="Supprimer", command=delete_customer)
clear_btn = Button(wrapper3, bd=3, bg="#D3D3D3", activebackground="#D3D3D3", width=13,text="Vider les champs", command=clearchamps)

add_btn.grid(row=0, column=4, padx=5, pady=3)
up_btn.grid(row=1, column=4, padx=5, pady=3)
delete_btn.grid(row=2, column=4, padx=5, pady=3)
clear_btn.grid(row=3, column=4, padx=5, pady=3)

root.title("قائمة الأتعاب")
root.geometry("1300x650")
root.minsize(1080,600)
root.state('zoomed')
root.iconphoto(False, tk.PhotoImage(file='AGC.png'))
root.mainloop()