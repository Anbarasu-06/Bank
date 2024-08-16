from tqdm import tqdm
import time 


amount=""
Amount=""          
    

     



print("==================== E-TRANSECTION ========================")
print(" ")
print("=============== Create the Account ==============")
print(" ")
print("=========== ACCOUNT 1 =========")
Acc_Num_1 = int(input("Enter the Account Number: "))
Name_1 = str(input("Enter the Name: "))
Phone_1= int(input("Enter the Phone Number: "))
bal_1 = int(input("Enter the Balance: "))
print(" ")
print(" ")
print("=========== ACCOUNT 2 =========")
Acc_Num_2 = int(input("Enter the Account Number: "))
Name_2 = str(input("Enter the Name: "))
Phone_2 = int(input("Enter the Phone Number: "))
bal_2 = int(input("Enter the Balance: "))
print(" ")
data=list(range(101))
for item in tqdm(data):
 time.sleep(0.1)
print(" ")
print(" ")
print("Choose Your Account Press 1 or 2 : ")
choose = int(input("Enter The Number: "))
if (choose == 1):
     print("+++++++++++++++++ Your Account ++++++++++++")
     print(" ")
     print("Account Number  : ",Acc_Num_1)
     print("Name            : ",Name_1)
     print("Phone Nummber   : ",Phone_1)
     print("Account Balance : ",bal_1)
else:
    print(" ")
    print("+++++++++++++++++ Your Account ++++++++++++")
    print(" ")
    print("Account Number  : ",Acc_Num_2)
    print("Name            : ",Name_2)
    print("Phone Nummber   : ",Phone_2)
    print("Account Balance : ",bal_2)
    
    


    

    
        
 
print(" " )
print('''
       1. NEFT
       2. IMBS
       3. Fund Transfer
       4. GPAY
       5. To quit.....
       
       ''')
 
print(" ")



while True:
    
     ch=int(input("Enter your Choice: "))
     # +++++++++++++++++ NEFT ++++++++++++++++
     
     if (ch==1):
         print(" ")
         print("It is Free of Cost .....")
         print(" ")
         if (choose==1):
             while True:
                NEFT_Name = str(input("Enter the Name of Reciver: "))
                NEFT_PH =int(input("Enter the Phone Number of Reciver: "))
                if (NEFT_Name == Name_2 and  NEFT_PH == Phone_2):
                     Amount = int(input("Enter the Amount: "))
                     bal_1= bal_1-Amount
                     deb=Amount
                     bal_2= bal_2+Amount
                     cre=0
                     print("Your Account Balance : ",bal_1)
                     
                     break
                else:
                 print("Please Check the Details...")
         else:
              while True:
                NEFT_Name = str(input("Enter the Name of Reciver: "))
                NEFT_PH =int(input("Enter the Phone Number of Reciver: "))
                if (NEFT_Name == Name_1 and  NEFT_PH == Phone_1):
                     Amount = int(input("Enter the Amount: "))
                     bal_1= bal_1+Amount
                     deb=Amount
                     cre=0
               
                     
                     bal_2= bal_2-Amount
                     
                     print("Your Account Balance : ",bal_2)
                     
                     break
                else:
                 print("Please Check the Details...")
            
     #    ++++++++++++++++++++++++++++ IMBS +++++++++++++++++++++++++++++
     
     elif(ch==2):
         print(" ")
         print("It is has 6% Commission")
         print(" ")
         if (choose==1):
             while True:
                NEFT_Name = str(input("Enter the Name of Reciver: "))
                NEFT_PH =int(input("Enter the Phone Number of Reciver: "))
                if (NEFT_Name == Name_2 and  NEFT_PH == Phone_2):
                    Amount = int(input("Enter the Amount: "))
                    Amount = Amount * 6/100
                    Amount=Amount+Ext
                    bal_1= bal_1-Amount
                    IMB_deb=Amount
                    bal_2= bal_2+Amount
                    IMB_cre=0
                    print("Your Account Balance : ",bal_1)
                    
                    break
                else:
                 print("Please Check the Details...")
         else:
              while True:
                NEFT_Name = str(input("Enter the Name of Reciver: "))
                NEFT_PH =int(input("Enter the Phone Number of Reciver: "))
                if (NEFT_Name == Name_1 and  NEFT_PH == Phone_1):
                    Amount = int(input("Enter the Amount: "))
                    Ext= Amount * 6/100
                    Amount=Amount+Ext
                    bal_1= bal_1+Amount
                    IMB_deb=Amount
                    IMB_cre=0
                    bal_2= bal_2-Amount
                     
                    print("Your Account Balance : ",bal_2)
                  
                     
                    break
                else:
                 print("Please Check the Details...")
                 
     # +++++++++++++++++++ ++++++++ GPAY +++++++++++++++++++++
     
     elif(ch==4):
      if (choose==1):
             while True:
                Gpay_Name = str(input("Enter the Name of Reciver: "))
                Gpay_PH =int(input("Enter the Phone Number of Reciver: "))
                if (Gpay_Name  == Name_2 and   Gpay_PH == Phone_2):
                     Amount = int(input("Enter the Amount: "))
                     bal_1= bal_1-Amount
                     Gpay_deb=Amount
                     bal_2= bal_2+Amount
                     Gpay_cre=0
                     print("Your Account Balance : ",bal_1) 
                    
                     
                     break
                else:
                 print("Please Check the Details...")
      else:
              while True:
                Gpay_Name = str(input("Enter the Name of Reciver: "))
                Gpay_PH =int(input("Enter the Phone Number of Reciver: "))
                if (Gpay_Name  == Name_1 and   Gpay_PH == Phone_1):
                      Amount = int(input("Enter the Amount: "))
                      bal_1= bal_1+Amount
                      Gpay_deb=Amount
                      Gpay_cre=0
                      bal_2= bal_2-Amount
                      break
                else:
                 print("Please Check the Details...")
     
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
     # +++++++++++++++++++++++++++ FUND TRANSFER +++++++++++++++++++++ 
     
     elif(ch==3):
          print("Fund transfer history")
          if (choose==1):
               while True:
                    Fund_Name = str(input("Enter the Name of Your Account: "))
                    Fund_ph =int(input("Enter Your Phone Number: "))
                    if (Fund_Name == Name_1 and  Fund_ph == Phone_1):
                         print("--------- NEFT --------------")
                         print("Credit : ",cre)
                         print("Debit : ",deb)
                         print(" ")
                         print("----------- GPAY -------------")
                         print("Credit : ")
                         print("Debit : ")
                         
                         print(" ")
                         print("---------------- IMBS --------")
                         print("Credit : ")
                         print("Debit : ")
                              
                         break
                    else:
                         print("Please Check the Details...")
          else:
               while True:
                    Fund_Name = str(input("Enter the Name of Your Account:  "))
                    Fund_ph =int(input("Enter Your Phone Number:  "))
                    if (Fund_Name == Name_2 and Fund_ph == Phone_2):
                    
                         print("--------- NEFT --------------")
                         print("Credit : ",cre)
                         print("Debit : ",deb)
                         print(" ")
                         print("----------- GPAY -------------")
                         print("Credit : ", Gpay_cre)
                         print("Debit : ",Gpay_deb)
                         
                         print(" ")
                         print("---------------- IMBS --------")
                         print("Credit : ",IMB_cre)
                         print("Debit : ",IMB_deb)
                         break
                    else:
                         print("Please Check the Details...")
                         
                         
                         
     else:
          print("Thank for Your transcation.........")
          break
               
                    
               
          
          
          
              
           
