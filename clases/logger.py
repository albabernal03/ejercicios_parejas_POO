class Logger:
    def __init__(self):
        self.log_file = open("log.txt", "w")
        self.log_count = 0
        self.log_file.write("--Inicio del log--\n")


    def __del__(self):
        self.log_file.write("--Fin del log: {} log(s)--\n".format(self.log_count))
        self.log_file.close()

    def log(self, message):
        self.log_file.write("{}\n".format(message))
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