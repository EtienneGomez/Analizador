class AnalizadorLL:
    def __init__(self, tokens):
        self.tokens = tokens
        self.index = 0

    def consume(self):
        self.index += 1

    def Q(self):
        if self.tokens[self.index] == "select":
            self.consume()
            self.D()
            if self.tokens[self.index] == "from":
                self.consume()
                self.T()
            else:
                raise Exception("Error de sintaxis: se esperaba 'from'")
        else:
            raise Exception("Error de sintaxis: se esperaba 'select'")

    def D(self):
        if self.tokens[self.index] == "distinct":
            self.consume()
            self.P()
        else:
            self.P()

    def P(self):
        if self.tokens[self.index] == "*":
            self.consume()
        else:
            self.A()

    def A(self):
        self.A2()
        self.A1()

    def A1(self):
        if self.tokens[self.index] == ",":
            self.consume()
            self.A()

    def A2(self):
        if isinstance(self.tokens[self.index], str):  # Suponemos que los identificadores son cadenas
            self.consume()
            self.A3()

    def A3(self):
        if self.tokens[self.index] == ".":
            self.consume()
            if isinstance(self.tokens[self.index], str):
                self.consume()

    def T(self):
        self.T2()
        self.T1()

    def T1(self):
        if self.tokens[self.index] == ",":
            self.consume()
            self.T()

    def T2(self):
        if isinstance(self.tokens[self.index], str):
            self.consume()
            self.T3()

    def T3(self):
        if isinstance(self.tokens[self.index], str):
            self.consume()
