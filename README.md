<h1 align="center">	Ejercicios por parejas</h1>

<h2>Repositorio:</h2>

Este es el link del [repositorio](https://github.com/albabernal03/ejercicios_parejas_POO)

***
<h2>¿De qué trata esta tarea?</h2>


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

***

## Ejercicio 4:


***
