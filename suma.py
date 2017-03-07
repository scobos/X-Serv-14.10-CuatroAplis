import webapp

class suma(webapp.app): #/suma/

    def __init__(self):
        self.primera = True
        self.entero = 0
    def parse(self, request,rest):
        return request.split()[1:]

    def process(self, parsedRequest):
        if parsedRequest == "favicon.ico":
            return("404 Not Found", "<html><body>Not found</body></html>")
        try:
            self.entero = int(parsedRequest)
        except ValueError:
            return ("HTTP/1.1 404 Not Found\r\n\r\n<html><body><h1> Me has dado un " + str(parsedRequest) +
                    ". Vete</h1></body></html>\r\n")



        if self.primera:
            sum1 = self.entero
            self.primera = False
            return ("HTTP/1.1 200 OK\r\n\r\n" +
                            "<html><body><p>Me has dado un " +
                             str(sum1) + ".Dame mas</p></body></html>" +
                             "\r\n")

        else:
            sum2 = self.entero
            self.primera = True
            return("HTTP/1.1 200 OK\r\n\r\n" +
                "<html><body><p>Me habias dado un " +
                str(sum1) + ".Ahora un " + str(sum2) +
                ".Suman " + str(sum1+sum2) +
                ".</p></body></html>" +
                "\r\n")

if __name__ == "__main__":
    sumaApp = suma()
    testSuma = webapp.webApp("localhost", 1234, {'/suma': sumaApp})
