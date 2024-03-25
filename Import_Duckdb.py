import duckdb

conn = duckdb.connect(database=':memory:', read_only=False)

arq = duckdb.read_csv("C:/Users/Lucas/Desktop/Arquivos/")
conn.execute("CREATE TABLE tb01 AS FROM read_csv('C:/Users/Lucas/Desktop/Arquivos/11.csv')")
conn.execute("SELECT * FROM tb01").fetchall()

conn.sql('SHOW TABLES')

conn.sql('INSTALL postgres')

conn.sql("ATTACH' dbname=dbunifor user=postgres password=1234 host=localhost port=5432' AS postgres (TYPE postgres);")

conn.sql("INSERT INTO postgres.tbl01 SELECT * FROM 'tb01'")

conn.execute("SELECT COUNT(*) FROM postgres.tbl01")