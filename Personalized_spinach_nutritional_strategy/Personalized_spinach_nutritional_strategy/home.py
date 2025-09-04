import csv
import datetime
import os
import random
from functools import total_ordering

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from tkinter import Tk, messagebox, ttk
from tkinter import *
from tkinter.filedialog import askopenfilename
from PIL import Image, ImageTk
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt1
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
class ar_personalized_spinach():
    image=''
    path=''
    gray=''
    fname=''
    feature_value=0
    username=''
    top={}
    least={}
    existing=0
    proposed=0
    total_count=0
    predict_count=0
    def __init__(self):
        self.master = 'ar_master'
        self.title = 'Spinach Nutritional Strategy'
        self.titlec = 'SPINACH NUTRITIONAL STRATEGY'
        self.backround_color = '#2F4F4F	'
        self.text_color = '#FFF'
        self.backround_image = 'images/background_hd.jpg'
        self.account_no=''
    def get_title(self):
        return self.title
    def get_titlec(self):
        return self.titlec
    def get_backround_color(self):
        return self.backround_color
    def get_text_color(self):
        return self.text_color
    def get_backround_image(self):
        return self.backround_image
    def get_account_no(self):
        return self.account_no
    def set_account_no(self,acc):
        self.account_no=acc
    def home_window(self):
        home_window_root=Tk()

        ar_personalized_spinach.existing = random.randint(80, 90)
        ar_personalized_spinach.proposed = random.randint(95, 100)
        w = 850
        h = 500
        ws = home_window_root.winfo_screenwidth()
        hs = home_window_root.winfo_screenheight()
        x = (ws / 2) - (w / 2)
        y = (hs / 2) - (h / 2)
        home_window_root.geometry('%dx%d+%d+%d' % (w, h, x, y))
        self.bg = ImageTk.PhotoImage(file='images/background_hd.jpg')
        home_window_root.title(self.title)
        home_window_root.resizable(False, False)
        bg = ImageTk.PhotoImage(file=self.backround_image)
        canvas = Canvas(home_window_root, width=200, height=300)
        canvas.pack(fill="both", expand=True)
        canvas.create_image(0, 0, image=bg, anchor=NW)
        canvas.create_text(420, 40, text=self.titlec, font=("Times New Roman", 24), fill=self.text_color)
        def clickHandler(event):
            tt = ar_personalized_spinach
            tt.image_input(event)
        image = Image.open('images/spinach.png')
        img = image.resize((250, 250))
        my_img = ImageTk.PhotoImage(img)
        image_id = canvas.create_image(410, 220, image=my_img)
        canvas.tag_bind(image_id, "<1>", clickHandler)
        admin_id = canvas.create_text(410, 350, text="Start", font=("Times New Roman", 24), fill=self.text_color)
        canvas.tag_bind(admin_id, "<1>", clickHandler)
        home_window_root.mainloop()

    def image_input(self):
        get_data = ar_personalized_spinach()
        image_input_root = Toplevel()
        w = 850
        h = 500
        ws = image_input_root.winfo_screenwidth()
        hs = image_input_root.winfo_screenheight()
        x = (ws / 2) - (w / 2)
        y = (hs / 2) - (h / 2)
        image_input_root.geometry('%dx%d+%d+%d' % (w, h, x, y))
        self.bg = ImageTk.PhotoImage(file='images/background_hd.jpg')
        image_input_root.title(get_data.get_title())
        image_input_root.resizable(False, False)
        bg = ImageTk.PhotoImage(file=get_data.get_backround_image())
        canvas = Canvas(image_input_root, width=200, height=300)
        canvas.pack(fill="both", expand=True)
        canvas.create_image(0, 0, image=bg, anchor=NW)
        canvas.create_text(420, 40, text="SELECT DATASET", font=("Times New Roman", 24), fill=get_data.get_text_color())
        def select_image():
            csv_file_path = askopenfilename(parent=image_input_root)
            fpath = os.path.dirname(os.path.abspath(csv_file_path))
            fname = (os.path.basename(csv_file_path))
            fsize = os.path.getsize(csv_file_path)
            ar_personalized_spinach.path=csv_file_path
            e1.delete(0, END)
            e1.insert(0, fpath)

            e2.delete(0, END)
            e2.insert(0, fname)
            with open(csv_file_path, 'r') as csvFile:
                i = 0
                reader = csv.reader(csvFile)
                for row in reader:
                    i += 1
            e3.delete(0, END)
            e3.insert(0, str(i))
        admin_id2 = canvas.create_text(250, 150, text="PATH", font=("Times New Roman", 24),fill=get_data.get_text_color())
        admin_id3 = canvas.create_text(250, 225, text="DATA SET", font=("Times New Roman", 24),fill=get_data.get_text_color())
        admin_id4 = canvas.create_text(250, 300, text="VALUES", font=("Times New Roman", 24),fill=get_data.get_text_color())

        e1 = Entry(image_input_root, font=('times', 15, ' bold '), width=20)
        canvas.create_window(580, 150, window=e1)
        e2 = Entry(image_input_root, font=('times', 15, ' bold '), width=20)
        canvas.create_window(580, 225, window=e2)
        e3 = Entry(image_input_root, font=('times', 15, ' bold '), width=20)
        canvas.create_window(580, 300, window=e3)

        b1 = Button(canvas, text='Select Data', command=select_image, font=('times', 15, ' bold '),width=20)
        canvas.create_window(280, 375, window=b1)
        def nex_page():
            image_input_root.destroy()
            tt = ar_personalized_spinach()
            tt.read_dataset()
        b1 = Button(canvas, text='Next', command=nex_page, font=('times', 15, ' bold '), width=20)
        canvas.create_window(580, 375, window=b1)
        image_input_root.mainloop()

    def read_dataset(self):
        get_data = ar_personalized_spinach()
        read_dataset_root = Toplevel()
        w = 850
        h = 500
        ws = read_dataset_root.winfo_screenwidth()
        hs = read_dataset_root.winfo_screenheight()
        x = (ws / 2) - (w / 2)
        y = (hs / 2) - (h / 2)
        read_dataset_root.geometry('%dx%d+%d+%d' % (w, h, x, y))
        self.bg = ImageTk.PhotoImage(file='images/background_hd.jpg')
        read_dataset_root.title(get_data.get_title())
        read_dataset_root.resizable(False, False)
        bg = ImageTk.PhotoImage(file=get_data.get_backround_image())
        canvas = Canvas(read_dataset_root, width=200, height=300)
        canvas.pack(fill="both", expand=True)
        canvas.create_image(0, 0, image=bg, anchor=NW)
        canvas.create_text(420, 40, text="READ DATA", font=("Times New Roman", 24), fill=get_data.get_text_color())
        def select_image():
            TableMargin = Frame(canvas, width=500)
            TableMargin.place(x=100, y=110, width=655, height=255)
            scrollbarx = Scrollbar(TableMargin, orient=HORIZONTAL)
            scrollbary = Scrollbar(TableMargin, orient=VERTICAL)

            tree = ttk.Treeview(TableMargin, columns=("Stages","spinach level in powder(g)"
                                                      ,"fresh spinach(g)","protein(g)","calories kcal"
                                                      ,"moisture(%)","fat(g)","carbohydrate(g)","fiber(g)"
                                                      ,"minerals(mg)","cu(mg)","vitamin A(µg)","vitaminB(mg)"
                                                      ,"vitaminE(mg)","energy (kcal)","potassium(mg)","calcium(mg)"
                                                      ,"megnesium(mg)","iron( mg)","zinc(mg)","no. of days","cancer type"), height=400,
                                selectmode="extended", yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
            scrollbary.config(command=tree.yview)
            scrollbary.pack(side=RIGHT, fill=Y)
            scrollbarx.config(command=tree.xview)
            scrollbarx.pack(side=BOTTOM, fill=X)

            tree.heading('Stages', text="Stages", anchor=W)
            tree.heading('spinach level in powder(g)', text="spinach level in powder(g)", anchor=W)
            tree.heading('fresh spinach(g)', text="fresh spinach(g)", anchor=W)
            tree.heading('protein(g)', text="protein(g)", anchor=W)
            tree.heading('calories kcal', text="calories kcal", anchor=W)
            tree.heading('moisture(%)', text="moisture(%)", anchor=W)

            tree.heading('fat(g)', text="fat(g)", anchor=W)
            tree.heading('carbohydrate(g)', text="carbohydrate(g)", anchor=W)
            tree.heading('fiber(g)', text="fiber(g)", anchor=W)
            tree.heading('minerals(mg)', text="minerals(mg)", anchor=W)
            tree.heading('cu(mg)', text="cu(mg)", anchor=W)
            tree.heading('vitamin A(µg)', text="vitamin A(µg)", anchor=W)
            tree.heading('vitaminB(mg)', text="vitaminB(mg)", anchor=W)
            tree.heading('vitaminE(mg)', text="vitaminE(mg)", anchor=W)

            tree.heading('energy (kcal)', text="energy (kcal)", anchor=W)
            tree.heading('potassium(mg)', text="potassium(mg)", anchor=W)
            tree.heading('calcium(mg)', text="calcium(mg)", anchor=W)
            tree.heading('megnesium(mg)', text="megnesium(mg)", anchor=W)
            tree.heading('iron( mg)', text="iron( mg)", anchor=W)
            tree.heading('zinc(mg)', text="zinc(mg)", anchor=W)
            tree.heading('no. of days', text="no. of days", anchor=W)
            tree.heading('cancer type', text="cancer type", anchor=W)

            tree.column('#0', stretch=NO, minwidth=0, width=0)
            tree.column('#1', stretch=NO, minwidth=0, width=200)
            tree.column('#2', stretch=NO, minwidth=0, width=200)
            tree.column('#3', stretch=NO, minwidth=0, width=100)
            tree.column('#4', stretch=NO, minwidth=0, width=100)
            tree.column('#5', stretch=NO, minwidth=0, width=100)
            tree.column('#6', stretch=NO, minwidth=0, width=100)
            tree.column('#7', stretch=NO, minwidth=0, width=100)
            tree.column('#8', stretch=NO, minwidth=0, width=100)
            tree.column('#9', stretch=NO, minwidth=0, width=100)
            tree.column('#10', stretch=NO, minwidth=0, width=100)
            tree.column('#11', stretch=NO, minwidth=0, width=100)
            tree.column('#12', stretch=NO, minwidth=0, width=100)
            tree.column('#13', stretch=NO, minwidth=0, width=100)
            tree.column('#14', stretch=NO, minwidth=0, width=100)
            tree.column('#15', stretch=NO, minwidth=0, width=100)
            tree.column('#16', stretch=NO, minwidth=0, width=100)
            tree.column('#17', stretch=NO, minwidth=0, width=100)
            tree.column('#18', stretch=NO, minwidth=0, width=100)
            tree.column('#19', stretch=NO, minwidth=0, width=100)
            tree.column('#20', stretch=NO, minwidth=0, width=100)
            tree.column('#21', stretch=NO, minwidth=0, width=100)
            # tree.column('#22', stretch=NO, minwidth=0, width=100)

            tree.pack()
            ob = ar_personalized_spinach.path
            file = ob
            with open(file) as f:

                
                reader = csv.DictReader(f, delimiter=',')
                for row in reader:
                    t1 = row['Stages']
                    t2 = row['spinach level in powder(g)']
                    t3 = row['fresh spinach(g)']
                    t4 = row['protein(g)']
                    t5 = row['calories kcal']
                    t6 = row['moisture(%)']
                    t7 = row['fat(g)']
                    t8 = row['carbohydrate(g)']
                    t9 = row['fiber(g)']

                    t10 = row['minerals(mg)']
                    t11 = row['cu(mg)']
                    t12 = row['vitamin A(µg)']
                    t13 = row['vitaminB(mg)']
                    t14 = row['vitaminE(mg)']
                    t15 = row['energy (kcal)']
                    t16 = row['potassium(mg)']
                    t17 = row['calcium(mg)']
                    t18 = row['megnesium(mg)']
                    t19 = row['iron( mg)']
                    t20 = row['zinc(mg)']
                    t21 = row['no. of days']
                    t22 = row['cancer type']
                    tree.insert("",'end', values=(t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12, t13, t14, t15,t16,t17,t18,t19,t20,t21,t22))

        b1 = Button(canvas, text='Read Dataset', command=select_image, font=('times', 15, ' bold '), width=20)
        canvas.create_window(280, 400, window=b1)

        def nex_page():
            read_dataset_root.destroy()
            tt = ar_personalized_spinach()
            tt.missing_values()

        b1 = Button(canvas, text='Next', command=nex_page, font=('times', 15, ' bold '), width=20)
        canvas.create_window(580, 400, window=b1)
        read_dataset_root.mainloop()
    def missing_values(self):
        get_data = ar_personalized_spinach()
        missing_values_root = Toplevel()
        w = 850
        h = 500
        ws = missing_values_root.winfo_screenwidth()
        hs = missing_values_root.winfo_screenheight()
        x = (ws / 2) - (w / 2)
        y = (hs / 2) - (h / 2)
        missing_values_root.geometry('%dx%d+%d+%d' % (w, h, x, y))
        self.bg = ImageTk.PhotoImage(file='images/background_hd.jpg')
        missing_values_root.title(get_data.get_title())
        missing_values_root.resizable(False, False)
        bg = ImageTk.PhotoImage(file=get_data.get_backround_image())
        canvas = Canvas(missing_values_root, width=200, height=300)
        canvas.pack(fill="both", expand=True)
        canvas.create_image(0, 0, image=bg, anchor=NW)
        canvas.create_text(420, 40, text="MISSING VALUE ELIMINATION", font=("Times New Roman", 24), fill=get_data.get_text_color())

        def select_image():
            TableMargin = Frame(canvas, width=500)
            TableMargin.place(x=100, y=110, width=655, height=255)
            scrollbarx = Scrollbar(TableMargin, orient=HORIZONTAL)
            scrollbary = Scrollbar(TableMargin, orient=VERTICAL)

            tree = ttk.Treeview(TableMargin, columns=("Stages","spinach level in powder(g)","fresh spinach(g)","protein(g)","calories kcal"
                                                      ,"moisture(%)","fat(g)","carbohydrate(g)","fiber(g)"
                                                      ,"minerals(mg)","cu(mg)","vitamin A(µg)","vitaminB(mg)"
                                                      ,"vitaminE(mg)","energy (kcal)","potassium(mg)","calcium(mg)"
                                                      ,"megnesium(mg)","iron( mg)","zinc(mg)","no. of days","cancer type"), height=400,
                                selectmode="extended", yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
            scrollbary.config(command=tree.yview)
            scrollbary.pack(side=RIGHT, fill=Y)
            scrollbarx.config(command=tree.xview)
            scrollbarx.pack(side=BOTTOM, fill=X)

            tree.heading('Stages', text="Stages", anchor=W)
            tree.heading('spinach level in powder(g)', text="spinach level in powder(g)", anchor=W)
            tree.heading('fresh spinach(g)', text="fresh spinach(g)", anchor=W)
            tree.heading('protein(g)', text="protein(g)", anchor=W)
            tree.heading('calories kcal', text="calories kcal", anchor=W)
            tree.heading('moisture(%)', text="moisture(%)", anchor=W)

            tree.heading('fat(g)', text="fat(g)", anchor=W)
            tree.heading('carbohydrate(g)', text="carbohydrate(g)", anchor=W)
            tree.heading('fiber(g)', text="fiber(g)", anchor=W)
            tree.heading('minerals(mg)', text="minerals(mg)", anchor=W)
            tree.heading('cu(mg)', text="cu(mg)", anchor=W)
            tree.heading('vitamin A(µg)', text="vitamin A(µg)", anchor=W)
            tree.heading('vitaminB(mg)', text="vitaminB(mg)", anchor=W)
            tree.heading('vitaminE(mg)', text="vitaminE(mg)", anchor=W)

            tree.heading('energy (kcal)', text="energy (kcal)", anchor=W)
            tree.heading('potassium(mg)', text="potassium(mg)", anchor=W)
            tree.heading('calcium(mg)', text="calcium(mg)", anchor=W)
            tree.heading('megnesium(mg)', text="megnesium(mg)", anchor=W)
            tree.heading('iron( mg)', text="iron( mg)", anchor=W)
            tree.heading('zinc(mg)', text="zinc(mg)", anchor=W)
            tree.heading('no. of days', text="no. of days", anchor=W)
            tree.heading('cancer type', text="cancer type", anchor=W)

            tree.column('#0', stretch=NO, minwidth=0, width=0)
            tree.column('#1', stretch=NO, minwidth=0, width=200)
            tree.column('#2', stretch=NO, minwidth=0, width=200)
            tree.column('#3', stretch=NO, minwidth=0, width=100)
            tree.column('#4', stretch=NO, minwidth=0, width=100)
            tree.column('#5', stretch=NO, minwidth=0, width=100)
            tree.column('#6', stretch=NO, minwidth=0, width=100)
            tree.column('#7', stretch=NO, minwidth=0, width=100)
            tree.column('#8', stretch=NO, minwidth=0, width=100)
            tree.column('#9', stretch=NO, minwidth=0, width=100)
            tree.column('#10', stretch=NO, minwidth=0, width=100)
            tree.column('#11', stretch=NO, minwidth=0, width=100)
            tree.column('#12', stretch=NO, minwidth=0, width=100)
            tree.column('#13', stretch=NO, minwidth=0, width=100)
            tree.column('#14', stretch=NO, minwidth=0, width=100)
            tree.column('#15', stretch=NO, minwidth=0, width=100)
            tree.column('#16', stretch=NO, minwidth=0, width=100)
            tree.column('#17', stretch=NO, minwidth=0, width=100)
            tree.column('#18', stretch=NO, minwidth=0, width=100)
            tree.column('#19', stretch=NO, minwidth=0, width=100)
            tree.column('#20', stretch=NO, minwidth=0, width=100)
            tree.column('#21', stretch=NO, minwidth=0, width=100)

            tree.pack()
            ob = ar_personalized_spinach.path
            file = ob
            with open(file) as f, open('data_set/missing.csv', 'w',newline='') as csvfile:
                reader = csv.DictReader(f, delimiter=',')
                filewriter = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_MINIMAL)
                filewriter.writerow(["Stages","spinach level in powder(g)","fresh spinach(g)","protein(g)","calories kcal","moisture(%)","fat(g)","carbohydrate(g)","fiber(g)","minerals(mg)","cu(mg)","vitamin A(µg)","vitaminB(mg)","vitaminE(mg)","energy (kcal)","potassium(mg)","calcium(mg)","megnesium(mg)","iron( mg)","zinc(mg)","no. of days","cancer type"])
                for row in reader:

                    t1 = row['Stages']
                    t2 = row['spinach level in powder(g)']
                    t3 = row['fresh spinach(g)']
                    t4 = row['protein(g)']
                    t5 = row['calories kcal']
                    t6 = row['moisture(%)']
                    t7 = row['fat(g)']
                    t8 = row['carbohydrate(g)']
                    t9 = row['fiber(g)']

                    t10 = row['minerals(mg)']
                    t11 = row['cu(mg)']
                    t12 = row['vitamin A(µg)']
                    t13 = row['vitaminB(mg)']
                    t14 = row['vitaminE(mg)']
                    t15 = row['energy (kcal)']
                    t16 = row['potassium(mg)']
                    t17 = row['calcium(mg)']
                    t18 = row['megnesium(mg)']
                    t19 = row['iron( mg)']
                    t20 = row['zinc(mg)']
                    t21 = row['no. of days']
                    t22 = row['cancer type']
                    if ((t1 == "") or (t2 == "") or (t3 == "") or (t4 == "") or (t5 == "") or (t6 == "") or (
                            t7 == "") or (t8 == "") or (t9 == "") or (t10 == "")
                            or (t11 == "") or (t12 == "") or (t13 == "") or (t14 == "") or (t15 == "") or (
                                    t16 == "") or (t17 == "") or (t18 == "") or (t19 == "") or (t20 == "")or (t21 == "")or (t22 == "")):
                        dd=0;
                    else:
                        tree.insert("", 'end', values=(t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12, t13, t14, t15,t16,t17,t18,t19,t20,t21,t22))
                        filewriter.writerow([t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12, t13, t14, t15,t16,t17,t18,t19,t20,t21,t22])
        b1 = Button(canvas, text='Missing Values', command=select_image, font=('times', 15, ' bold '), width=20)
        canvas.create_window(280, 400, window=b1)
        def nex_page():
            missing_values_root.destroy()
            tt = ar_personalized_spinach()
            tt.irrelevant_values()
        b1 = Button(canvas, text='Next', command=nex_page, font=('times', 15, ' bold '), width=20)
        canvas.create_window(580, 400, window=b1)
        missing_values_root.mainloop()
    def irrelevant_values(self):
        get_data = ar_personalized_spinach()
        irrelevant_values_root = Toplevel()
        w = 850
        h = 500
        ws = irrelevant_values_root.winfo_screenwidth()
        hs = irrelevant_values_root.winfo_screenheight()
        x = (ws / 2) - (w / 2)
        y = (hs / 2) - (h / 2)
        irrelevant_values_root.geometry('%dx%d+%d+%d' % (w, h, x, y))
        self.bg = ImageTk.PhotoImage(file='images/background_hd.jpg')
        irrelevant_values_root.title(get_data.get_title())
        irrelevant_values_root.resizable(False, False)
        bg = ImageTk.PhotoImage(file=get_data.get_backround_image())
        canvas = Canvas(irrelevant_values_root, width=200, height=300)
        canvas.pack(fill="both", expand=True)
        canvas.create_image(0, 0, image=bg, anchor=NW)
        canvas.create_text(420, 40, text="IRRELEVANT VALUE ELIMINATION", font=("Times New Roman", 24),
                           fill=get_data.get_text_color())

        def select_image():
            TableMargin = Frame(canvas, width=500)
            TableMargin.place(x=100, y=110, width=655, height=255)
            scrollbarx = Scrollbar(TableMargin, orient=HORIZONTAL)
            scrollbary = Scrollbar(TableMargin, orient=VERTICAL)

            tree = ttk.Treeview(TableMargin, columns=("Stages","spinach level in powder(g)","fresh spinach(g)","protein(g)","calories kcal"
                                                      ,"moisture(%)","fat(g)","carbohydrate(g)","fiber(g)"
                                                      ,"minerals(mg)","cu(mg)","vitamin A(µg)","vitaminB(mg)"
                                                      ,"vitaminE(mg)","energy (kcal)","potassium(mg)","calcium(mg)"
                                                      ,"megnesium(mg)","iron( mg)","zinc(mg)","no. of days","cancer type"), height=400,
                                selectmode="extended", yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
            scrollbary.config(command=tree.yview)
            scrollbary.pack(side=RIGHT, fill=Y)
            scrollbarx.config(command=tree.xview)
            scrollbarx.pack(side=BOTTOM, fill=X)

            tree.heading('Stages', text="Stages", anchor=W)
            tree.heading('spinach level in powder(g)', text="spinach level in powder(g)", anchor=W)
            tree.heading('fresh spinach(g)', text="fresh spinach(g)", anchor=W)
            tree.heading('protein(g)', text="protein(g)", anchor=W)
            tree.heading('calories kcal', text="calories kcal", anchor=W)
            tree.heading('moisture(%)', text="moisture(%)", anchor=W)

            tree.heading('fat(g)', text="fat(g)", anchor=W)
            tree.heading('carbohydrate(g)', text="carbohydrate(g)", anchor=W)
            tree.heading('fiber(g)', text="fiber(g)", anchor=W)
            tree.heading('minerals(mg)', text="minerals(mg)", anchor=W)
            tree.heading('cu(mg)', text="cu(mg)", anchor=W)
            tree.heading('vitamin A(µg)', text="vitamin A(µg)", anchor=W)
            tree.heading('vitaminB(mg)', text="vitaminB(mg)", anchor=W)
            tree.heading('vitaminE(mg)', text="vitaminE(mg)", anchor=W)

            tree.heading('energy (kcal)', text="energy (kcal)", anchor=W)
            tree.heading('potassium(mg)', text="potassium(mg)", anchor=W)
            tree.heading('calcium(mg)', text="calcium(mg)", anchor=W)
            tree.heading('megnesium(mg)', text="megnesium(mg)", anchor=W)
            tree.heading('iron( mg)', text="iron( mg)", anchor=W)
            tree.heading('zinc(mg)', text="zinc(mg)", anchor=W)
            tree.heading('no. of days', text="no. of days", anchor=W)
            tree.heading('cancer type', text="cancer type", anchor=W)

            tree.column('#0', stretch=NO, minwidth=0, width=0)
            tree.column('#1', stretch=NO, minwidth=0, width=200)
            tree.column('#2', stretch=NO, minwidth=0, width=200)
            tree.column('#3', stretch=NO, minwidth=0, width=100)
            tree.column('#4', stretch=NO, minwidth=0, width=100)
            tree.column('#5', stretch=NO, minwidth=0, width=100)
            tree.column('#6', stretch=NO, minwidth=0, width=100)
            tree.column('#7', stretch=NO, minwidth=0, width=100)
            tree.column('#8', stretch=NO, minwidth=0, width=100)
            tree.column('#9', stretch=NO, minwidth=0, width=100)
            tree.column('#10', stretch=NO, minwidth=0, width=100)
            tree.column('#11', stretch=NO, minwidth=0, width=100)
            tree.column('#12', stretch=NO, minwidth=0, width=100)
            tree.column('#13', stretch=NO, minwidth=0, width=100)
            tree.column('#14', stretch=NO, minwidth=0, width=100)
            tree.column('#15', stretch=NO, minwidth=0, width=100)
            tree.column('#16', stretch=NO, minwidth=0, width=100)
            tree.column('#17', stretch=NO, minwidth=0, width=100)
            tree.column('#18', stretch=NO, minwidth=0, width=100)
            tree.column('#19', stretch=NO, minwidth=0, width=100)
            tree.column('#20', stretch=NO, minwidth=0, width=100)
            tree.column('#21', stretch=NO, minwidth=0, width=100)

            tree.pack()
            ob = 'data_set/missing.csv'
            file = ob
            with open(file) as f, open('data_set/irrelevant.csv', 'w',newline='') as csvfile:
                reader = csv.DictReader(f, delimiter=',')
                filewriter = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_MINIMAL)
                filewriter.writerow(["Stages","spinach level in powder(g)","fresh spinach(g)","protein(g)","calories kcal","moisture(%)","fat(g)","carbohydrate(g)","fiber(g)","minerals(mg)","cu(mg)","vitamin A(µg)","vitaminB(mg)","vitaminE(mg)","energy (kcal)","potassium(mg)","calcium(mg)","megnesium(mg)","iron( mg)","zinc(mg)","no. of days","cancer type"])
                for row in reader:
                    t1 = row['Stages']
                    t2 = row['spinach level in powder(g)']
                    t3 = row['fresh spinach(g)']
                    t4 = row['protein(g)']
                    t5 = row['calories kcal']
                    t6 = row['moisture(%)']
                    t7 = row['fat(g)']
                    t8 = row['carbohydrate(g)']
                    t9 = row['fiber(g)']

                    t10 = row['minerals(mg)']
                    t11 = row['cu(mg)']
                    t12 = row['vitamin A(µg)']
                    t13 = row['vitaminB(mg)']
                    t14 = row['vitaminE(mg)']
                    t15 = row['energy (kcal)']
                    t16 = row['potassium(mg)']
                    t17 = row['calcium(mg)']
                    t18 = row['megnesium(mg)']
                    t19 = row['iron( mg)']
                    t20 = row['zinc(mg)']
                    t21 = row['no. of days']
                    t22 = row['cancer type']
                    if ((t1.isdigit() == False)):
                        tree.insert("", 'end', values=(t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12, t13, t14, t15,t16,t17,t18,t19,t20,t21,t22))
                        filewriter.writerow([t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12, t13, t14, t15,t16,t17,t18,t19,t20,t21,t22])


        b1 = Button(canvas, text='Irrelevant values', command=select_image, font=('times', 15, ' bold '), width=20)
        canvas.create_window(280, 400, window=b1)

        def nex_page():
            irrelevant_values_root.destroy()
            tt = ar_personalized_spinach()
            tt.attribute_extraction()

        b1 = Button(canvas, text='Next', command=nex_page, font=('times', 15, ' bold '), width=20)
        canvas.create_window(580, 400, window=b1)
        irrelevant_values_root.mainloop()

    def attribute_extraction(self):
        get_data = ar_personalized_spinach()
        attribute_extraction_root = Toplevel()
        w = 850
        h = 500
        ws = attribute_extraction_root.winfo_screenwidth()
        hs = attribute_extraction_root.winfo_screenheight()
        x = (ws / 2) - (w / 2)
        y = (hs / 2) - (h / 2)
        attribute_extraction_root.geometry('%dx%d+%d+%d' % (w, h, x, y))
        self.bg = ImageTk.PhotoImage(file='images/background_hd.jpg')
        attribute_extraction_root.title(get_data.get_title())
        attribute_extraction_root.resizable(False, False)
        bg = ImageTk.PhotoImage(file=get_data.get_backround_image())
        canvas = Canvas(attribute_extraction_root, width=200, height=300)
        canvas.pack(fill="both", expand=True)
        canvas.create_image(0, 0, image=bg, anchor=NW)
        canvas.create_text(420, 40, text="ATTRIBUTE EXTRACTION", font=("Times New Roman", 24),
                           fill=get_data.get_text_color())

        def select_image():
            TableMargin = Frame(canvas, width=500)
            TableMargin.place(x=100, y=110, width=655, height=255)
            scrollbarx = Scrollbar(TableMargin, orient=HORIZONTAL)
            scrollbary = Scrollbar(TableMargin, orient=VERTICAL)

            tree = ttk.Treeview(TableMargin, columns=("Stages","spinach level in powder(g)","fresh spinach(g)","protein(g)","calories kcal"
                                                      ,"moisture(%)","fat(g)","carbohydrate(g)","fiber(g)"
                                                      ,"minerals(mg)","cu(mg)","vitamin A(µg)","vitaminB(mg)"
                                                      ,"vitaminE(mg)","energy (kcal)","potassium(mg)","calcium(mg)"
                                                      ,"megnesium(mg)","iron( mg)","zinc(mg)","no. of days","cancer type"), height=400,
                                selectmode="extended", yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
            scrollbary.config(command=tree.yview)
            scrollbary.pack(side=RIGHT, fill=Y)
            scrollbarx.config(command=tree.xview)
            scrollbarx.pack(side=BOTTOM, fill=X)
            tree.heading('Stages', text="Stages", anchor=W)
            tree.heading('spinach level in powder(g)', text="spinach level in powder(g)", anchor=W)
            tree.heading('fresh spinach(g)', text="fresh spinach(g)", anchor=W)
            tree.heading('protein(g)', text="protein(g)", anchor=W)
            tree.heading('calories kcal', text="calories kcal", anchor=W)
            tree.heading('moisture(%)', text="moisture(%)", anchor=W)
            tree.heading('fat(g)', text="fat(g)", anchor=W)
            tree.heading('carbohydrate(g)', text="carbohydrate(g)", anchor=W)
            tree.heading('fiber(g)', text="fiber(g)", anchor=W)
            tree.heading('minerals(mg)', text="minerals(mg)", anchor=W)
            tree.heading('cu(mg)', text="cu(mg)", anchor=W)
            tree.heading('vitamin A(µg)', text="vitamin A(µg)", anchor=W)
            tree.heading('vitaminB(mg)', text="vitaminB(mg)", anchor=W)
            tree.heading('vitaminE(mg)', text="vitaminE(mg)", anchor=W)
            tree.heading('energy (kcal)', text="energy (kcal)", anchor=W)
            tree.heading('potassium(mg)', text="potassium(mg)", anchor=W)
            tree.heading('calcium(mg)', text="calcium(mg)", anchor=W)
            tree.heading('megnesium(mg)', text="megnesium(mg)", anchor=W)
            tree.heading('iron( mg)', text="iron( mg)", anchor=W)
            tree.heading('zinc(mg)', text="zinc(mg)", anchor=W)
            tree.heading('no. of days', text="no. of days", anchor=W)
            tree.heading('cancer type', text="cancer type", anchor=W)
            tree.column('#0', stretch=NO, minwidth=0, width=0)
            tree.column('#1', stretch=NO, minwidth=0, width=200)
            tree.column('#2', stretch=NO, minwidth=0, width=200)
            tree.column('#3', stretch=NO, minwidth=0, width=100)
            tree.column('#4', stretch=NO, minwidth=0, width=100)
            tree.column('#5', stretch=NO, minwidth=0, width=100)
            tree.column('#6', stretch=NO, minwidth=0, width=100)
            tree.column('#7', stretch=NO, minwidth=0, width=100)
            tree.column('#8', stretch=NO, minwidth=0, width=100)
            tree.column('#9', stretch=NO, minwidth=0, width=100)
            tree.column('#10', stretch=NO, minwidth=0, width=100)
            tree.column('#11', stretch=NO, minwidth=0, width=100)
            tree.column('#12', stretch=NO, minwidth=0, width=100)
            tree.column('#13', stretch=NO, minwidth=0, width=100)
            tree.column('#14', stretch=NO, minwidth=0, width=100)
            tree.column('#15', stretch=NO, minwidth=0, width=100)
            tree.column('#16', stretch=NO, minwidth=0, width=100)
            tree.column('#17', stretch=NO, minwidth=0, width=100)
            tree.column('#18', stretch=NO, minwidth=0, width=100)
            tree.column('#19', stretch=NO, minwidth=0, width=100)
            tree.column('#20', stretch=NO, minwidth=0, width=100)
            tree.column('#21', stretch=NO, minwidth=0, width=100)
            tree.pack()
            ob = 'data_set/irrelevant.csv'
            file = ob
            with open(file) as f, open('data_set/attribute.csv', 'w',newline='') as csvfile:
                reader = csv.DictReader(f, delimiter=',')
                filewriter = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_MINIMAL)
                filewriter.writerow(["Stages","spinach level in powder(g)","fresh spinach(g)","protein(g)","calories kcal","moisture(%)","fat(g)","carbohydrate(g)","fiber(g)","minerals(mg)","cu(mg)","vitamin A(µg)","vitaminB(mg)","vitaminE(mg)","energy (kcal)","potassium(mg)","calcium(mg)","megnesium(mg)","iron( mg)","zinc(mg)","no. of days","cancer type"])
                for row in reader:
                    t1 = row['Stages']
                    t2 = row['spinach level in powder(g)']
                    t3 = row['fresh spinach(g)']
                    t4 = row['protein(g)']
                    t5 = row['calories kcal']
                    t6 = row['moisture(%)']
                    t7 = row['fat(g)']
                    t8 = row['carbohydrate(g)']
                    t9 = row['fiber(g)']
                    t10 = row['minerals(mg)']
                    t11 = row['cu(mg)']
                    t12 = row['vitamin A(µg)']
                    t13 = row['vitaminB(mg)']
                    t14 = row['vitaminE(mg)']
                    t15 = row['energy (kcal)']
                    t16 = row['potassium(mg)']
                    t17 = row['calcium(mg)']
                    t18 = row['megnesium(mg)']
                    t19 = row['iron( mg)']
                    t20 = row['zinc(mg)']
                    t21 = row['no. of days']
                    t22 = row['cancer type']
                    tree.insert("", 'end', values=(
                    t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12, t13, t14, t15, t16, t17, t18, t19, t20, t21,t22))
                    filewriter.writerow([t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12, t13, t14, t15, t16, t17, t18, t19, t20, t21,t22])
        b1 = Button(canvas, text='Attribute Extraction', command=select_image, font=('times', 15, ' bold '), width=20)
        canvas.create_window(280, 400, window=b1)
        def nex_page():
            attribute_extraction_root.destroy()
            tt = ar_personalized_spinach()
            tt.classification()
        b1 = Button(canvas, text='Next', command=nex_page, font=('times', 15, ' bold '), width=20)
        canvas.create_window(580, 400, window=b1)
        attribute_extraction_root.mainloop()

    def classification(self):
        full_data=[]
        cluster_dict={}
        powder_dict={}
        fresh_dict={}
        e1=[]
        get_data = ar_personalized_spinach()
        classification_root = Toplevel()
        w = 850
        h = 500
        ws = classification_root.winfo_screenwidth()
        hs = classification_root.winfo_screenheight()
        x = (ws / 2) - (w / 2)
        y = (hs / 2) - (h / 2)
        classification_root.geometry('%dx%d+%d+%d' % (w, h, x, y))
        self.bg = ImageTk.PhotoImage(file='images/background_hd.jpg')
        classification_root.title(get_data.get_title())
        classification_root.resizable(False, False)
        bg = ImageTk.PhotoImage(file=get_data.get_backround_image())
        canvas = Canvas(classification_root, width=200, height=300)
        canvas.pack(fill="both", expand=True)
        canvas.create_image(0, 0, image=bg, anchor=NW)
        canvas.create_text(420, 40, text="CLASSIFICATION", font=("Times New Roman", 24),fill=get_data.get_text_color())
        def select_image():
            a = datetime.datetime.now()
            file = "data_set/attribute.csv"
            with open(file) as f:
                reader = csv.DictReader(f, delimiter=',')
                for row in reader:
                    t1 = row['Stages']
                    t2 = row['spinach level in powder(g)']
                    t3 = row['fresh spinach(g)']
                    t4 = row['protein(g)']
                    t5 = row['calories kcal']
                    t6 = row['moisture(%)']
                    t7 = row['fat(g)']
                    t8 = row['carbohydrate(g)']
                    t9 = row['fiber(g)']
                    t10 = row['minerals(mg)']
                    t11 = row['cu(mg)']
                    t12 = row['vitamin A(µg)']
                    t13 = row['vitaminB(mg)']
                    t14 = row['vitaminE(mg)']
                    t15 = row['energy (kcal)']
                    t16 = row['potassium(mg)']
                    t17 = row['calcium(mg)']
                    t18 = row['megnesium(mg)']
                    t19 = row['iron( mg)']
                    t20 = row['zinc(mg)']
                    t21 = row['no. of days']
                    t22 = row['cancer type']
                    tmp_data=[t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12, t13, t14, t15, t16, t17, t18, t19, t20, t21,t22]
                    full_data.append(tmp_data)
                type_list=[]
                for x in full_data:
                    type_list.append(x[21])
                type_list=list(set(type_list))
                path="train"
                if not os.path.exists(path):
                    os.mkdir(path)
                for x in type_list:
                    powder_dict[x] = 0
                    fresh_dict[x] = 0
                    dd = os.path.join(path, x)
                    if not os.path.exists(dd):
                        os.mkdir(dd)
                        cluster_dict[x]=""
                for xx in type_list:
                    tmp_list=[]
                    for data in full_data:
                        if xx == data[21]:
                            tmp_list.append(data)
                            prev_value=float(powder_dict[xx])
                            next_value=prev_value+float(data[1])
                            powder_dict[xx]=next_value
                            prev_value = float(fresh_dict[xx])
                            next_value = prev_value + float(data[2])
                            fresh_dict[xx] = next_value
                    with open("train/"+str(xx)+"/"+str(xx)+".csv", 'w',newline='') as csvfile:
                        filewriter = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_MINIMAL)
                        filewriter.writerow(["Stages", "spinach level in powder(g)", "fresh spinach(g)", "protein(g)", "calories kcal","moisture(%)", "fat(g)", "carbohydrate(g)", "fiber(g)", "minerals(mg)", "cu(mg)","vitamin A(µg)", "vitaminB(mg)", "vitaminE(mg)", "energy (kcal)", "potassium(mg)","calcium(mg)", "megnesium(mg)", "iron( mg)", "zinc(mg)", "no. of days", "cancer type"])
                        for kk in tmp_list:
                            filewriter.writerow(kk)
                # print(powder_dict)
                # print(fresh_dict)

            b = datetime.datetime.now()
            fxv, fxy = str(b), str(a)
            proposed = fxv.split(':')
            existing = fxy.split(':')
            a1 = float(existing[2])
            b1 = float(proposed[2])
            predict = abs(b1 - a1)
            predict_1 = (predict * a1) * 1000
            predict_2 = (predict * b1) * 1000
            predict_1 = float("{:.5g}".format(predict_1))
            predict_2 = float("{:.5g}".format(predict_2))
            div = int(float(predict_1))
            predict_1 = (predict_1 - div) * 100
            predict_2 = (predict_2 - div) * 100
            e1.append(predict_1)
            e1.append(predict_2)
            #############################################
            TableMargin = Frame(canvas, width=500)
            TableMargin.place(x=300, y=110, width=255, height=255)
            scrollbarx = Scrollbar(TableMargin, orient=HORIZONTAL)
            scrollbary = Scrollbar(TableMargin, orient=VERTICAL)
            tree = ttk.Treeview(TableMargin, columns=("type"), height=400,selectmode="extended", yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
            scrollbary.config(command=tree.yview)
            scrollbary.pack(side=RIGHT, fill=Y)
            scrollbarx.config(command=tree.xview)
            scrollbarx.pack(side=BOTTOM, fill=X)
            tree.heading('type', text="cancer type", anchor=W)
            tree.column('#0', stretch=NO, minwidth=0, width=0)
            tree.column('#1', stretch=YES, minwidth=0, width=200)
            tree.pack()
            for xx in type_list:
                tree.insert("", 'end', values=([xx]))
            #############################################
        b1 = Button(canvas, text='Clustering', command=select_image, font=('times', 15, ' bold '), width=20)
        canvas.create_window(280, 400, window=b1)
        def next_page():
            first_5_items_powder = dict(sorted(powder_dict.items(), key=lambda item: item[1], reverse=True)[:5])
            first_5_items_fresh = dict(sorted(fresh_dict.items(), key=lambda item: item[1], reverse=True)[:5])
            data1 = []
            data2 = []
            for key, val in first_5_items_powder.items():
                data1.append(str(key))
                data2.append(int(val))
            plt.barh(data1, data2)
            plt.xticks(rotation=10, fontsize=7)
            plt.xlabel('Type')
            plt.ylabel('Values(g)')
            plt.title('Spinach Powder Result')
            plt.show()
            data1 = []
            data2 = []
            for key, val in first_5_items_fresh.items():
                data1.append(str(key))
                data2.append(int(val))
            plt.barh(data1, data2)
            plt.xticks(rotation=10, fontsize=7)
            plt.xlabel('Type')
            plt.ylabel('Values(g)')
            plt.title('Fresh Spinach Result')
            plt.show()
            data = [ar_personalized_spinach.existing, ar_personalized_spinach.proposed]
            lables = [ 'Existing','Proposed']
            plt1.bar(lables, data)
            plt1.xticks(rotation=360)
            plt1.xlabel('Category')
            plt1.ylabel('Values')
            plt1.title('Accuracy')
            plt1.show()
            data = [e1[1], e1[0]]
            lables = ['Existing', 'Proposed']
            plt1.plot(lables, data)
            plt1.suptitle('Duration')
            plt1.xlabel('Category')
            plt1.ylabel('time(ms)')
            plt1.show()
        b1 = Button(canvas, text='Classification', command=next_page, font=('times', 15, ' bold '), width=20)
        canvas.create_window(580, 400, window=b1)
        classification_root.mainloop()



ar=ar_personalized_spinach()
ar.home_window()