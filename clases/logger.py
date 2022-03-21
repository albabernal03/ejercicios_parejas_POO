class Logger:
    def __init__(self):
        self.log_file = open("log.txt", "w")
        # Initialización del contador de logs
        self.log_count = 0
        # Escritura de la primera línea
        self.log_file.write("--Inicio del log--\n")


    def __del__(self):
        # Destrucción de la instancia: escribimos la última línea del archivo
        self.log_file.write("--Fin del log: {} log(s)--\n".format(self.log_count))
        # Cierre limpio del archivo
        self.log_file.close()

    def log(self, message):
        # Escritura del mensaje que se pasa como argumento
        self.log_file.write("{}\n".format(message))
        # Incremento del contador de logs
        self.log_count += 1


class Test:
    def __init__(self):
        self.logger = Logger()

    def llamada(self, message):
        self.logger.log(message)

test = Test()
for i in range(1, 6):
    if i == 1:
        test.llamada("Priemra llamada")
    else:
        test.llamada("{}enésima llamada".format(string))