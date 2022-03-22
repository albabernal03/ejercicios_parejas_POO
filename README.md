<h1 align="center">	Ejercicios por parejas</h1>

<h2>Repositorio:</h2>

Este es el link del [repositorio](https://github.com/albabernal03/ejercicios_parejas_POO)

***
<h2>¿De qué trata esta tarea?</h2>
La tarea consiste en elaborar el código y UML de cada uno de los ejercicios.

***
## Integrantes

1. [Alba](https://github.com/albabernal03) 
2. [Carmen](https://github.com/carmenm02)



***
## Indice

1. [Ejercicio 1](#id1)
2. [Ejercicio 2](#id2)
3. [Ejercico 3](#id3)
4. [Ejercicio 4](#id4)

***

## Ejercicio 1:

**Código:**
```
class palindromo():
  def __init__(self,palabra):
    self.palabra=palabra
    
  def verificacion(self):
    palabra = input('Introduzca la palabra que desea verificar si es palindroma')
    if palabra == ''.join(reversed(palabra)):
      print('True')
    else:
      print('False')
      
print(palindromo.verificacion('palabra'))
```

**UML:**

<img width="246" alt="palindromo" src="https://user-images.githubusercontent.com/91721886/159340627-0a7b8f68-c782-4e7a-905d-acfadaaac8a8.png">



***

## Ejercicio 2:

**Código:**

```
class palindromo_2():
  def __init__(self,palabra):
    self.palabra=palabra
    
  def verificacion(self):
    palabra = input('Introduzca la palabra que desea verificar si es palindroma')
    print(palabra.upper())
    if palabra == ''.join(reversed(palabra)):
      print('True')
    else:
      print('False')
      
print(palindromo_2.verificacion('palabra'))
```
**UML:**

<img width="207" alt="palindromo 2" src="https://user-images.githubusercontent.com/91721886/159341861-28562644-bf18-4fcb-a79e-5ad753471151.png">


***

## Ejercicio 3:

**Código:**

```
class A: 
    def z(self): 
        return self 
 
    def y(self, t): 
        return len(t) 
 
a = A 
y = a.z 
print(y(a)) 
aa = a() 
print(aa is a()) 
z = aa.y 
print(z(())) 
print(a().y((a,))) 
print(A.y(aa, (a,z))) 
print(aa.y((z,1,'z'))) 

#El resultado obtenido es el siguiente:
#False
#0
#1
#2
#3
```

**UML:**

<img width="243" alt="puzzle" src="https://user-images.githubusercontent.com/91721886/159344658-ba068d62-04b8-4e65-a7ec-303d6a9b83c4.png">


***

## Ejercicio 4:

**Código:**
```
class Logger:
  def log():
    print('--Start log--')
    for i in range (1,6):
      if i == 1:
        print('Primera llamada')
      else:
        print('{}ª llamada'.format(i))
    print('--End log--:', '{}'.format(i), 'log(s)')
print(Logger.log())
```
**UML:**
***
