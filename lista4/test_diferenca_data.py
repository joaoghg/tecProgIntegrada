import pytest
from diferenca_data import diferenca_entre_datas

def test_diferenca_entre_datas():
    data1 = "2024-03-20 12:00:00"
    data2 = "2024-03-22 15:30:00"

    dias_esperados = 2
    meses_esperados = 0
    anos_esperados = 0
    horas_esperadas = 3
    minutos_esperados = 30

    dias, meses, anos, horas, minutos = diferenca_entre_datas(data1, data2)

    assert dias == dias_esperados
    assert meses == meses_esperados
    assert anos == anos_esperados
    assert horas == horas_esperadas
    assert minutos == minutos_esperados
