class palindromo():
  def __init__(self,palabra):
    self.palabra=palabra
  def verificacion(self):
    palabra = input('Introduzca la palabra que desea verificar si es palindroma')
    if palabra == ''.join(reversed(palabra)):
      print('True')
    else:
      print('False')
    
    