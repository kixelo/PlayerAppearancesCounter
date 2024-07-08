import pandas
import pandas as pd

df = pd.read_csv("3_liga_east_2023_24_squad_v2.csv")
#print(df)

df = df.reindex(columns=['Name', 'Appearances', 'Goals', 'Yellow cards', 'Red cards'])
df.to_csv("3_liga_east_2023_24_squad_v2.csv", encoding='utf-8-sig', index=False)