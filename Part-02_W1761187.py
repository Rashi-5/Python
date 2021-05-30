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
        if c_Pass==120:                     #progress
            print("Your Progression outcome is 'PROGRESS'\n")
            p_count+=1
        elif c_Pass==100:                   #Progress-module trailer
            print("Your progression outcome is 'PROGRESS-MODULE TRAILER'\n")
            t_count+=1
        elif c_Pass<=40 and c_Fail>=80:     #excluded
            print("Your progression outcome is 'EXCLUDE'")
            e_count+=1
        else:                               #Do not progress-module trailer
            print("Your progression outcome is 'DO NOT PROGRESS-MODULE RETRIEVER'\n")
            f_count+=1

        count=p_count+f_count+e_count+t_count
        list_1=[["Progress ","    *    "*p_count],["Trailing ","    *    "*t_count],["Retriever","    *    "*f_count],[" Excluded","    *    "*e_count]] 
        Quit=str(input("***Press enter to continue the program***\n   Enter 'q' to quit the program\n"))
        if Quit=="q":
            for x,y,z,a in zip(*list_1): 
                print(x,y,z,a)              #print vertical list
            print(count,"outcomes in total\n")
            print("__You are exiting the program__\n")
            Exit=True                       #the program terminates here
    else:
        print("Total incorrect. Please Enter valid marks!\n")
        continue
            

