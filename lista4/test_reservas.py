import pytest
from reservas import SistemaReservas

@pytest.fixture
def sistema_reservas():
    sistema = SistemaReservas()
    sistema.adicionar_voo("Voo1", 10)
    sistema.adicionar_voo("Voo2", 5)
    return sistema

def test_adicionar_voo(sistema_reservas):
    assert sistema_reservas.voos_disponiveis == {"Voo1": 10, "Voo2": 5}

def test_pesquisar_voos_disponiveis(sistema_reservas):
    assert sistema_reservas.pesquisar_voos_disponiveis() == {"Voo1": 10, "Voo2": 5}

def test_fazer_reserva(sistema_reservas):
    assert sistema_reservas.fazer_reserva("Voo1", "Assento1") == True
    assert sistema_reservas.fazer_reserva("Voo1", "Assento1") == False  # Reserva duplicada
    assert sistema_reservas.fazer_reserva("Voo2", "Assento1") == True
    assert sistema_reservas.fazer_reserva("Voo1", "Assento2") == True
    assert sistema_reservas.fazer_reserva("Voo2", "Assento2") == True
    assert sistema_reservas.fazer_reserva("Voo2", "Assento3") == True
    assert sistema_reservas.fazer_reserva("Voo1", "Assento3") == True
    assert sistema_reservas.fazer_reserva("Voo1", "Assento4") == True
    assert sistema_reservas.fazer_reserva("Voo1", "Assento5") == True
    assert sistema_reservas.fazer_reserva("Voo1", "Assento6") == True
    assert sistema_reservas.fazer_reserva("Voo1", "Assento7") == True
    assert sistema_reservas.fazer_reserva("Voo1", "Assento8") == True
    assert sistema_reservas.fazer_reserva("Voo1", "Assento9") == True
    assert sistema_reservas.fazer_reserva("Voo1", "Assento10") == True
    assert sistema_reservas.fazer_reserva("Voo1", "Assento11") == False  # Capacidade excedida

def test_visualizar_reservas(sistema_reservas):
    assert sistema_reservas.visualizar_reservas() == {'Voo1': {'Assento1', 'Assento2', 'Assento3', 'Assento4', 'Assento5', 'Assento6', 'Assento7', 'Assento8', 'Assento9', 'Assento10'}, 'Voo2': {'Assento1', 'Assento2', 'Assento3'}}

def test_cancelar_reserva(sistema_reservas):
    assert sistema_reservas.cancelar_reserva("Voo1", "Assento1") == True
    assert sistema_reservas.cancelar_reserva("Voo2", "Assento1") == True
    assert sistema_reservas.cancelar_reserva("Voo1", "Assento11") == False  # Reserva inexistente
    assert sistema_reservas.cancelar_reserva("Voo1", "Assento1") == False  # Reserva já cancelada
