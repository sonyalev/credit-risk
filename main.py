import pandas as pd

df_raw = pd.read_csv('Data/credit risk dataset.csv')

df = df_raw.sample(n=5000, random_state=42).reset_index(drop=True)
df.to_csv('Data/credit_risk_dataset.csv', index=False)
# 3. Виводимо базову інформацію про розмірність
print(f"Початковий розмір: {df_raw.shape}")
print(f"Розмір після обрізки: {df.shape[0]} рядків, {df.shape[1]} стовпчиків\n")
print("="*50)

# 4. Виводимо список усіх стовпчиків, їхні типи даних та кількість непустих значень
print("\nІНФОРМАЦІЯ ПРО СТОВПЦІ ТА ТИПИ ДАНИХ:")
df.info()

# 5. Відображаємо перші 5 рядків датасету для наочності
print("\nПЕРШІ 5 РЯДКІВ ДАТАСЕТУ:")
df.head()