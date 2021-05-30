credit=[[120,0,0],
        [100,20,0],
        [100,0,20],
        [80,40,0],
        [80,20,20],
        [80,0,40],
        [60,60,0],
        [60,40,20],
        [60,20,40],
        [60,0,60]]
print("|-------------------------------|")
print("|Volume of credit at each level |")
print("|-------------------------------|\n")
for i in range(len(credit)):
    if credit[i][0]==120:
        print("Credits at pass is",credit[i][0])
        print("Credits at Defer is",credit[i][1])
        print("Credits at fail is",credit[i][2])
        print("Progression outcome is PROGRSS\n")
    elif credit[i][0]==100:
        print("Credits at pass is",credit[i][0])
        print("Credits at Defer is",credit[i][1])
        print("Credits at fail is",credit[i][2])
        print("Progression outcome is PROGRSS-MODULE TRAILER\n")
    else:
        print("Credits at pass is",credit[i][0])
        print("Credits at Defer is",credit[i][1])
        print("Credits at fail is",credit[i][2])
        print("Progression outcome is DO NOT PROGRESS-MODULE RETRIEVER\n")
        
   

     
