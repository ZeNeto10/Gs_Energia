import pandas as pd

df = pd.read_csv("C:/Users/zenet/OneDrive/Documents/FIAP/Global_Solution/SOLUÇÕES EM ENERGIAS RENOVÁVEIS E SUSTENTÁVEIS/data/consumo_energetico_simulado.csv")

df['DataHora'] = pd.to_datetime(df['DataHora'])
df['dia_semana'] = df['DataHora'].dt.dayofweek 
df['hora'] = df['DataHora'].dt.hour

tarifa = df['Tarifa_RS_kWh'].iloc[0]

cond_setor = df['Setor'] == 'Escritorio_Geral'
cond_comercial = (df['hora'] >= 9) & (df['hora'] < 19) & (df['dia_semana'] < 5)
cond_fora_comercial = ~cond_comercial
cond_baixa_ocupacao = df['Ocupacao_Pessoas'] <= 1
cond_consumo_acima_baseline = df['Consumo_kWh'] > 0.55 

df_desperdicio = df[
    cond_setor &
    cond_fora_comercial &
    cond_baixa_ocupacao &
    cond_consumo_acima_baseline
]

desperdicio_kwh = df_desperdicio['Consumo_kWh'].sum()
custo_desperdicio = desperdicio_kwh * tarifa
consumo_total_mensal = df['Consumo_kWh'].sum()
percentual_desperdicio = (desperdicio_kwh / consumo_total_mensal) * 100

print(f"Desperdício isolado no Escritório Geral: {desperdicio_kwh:,.2f} kWh")
print(f"Custo Financeiro Estimado: R$ {custo_desperdicio:,.2f}")
print(f"Percentual do desperdício: {percentual_desperdicio:.2f}%")
