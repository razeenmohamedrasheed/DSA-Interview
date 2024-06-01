from datetime import datetime

class User:
    # Get the current date and time
    current_datetime = datetime.now()
    # Access the year attribute to get the current year
    current_year = current_datetime.year
    all_data = []
    def __init__(self,name:str,email:str,birthyear:int):
        # Assert is used to check the validation
        assert birthyear>=1000 
        self.name = name
        self.email = email
        self.birthyear = birthyear


        User.all_data.append(self)
    
    def UserData(self):
        word = f"Name : {self.name} email :{self.email}"
        return word
    
    def userAge(self):
        age = User.current_year - self.birthyear 
        return age
    
    def __repr__(self):
        return f"(Name : {self.name} email :{self.email})"
        


User1 = User("razeen","razeenrasheed83@gmail.com",1999)
User2 = User("gopika","gopikasudhakar@gmail.com",1999)
User3 = User("govind","govindnair@gmail.com",1997)
User4 = User("sooarj","soorajsree@gmail.com",2000)


print(User.all_data)

for instance in User.all_data:
    print(instance.name)

