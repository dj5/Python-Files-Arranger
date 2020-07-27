"""
This program helps in arranging file based on there date.
It arranges files in folders of their date (month year)
It creates a csv file which shows folder name and no. of files in it
Requirement:
Pandas library
"""
import os,time
import pandas
from tkinter import filedialog
from tkinter import *
class Arrange:
    def select_path(self):
        self.path=filedialog.askdirectory()
        
    def gui(self):	# User interface using Tkinter
        self.window = Tk()
        self.path= StringVar()
        arng_btn=Button(self.window,text="Select Path",command=self.select_path)
        arng_btn.grid(row=0,column=0)
        btn=Button(self.window,text="Arrange",command=self.arr)
        btn.grid(row=0,column=1)
        self.window.mainloop()
    def arr(self):	# This function arranges files inside the path specified in ascending order 
        year=[]
        df=pandas.DataFrame()
        no_of_files={}
        cd= self.path  #input("Enter the path which you want to arrange ")
        self.window.destroy()
        if os.path.exists(cd)==False:
         self.gui()
        else:
            os.chdir(cd)

            for l in os.listdir(os.curdir):
            	try:
            		fls=time.gmtime(os.path.getmtime(l))
            		yr=str(fls.tm_year) + " "+str(fls.tm_mon)

            	except:
            		pass
            	if yr not in year:
            		year.append(yr)
            		no_of_files[yr]=0

            #print(year)
            cnt=0
            df["Folders"]=[]
            df2=df.T
            for y in year:

                try:
                    os.mkdir(y)
                    df2[cnt]=y
                    cnt+=1
                except:
                    pass
            for l in os.listdir(os.curdir):
            	try:
            		fls=time.gmtime(os.path.getmtime(l))
            		yr=str(fls.tm_year) + " "+str(fls.tm_mon)
            	except:
            		pass

            	if l not in year and l!="arranger.py":

            		try:
            			os.rename(l , yr+"/"+l)
            			no_of_files[yr]+=1
            		except:
            			pass
            df=df2.T
            df["No. of files"]=list(no_of_files.values())
            df.to_csv("arrange.csv")
            #print (no_of_files)
if __name__=="__main__":
	obj=Arrange()
	obj.gui()
