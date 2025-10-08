
from openai import OpenAI

def perguntaalternativa(perguntaealternativa, img):    
    client = OpenAI()
    if img == None:
        pergunta = (f"Responda diretamente: e apenas com um caracter, se a resposta for a primeira opção responda 0 se for a segunda responda 1 e assim por diante, em Caso de verdadeiro o falso, retorne 0 para V e 1 para Falso\n {perguntaealternativa}")
    else: 
        pergunta =(f"Responda diretamente: e apenas com um caracter, se a resposta for a primeira opção responda 0 se for a segunda responda 1 e assim por diante, em Caso de verdadeiro o falso, retorne 0 para V e 1 para Falso\n {perguntaealternativa} se necessario use essa imagem para responder {img}")


    resposta = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": pergunta}]
    )

    print(f"A reposta foi: {resposta.choices[0].message.content}")
    return int(resposta.choices[0].message.content)

"""gpt-3.5-turbo"""