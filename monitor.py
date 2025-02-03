import psutil
import csv
import time
from datetime import datetime

# Função para coletar as informações
def coletar_dados_sistema():
    # Coleta de informações sobre o sistema
    cpu = psutil.cpu_percent(interval=1)
    memoria = psutil.virtual_memory().percent
    disco = psutil.disk_usage('/').percent

    # Registro de dados
    data_atual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return [data_atual, cpu, memoria, disco]

# Função para salvar os dados em um arquivo CSV
def salvar_dados(dados):
    with open('monitoramento_sistema.csv', mode='a', newline='') as arquivo:
        writer = csv.writer(arquivo)
        writer.writerow(dados)

# Monitoramento contínuo
while True:
    dados_sistema = coletar_dados_sistema()
    salvar_dados(dados_sistema)
    print(f"Dados registrados: {dados_sistema}")
    time.sleep(60)  # Espera de 1 minuto
