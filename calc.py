import gi
import time
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class GridWindow(Gtk.Window):


    def __init__(self):
        Gtk.Window.__init__(self, title="Calculator")

        grid = Gtk.Grid()
        self.add(grid)
        self.entry=Gtk.Entry()
        self.st=''
        self.ls=[]
        self.flag=''

        button1 = Gtk.Button(label="1")
        button2 = Gtk.Button(label="2")
        button3 = Gtk.Button(label="3")
        button4 = Gtk.Button(label="4")
        button5 = Gtk.Button(label="5")
        button6 = Gtk.Button(label="6")
        button7 = Gtk.Button(label="7")
        button8 = Gtk.Button(label="8")
        button9 = Gtk.Button(label="9")
        button0 = Gtk.Button(label="0")
        buttonp = Gtk.Button(label="+")
        buttonmi = Gtk.Button(label="-")
        buttonmu = Gtk.Button(label="*")
        buttond = Gtk.Button(label="/")
        buttonc = Gtk.Button(label="c")
        buttone = Gtk.Button(label="=")
        button1.connect("clicked",self.on_click_button)
        button2.connect("clicked",self.on_click_button)
        button3.connect("clicked",self.on_click_button)
        button4.connect("clicked",self.on_click_button)
        button5.connect("clicked",self.on_click_button)
        button6.connect("clicked",self.on_click_button)
        button7.connect("clicked",self.on_click_button)
        button8.connect("clicked",self.on_click_button)
        button9.connect("clicked",self.on_click_button)
        button0.connect("clicked",self.on_click_button)
        buttonp.connect("clicked",self.on_click_button)
        buttonmi.connect("clicked",self.on_click_button)
        buttonmu.connect("clicked",self.on_click_button)
        buttond.connect("clicked",self.on_click_button)
        buttonc.connect("clicked",self.on_click_button)
        buttone.connect("clicked",self.on_click_button)


 
        grid.attach(self.entry,0,0,3,1)
        grid.attach(button1, 0, 1, 1, 1)
        grid.attach(button2, 1, 1, 1, 1)
        grid.attach(button3, 2, 1, 1, 1)
        grid.attach(button4, 0, 2, 1, 1)
        grid.attach(button5, 1, 2, 1, 1)
        grid.attach(button6, 2, 2, 1, 1)
        grid.attach(button7, 0, 3, 1, 1)
        grid.attach(button8, 1, 3, 1, 1)
        grid.attach(button9, 2, 3, 1, 1)
        grid.attach(button0, 0, 4, 1, 1)
        grid.attach(buttone, 1, 4, 1, 1)
        grid.attach(buttonc, 2, 4, 1, 1)
        grid.attach(buttonp, 3, 1, 1, 1)
        grid.attach(buttonmi, 3, 2, 1, 1)
        grid.attach(buttonmu, 3, 3, 1, 1)
        grid.attach(buttond, 3, 4, 1, 1)
    def on_click_button(self,button):
        if button.props.label=="c":
            self.st = self.st[:-1]
            self.entry.set_text(self.st)
        elif button.props.label=="=":
            if len(self.ls)!=1:
                self.entry.set_text("ooops")
                #self.entry.set_text("")
                print self.ls
                self.st=''
                self.ls=[]
            else:
                #print self.ls
                self.ls.append(int(self.st))
                if self.flag=="+":
                 self.entry.set_text(str(self.ls[0]+self.ls[1]))
                elif self.flag=="-":
                 self.entry.set_text(str(self.ls[0]-self.ls[1]))
                elif self.flag=="*":
                 self.entry.set_text(str(self.ls[0]*self.ls[1]))
                if self.flag=="/":
                 self.entry.set_text(str(self.ls[0]/self.ls[1]))

                self.ls=[]
                self.st=''
        elif button.props.label=="1" or button.props.label=="2" or button.props.label=="3" or button.props.label=="4" or button.props.label=="5" or button.props.label=="6" or  button.props.label=="7" or  button.props.label=="8" or button.props.label=="9" or  button.props.label=="0":
            self.st=self.st+button.props.label
            self.entry.set_text(self.st)
        elif button.props.label=="+":
            self.flag="+"
            self.ls.append(int(self.st))
            self.entry.set_text("")
            self.st=''

        elif button.props.label=="-":
            self.flag="-"
            self.ls.append(int(self.st))
            self.entry.set_text("")
            self.st=''
    

        elif button.props.label=="*":
            self.flag="*"
            self.ls.append(int(self.st))
            self.entry.set_text("")
            self.st=''

        else:
            self.flag="/"
            self.ls.append(int(self.st))
            self.entry.set_text("")
            self.st=''

            
            
            
        
win = GridWindow()
win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()
