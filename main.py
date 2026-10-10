import pandas as pd

df_raw = pd.read_csv('Data/credit risk dataset.csv')

df = df_raw.sample(n=5000, random_state=42).reset_index(drop=True)
df.to_csv('Data/credit_risk_dataset.csv', index=False)
print(f"Початковий розмір: {df_raw.shape}")
print(f"Розмір після обрізки: {df.shape[0]} рядків, {df.shape[1]} стовпчиків\n")
print("="*50)

print("\nІНФОРМАЦІЯ ПРО СТОВПЦІ ТА ТИПИ ДАНИХ:")
df.info()
print("\nПЕРШІ 5 РЯДКІВ ДАТАСЕТУ:")
df.head()