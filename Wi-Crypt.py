import os,sys,base64
from os import write
from tkinter import filedialog
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives.kdf.scrypt import Scrypt

print("**     **  *****           ******  ********   *    *  *****   *****")
print("**     **    *             *       *       *   *  *   *    *    *  ")
print("**  *  **    *             *       ********     **    *****     *  ")
print("** * * **    *             *       *     **     **    *         *  ")
print("**    ***  *****           ******  *       *    **    *         *  ")
print("******************************(V=1.0)******************************")

def Control():
    while(1):
        print("Enter Your Choice:\n")
        print("1.Symmetric(Key Based Encryption)\n2.Scrypt(Password Based Encryption)\n3.Exit") 
        choice=int(input())
        if(choice==1):
            Symmetric() 
        elif(choice==2):
            scrypt()
        elif(choice==3):
            sys.exit()
        else:
            print("Enter A Valid Choice!\n")
                 
 
def Symmetric():

 def Encryption():
     while(1):
         Path=filedialog.askopenfilename(title="Select The File To Be Encrypted")
         if(Path!=''):
            break
     path_Extn=os.path.splitext(Path)
     f_path_Extn=path_Extn[-1]
     f_type=Path.split(".")
     f_type=f_type[-1].capitalize()
     
     with open(Path,'rb') as File:
      Original_Data=File.read()

     Encrypted_Data=f.encrypt(Original_Data)

     while(1):
        Extension=filedialog.asksaveasfilename(title="Enter A Name To Save The Encrypted File",defaultextension=f_path_Extn,filetypes=[(f_type,f_path_Extn)])
        if(Extension!=''):
            break
     with open(Extension,'wb') as File1:
        File1.write(Encrypted_Data)
          
   

 def Decryption():
    while(1):
        Path1=filedialog.askopenfilename(title="Select The Key File")
        if(Path1!=''):
            break
    
    with open(Path1,'rb') as File2:
        Key_file=File2.read()

    g=Fernet(Key_file)
    while(1):
        Path2=filedialog.askopenfilename(title="Select The Encrypted File")
        if(Path2!=''):
            break
    extn=os.path.splitext(Path2)
    extn=extn[-1]
    f_type=Path2.split(".")
    f_type=f_type[-1].capitalize()
    

    with open(Path2,'rb') as File3: 
        Enc_File=File3.read()

    Decrypted_Data=g.decrypt(Enc_File)
    while(1):
        Extension1=filedialog.asksaveasfilename(title="Enter A Name To Save The Decrypted File",defaultextension=extn,filetypes=[(f_type,extn)])
        if(Extension1!=''):
            break

    with open(Extension1,'wb') as File4:
        File4.write(Decrypted_Data)
   
    



 while(1):
   print("Enter Your Choice:\n")
   print("1.Encryption\n2.Decryption\n3.Exit") 
   choice=int(input())
   if(choice==1):
      key=Fernet.generate_key()
      f=Fernet(key)
      Save_Key=filedialog.asksaveasfilename(title="Enter A Name & Save The Key Safely",defaultextension='.txt',filetypes=[("Text File",'.txt')])
      with open(Save_Key,'wb') as Key:      
        Key.write(key)
      Encryption() 
   elif(choice==2):
    Decryption()
   elif(choice==3):
    Control()
   else:
       print("Enter A Valid Choice!\n")
        

def scrypt():
 def Encryption():
    Password=input("Enter Your Password To Encrypt\n")
    Encoded_Password=Password.encode()

    salt = b'\x08\xcfTfw\xd2\x85\x12\xa5D\xa9\xd3:\x86\xda\xa1'

    # derive
    kdf = Scrypt(salt=salt,length=32,n=2**14,r=8,p=1,)
    key = kdf.derive(Encoded_Password)
    key = base64.urlsafe_b64encode(key)
    f=Fernet(key)
    
    while(1):
        Path=filedialog.askopenfilename(title="Select The File To Be Encrypted")
        if(Path!=''):
            break
    f_extn=os.path.splitext(Path)
    f_extn=f_extn[-1]
    f_type=Path.split(".")
    f_type=f_type[-1].capitalize()

    with open(Path,'rb') as File:
        Original_Data=File.read()

    Encrypted_Data=f.encrypt(Original_Data)
    while(1):
        Extension=filedialog.asksaveasfilename(title="Enter A Name To Save The Encrypted File",defaultextension=f_extn,filetypes=[(f_type,f_extn)])
        if(Extension!=''):
            break
     
    with open(Extension,'wb') as File1:
        File1.write(Encrypted_Data)

    
    
    

 def Decryption():
   
    Password=input("Enter Your Password To Decrypt\n")
    Encoded_Password=Password.encode()

    salt = b'\x08\xcfTfw\xd2\x85\x12\xa5D\xa9\xd3:\x86\xda\xa1'

    # derive
    kdf = Scrypt(salt=salt,length=32,n=2**14,r=8,p=1,)
    key1 = kdf.derive(Encoded_Password)
    key1 = base64.urlsafe_b64encode(key1)
    
    g=Fernet(key1)


    while(1):
        Path2=filedialog.askopenfilename(title="Select The Encrypted File") 
        if(Path2!=''):
            break
    f_extn=os.path.splitext(Path2)
    f_extn=f_extn[-1]
    f_type=Path2.split(".")
    f_type=f_type[-1].capitalize()

    with open(Path2,'rb') as File3: 
        Enc_File=File3.read()

    Decrypted_Data=g.decrypt(Enc_File)
    while(1):
        Extension1=filedialog.asksaveasfilename(title="Enter A Name To Save The Decrypted File",defaultextension=f_extn,filetypes=[(f_type,f_extn)])
        if(Extension1!=''):
            break

    with open(Extension1,'wb') as File4:
        File4.write(Decrypted_Data)
   
    

 while(1):     

    print("Enter Your Choice:\n")
    print("1.Encryption\n2.Decryption\n3.Exit")
    choice=int(input()) 

    if(choice==1):
     Encryption() 

    elif(choice==2):
     Decryption()
    
    elif(choice==3):
       Control()
    else:
       print("Enter A Valid Choice!\n")
           

Control()