class SistemaReservas:
    def __init__(self):
        self.voos_disponiveis = {}
        self.reservas = {}

    def adicionar_voo(self, voo, capacidade):
        self.voos_disponiveis[voo] = capacidade

    def pesquisar_voos_disponiveis(self):
        return self.voos_disponiveis

    def fazer_reserva(self, voo, assento):
        if voo in self.voos_disponiveis and self.voos_disponiveis[voo] > 0:
            if voo not in self.reservas:
                self.reservas[voo] = set()
            if assento not in self.reservas[voo]:
                self.reservas[voo].add(assento)
                self.voos_disponiveis[voo] -= 1
                return True
        return False

    def visualizar_reservas(self):
        return self.reservas

    def cancelar_reserva(self, voo, assento):
        if voo in self.reservas and assento in self.reservas[voo]:
            self.reservas[voo].remove(assento)
            self.voos_disponiveis[voo] += 1
            return True
        return False
