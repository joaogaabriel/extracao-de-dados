from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pandas as pd

def get_document_links(driver):
    try:
        # Localizar todos os documentos na página atual
        documentos = driver.find_elements(By.CSS_SELECTOR, "td.evenRowOddCol > strong > a, td.oddRowOddCol > strong > a")
        links = [(doc.get_attribute("href"), doc.text) for doc in documentos]
        return links
    except Exception as e:
        print("Erro ao recuperar os documentos:", e)
        return []

def extrair_valores(driver, url):
    try:
        driver.get(url)
        WebDriverWait(driver, 20).until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'metadataFieldValue')))
        elementos = driver.find_elements(By.CLASS_NAME, 'metadataFieldValue')
        valores = [elemento.text for elemento in elementos]
        return valores
    except Exception as e:
        print(f"Erro ao acessar a URL {url}: {e}")
        return []

# Configurar o driver do navegador
driver = webdriver.Chrome()
driver.get("http://dspace.sti.ufcg.edu.br:8080/jspui/handle/riufcg/19193?offset=140")

# Lista para armazenar todos os links de documentos
all_links = []

while True:
    # Esperar até que os documentos estejam presentes
    WebDriverWait(driver, 20).until(
        EC.presence_of_all_elements_located(
            (By.CSS_SELECTOR, "td.evenRowOddCol > strong > a, td.oddRowOddCol > strong > a"))
    )

    # Obter os links dos documentos na página atual
    links = get_document_links(driver)
    all_links.extend(links)

    # Tentar encontrar o botão "Próximo"
    try:
        next_button = driver.find_element(By.LINK_TEXT, "Próximo >")
        next_button.click()

        # Esperar um pouco para a próxima página carregar
        time.sleep(3)
    except Exception as e:
        print("Botão 'Próximo' não encontrado ou não clicável:", e)
        break

# Definir as colunas do CSV
colunas = [
    'Título', 'Título(s) alternativo(s)', 'Autor', 'Orientador', 'Membro da Banca 1', 'Membro da Banca 2', 
    'Palavras-chave', 'Data do documento', 'Editor', 'Citação', 'Resumo 1', 'Resumo 2', 
    'Palavras-chave 2', 'CNPq', 'URI', 'Aparece nas coleções'
]

# Inicializa o CSV com o cabeçalho (apenas se o arquivo não existir)
arquivo_csv = 'dados_extraidos.csv'
try:
    with open(arquivo_csv, 'x', encoding='utf-8') as f:
        f.write(','.join(colunas) + '\n')
except FileExistsError:
    pass  # Arquivo já existe, não faz nada

# Extrair valores e salvar no CSV
for link, text in all_links:
    valores = extrair_valores(driver, link)
    if len(valores) == len(colunas):  # Certifica-se de que o número de valores corresponde ao número de colunas
        df = pd.DataFrame([valores], columns=colunas)
        df.to_csv(arquivo_csv, mode='a', index=False, header=False, encoding='utf-8')
    else:
        print(f"Dados incompletos para o link: {link}")

driver.quit()
print(f"Valores extraídos e salvos em {arquivo_csv}")
