# Chatbot

Instituto de Educação Superior de Brası́lia – IESB
Pós-Graduação em Inteligência Artificial
IANA-P8904 - IESB NORTE
Chatbot 2020-1 A

Aluno: Thiago Jorge Almeida dos Santos
Matrícula: 2031143029

## Trabalho 2 - Rasa Framework

Objetivo: Criar um chatbot utilizando o Rasa Framework com as mesmas características do primeiro trabalho.

Requisitos:
- Estrutura básica: Saudação, Finalização, Ação, Outras perguntas (opcional) 5 pts
- Executar ao menos uma ação customizada dentro de um fluxo de formulário que conecte em um serviço externo (usando requests do python) 5 pts

Requisito obrigatório: a pipeline deve ser configurada permitindo o treinamento do chatbot em português. Não será cobrado excelência na configuração e treinamento, mas o treinamento deve ser suficiente para que os fluxos de diálogo sejam executados.

Não é necessário integrar com nenhum mensageiro de frontend, apenas entregar o projeto do Rasa Framework

Entrega:
Enviar a pasta do projeto do Rasa Framework sem os arquivos de modelo. Para entregar, apague os arquivos da pasta model, compacte e envie. Se desejar, podem versionar os arquivos no GitHub.

## Instruções para Rodar Localmente

- Necessário criar e acessar o ambiente virtual com Python até a versão 3.8
  - Exemplo (Linux): 
    - virtualenv venv --python=/usr/local/bin/python3.8 
    - source venv/bin/activate
- Instalar as dependências do arquivo requirements.txt
  - pip install -r requirements.txt
- Treinar o modelo
  - rasa train
- Rodar o Action Server:
  - rasa run actions
- Rodar o Rasa Shell:
  - rasa shel