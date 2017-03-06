import webapp

class aleat(webapp.app):
    def process(self,parsedRequest):
        import random
        numero = random.randint(1,100000)
        return ("200 OK", "<html><body><a href="+ str(numero)+">Dame mas</a>"
                + "</body></html>")

if __name__ == "__main__":
    aleatApp = aleat()
    testAleat = webapp.webApp("localhost", 1234,{'/aleat': aleatApp})
