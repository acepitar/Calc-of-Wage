from ast import Continue, While
from tkinter import Y

Y = 1
N = 2
A = Y
while A ==Y:
        A = input('Next Cogboy?(Y/N)?')
        id = int(input('Hello Cogboy, please enter your cog ID number:'))
        print (id)
        hrs = int(input("Please enter hrs spunt:"))
        HW = 32.9
        OT= hrs - 40 
        if id >=1900:
            if hrs >=40:
                int(OT)
                hrs -= OT
                TOT = 27.9*1.5
                TOT += 5
                int(HW)
                HW *= hrs
                TOT *= OT
                print ('$'+str(TOT)+ 'Overtime Pay')
                print ('$'+str(HW)+' Normal Pay')  
                print (str(hrs) + 'Normal hrs')
                print (str(OT)+ 'Overtime hrs')  
            else:
                HW *= hrs
                print ('$'+str(HW))  
                print (str(hrs) + 'Normal hrs')
        else:
            if hrs >=40:
                HW = 27.9
                int(OT)
                hrs -= OT
                TOT = 27.9*1.5
                int(HW)
                HW *= hrs
                TOT *= OT
                print ('$'+str(TOT))
                print ('$'+str(HW))  
                print (str(hrs) + ' Normal hrs')
                print (str(OT)+ ' Overtime hrs')  

            else:
                HW *= hrs
                print ('$'+str(HW))  
                print (str(hrs) + ' Normal hrs')
        A = Y
        continue
