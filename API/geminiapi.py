import google.generativeai as genai

def perguntaalternativa(perguntaealternativa, img):
       try:
              genai.configure()
              print("Chave de API configurada com sucesso a partir da variável de ambiente!")
       except Exception as e:
              print(f"Erro ao configurar a API. Verifique se a variável de ambiente GOOGLE_API_KEY está definida corretamente. Erro: {e}")
              exit()
              
       model = genai.GenerativeModel('gemini-2.5-flash')
       
       if img == None:
              response = model.generate_content(f"Responda diretamente: e apenas com um caracter, se a resposta for a primeira opção responda 0 se for a segunda responda 1 e assim por diante, em Caso de verdadeiro o falso, retorne 0 para V e 1 para Falso\n {perguntaealternativa}")
       else:
              response = model.generate_content(f"Responda diretamente: e apenas com um caracter, se a resposta for a primeira opção responda 0 se for a segunda responda 1 e assim por diante, em Caso de verdadeiro o falso, retorne 0 para V e 1 para Falso\n {perguntaealternativa} se necessario use essa imagem para responder {img}")

       # Imprima a resposta
       
       return int(response.text)