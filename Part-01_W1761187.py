# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
# Any code taken from other sources is referenced within my code solution.  
# Student ID: 2019102
# Uow Number: W1761187
# Date:29th November 2019


c_Pass,c_Defer,c_Fail,total=0,0,0,0         #number of credits at Pass,Defer,Fail the sum of all 3 creadits

def credit(name):                           #getting inputs all three credits
    while True:
        try:
            marks=int(input("Enter Your Credit at {}:".format(name)))
            if marks in(0,20,40,60,80,100,120):         #check the range
                return marks
            else:
                print("Range error\n")
        except:
            print("Intigers required\n")
        
print("------CHECK YOUR PROGRESSION OUTCOME-------\n")
while total!=120:                           #run until total of input become 120
    c_Pass=credit("Pass")
    c_Defer=credit("Defer")
    c_Fail=credit("Fail") 
   
    total=c_Pass+c_Defer+c_Fail
    if total==120:
        if c_Pass==120:                     #progress
            print("Your Progression outcome is 'PROGRESS'\n")
        elif c_Pass==100:                   #Progress-module trailer
            print("Your progression outcome is 'PROGRESS-MODULE TRAILER'\n")
        elif c_Pass<=40 and c_Fail>=80:     #excluded
            print("Your progression outcome is 'EXCLUDE'")
        else:                               #Do not progress-module trailer
            print("Your progression outcome is 'DO NOT PROGRESS-MODULE RETRIEVER'\n")
    else:
        print("Total incorrect. Please Enter valid marks!\n")
            


