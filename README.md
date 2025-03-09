Este projeto é um estudo de um pipeline ETL (Extract, Transform, Load) que consome dados fictícios da API JSONPlaceholder, realiza transformações e os armazena em um banco de dados SQLite3.

Tecnologias e Bibliotecas Utilizadas
O projeto utiliza as seguintes bibliotecas:

deep_translator – Para tradução automática de textos, caso necessário.
json – Para manipulação de dados no formato JSON.
os – Para operações no sistema de arquivos.
pandas – Para processamento e análise de dados.
papermill – Para execução de notebooks parametrizados.
requests – Para fazer requisições HTTP à API JSONPlaceholder.
sqlite3 – Para armazenamento dos dados em um banco de dados SQLite.
subprocess – Para execução de processos externos.

Ao executar o pipeline ETL, o projeto criará automaticamente a seguinte estrutura de diretórios:
📂 Projeto_ETL
│-- main.py
│-- 📂 DataLake/          # Armazena os dados brutos e processados seguindo o método Medallion
│-- 📂 notebook_outputs/  # Armazena os outputs das execuções do Papermill
│-- database.sqlite       # Banco de dados SQLite com os dados processados

Como Executar o Projeto?
1. Baixe os arquivos do projeto e coloque-os em uma pasta dedicada.
2. Abra o terminal (CMD) e navegue até a pasta do projeto usando o comando cd <caminho_da_pasta>.
3. Execute o seguinte comando: python main.py

Isso iniciará o processo ETL completo, extraindo os dados da API, realizando as transformações necessárias e armazenando os resultados no SQLite3.

Consultando os Dados no SQLite3
Após a execução, os dados estarão disponíveis no banco de dados SQLite (database.sqlite). Você pode explorá-los utilizando um cliente SQLite ou via linha de comando. Dessa forma, é possível cruzar informações entre users e todos.

Considerações Finais
Este projeto serve como base para estudos de processos ETL, incluindo a utilização de APIs públicas, transformação de dados e armazenamento em banco de dados. Ele pode ser expandido para incluir novas fontes de dados, mais validações e outras etapas do pipeline de dados.
Fique à vontade para modificar e aprimorar conforme suas necessidades!
