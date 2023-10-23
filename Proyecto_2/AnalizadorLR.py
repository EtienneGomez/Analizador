class AnalizadorLR:
    def __init__(self, tokens):
        self.tokens = tokens
        self.stack = []

    def parse(self):
        self.stack.append("$")
        token = self.tokens.pop(0)
        while True:
            top = self.stack[-1]
            if top == "$" and token == "$":
                break
            elif top == token:
                self.stack.pop()
                token = self.tokens.pop(0)
            elif top == "Q":
                self.match("select", "D", "from", "T")
            elif top == "D":
                if token == "distinct":
                    self.match("distinct", "P")
                else:
                    self.match("P")
            elif top == "P":
                if token == "*":
                    self.match("*")
                else:
                    self.match("A")
            elif top == "A":
                if token == "id":
                    self.match("A1")
                else:
                    self.match("A", ",", "A1")
            elif top == "A1":
                self.match("id", "A2")
            elif top == "A2":
                if token == ".":
                    self.match(".", "id")
            elif top == "T":
                if token == "id":
                    self.match("T1")
                else:
                    self.match("T", ",", "T1")
            elif top == "T1":
                self.match("id", "T2")
            elif top == "T2":
                if token == "id":
                    self.match("id")
            else:
                raise Exception("Error de sintaxis")

    def match(self, *args):
        self.stack.pop()
        self.stack.extend(reversed(args))
