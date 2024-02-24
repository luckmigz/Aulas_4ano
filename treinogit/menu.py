
options = int(input("Escolha a operação : \n ---> 1 Soma \n ---> 2 Subitração \n ---> 3 Multiplicação \n ---> 4 Divisão \n ---> Sair \n"))
def menu(options):
    n1 = int(input("digite o 1 numero: "))
    n2 = int(input("digite o 2 numero: "))
    if options == 1:
         somar(n1, n2);
    elif options == 2:
         sub(n1, n2);
    elif options == 3:
         mult(n1, n2);
    elif options == 4:
         div(n1, n2);
    else:
        print("Saindo")
        exit();
        
def somar(n1,n2):
    print(n1+n2);

def sub(n1,n2):
    print(n1-n2);

def mult(n1,n2):
    print(n1*n2);

def div(n1,n2):
    print(n1/n2);

menu(options);
    