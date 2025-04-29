import pandas as pd  

df = pd.read_csv('data.csv') 
# Gera estatísticas em HTML  
relatorio = df.describe().to_html()   

# Salva o HTML 
with open('relatorio.html', 'w') as f:  
    f.write(f"<h1>Relatório de Dados</h1>\n{relatorio}")  

