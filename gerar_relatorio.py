import pandas as pd  

df = pd.read_csv('data.csv')  
relatorio = df.describe().to_html() # Gera estatísticas em HTML   

with open('relatorio.html', 'w') as f:  
    f.write(f"<h1>Relatório de Dados</h1>\n{relatorio}")  # Salva o HTML 

