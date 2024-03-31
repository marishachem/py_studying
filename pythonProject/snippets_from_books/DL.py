from datetime import datetime

from sqlalchemy import create_engine
import pandas as pd

engine_1 = create_engine("postgresql://bi:bi@bi9.spb.luxms.com/mi")
engine_2 = create_engine("postgresql://bi:bi@db.spb.luxms.com/mi")
connection_res = engine_1.connect()
connection_dest = engine_2.connect()
#query = text("CREATE TABLE if not exists custom.income (code INT NOT NULL,date date not null,inm DECIMAL(12, 2) NOT NULL,inc DECIMAL(12, 2) NOT NULL,product_id INT NOT NULL,transfered INT NOT NULL default 0)")
#connection_res.execute(query)
#for row in result:
#  print(row)

sql ="select * from custom.customers"
df = pd.read_sql(sql,engine_1)
df_filtered = df.query("country=='Norway'")
# Filter the DataFrame

# Specify the target table in the to_sql method
df_filtered.to_sql('customers', engine_2, schema='custom', if_exists='append', index=False)
filename = datetime.now().strftime("%Y%m%d-%H%M%S")
df_filtered.to_csv('/Users/marina/pypro/learning/' + filename + '.csv')
