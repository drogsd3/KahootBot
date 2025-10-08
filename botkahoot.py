import time
from bot_funcao import *
from API.chatgpt import perguntaalternativa
def main():
    while True:
        driver.get("https://kahoot.it/")
        #driver.maximize_window()
        print("-----******------ AGUARDE TODOS COMPONENTES CARREGAREM --------*******-------")
        time.sleep(12)
        clear_terminal()
        Entrar(driver)
        Aguardar(driver)
        x=1
        img = None
        quantidadeperguntas = PegarQuantidadePergunta(driver)       
        while x < quantidadeperguntas:
            perguntaealtenartivas = PegarPergunta(driver)
            img = PegarImagem(driver)
            aswer = perguntaalternativa(perguntaealtenartivas, img)
            seletor = f"button[data-functional-selector='answer-{aswer}']"
            botao = driver.find_element(By.CSS_SELECTOR, seletor)
            botao.click()
            print("Esperando proxima pergunta....")
            time.sleep(5)
            clear_terminal()
        print("Finalizou todas as perguntas")
        terminar = input("Finalizar o programa ou entrar em outro kahoot? S ou N?")
        if terminar == 'N':
            driver.quit()
        else:
            clear_terminal()

if __name__ == "__main__":
    main()