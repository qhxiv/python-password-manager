
import tkinter
from tkinter import ttk
from PIL import Image, ImageTk
class center_frame_window: 
    def __init__(self,root):
        
        img = tkinter.PhotoImage(file='img\icon.png')
        
        self.root = root
        self.root.title("Password Manager")
        self.root.geometry("850x420+0+0")
        self.root.configure(bg="orange")
        self.root.resizable(False,False)
        self.root.iconphoto(False,img)
        
        self.center_frame = tkinter.Frame(root, bg="#d3d3d3")
        self.center_frame.grid(row=0, column=0, padx=10, pady=10)

        self.frame = tkinter.Frame(self.center_frame,highlightbackground='brown',highlightthickness=2 ,padx=10,pady=20)
        self.frame.grid()
        self.frame1 = tkinter.Frame(self.center_frame,highlightbackground='black',highlightthickness=1 ,padx=10,pady=20)
        self.frame1.grid()
        
        #Create
        self.create_buttons()
        self.create_records_tree()
        
        self.search_entry = tkinter.Entry(self.frame,width=20,font = ('Arial',12))
        tkinter.Button(self.frame,text='Search',background='#def3f6',font = ('Arial',12),width=20).grid(row= self.row_num,column=self.col_num)
        self.col_num +=1
        self.search_entry.grid(row = self.row_num,column = self.col_num)
        
        
    def create_buttons(self):
        self.row_num = 0
        self.col_num = 0
        buttons_info = (('Add','#def3f6',self.add_btn), ('Update','#def3f6',self.update_record),('Copy Password','#def3f6',self.copy_password),('Delete' , 'red',self.delete_record),('Show All Records','#def3f6',self.show_record),('Encrypt Password','#def3f6',self.encrypt_password))   
        for button in buttons_info:
            if button[0] == 'Show All Records':
                self.row_num += 1
                self.col_num = 0
            tkinter.Button(self.frame, text=button[0],background=button[1],foreground='black',font=('Arial',12),width=20,pady=1,command=button[2]).grid(row=self.row_num,column=self.col_num,padx= 5,pady=10)    
            self.col_num += 1
    
    def create_entry_labels(self,add_window):
        col_num = row_num = 0
        labels_info =('Website','Username','Password')
        for label_info in labels_info:
            tkinter.Label(add_window,text=label_info,font=('Arial',12),padx=5,pady=3).grid(row=row_num,column=col_num,padx=5,pady=2)
            row_num += 1
               
    def create_entry_boxes(self,add_window):
        self.entry_boxes = []
        row_num = 0
        col_num = 1
        for i in range(3):
            showw = ""
            if i == 2:
                showw = "*"
            entry_box = tkinter.Entry(add_window,width=20,font=("Arial",12),show=showw)
            entry_box.grid(row=row_num,column=col_num,padx=5,pady=2)
            row_num += 1
            self.entry_boxes.append(entry_box)
            
    def create_records_tree(self):
        columns = ('ID','Website','Username','Password')
        self.records_tree = ttk.Treeview(self.center_frame,columns=columns,show='headings')
        self.records_tree.heading('ID',text='ID')
        self.records_tree.heading('Website',text='Website')
        self.records_tree.heading('Username',text='Username')
        self.records_tree.heading('Password',text='Password')
        self.records_tree.grid(padx=10, pady=10)
            
    def add_btn(self):
        self.add_window = tkinter.Tk()
        self.add_window.title("Add new record")
        self.add_window.resizable(False,False)
        self.create_entry_labels(self.add_window)
        self.create_entry_boxes(self.add_window)
        add_window_btn = tkinter.Button(self.add_window, text='Add',font=('Arial',12),width=10,pady=1,background='#def3f6',command=self.add_record).grid(row=4,column=0,padx= 5,pady=10)
        self.add_window.mainloop()
    
    def add_record(self):
        pass
        
    def update_record(self):
        pass    
    
    def delete_record(self):
        pass

    def show_record(self):
        pass
    
    def encrypt_password(self):
        pass
  
    def copy_password(self):
        pass    
    
    def search(self):
        pass

        
if __name__ == '__main__':
    
    root = tkinter.Tk()
    root_class = center_frame_window(root)
    root.mainloop()