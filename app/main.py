from app import ui_terminal, query_generator, db_connector, report_builder
import pandas as pd

pergunta = ui_terminal.iniciar_interface()
sql = query_generator.gerar_sql(pergunta)
print("[SQL gerada]", sql)

conn = db_connector.conectar()
df = pd.read_sql_query(sql, conn)
print(df.head())

report_builder.gerar_relatorio(df)
print("Relatório gerado com sucesso.")
