###### Python program to print 
# colored text and background 
import os
import time
import sys 
import simpleaudio as sa
import pandas as tl 
import csv
import sklearn
df = tl.read_csv('desktop/Bike1.csv') 
from termcolor import colored, cprint 

def Bike():      #by vinay
        
    text = colored(':::::::::::: BIKE GARAGE ::::::::::', 'green', attrs=['reverse', 'blink']) 

        
    def Budget():   #budget function
     
                   
                    cprint(" Attention You Are Entering a Case Sensitive Area !", 'red', attrs=['bold'], file=sys.stderr)
                    print("-------------------------------------------------------------------------------------------------------")
                    print("Enter The Value Of Your Budget : \n")
                    
                    miin = input("Enter min value : ex : 50 k , 1.2 lakh =>")

                    maax = input("Enter max value : ex : 90 k , 14 lakh =>")

                    
                    data = tl.read_csv("desktop/bike1.csv", index_col ="Price")         
                    rows = data.loc[miin:maax] 
                    
                    print("\n\nxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
                    
                    from tqdm.auto import tqdm
                    #import tqdm  # or whatever tqdm imports you use
                    import colorama
                    colorama.deinit()
                    colorama.init(strip=False)
                    for i in tqdm(range(50000)):
                        print(" ", end='\r') 

                    time.sleep(1)
                    
                    print("::::::::: THE FOLLOWING BIKES ARE GOOD FOR YOU ::::::::::::: :")
                            # checking data type of rows 
                            #print(type(rows)) 
                    print(rows)     
                    print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx   FINISHED xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
                    print("\nxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx \n\n\n")
                    time.sleep(2)
                    
    def Vname():  #vehicle type function
        
                cprint(" Attention You Are Entering a Case Sensitive Area !", 'red', attrs=['bold'], file=sys.stderr)
                print("\n\n -------------------------------------------------------------------------------------------------")


                print("\n Enter The Vehicle name from the list: \n")

                print("Name : Honda HF , Honda , Hero Splendor Plus, Honda Activa , Honda ,TVS , Honda CB , Yamaha FZ , Bajaj , Revolt  , Yamaha YZF , Bajaj Pulsar , Royal Enfield , KTM Duke , 2006 Big Dog , Suzuki Hayabusa , 2017 Fonzarelli Fz , 2017 KTM 50 SX , Kawasaki Ninja , 2012 Choper Custom ")
                print("\n\n -------------------------------------------------------------------------------------------------")


                name =input("\n \n Enter vehicle name from above list :")

                data = tl.read_csv("desktop/bike1.csv", index_col ="Name") 
                rows = data.loc[name] 

                # checking data type of rows 
                print("\n\nxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
                from tqdm.auto import tqdm
                #import tqdm  # or whatever tqdm imports you use
                import colorama
                colorama.deinit()
                colorama.init(strip=False)
                for i in tqdm(range(50000)):
                        print(" ", end='\r')
                time.sleep(1)
                
                print("::::::::::: THE FOLLOWING BIKES ARE GOOD FOR YOU :::::::::::: \n \n ")
                print(rows)
                print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx   FINISHED xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
                print("\nxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx \n\n\n")
                time.sleep(2)
   
    def sf():   #special feature function
        
        cprint(" Attention You Are Entering a Case Sensitive Area !", 'red', attrs=['bold'], file=sys.stderr)
        print("\n\n -------------------------------------------------------------------------------------------------")
        
        
        print("\n Enter The FEATURE : ex : cheap , drum brakes , ABS , 5 or 6 gear , gear box , economical , speed , high milege\n")


        
        print("\n\n -------------------------------------------------------------------------------------------------")
        

        name =input("\n \n Enter vehicle name from list :")
        
        data = tl.read_csv("desktop/bike1.csv", index_col ="Keyword") 
        rows = data.loc[name] 

        # checking data type of rows 
        print("\n\nxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
        from tqdm.auto import tqdm
        #import tqdm  # or whatever tqdm imports you use
        import colorama
        colorama.deinit()
        colorama.init(strip=False)
        for i in tqdm(range(50000)):
                        print(" ", end='\r') 
        time.sleep(1)
        
        
        print("::::::::::::: THE FOLLOWING BIKES ARE GOOD FOR YOU :::::::::::::: \n \n")
        print(rows)
        print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx   FINISHED xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
        print("\nxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx \n\n\n")
        time.sleep(2)
        
    def Biket():    #bike type function 
        
        
        cprint(" Attention You Are Entering a Case Sensitive Area !", 'red', attrs=['bold'], file=sys.stderr)
        print("\n\n -------------------------------------------------------------------------------------------------")
        
        
        print("\n Enter The Vehicle Type : ex : Cruiser , Sports ,Dual Sport , Electric scooter , Fun \n")
        
        print("\n\n -------------------------------------------------------------------------------------------------")
        

        name =input("\n \n Enter vehicle name from above list :")
        
        data = tl.read_csv("desktop/bike1.csv", index_col ="Body type") 
        rows = data.loc[name] 

        # checking data type of rows 
        print("\n\nxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
        from tqdm.auto import tqdm
        #import tqdm  # or whatever tqdm imports you use
        import colorama
        colorama.deinit()
        colorama.init(strip=False)
        for i in tqdm(range(50000)):
                        print(" ", end='\r') 
        time.sleep(1)
        
        
        print("::::::::::::: THE FOLLOWING BIKES ARE GOOD FOR YOU \n \n ::::::::::::::")
        print(rows)
        print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx   FINISHED xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
        print("\nxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx \n\n\n")
        time.sleep(2)  

        
    cprint(' !!!!! RECOMMEND BIKE ON BASIS OF !!!!', 'red', 'on_white') 
   
    while(True):   #by vinay main of bike function
            
            print(bold_start,"1. Budget \n"  )
            print("2. Vehicle Name \n" )
            print("3. Bike Type \n" )
            print("4. Any Special Feature \n")
            print("5. Bikes List \n")
            text = colored('6. EXIT (bike garage) !', 'red', attrs=['reverse', 'blink']) 
            print(text) 
            time.sleep(1)
            l =int(input("Enter your choice (in bike garage)=> "));
            
            if(l==1):
                    Budget()
                    continue;


            elif(l==2):
                    Vname()
                    continue;
            elif(l==3):
                    Biket()
                    continue;

            elif(l==4):
                    sf()
                    continue;
            elif(l==5):
                import pandas as jk 
                df = jk.read_csv('desktop/Bike1.csv') 
                print(jk)
                continue;
            elif(l==6): 
                        break;
            else:
                print("WRONG CHOICE !!!! ");
                print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
                print("\nxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx \n\n\n")
           
                continue;
            print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
            print("\nxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx \n\n\n")
           

def Car():    #by shubhi
        import pandas as pd 
        import warnings
        import string as str
        from sklearn.neighbors import NearestNeighbors
        warnings.filterwarnings('ignore')

        def key_word():
            filename="desktop/car.csv"
            fields=[]
            rows=[]
            with open(filename, 'r') as csvfile: 
                freader = csv.reader(csvfile)
                fields = next(freader)

                for row in freader: 
                    rows.append(row)

            print("\nEnter any keyword(specification) from the options: ") 
            print("High milege , durable, economical, cheap, low maintainence, Less pollution, low fuel consumption")
            keyword=input()
            print("\n")
            j=1
            for row in rows:
                for field in row:
                    count=field
                    p=count.find(keyword)
                    if(p>-1) :
                        j=j+1
                        for s in row:
                            print(s)
                        print('\n')
            if(j==1):
                print("\nWrong choice,Try again\n")
                key_word()

        def price_labeled():
            filename="desktop/car.csv"
            fields=[]
            rows=[]
            with open(filename, 'r') as csvfile: 
                freader = csv.reader(csvfile) 
                fields = next(freader)

                for row in freader:
                    rows.append(row)

            car = pd.read_csv('desktop/car.csv',index_col = 'Price (in lakh)')
            car = car.sort_index()
            r = car.loc[6:67]
            print(type(r))
            print(r)

        def choice():
                x=int(input())
                if(x==1):
                    price_labeled()
                elif(x==2):
                    key_word()
                else:
                    print("Try again\n")
                    choice(); 

        def fun():
            y=int(input())
            if(y==1):
                col_list = ["Name","Suited for","Age group","Body type","Fuel type","Price(in lakh)","Keywords"]
                car = pd.read_csv('desktop/ai.csv',index_col = 'Type of vehicle')
                r = car.loc["Car"]
                print(type(r))
                r
            elif(y==2):
                print("You can get recommendations on the basis of following fields:\n")
                print("1->Labeling price\n2->Keywords\n")
                choice()
            else:
                print("Try again\n")
                fun(); 

        def abc():
            print("The division of CARS\n")
            print("--------------------------------------------------------------")
            print("You can see all options available or options based on your choice:\n")
            print("1->All options\n2->Choice based\n")
            fun()
        abc()

    
    
import csv    #by gurnoor
import string as st
        
def publict():
    filename="desktop/ai.csv"
    feids=[]
    rows=[]
    with open(filename, 'r') as csvfile: 
    # creating a csv reader object 
        csvreader = csv.reader(csvfile) 
 # extracting field names through first row 
        fields = next(csvreader) 
  
    # extracting each data row one by one 
        for row in csvreader: 
            rows.append(row) 
  

    print("\nWhich type of public transport are u looking for?\nEnter a keyword to help us find it for you:\n")
    keyword=input()
    print("\n\n")
    i=1
    for row in rows:
        for field in row:
            temp=field
            n=temp.find(keyword)
            if(n>-1) :
                i=i+1
                for x in row:
                    print(x)
                print('\n')
    if(i==1):
        print("\nTry to search with another keyword\n")
        publict()

        
        
    
text = colored(':::::::::::: VEHICLE RECOMENDADTION SYSTEM ::::::::::', 'green', attrs=['reverse', 'blink']) 

bold_start = '\033[1m'
bold_end   = '\033[0m'


print(bold_start, text)


cprint("WELCOME!", 'green', attrs=['bold','underline'], file=sys.stderr) 

n=input(" Enter Your Name :")

print("\n HELLO " +bold_start, n , bold_end )

print("\n\n")


import csv   # by mayank
import string as st
        
def truck():
    filename="desktop/truckai.csv"
    feids=[]
    rows=[]
    with open(filename, 'r') as csvfile: 
    # creating a csv reader object 
        csvreader = csv.reader(csvfile) 
 # extracting field names through first row 
        fields = next(csvreader) 
  
    # extracting each data row one by one 
        for row in csvreader: 
            rows.append(row) 
  
# printing the field names 
    print('Field names are:\n' + ', '.join(field for field in fields))
    print("\nWhich type of truck are u looking for?\nEnter a keyword to find trucks which suits you\n")
    keyword=input()
    print("\n\n")
    i=1
    for row in rows:
        for field in row:
            temp=field
            n=temp.find(keyword)
            if(n>-1) :
                i=i+1
                for x in row:
                    print(x)
                print('\n')
    if(i==1):
        print("\nTry to search with another keyword\n")
        truck()
        

def loader():
    filename="desktop/loaderai.csv"
    feids=[]
    rows=[]
    with open(filename, 'r') as csvfile: 
    # creating a csv reader object 
        csvreader = csv.reader(csvfile) 
 # extracting field names through first row 
        fields = next(csvreader) 
  
    # extracting each data row one by one 
        for row in csvreader: 
            rows.append(row) 
  
# printing the field names 
    print('Field names are:\n' + ', '.join(field for field in fields)) 
    print("\nWhich type of loader are u looking for?\nEnter a keyword to find loader which suits you\n")
    keyword=input()
    print("\n\n")
    
    i=1
    for row in rows:
        for field in row:
            temp=field
            n=temp.find(keyword)
            if (n>-1):
                i=i+1
                for x in row:
                    print(x)
                print('\n')
    if(i==1):
        print("\nTry to search with another keyword")
        loader()

def main():
    print("Welcome to section of  vehicles used to carry loads\n")
    print("Enter value:")
    print("1=> Trucks\n2=> Loaders\n")
    def entry():
        value=int(input())
        
        if(value==1):
            truck()
        elif(value==2):
            loader()
        else:
            print("Enter correct value\n")
            entry();
    entry()
    
    
    
    
    
# (by vinay) main  of the program 


while(True):
        print("---------------------------------------------------------------------------------------------------------------\n\n\n")
        print("---------------------------------------------------------------------------------------------------------------\n\n\n")
       
        print("WHAT IS YOUR PLAN TO BUY : \n\n")
        cprint(' !!!!! PRIVATE Transport !!!!', 'red', 'on_white') 

        print(bold_start,"1. BIKE \n" )
        print("2. CAR \n" , bold_end )


        cprint(' !!!!! PUBLIC Transport !!!!', 'red', 'on_white') 

        print(bold_start,"3. Loader 4 Wheeler \n" )
        print("4. Public Transport (4 wheeler, 3 wheeler) \n");

        text = colored('5. EXIT (source) !', 'red', attrs=['reverse', 'blink']) 
        print(text) 
        
        c =int(input("Enter your choice (source)=> \n\n\n"));
        if(c==1):
                
                cprint(' !!!!! Igniting !!!!!', 'red', 'on_white');
                time.sleep(1);
                filename = 'desktop/test1.wav'
                wave_obj = sa.WaveObject.from_wave_file(filename)
                play_obj = wave_obj.play()
                play_obj.wait_done() 
                print("-------------------------------------------------------------------------------------------------------");
                cprint("WELCOME To The BIKE Section !!!! ", 'green', attrs=['bold','underline'], file=sys.stderr) 
                Bike()
                continue;

        elif(c==2):
            Car()
            continue;
        elif(c==3):
            main()
            continue;

        elif(c==4):
                publict()
                continue;
        
        elif(c==5):
                
                print("\n HAVE A GOOD DAY " +bold_start, n , bold_end )
                break;
            
        else:
            print("WRONG CHOICE !!!! ");
            continue;


