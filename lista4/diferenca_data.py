from datetime import datetime

def diferenca_entre_datas(data1, data2):
    data1 = datetime.strptime(data1, "%Y-%m-%d %H:%M:%S")
    data2 = datetime.strptime(data2, "%Y-%m-%d %H:%M:%S")

    diferenca = data2 - data1

    dias = diferenca.days

    meses = diferenca.days // 30
    anos = meses // 12

    horas = diferenca.seconds // 3600
    minutos = (diferenca.seconds % 3600) // 60

    return dias, meses, anos, horas, minutos
