import os
import time
from selenium import webdriver # type: ignore
from selenium.webdriver.chrome.service import Service as ChromeService # type: ignore
from selenium.webdriver.common.keys import Keys # type: ignore
from selenium.webdriver.common.by import By # type: ignore
from webdriver_manager.chrome import ChromeDriverManager # type: ignore
from selenium.webdriver.support.ui import WebDriverWait # type: ignore
from selenium.webdriver.support import expected_conditions as EC # type: ignore

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

def Entrar(driver):
    
    try:
        print("Entramos, agora é colocar o codigo")
        entrar = driver.find_element(By.NAME, "gameId")
        codigo = input("Digite um codigo do Kahoot: ")
        entrar.send_keys(codigo)
        entrar.send_keys(Keys.RETURN)
        apelido = input("Digite um apelido: ")
        username = driver.find_element(By.NAME, "nickname")
        username.send_keys(apelido)
        username.send_keys(Keys.RETURN)
    except ValueError:
        print("Não deu certo")
        time.sleep(1)

def Aguardar(driver):
    print("Aguardando começar o jogo")
    try:
        elemento = WebDriverWait(driver, 500).until(EC.presence_of_element_located((By.CSS_SELECTOR, "div[data-functional-selector='question-index-counter']")))
        #elemento1 = driver.find_element(By.CSS_SELECTOR, "div[data-functional-selector='question-block-title']")       
        print("VAI COMEÇAR")
        #print(f"O elemento é: {elemento1.text}")
    except ValueError:
        print("Deu Ruim")
    return

def PegarQuantidadePergunta(driver):
    x=0    
    print("COMEÇOU")
    WebDriverWait(driver,100).until(EC.presence_of_element_located((By.CSS_SELECTOR, "span[data-functional-selector='block-title']")))      
    time.sleep(1)
    quantidade = driver.title
    print(f"quantidade string: {quantidade}")    
    if quantidade[11] == " ":
        quantidade = int(quantidade[11])
        print(f"A quantidade de perguntas é {quantidade}")
    else:
         a = quantidade[11]+quantidade[12]
         quantidade = int(a)
         #print(f"A quantidade de perguntas é {quantidade}")
    print(f"Quantidade inteiro {quantidade} {type(quantidade)}")
    return quantidade

def PegarPergunta(driver):    
    pergunta_lista = []
    y=0
    pergunta = WebDriverWait(driver,500).until(EC.presence_of_element_located((By.CSS_SELECTOR, "span[data-functional-selector='block-title']")))
    pergunta_lista.append(pergunta.text)
    alternativas = driver.find_elements(By.CSS_SELECTOR, "button[data-functional-selector^='answer-']")
    quantidadealternativa = len(alternativas)
    while y < quantidadealternativa:
        try:
                texto = alternativas[y].text.strip()
                pergunta_lista.append(texto)
        except:
                pergunta_lista.append("[Erro ao ler]")
        y += 1
    return pergunta_lista

def PegarImagem(driver):
    try:
        img_element = driver.find_element(By.CSS_SELECTOR, '[data-functional-selector="media-container__media-image"]')
        img_url = img_element.get_attribute("src")
        print("URL da imagem:", img_url)
        return img_url
    except:
         print("Erro ao pegar a imagem ou não existe imagem para pegar")
         return None

def clear_terminal():
    """Limpa o terminal."""
    # Para sistemas Windows
    if os.name == 'nt':
        os.system('cls')
    # Para sistemas Unix (Linux, macOS)
    else:
        os.system('clear')