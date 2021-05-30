c_Pass,c_Defer,c_Fail,total=0,0,0,0         #number of credits at Pass,Defer,Fail the sum of all 3 creadits
Exit=False                                  #if the user enter "q" Exit value become False and program terminates
p_count,t_count,f_count,e_count=0,0,0,0
def credit(name): 
    while True:
        try:
            marks=int(input("Enter Your Credit {} :".format(name)))
            if marks in(0,20,40,60,80,100,120):
                return marks
            else:
                print("Range error\n")
        except:
            print("Intigers required")
        
print("------PROGRESSION OUTCOME-------\n")
while Exit==False:                          #this will run until "q" is enetered
    c_Pass=credit("Pass")
    c_Defer=credit("Defer")
    c_Fail=credit("Fail")
    
    total=c_Pass+c_Defer+c_Fail
    if total==120:
        print("__Total is correct__\n")
        if c_Pass==120:                       #progress
            print("Progression outcome is 'PROGRESS'\n")
            p_count+=1
                    
        elif c_Pass==100:                     #Progress-module trailer
            print("Progression outcome is 'PROGRESS-MODULE TRAILER'\n")
            t_count+=1
                    
        elif c_Pass<=40 and c_Fail>=80:         #excluded
            print("Progression outcome is 'EXCLUDE'\n")
            e_count+=1
                
        else:                               #Do not progress-module trailer
            print("Progression outcome is 'DO NOT PROGRESS-MODULE RETRIEVER'\n")
            f_count+=1                   
        
        count=p_count+f_count+e_count+t_count
        Quit=str(input("***Press enter to continue the program***\n   Enter 'q' to quit the program\n"))
        if Quit=="q":
            print("Progress ",p_count," *"*p_count)
            print("Trailing ",t_count," *"*t_count)
            print("Retriever ",f_count," *"*f_count)
            print("Excluded ",e_count," *"*e_count)
            print(count,"outcomes in total\n")
            print("__You are exiting the program__\n")
            Exit=True                       #the program terminates here
                    
    else:
        print("__Total incorrect__\nPlease Enter valid marks!")
        continue
        
        

