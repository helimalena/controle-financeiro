class ContaBancaria:
    def __init__(self, nome, saldo_inicial=0):
        self.nome = nome
        self.saldo = saldo_inicial

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f"Depósito de R${valor} realizado com sucesso.")
        else:
            print("Valor de depósito inválido.")

    def sacar(self, valor):
        if valor > 0 and valor <= self.saldo:
            self.saldo -= valor
            print(f"Saque de R${valor} realizado com sucesso.")
        else:
            print("Saque inválido. Saldo insuficiente.")

    def consultar_saldo(self):
        print(f"Saldo da conta de {self.nome}: R${self.saldo}")


# Exemplo de uso
if __name__ == "__main__":
    conta = ContaBancaria("João", 1000)
    conta.consultar_saldo()
    conta.depositar(500)
    conta.sacar(200)
    conta.consultar_saldo()
