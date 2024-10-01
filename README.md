# Extração de Dados com Web Scraping #

Este projeto utiliza técnicas de web scraping com Selenium para extrair dados de documentos disponíveis no repositório digital DSpace da Universidade Federal de Campina Grande (UFCG). O código coleta informações sobre documentos acadêmicos e armazena os dados extraídos em um arquivo CSV.

## Descrição
O script automatiza a navegação em páginas de listagem de documentos e extrai os seguintes dados de cada um:

- Título
- Título(s) alternativo(s)
- Autor
- Orientador
- Membros da banca
- Palavras-chave
- Data do documento
- Editor
- Citação
- Resumo(s)


## Funcionamento
**Configuração do WebDriver**: Utiliza o Selenium WebDriver para abrir o navegador e acessar o site alvo.  

**Extração de Links**: O código navega pelas páginas da listagem de documentos e coleta os links de cada documento.  

**Extração de Dados**: Para cada link de documento, o script acessa a página específica e extrai os dados mencionados.  

**Armazenamento dos Dados**: Os dados extraídos são salvos em um arquivo CSV com as colunas correspondentes.  

## Tecnologias Utilizadas
**Python**  

**Selenium**: Automação da interação com o navegador.  

**Pandas**: Manipulação e salvamento dos dados em formato CSV.  


## Instruções
**Instale as dependências necessárias**:
```
pip install selenium pandas
```
**Execute o script**.  

Certifique-se de que o ChromeDriver esteja corretamente configurado e adicione o caminho do WebDriver se necessário.  


O script irá gerar um arquivo `dados_extraidos.csv` contendo as informações extraídas.  


## Exemplo de Execução
Após a execução, os dados coletados serão armazenados no arquivo `dados_extraidos.csv`, onde cada linha corresponde a um documento, e cada coluna representa um campo de metadados extraído.
