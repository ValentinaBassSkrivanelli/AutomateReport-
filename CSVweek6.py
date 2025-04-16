import pandas as pd
from sqlalchemy import create_engine
from datetime import datetime


user= 'root'
password = 'Pa55word'
host = 'localhost'
db = 'world'


engine = create_engine(f'mysql+mysqlconnector://{user}:{password}@{host}/{db}')


query = """
SELECT 
    Name AS ciudad,
    CountryCode,
    Population
FROM city
WHERE Population > 500000
ORDER BY Population DESC
"""


df = pd.read_sql(query, engine)


df['fecha_procesado'] = datetime.today().strftime('%Y-%m-%d')

# Export to CSV
df.to_csv('data_to_powerbi.csv', index=False)

# Exportar también a Excel (opcional)
df.to_excel('data_to_powerbi.xlsx', index=False)

print("✅ Data exported successfully")
