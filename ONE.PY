"""
  Correspondete:
  
  Como usar:
  
  Tenha a variável LANG devidamente configurada ex:
        export LANG=pt_BR
        
        Execução:
        
        python3 hello.py
        ou
        ./hello.py
        
"""
__version_ ="0.0.1"
__author__="Danilo Araujo"
__License__= "Unlicense"

import  os 


current_languagem="en_US"

msg = "Hello, Word!"

if current_languagem == "pt_BR":
  msg = "Olá, Mundo!"

elif current_languagem == "it_IT":
  
  msg = "Ciao, Mondo!"

print(msg)


Br= "Olá mundo !"
print(Br)