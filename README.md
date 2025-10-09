# Kahoot Bot
Esse projeto entra na sala do kahoot, envia a pergunta para IA, aguarda o retorno da IA e responde a pergunta.

### Introdução
Para o projeto usa-se `Python` e os import:
- `Selenium`: Para automação no navegador.
- `webdriver-manager`: Para gerenciar o driver do navegador.
- `google.generativeai`: Para API com o Gemini do Google.
- `openai`: Para API com o ChatGPT.
Esse projeto é para treinar e aplicar o conhecimento em Python e não tem intuito de ser usado como um facilitador em avaliações no Kahoot.

### Como usar
- Para conseguir "pegar" as perguntas e alternativas dos kahoot, é necessário o "modo Halloween" (Projeto postado em Outubro) já que esse modo, as perguntas e alternativas também ficam na tela do aluno, portanto o "modo clássico" não é possível usar esse codigo.
- Usei o `Gemini` e `ChatGPT` Somente para analisar os desempenhos de ambas, é possivel usar apenas uma das duas no projeto, o arquivo `BOTKA.py` usa o `Gemini` e o `botkahoot.py` usa o `ChatGPT`.
- É necessario que você tenha a chave API para interagir com as IAs, o metodo usado é criando um variavel de ambiente com o Nome: `GOOGLE_API_KEY` e Valor `SUA CHAVE` para o `Gemini` e Nome `OPENAI_API_KEY` e Valor `SUA CHAVE` para o `ChatGPT`
- As minhas chaves são foram deletadas por segurança após subir esse codigo.
- Para acessar a sala digite o codigo da sala no terminal quando requisitado, logo após, insira o apelido.

### Informações Finais
Esse é meu primeiro projeto postado no GitHub, peço compreensão caso haja solução pratica não usual, falta de padrão nas criações (variavel, funções e arquivos) ou até erros não acerto na area de trabalho. 
