# write a script to take stud
import pickle
import random
d = {}
def create():
                r=random.randint(0,999)
                print("\t\t\t\t\t\t\t\t\t\t\t........[  ",r," ]........")
                R=int(input('\n\tEnter the verication code generated above to continue updation :'))
                if R==r:
                	ch = "y"
                	count = int(input("\n\tHow many records u wanna enter : "))
                	for i in range(count):
                	    print("\n\t**********  Student Information ************** ")
	                    roll = int(input("\tRollno:\t"))
	                    d[roll]={}
	                    name = input("\tName:\t")
	                    d[roll]["name"]=name
	                    per  = float(input("\tPercentage:\t"))
	                    d[roll]["percentage"]=per
	                    print('\n\t',d)
	                    pickle.dump(d , f)
                    
def add():
                    r=random.randint(0,999)
                    print("\t\t\t\t\t\t\t\t\t\t\t........[  ",r," ]........")
                    R=int(input('\n\tEnter the verication code generated above to continue updation :'))
                    if R==r:
                    			print("\n\t**********  Student Information ************** ")
                    			roll = int(input("\tRollno:\t"))
                    			d[roll]={}
                    			name = input("\tName:\t")
                    			d[roll]["name"]=name
                    			per  = float(input("\tPercentage:\t"))
                    			d[roll]["percentage"]=per
                    			print('\n\t',d)
                    			pickle.dump(d , f)
                    
def search():
                r=random.randint(0,999)
                print("\t\t\t\t\t\t\t\t\t\t\t........[  ",r," ]........")
                R=int(input('\n\tEnter the verication code generated above to continue updation :'))
                if R==r:
                 roll = int(input("\n\tEnter Rollnumber:  "))  # [[111 , 'a' , 33] , [123 , 'b' , 44]   ]
                 flag = 0
                 for i in d:
                             if i==roll:
                             	print("\trollno: " , i)
                             	print("\tName:   " , d[i]["name"])
                             	print("\tPer:    " , d[i]["percentage"])
                             	print()
                             	flag=1
                             	
                 if flag==0:
                     print("\n\tRecord not found  \n")
                    
def update():
                r=random.randint(0,999)
                print("\t\t\t\t\t\t\t\t\t\t\t........[  ",r," ]........")
                R=int(input('\n\tEnter the verication code generated above to continue updation :'))
                if R==r:
                    print(d,'\n')
                    roll = int(input("\n\tEnter Roll number to update :  "))  
                    print("\n\t************ Details are here ************** ")
                    flag = 0
                    for i in d:
                        print(i)
                        if i==roll:
                            flag = 1
                            print("\trollno: " , i)
                            print("\tName:   " , d[i]["name"])
                            print("\tPer:    " , d[i]["percentage"])
                            print()
                            r=random.randint(0,999)
                            print("\t\t\t\t\t\t\t\t\t\t\t........[  ",r," ]........")
                            R=int(input('\n\tEnter the verication code generated above to continue updation :'))
                            if R==r:
                                print("\n\t1. Name  2. Percentage: ")
                                c = int(input("\n\tEnter the choice:  "))
                                if c==1:
                                    if i==roll:
                                        print("\trollno: " , i)
                                        print("\tName:   " , d[i]["name"])
                                        print("\tPer:    " , d[i]["percentage"])
                                        print()                           
                                        nam = input("\tEnter the Name :  ")
                                        # updation process is started
                                        d[i]['name']=nam
                                        print("\trollno: " , i)
                                        print("\tName:   " , d[i]["name"])
                                        print("\tPer:    " , d[i]["percentage"])
                                        print("\n\t****record is updated*******")
                                        print()
                                        pickle.dump(d,f)
                                        break
                                    
                                elif c==2:
                                    p = float(input("\tEnter the percentage :  ")) # updation process is started
                                    d[i]['percentage']=p
                                    print("\trollno: " , i)
                                    print("\tName:   " , d[i]["name"])
                                    print("\tPer:    " , d[i]["percentage"])
                                    print("\n\t****record is updated*******")
                                    print()
                                    pickle.dump(d,f)
                                    break                               
                                    
                                else:
                                    print("\n\tNot found the option:  ")
                            
                    if flag ==0:
                        print('Roll not found in the data')
def delete():
                r=random.randint(0,999)
                print("\t\t\t\t\t\t\t\t\t\t\t........[  ",r," ]........")
                R=int(input('\n\tEnter the verication code generated above to continue updation :'))
                if R==r:
                    flag =0
                    roll = int(input("\n\tEnter Rollnumber for deletion :  "))  # [[111 , 'a' , 33] , [123 , 'b' , 44]   ]
                    for i in d:
                        if i==roll:
                            flag=1
                            print("\trollno: " , i)
                            print("\tName:   " , d[i]["name"])
                            print("\tPer:    " , d[i]["percentage"])
                            m = 'y'
                            m = input("\n\tPress 'y' to delete or 'n' not to delete:  ")
                            if m=='y':
                                del d[roll]
                                print("\tRecord has been deleted:  ")
                                print("\t",d)
                                pickle.dump(d,f)
                    if flag == 0:
                        print('\n\tentered roll no. doesnt exist in the data')
                    
def display():
                print("\n\tChoose the option:  1. Display all    2.  Display individual:  ")
                n = int(input("\n\tEnter the choice:  "))
                if n == 1:
                    for i in d:
                            print("\trollno: " , i)
                            print("\tName:   " , d[i]["name"])
                            print("\tPer:    " , d[i]["percentage"])
                            print()
                else:
                    flag=0
                    roll = int(input("\n\tEnter Rollnumber:  "))
                    for i in d:
                        if i==roll:
                            flag=1
                            print("\trollno: " , i)
                            print("\tName:   " , d[i]["name"])
                            print("\tPer:    " , d[i]["percentage"])
                            print()
                    if flag==0:
                        print("entered roll no. doesnt exist in the data")
                        
                            
                        
with open ("binary.dat","wb")as f:
    while True:
        print("\tList operations Menus ->  ")
        print("\t1. Create records :")
        print("\t2. Add records    :  ")
        print("\t3. Search records :  ")
        print("\t4. Update records :  ")
        print("\t5. Delete records :  ")
        print("\t6. Display records(individual / All):  ")
        n = input("\n\tEnter the choice or n to quit:  ")
        
        if n=='1':        
            create()
                
        elif n=='2':        
            ch = 'y'
            while ch=='y':    
                add()
                ch = input("\n\tWana add more..... 'y' / 'n' : ")
                        
        elif n=='3':
            search()        
          #  ch = input("Wana add more..... 'y' / 'n' : ")  
        elif n=='4':
            b='y'
            while b=='y':        
                update()    
                b = input("\n\tWant to do more updation:  'y'  /  'n'  ")
                if b == "n":
                    break        
        #ch = input("press 'y or  'n':   ")                   
        elif n=='5':
            ch = 'y'
            while ch=='y':    
                delete()
                ch = input("\n\tWant to delete more..... 'y' / 'n' : ")
            
        
        elif n=='6':
            display()
        else:
            print("\n\tCONTENTS HAS BEEN SAVED")
            break