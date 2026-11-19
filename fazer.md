PASSO 1 — Tratar os dados no código
1. No app.py, carregue censo_1872.csv e apague as duplicatas com este código:
import pandas as pd
df = pd.read_csv("censo_1872.csv")
df = df.drop_duplicates()
2. Some o total de todas as linhas, depois de tirar as duplicatas: o total de homens_livres, o total de
homens_escravizados, o total de mulheres_livres e o total de mulheres_escravizadas.
3. Calcule o percentual de cada grupo entre os homens. A base é o total somado dos dois:
• percentual de homens livres = homens livres / (homens livres + homens escravizados);
• percentual de homens escravizados = homens escravizados / (homens livres + homens
escravizados).
Os dois percentuais somam 100%.
4. Faça o mesmo para as mulheres, com mulheres_livres e mulheres_escravizadas. A base é só a
soma das mulheres. Não misture homens e mulheres no mesmo percentual.
5. O tratamento fica somente no código. Não crie outro arquivo de dados e não altere os números do
censo.


PASSO 2 — Criar o arquivo app.py
Crie o app.py com o cálculo dos percentuais e o painel Streamlit. Inclua no requirements.txt as
bibliotecas abaixo, uma por linha. Se o arquivo de dados for xlsx, utilize o openpyxl para a leitura.
Inclua também o python-calamine.
pandas
plotly
streamlit
openpyxl
python-calamine
Para testar localmente:
pip install -r requirements.txt
streamlit run app.py
A extensão Streamlit Runner também pode ser usada. O painel é obrigatoriamente composto pelos itens
abaixo.
• st.title com o título do painel.
• st.header com um cabeçalho da seção exibida.
• Barra lateral (st.sidebar) com um controle que troca a visualização entre Tabela e Gráficos. Sem a
barra lateral, a prova não atende ao enunciado.
• Na opção Tabela: st.dataframe com os quatro grupos, o total somado de pessoas e o percentual.
• Na opção Gráficos: dois gráficos de pizza.
○ um com o percentual de homens livres e homens escravizados;
○ um com o percentual de mulheres livres e mulheres escravizadas.
• A fonte dos dados visível no painel: https://basedosdados.org/.
PASSO 3 — Fazer o deploy
1. Publique o app.py (Streamlit Community Cloud ou plataforma equivalente).
2. O link público deve abrir o mesmo painel: barra lateral, tabela e os dois gráficos.
3. Grave esse link no arquivo deploy.txt, dentro da pasta da prova.


1. Tratar os dados
Lê censo_1872.csv e usa drop_duplicates() antes de somar.
Soma o total de todas as linhas de cada uma das quatro colunas. Não usa uma linha
só.

Calcula o percentual de cada grupo dentro do próprio sexo, só no código. 
2. Funcionar localmente 
Existe o arquivo app.py. 
requirements.txt lista pandas, plotly, streamlit, openpyxl e python-calamine. 
O painel abre sem erro (streamlit run ou extensão Streamlit Runner). 
A barra lateral troca a visualização sem quebrar a aplicação. 
3. Ter o exigido
Usa st.title e st.header.
A barra lateral alterna Tabela e Gráficos.
st.dataframe mostra os quatro grupos, o total somado e o percentual.
Pizza dos homens (livres e escravizados) e pizza das mulheres (livres e escravizadas).
A fonte https://basedosdados.org/ aparece no painel.
4. Fazer o deploy
A aplicação está publicada.
deploy.txt contém o link, e o link abre o mesmo painel.
