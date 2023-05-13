def is_admin():
    pass
def is_warekeeper():
    pass





class User():
    def __init__ (self, email:str, password:str, role:str , personalcode:int):
        # username(email) password pesonalNumber
        # role -> list {admin , anbar , sandoq}
        self.email = email
        self.password = password
        self.role = role
        self.personalcode = personalcode
    def has_permission():
        # querying throw db to find user role
        pass
    def create_user(self,*args, **kwargs):
        pass
    def delete_user(self, *args, **kwargs):
        pass
    
    def login(self, username, password):
        pass
    
    def change_pass(self, username, password, newpassword):
        pass
        

class Goods():
    def __init__(self) :
        # name, price, amount, 
        pass
    def add(self, *args, **kwargs):
        pass
    def change(self, *args, **kwargs):
        pass
    def remove(self , *args, **kwargs):
        pass
class Factor(Goods):
    def __init__(self):
        
        super().__init__()
    pass
    def show_inp(self,*args, **kwargs):
        
        pass
    def show_out(self, *args, **kwargs):
        pass
    
    def add_input():
        pass
    def add_output():
        pass