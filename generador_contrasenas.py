"""
Proyecto en Python
Generador de contraseñas y encriptacion de mensajes
Crea contraseñas de manera aleatoria, cifra cadenas de texto
y guardar lo anterior nombrado en listas, el usuario puede
acceder a esta informacion
"""

#bibliotecas
import random

"""
===============Funciones de opciones del menu=================================
"""

def password_generator(num_passwords,conjunto,longitud):
    """
    recibe: num_passwords, conjunto y longitud
    genera multiples strings determinados por el usuario por medio de un 
    ciclo for y lo manda a imprimir por la variable new_password
    """
    for i in range(num_passwords):
        generar = random.sample(conjunto, longitud)
        new_password = ''.join(generar)
        print (new_password)
        
def save_password(usuario,password,saved_passwords):
    """
    recibe: usuario, password y la lista saved_passwords
    agrega una lista anidada a la lista de saved_passwords guardando 
    el usuario y la contraseña
    """
    saved_passwords.append([])
    saved_passwords[-1].append(usuario)
    saved_passwords[-1].append(password)    

def encriptar():
    encriptada=''
    for letra in mensajeEncriptado: 
        if letra in 'aeiouáéíóú':
            encriptada = encriptada + 'x'
        else :
            encriptada = encriptada + letra
    return encriptada
 
def save_messages(mensaje):
    return

def desencriptar(): 
    return
    
#Se definen las variables con caracteres que llevara una contraseña
MINUSCULAS='abcdefghijklmnñopqrstuvwxyz'
MAYUSCULAS=MINUSCULAS.upper()
NUMEROS='1234567890'
CARACTERES_ESPECIALES='!@#$%^&*()_-{[}]/<>'

#variables para generar la contraseña
generar= None
password=None

conjunto=MINUSCULAS+NUMEROS

contraseñasGuardadas=[]
        
opcion=input('Si deseas generar una o varias contraseñas selecciona 1 \n'
            'Si deseas guardar tu contraseña generada selecciona 2\n'
            'Si deseas recuperar las contrañas guardadas selecciona 3\n:')
while opcion!='0' or opcion<'4' or opcion == 'no':
    if opcion=='1':
        tamano=int(input('¿Cuantos caracteres quieres que tenga tu contraseña?: '))
        pedir_ma= input('¿Quieres que tu contraseña contenga mayusculas?: ')
        if pedir_ma=='si' or pedir_ma=='Si':
             conjunto=conjunto+MAYUSCULAS
        pedir_ce= input('¿Quieres que tu contraseña contenga caracteres especiales?: ')
        if pedir_ce=='si' or pedir_ce=='Si':
             conjunto=conjunto+CARACTERES_ESPECIALES
        rango=int(input('Cuantas contraseñas deseas generar? :'))
        generarPasswords(rango,generar,conjunto,tamano,password)
        opcion=input('¿Deseas elegir otra opcion?: ')
    elif opcion=='2':
        usuario=input('Usuario,correo electronico o cuenta: ')
        contraseña=input('Contraseña: ')
        save_password(saved_passwords,usuario,contraseña)
        opcion=input('¿Deseas elegir otra opcion?: ')
    elif opcion=='3':
        print(contraseñasGuardadas)
        opcion=input('¿Deseas elegir otra opcion?: ')
    elif opcion=='no' or 'No':  
        break
else:
    print('Opcion invalida')
