from tkinter import *
import subprocess
import os
from tkinter import messagebox
from tkinter import ttk

def ExecuteFunction(process, outputwidget):
    outputwidget.delete('1.0', END)
    p = subprocess.Popen(process,shell=True, stdout=subprocess.PIPE,stderr=subprocess.PIPE, universal_newlines=True)
    if p.stdout:
        for line in p.stdout:
            outputwidget.insert(END, line)
    if p.stderr:
        for line in p.stderr:
            outputwidget.insert(END, line)

def RESETFunction(outputwidget):
    outputwidget.delete('1.0', END)
    ExecuteFunction('ipconfig /flushdns', outputwidget)
    ExecuteFunction('ipconfig /renew', outputwidget)

def flush():
    os.system('ipconfig /flushdns')
    os.system('ipconfig /renew')
    messagebox.showinfo('Wincheck by Rish', 'Your DNS has been flushed and renewed sucessfully!')

def AD():
    os.startfile("c:\windows\system32\dsa.exe")
    

class app:
    def __init__(self, master):
        self.master = master
        self.master.geometry("560x490")
        self.master.title(" WinCheck by Rish")
        self.master.iconbitmap('mclaren.ico')
        self.master['background']='#F48500'
        self.Main_Menu()

    def Main_Menu(self):
        for i in self.master.winfo_children():
            i.destroy()
        self.frame1 = Frame(self.master, width=300, height=300, bg="#F48500")
        self.frame1.grid(row=0, column=0, sticky='nwse')

        self.Title = Label(self.frame1, text='Welcome to Wincheck',bg="#F48500")
        self.Title.config(font=('McLaren Bespoke Bold', 18))
        self.Title.grid(row=0, column=0, columnspan=3)

        self.logo = PhotoImage(file="McLaren_Logo_1.png")
        self.logo_label = Label(self.frame1, image=self.logo,borderwidth=0, highlightthickness=0)
        self.logo_label.grid(row=0, column=0, sticky=S, pady=5, rowspan=2)

        self.Subtitle = Label(self.frame1, text="Please select an option to begin", bg="#F48500")
        self.Subtitle.config(font=('McLaren Bespoke',12))
        self.Subtitle.grid(row=1, column=0, columnspan=3)

        self.Space = Label(self.frame1, text=' ', bg="#F48500")
        self.Space.grid(row=2, column=0)

        #self.pingbutton = Button(self.frame1, text="Ping", padx=50, pady=25, bg="#c7c7c7", command=self.ping)
        #self.pingbutton.config(font=('McLaren Bespoke',11))
        #self.pingbutton.grid(row=3, column=0, padx=10, pady=10)
        self.pingbutton = ttk.Button(self.frame1, text="  Ping  ", command=self.ping)
        self.pingbutton.grid(row=3, column=0,ipadx=45, ipady=25, padx=10, pady=10)

        #self.usernamebutton = Button(self.frame1, text="Username", padx=50, pady=25, bg="#c7c7c7", command=self.username)
        #self.usernamebutton.config(font=('McLaren Bespoke',11))
        #self.usernamebutton.grid(row=3, column=1, padx=10, pady=10)
        self.usernamebutton = ttk.Button(self.frame1, text="Username", command=self.username)
        self.usernamebutton.grid(row=3, column=1, ipadx=45, ipady=25, padx=10, pady=10)

        #self.buildbutton = Button(self.frame1, text="  Build  ", bg="#c7c7c7", padx=50, pady=25, command=self.build)
        #self.buildbutton.config(font=('McLaren Bespoke',11))
        #self.buildbutton.grid(row=3, column=2, padx=10, pady=10)
        self.buildbutton = ttk.Button(self.frame1, text="  Build  ", command=self.username)
        self.buildbutton.grid(row=3, column=2, ipadx=45, ipady=25, padx=10, pady=10)

        #self.rdpbutton = Button(self.frame1, text=" RDP  ", padx=50, pady=25, bg="#c7c7c7", command=self.rdp)
        #self.rdpbutton.config(font=('McLaren Bespoke',11))
        #self.rdpbutton.grid(row=4, column=0, padx=10, pady=10)
        self.rdpbutton = ttk.Button(self.frame1, text=" RDP  ", command=self.rdp)
        self.rdpbutton.grid(row=4, column=0, ipadx=45, ipady=25, padx=10, pady=10)

        #self.msinfo32button = Button(self.frame1, text="MSINFO32", bg="#c7c7c7", padx=45, pady=25, command=self.msinfo32)
        #self.msinfo32button.config(font=('McLaren Bespoke', 11))
        #self.msinfo32button.grid(row=4, column=1, padx=10, pady=10)
        self.msinfo32button = ttk.Button(self.frame1, text="MSINFO32", command=self.msinfo32)
        self.msinfo32button.grid(row=4, column=1, ipadx=45, ipady=25, padx=10, pady=10)

        #self.flushbutton = Button(self.frame1, text="Flush DNS", bg="#c7c7c7", padx=37, pady=25, command=flush)
        #self.flushbutton.config(font=('McLaren Bespoke',11))
        #self.flushbutton.grid(row=4, column=2, padx=10, pady=10)
        self.flushbutton = ttk.Button(self.frame1, text="Flush DNS", command=flush)
        self.flushbutton.grid(row=4, column=2, ipadx=45, ipady=25, padx=10, pady=10)

        #self.domainbutton = Button(self.frame1, text="Domain", bg="#c7c7c7", padx=46, pady=25, command=self.domain)
        #self.domainbutton.config(font=('McLaren Bespoke',11))
        #self.domainbutton.grid(row=5, column=0, padx=10, pady=10)
        self.domainbutton = ttk.Button(self.frame1, text="Domain", command=self.domain)
        self.domainbutton.grid(row=5, column=0, ipadx=45, ipady=25, padx=10, pady=10)

        #self.modelbutton = Button(self.frame1, text="   Model   ", bg="#c7c7c7", padx=50, pady=25, command=self.model)
        #self.modelbutton.config(font=('McLaren Bespoke',11))
        #self.modelbutton.grid(row=5, column=1, padx=10, pady=10)
        self.modelbutton = ttk.Button(self.frame1, text="   Model   ", command=self.model)
        self.modelbutton.grid(row=5, column=1, ipadx=45, ipady=25, padx=10, pady=10)

        #self.sparebutton = Button(self.frame1, text=" Spare ", bg="#c7c7c7", padx=50, pady=25, command=self.spare)
        #self.sparebutton.config(font=('McLaren Bespoke',11))
        #self.sparebutton.grid(row=5, column=2, padx=10, pady=10)
        self.adbutton = ttk.Button(self.frame1, text="Open AD", command=AD)
        self.adbutton.grid(row=5, column=2, ipadx=45, ipady=25, padx=10, pady=10)

        self.signature = Label(self.frame1, text="Wincheck by Rish", bg="#F48500")
        self.signature.config(font=('McLaren Bespoke',8))
        self.signature.grid(row=6, column=0, columnspan=3, pady=20)
        
    
    def ping(self):
        for i in self.master.winfo_children():
            i.destroy()
        self.frame2 = Frame(self.master, width=300, height=300, bg="#F48500")
        self.frame2.grid(row=0, column=0, sticky='nwse')

        self.Title = Label(self.frame2, text='Welcome to Wincheck',bg="#F48500")
        self.Title.config(font=('McLaren Bespoke Bold', 18))
        self.Title.grid(row=0, column=0, columnspan=3)

        self.logo = PhotoImage(file="McLaren_Logo_1.png")
        self.logo_label = Label(self.frame2, image=self.logo,borderwidth=0, highlightthickness=0)
        self.logo_label.grid(row=0, column=0, sticky=S, pady=5, rowspan=2)

        self.Subtitle = Label(self.frame2, text="Please enter a computername and press submit", bg="#F48500")
        self.Subtitle.config(font=('McLaren Bespoke',12))
        self.Subtitle.grid(row=1, column=0, columnspan=3)

        self.Space = Label(self.frame2, text=' ', bg="#F48500")
        self.Space.grid(row=2, column=0)

        self.pinglabel = Label(self.frame2, text="Computer Name:", bg="#F48500")
        self.pinglabel.config(font=('McLaren Bespoke',10))
        self.pinglabel.grid(row=3, column=0)

        #self.pinginputbox = Entry(self.frame2, width =15, bg="#c7c7c7")
        #self.pinginputbox.config(font=('McLaren Bespoke',10))
        #self.pinginputbox.grid(row=3, column=1)
        self.pinginputbox = ttk.Entry(self.frame2)
        self.pinginputbox.config(font=('McLaren Bespoke',10))
        self.pinginputbox.grid(row=3, column=1, ipadx=15)

        #self.submitping = Button(self.frame2, text="Submit", height=1, width=10, bg="#c7c7c7", command= lambda: ExecuteFunction('ping '+self.pinginputbox.get(), self.pingoutput))
        #self.submitping.config(font=('McLaren Bespoke',8))
        #self.submitping.grid(row=3, column=2)
        self.submitping = ttk.Button(self.frame2, text="Submit", command= lambda: ExecuteFunction('ping '+self.pinginputbox.get(), self.pingoutput)) 
        self.submitping.grid(row=3, column=2, ipadx=10, ipady=1)
        

        self.pingoutput = Text(self.frame2, width=63, height=15, bg="white",borderwidth=0)
        self.pingoutput.grid(row=4, column=0, columnspan=3, padx=30, pady=30)

        #self.returnbutton = Button(self.frame2, text="Main Menu", width=20, height=1, bg="#c7c7c7", command=self.Main_Menu)
        #self.returnbutton.config(font=('McLaren Bespoke',8))
        #self.returnbutton.grid(row=5, column=0, columnspan=3, padx=30, pady=10)
        self.returnbutton = ttk.Button(self.frame2, text="Main Menu", command=self.Main_Menu) 
        self.returnbutton.grid(row=5, column=0, ipadx=20, ipady=1, columnspan=3)

    def username(self):
        for i in self.master.winfo_children():
            i.destroy()
        self.frame3 = Frame(self.master, width=300, height=300, bg="#F48500")
        self.frame3.grid(row=0, column=0, sticky='nwse')

        self.Title = Label(self.frame3, text='Welcome to Wincheck',bg="#F48500")
        self.Title.config(font=('McLaren Bespoke Bold', 18))
        self.Title.grid(row=0, column=0, columnspan=3)

        self.logo = PhotoImage(file="McLaren_Logo_1.png")
        self.logo_label = Label(self.frame3, image=self.logo,borderwidth=0, highlightthickness=0)
        self.logo_label.grid(row=0, column=0, sticky=S, pady=5, rowspan=2)

        self.Subtitle = Label(self.frame3, text="Please enter a computername and press submit", bg="#F48500")
        self.Subtitle.config(font=('McLaren Bespoke',12))
        self.Subtitle.grid(row=1, column=0, columnspan=3)

        self.Space = Label(self.frame3, text=' ', bg="#F48500")
        self.Space.grid(row=2, column=0)

        self.usernamelabel = Label(self.frame3, text="Computer Name:", bg="#F48500")
        self.usernamelabel.config(font=('McLaren Bespoke',10))
        self.usernamelabel.grid(row=3, column=0)

        #self.usernameinputbox = Entry(self.frame3, width =15, bg="#c7c7c7")
        #self.usernameinputbox.config(font=('McLaren Bespoke',10))
        #self.usernameinputbox.grid(row=3, column=1)
        self.usernameinputbox = ttk.Entry(self.frame3)
        self.usernameinputbox.config(font=('McLaren Bespoke',10))
        self.usernameinputbox.grid(row=3, column=1, ipadx=15)

        #self.submitusername = Button(self.frame3, text="Submit", height=1, width=10, bg="#c7c7c7", command= lambda: ExecuteFunction('wmic /node:'+self.usernameinputbox.get()+' computersystem get username', self.usernameoutput))
        #self.submitusername.config(font=('McLaren Bespoke',8))
        #self.submitusername.grid(row=3, column=2)
        self.submitusername = ttk.Button(self.frame3, text="Submit", command= lambda: ExecuteFunction('wmic /node:'+self.usernameinputbox.get()+' computersystem get username', self.usernameoutput))
        self.submitusername.grid(row=3, column=2, ipadx=10, ipady=1)


        self.usernameoutput = Text(self.frame3, width=63, height=15, bg="white", borderwidth=0)
        self.usernameoutput.grid(row=4, column=0, columnspan=3, padx=30, pady=30)
        
        #self.returnbutton = Button(self.frame3, text="Main Menu", width=20, height=1, bg="#c7c7c7", command=self.Main_Menu)
        #self.returnbutton.config(font=('McLaren Bespoke',8))
        #self.returnbutton.grid(row=5, column=0, columnspan=3, padx=30, pady=10)
        self.returnbutton = ttk.Button(self.frame3, text="Main Menu", command=self.Main_Menu) 
        self.returnbutton.grid(row=5, column=0, ipadx=20, ipady=1, columnspan=3)

    def build(self):
        for i in self.master.winfo_children():
            i.destroy()
        self.frame4 = Frame(self.master, width=300, height=300, bg="#F48500")
        self.frame4.grid(row=0, column=0, sticky='nwse')

        self.Title = Label(self.frame4, text='Welcome to Wincheck',bg="#F48500")
        self.Title.config(font=('McLaren Bespoke Bold', 18))
        self.Title.grid(row=0, column=0, columnspan=3)

        self.logo = PhotoImage(file="McLaren_Logo_1.png")
        self.logo_label = Label(self.frame4, image=self.logo,borderwidth=0, highlightthickness=0)
        self.logo_label.grid(row=0, column=0, sticky=S, pady=5, rowspan=2)

        self.Subtitle = Label(self.frame4, text="Please enter a computername and press submit", bg="#F48500")
        self.Subtitle.config(font=('McLaren Bespoke',12))
        self.Subtitle.grid(row=1, column=0, columnspan=3)

        self.Space = Label(self.frame4, text=' ', bg="#F48500")
        self.Space.grid(row=2, column=0)

        self.buildlabel = Label(self.frame4, text="Computer Name:", bg="#F48500")
        self.buildlabel.config(font=('McLaren Bespoke',10))
        self.buildlabel.grid(row=3, column=0)

        #self.buildinputbox = Entry(self.frame4, width =15, bg="#c7c7c7")
        #self.buildinputbox.config(font=('McLaren Bespoke',10))
        #self.buildinputbox.grid(row=3, column=1)
        self.buildinputbox = ttk.Entry(self.frame4)
        self.buildinputbox.config(font=('McLaren Bespoke',10))
        self.buildinputbox.grid(row=3, column=1, ipadx=15)

        #self.submitbuild = Button(self.frame4, text="Submit", height=1, width=10, bg="#c7c7c7", command= lambda: ExecuteFunction('wmic /node: '+self.buildinputbox.get()+' os get BuildNumber',self.buildoutput))
        #self.submitbuild.config(font=('McLaren Bespoke',8))
        #self.submitbuild.grid(row=3, column=2)
        self.submitbuild = ttk.Button(self.frame4, text="Submit", command= lambda: ExecuteFunction('wmic /node: '+self.buildinputbox.get()+' os get BuildNumber',self.buildoutput))
        self.submitbuild.grid(row=3, column=2, ipadx=10, ipady=1)

        self.buildoutput = Text(self.frame4, width=63, height=15, bg="white", borderwidth=0)
        self.buildoutput.grid(row=4, column=0, columnspan=3, padx=30, pady=30)
        
        #self.returnbutton = Button(self.frame4, text="Main Menu", width=20, height=1, bg="#c7c7c7", command=self.Main_Menu)
        #self.returnbutton.config(font=('McLaren Bespoke',8))
        #self.returnbutton.grid(row=5, column=0, columnspan=3, padx=30, pady=10)
        self.returnbutton = ttk.Button(self.frame4, text="Main Menu", command=self.Main_Menu) 
        self.returnbutton.grid(row=5, column=0, ipadx=20, ipady=1, columnspan=3)


    def rdp(self):
        for i in self.master.winfo_children():
            i.destroy()
        self.frame5 = Frame(self.master, width=300, height=300, bg="#F48500")
        self.frame5.grid(row=0, column=0, sticky='nwse')

        self.Title = Label(self.frame5, text='Welcome to Wincheck',bg="#F48500")
        self.Title.config(font=('McLaren Bespoke Bold', 18))
        self.Title.grid(row=0, column=0, columnspan=3)

        self.logo = PhotoImage(file="McLaren_Logo_1.png")
        self.logo_label = Label(self.frame5, image=self.logo,borderwidth=0, highlightthickness=0)
        self.logo_label.grid(row=0, column=0, sticky=S, pady=5, rowspan=2)

        self.Subtitle = Label(self.frame5, text="Please enter a computername and press submit", bg="#F48500")
        self.Subtitle.config(font=('McLaren Bespoke',12))
        self.Subtitle.grid(row=1, column=0, columnspan=3)

        self.Space = Label(self.frame5, text=' ', bg="#F48500")
        self.Space.grid(row=2, column=0)

        self.rdplabel = Label(self.frame5, text="Computer Name:", bg="#F48500")
        self.rdplabel.config(font=('McLaren Bespoke',10))
        self.rdplabel.grid(row=3, column=0)

        #self.rdpinputbox = Entry(self.frame5, width =15, bg="#c7c7c7")
        #self.rdpinputbox.config(font=('McLaren Bespoke',10))
        #self.rdpinputbox.grid(row=3, column=1)
        self.rdpinputbox = ttk.Entry(self.frame5)
        self.rdpinputbox.config(font=('McLaren Bespoke',10))
        self.rdpinputbox.grid(row=3, column=1, ipadx=15)

        #self.submitrdp = Button(self.frame5, text="Submit", height=1, width=10, bg="#c7c7c7", command= lambda: ExecuteFunction('mstsc /console /v:'+self.rdpinputbox.get(), self.rdpoutput)) 
        #self.submitrdp.config(font=('McLaren Bespoke',8))
        #self.submitrdp.grid(row=3, column=2)
        self.submitrdp = ttk.Button(self.frame5, text="Submit", command= lambda: ExecuteFunction('mstsc /console /v:'+self.rdpinputbox.get(), self.rdpoutput)) 
        self.submitrdp.grid(row=3, column=2, ipadx=10, ipady=1)

        self.rdpoutput = Text(self.frame5, width=63, height=15, bg="white", borderwidth=0)
        self.rdpoutput.grid(row=4, column=0, columnspan=3, padx=30, pady=30)
        
        #self.returnbutton = Button(self.frame5, text="Main Menu", width=20, height=1, bg="#c7c7c7", command=self.Main_Menu)
        #self.returnbutton.config(font=('McLaren Bespoke',8))
        #self.returnbutton.grid(row=5, column=0, columnspan=3, padx=30, pady=10)
        self.returnbutton = ttk.Button(self.frame5, text="Main Menu", command=self.Main_Menu) 
        self.returnbutton.grid(row=5, column=0, ipadx=20, ipady=1, columnspan=3)
    
    def msinfo32(self):
        for i in self.master.winfo_children():
            i.destroy()
        self.frame6 = Frame(self.master, width=300, height=300, bg="#F48500")
        self.frame6.grid(row=0, column=0, sticky='nwse')

        self.Title = Label(self.frame6, text='Welcome to Wincheck',bg="#F48500")
        self.Title.config(font=('McLaren Bespoke Bold', 18))
        self.Title.grid(row=0, column=0, columnspan=3)

        self.logo = PhotoImage(file="McLaren_Logo_1.png")
        self.logo_label = Label(self.frame6, image=self.logo,borderwidth=0, highlightthickness=0)
        self.logo_label.grid(row=0, column=0, sticky=S, pady=5, rowspan=2)

        self.Subtitle = Label(self.frame6, text="Please enter a computername and press submit", bg="#F48500")
        self.Subtitle.config(font=('McLaren Bespoke',12))
        self.Subtitle.grid(row=1, column=0, columnspan=3)

        self.Space = Label(self.frame6, text=' ', bg="#F48500")
        self.Space.grid(row=2, column=0)

        self.msinfo32label = Label(self.frame6, text="Computer Name:", bg="#F48500")
        self.msinfo32label.config(font=('McLaren Bespoke',10))
        self.msinfo32label.grid(row=3, column=0)

        #self.msinfo32inputbox = Entry(self.frame6, width =15, bg="#c7c7c7")
        #self.msinfo32inputbox.config(font=('McLaren Bespoke',10))
        #self.msinfo32inputbox.grid(row=3, column=1)
        self.msinfo32inputbox = ttk.Entry(self.frame6)
        self.msinfo32inputbox.config(font=('McLaren Bespoke',10))
        self.msinfo32inputbox.grid(row=3, column=1, ipadx=15)

        #self.submitmsinfo32 = Button(self.frame6, text="Submit", height=1, width=10, bg="#c7c7c7", command= lambda: ExecuteFunction('msinfo32 /computer '+self.msinfo32inputbox.get(),self.msinfo32output))
        #self.submitmsinfo32.config(font=('McLaren Bespoke',8))
        #self.submitmsinfo32.grid(row=3, column=2)
        self.submitmsinfo32 = ttk.Button(self.frame6, text="Submit", command= lambda: ExecuteFunction('msinfo32 /computer '+self.msinfo32inputbox.get(),self.msinfo32output))
        self.submitmsinfo32.grid(row=3, column=2, ipadx=10, ipady=1)

        self.msinfo32output = Text(self.frame6, width=63, height=15, bg="white", borderwidth=0)
        self.msinfo32output.grid(row=4, column=0, columnspan=3, padx=30, pady=30)
        
        #self.returnbutton = Button(self.frame6, text="Main Menu", width=20, height=1, bg="#c7c7c7", command=self.Main_Menu)
        #self.returnbutton.config(font=('McLaren Bespoke',8))
        #self.returnbutton.grid(row=5, column=0, columnspan=3, padx=30, pady=10)
        self.returnbutton = ttk.Button(self.frame6, text="Main Menu", command=self.Main_Menu) 
        self.returnbutton.grid(row=5, column=0, ipadx=20, ipady=1, columnspan=3)

    def domain(self):
        for i in self.master.winfo_children():
            i.destroy()
        self.frame8 = Frame(self.master, width=300, height=300, bg="#F48500")
        self.frame8.grid(row=0, column=0, sticky='nwse')

        self.Title = Label(self.frame8, text='Welcome to Wincheck',bg="#F48500")
        self.Title.config(font=('McLaren Bespoke Bold', 18))
        self.Title.grid(row=0, column=0, columnspan=3)

        self.logo = PhotoImage(file="McLaren_Logo_1.png")
        self.logo_label = Label(self.frame8, image=self.logo,borderwidth=0, highlightthickness=0)
        self.logo_label.grid(row=0, column=0, sticky=S, pady=5, rowspan=2)

        self.Subtitle = Label(self.frame8, text="Please enter a computername and press submit", bg="#F48500")
        self.Subtitle.config(font=('McLaren Bespoke',12))
        self.Subtitle.grid(row=1, column=0, columnspan=3)

        self.Space = Label(self.frame8, text=' ', bg="#F48500")
        self.Space.grid(row=2, column=0)

        self.domainlabel = Label(self.frame8, text="Computer Name:", bg="#F48500")
        self.domainlabel.config(font=('McLaren Bespoke',10))
        self.domainlabel.grid(row=3, column=0)

        #self.domaininputbox = Entry(self.frame8, width =15, bg="#c7c7c7")
        #self.domaininputbox.config(font=('McLaren Bespoke',10))
        #self.domaininputbox.grid(row=3, column=1)
        self.domaininputbox = ttk.Entry(self.frame8)
        self.domaininputbox.config(font=('McLaren Bespoke',10))
        self.domaininputbox.grid(row=3, column=1, ipadx=15)

        #self.submitdomain = Button(self.frame8, text="Submit", height=1, width=10, bg="#c7c7c7", command= lambda: ExecuteFunction('wmic /node:'+self.domaininputbox.get()+' computersystem get domain | findstr /r /v "Domain"', self.domainoutput))
        #self.submitdomain.config(font=('McLaren Bespoke',8))
        #self.submitdomain.grid(row=3, column=2)
        self.submitdomain = ttk.Button(self.frame8, text="Submit", command= lambda: ExecuteFunction('wmic /node:'+self.domaininputbox.get()+' computersystem get domain | findstr /r /v "Domain"', self.domainoutput))
        self.submitdomain.grid(row=3, column=2, ipadx=10, ipady=1)

        self.domainoutput = Text(self.frame8, width=63, height=15, bg="white", borderwidth=0)
        self.domainoutput.grid(row=4, column=0, columnspan=3, padx=30, pady=30)
        
        #self.returnbutton = Button(self.frame8, text="Main Menu", width=20, height=1, bg="#c7c7c7", command=self.Main_Menu)
        #self.returnbutton.config(font=('McLaren Bespoke',8))
        #self.returnbutton.grid(row=5, column=0, columnspan=3, padx=30, pady=10)
        self.returnbutton = ttk.Button(self.frame8, text="Main Menu", command=self.Main_Menu) 
        self.returnbutton.grid(row=5, column=0, ipadx=20, ipady=1, columnspan=3)

    def model(self):
        for i in self.master.winfo_children():
            i.destroy()
        self.frame9 = Frame(self.master, width=300, height=300, bg="#F48500")
        self.frame9.grid(row=0, column=0, sticky='nwse')

        self.Title = Label(self.frame9, text='Welcome to Wincheck',bg="#F48500")
        self.Title.config(font=('McLaren Bespoke Bold', 18))
        self.Title.grid(row=0, column=0, columnspan=3)

        self.logo = PhotoImage(file="McLaren_Logo_1.png")
        self.logo_label = Label(self.frame9, image=self.logo,borderwidth=0, highlightthickness=0)
        self.logo_label.grid(row=0, column=0, sticky=S, pady=5, rowspan=2)

        self.Subtitle = Label(self.frame9, text="Please enter a computername and press submit", bg="#F48500")
        self.Subtitle.config(font=('McLaren Bespoke',12))
        self.Subtitle.grid(row=1, column=0, columnspan=3)

        self.Space = Label(self.frame9, text=' ', bg="#F48500")
        self.Space.grid(row=2, column=0)

        self.modellabel = Label(self.frame9, text="Computer Name:", bg="#F48500")
        self.modellabel.config(font=('McLaren Bespoke',10))
        self.modellabel.grid(row=3, column=0)

        #self.modelinputbox = Entry(self.frame9, width =15, bg="#c7c7c7")
        #self.modelinputbox.config(font=('McLaren Bespoke',10))
        #self.modelinputbox.grid(row=3, column=1)
        self.modelinputbox = ttk.Entry(self.frame9)
        self.modelinputbox.config(font=('McLaren Bespoke',10))
        self.modelinputbox.grid(row=3, column=1, ipadx=15)

        #self.submitmodel = Button(self.frame9, text="Submit", height=1, width=10, bg="#c7c7c7", command= lambda: ExecuteFunction('WMIC /node:'+self.modelinputbox.get()+' CSPRODUCT GET NAME | findstr /r /v "Name"', self.modeloutput))
        #self.submitmodel.config(font=('McLaren Bespoke',8))
        #self.submitmodel.grid(row=3, column=2)
        self.submitmodel = ttk.Button(self.frame9, text="Submit", command= lambda: ExecuteFunction('WMIC /node:'+self.modelinputbox.get()+' CSPRODUCT GET NAME | findstr /r /v "Name"', self.modeloutput))
        self.submitmodel.grid(row=3, column=2, ipadx=10, ipady=1)

        self.modeloutput = Text(self.frame9, width=63, height=15, bg="white", borderwidth=0)
        self.modeloutput.grid(row=4, column=0, columnspan=3, padx=30, pady=30)
        
        #self.returnbutton = Button(self.frame9, text="Main Menu", width=20, height=1, bg="#c7c7c7", command=self.Main_Menu)
        #self.returnbutton.config(font=('McLaren Bespoke',8))
        #self.returnbutton.grid(row=5, column=0, columnspan=3, padx=30, pady=10)
        self.returnbutton = ttk.Button(self.frame9, text="Main Menu", command=self.Main_Menu) 
        self.returnbutton.grid(row=5, column=0, ipadx=20, ipady=1, columnspan=3)

root = Tk()
app(root)
root.mainloop()