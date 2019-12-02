class MyExceptionError(Exception):
    pass

class MyInputError(MyExceptionError):
    def __init__(self, expression="Express"):
        self.expression = expression

raise MyInputError("Errore tuo")
