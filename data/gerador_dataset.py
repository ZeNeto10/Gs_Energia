import pandas as pd
import numpy as np
from datetime import timedelta

dias = 30
horas = 24 * dias
start_date = pd.to_datetime('2025-09-01 00:00:00')
datas = [start_date + timedelta(hours=i) for i in range(horas)]
tarifa_kwh = 0.85 


df_base = pd.DataFrame(datas, columns=['data_hora'])
df_base['dia_semana'] = df_base['data_hora'].dt.dayofweek 
df_base['hora'] = df_base['data_hora'].dt.hour
df_base['Tarifa_RS_kWh'] = tarifa_kwh


setores = ['Sala_Servidores', 'Escritorio_Geral', 'Copa_Comum']
dados_finais = []

for setor in setores:
    df_setor = df_base.copy()
    

    cond_comercial = (df_setor['hora'] >= 9) & (df_setor['hora'] < 19) & (df_setor['dia_semana'] < 5)
    

    if setor == 'Sala_Servidores':

        base_consumo = 5.0  
        pico_dia = np.where(cond_comercial, 1.5, 0) 
        df_setor['Consumo_kWh'] = base_consumo + np.random.normal(loc=pico_dia, scale=0.3)
        df_setor['Equipamento_Dominante'] = 'Servidores'
        df_setor['Ocupacao_Pessoas'] = np.where(cond_comercial, np.random.randint(1, 3, size=len(df_setor)), 0)

    elif setor == 'Escritorio_Geral':
        # Consumo Diurno (Computadores, Iluminação, AC)
        base_consumo = 0.5  # Consumo base (roteadores, etc.)
        pico_dia = np.where(cond_comercial, np.random.normal(9.0, 1.8), 0)
        
        # 🚨 INJEÇÃO DE DESPERDÍCIO (Nosso Target de Otimização)
        # Simula 20% do consumo diurno (média de 1.8 kWh/h) ficando ligado após o horário e no fim de semana
        cond_desperdicio = ~cond_comercial # Fora do horário comercial
        desperdicio = np.where(cond_desperdicio, np.random.normal(1.8, 0.4), 0)
        
        df_setor['Consumo_kWh'] = base_consumo + pico_dia + desperdicio
        df_setor['Equipamento_Dominante'] = np.where(desperdicio > 0.5, 'Iluminação/Monitores (Desperdício)', 'Computadores/AC')
        df_setor['Ocupacao_Pessoas'] = np.where(cond_comercial, np.random.randint(7, 18, size=len(df_setor)), 0)

    elif setor == 'Copa_Comum':
        # Consumo Pontual (Picos de Eletrodomésticos)
        base_consumo = 0.1
        cond_pausa = ((df_setor['hora'] == 10) | (df_setor['hora'] == 13) | (df_setor['hora'] == 16)) & (df_setor['dia_semana'] < 5)
        pico_pausa = np.where(cond_pausa, np.random.normal(2.5, 0.5), 0)
        df_setor['Consumo_kWh'] = base_consumo + pico_pausa
        df_setor['Equipamento_Dominante'] = 'Eletrodomésticos'
        df_setor['Ocupacao_Pessoas'] = np.where(cond_comercial, np.random.randint(3, 8, size=len(df_setor)), 0)
    
    # Garantir que o consumo seja não-negativo
    df_setor['Consumo_kWh'] = df_setor['Consumo_kWh'].clip(lower=0)
    df_setor['Setor'] = setor
    dados_finais.append(df_setor)

# --- 4. Concatenação e Formato Final ---
dataset_projeto = pd.concat(dados_finais)
dataset_projeto.drop(columns=['dia_semana', 'hora'], inplace=True)

# Reordenar colunas e garantir o nome mais legível
colunas_finais = ['data_hora', 'Setor', 'Consumo_kWh', 'Ocupacao_Pessoas', 'Equipamento_Dominante', 'Tarifa_RS_kWh']
dataset_projeto = dataset_projeto[colunas_finais]

# Renomear conforme o mapeamento final do projeto
dataset_projeto.rename(columns={'data_hora': 'DataHora'}, inplace=True)

# Salvar o dataset para o entregável
dataset_projeto.to_csv('consumo_energetico_simulado.csv', index=False)

# Exibindo as primeiras linhas e o resumo do consumo total
print("✅ Dataset 'consumo_energetico_simulado.csv' criado com sucesso.")
print("\n--- Cabeçalho do Dataset ---")
print(dataset_projeto.head())
print("\n--- Resumo de Consumo Simulado ---")
consumo_total_mensal = dataset_projeto['Consumo_kWh'].sum()
custo_total_mensal = consumo_total_mensal * tarifa_kwh
print(f"Consumo Total (1 mês): {consumo_total_mensal:,.2f} kWh")
print(f"Custo Total (1 mês): R$ {custo_total_mensal:,.2f}")