class Logger:
  def log():
    print('--Start log--')
    for i in range (1,6):
      if i == 1:
        print('Primera llamada')
      else:
        print('{}ª llamada'.format(i))

      