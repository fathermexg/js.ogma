import email


com = ".com" 
dominio_ = {1:"@hotmail", 2:"gmail",3:"yahoo"}
dominio_2 = list(dominio_.values())


email_ = str (input())
if email_ == str(input()) + dominio_[1]+ com:
    print(email_ + dominio_[1]+com)