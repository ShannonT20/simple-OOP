class Ecocash:
    def __init__(self,pin,trial,reEnter):
        #defining varibales
        self.pin=pin
        self.trial=trial
        self.reEnter=reEnter
    def econetcode(self,code):
        #econet code for ecocash
        self.code=input("Enter Ecocash code :")
        if self.code=="*151#":
            print()
        else:
            exit()
    def login(self):
        #try to check if you enter a number
        try:
            print("Welcome to Ecocash\n"
                   "Please enter pin to start ",end="")
            self.pin=eval(input(":"))
            #loop for trials 1,2 and 3
            while self.trial>0:  
                if self.pin==1234:
                    print("Login sucessful!")
                    break
                self.trial -=1
                if self.trial==2:
                   print(f"\tPlease re-enter pin you have |{(self.trial)}| attempts left")
                if self.pin!=1234 and self.trial<2:
                   self.reEnter=eval(input("Re-enter pin :"))
                   if self.reEnter!=1234:
                      print(f"\tPlease re-enter pin you have |{self.trial}| attempts left")
                   elif self.reEnter==1234:
                      print("Login sucessful!")
                      break
            #account blocked after 3 attemps
            else:
                print("***Your account has been blocked***")   
        except NameError:
            print("\nPlease Enter a number!")
            exit()
    def login_successful(self):
        #When successful it will print this
        if self.pin==1234 or self.reEnter==1234:
            print ("\n1.Send Money \n"
           "2.Recieve Money \n"
           "3.Update Ecocash Pin \n"
           "4.Balance Enquiry" )        
eco=Ecocash(1234,3,1234)
eco.econetcode("*151#")
eco.login()
eco.login_successful()

    
