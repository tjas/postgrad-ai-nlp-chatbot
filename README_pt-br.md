# postgrad-ai-nlp-chatbot

[![Status](https://img.shields.io/badge/status-active-brightgreen.svg?label=Status)](./README.md)
[![Acessos](https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fgithub.com%2Ftjas%2Fpostgrad-ai-nlp-chatbot&count_bg=%2379C83D&title_bg=%23555555&title=Acessos&edge_flat=false)](https://hits.seeyoufarm.com)
[![Licença](https://img.shields.io/github/license/tjas/postgrad-ai-nlp-chatbot?color=orange&label=Licença)](https://github.com/tjas/postgrad-ai-nlp-chatbot/blob/master/LICENCE)
[![Commits](https://img.shields.io/github/commit-activity/t/tjas/postgrad-ai-nlp-chatbot?label=Commits)](https://github.com/tjas/postgrad-ai-nlp-chatbot/graphs/commit-activity)
![Último commit](https://img.shields.io/github/last-commit/tjas/postgrad-ai-nlp-chatbot?color=blue&label=Último%20commit)
![Tamanho do repositório](https://img.shields.io/github/repo-size/tjas/postgrad-ai-nlp-chatbot?color=888888&label=Tam.%20repositório)
![Tamanho do código](https://img.shields.io/github/languages/code-size/tjas/postgrad-ai-nlp-chatbot?color=888888&label=Tam.%20código)
[![Stars](https://img.shields.io/github/stars/tjas/postgrad-ai-nlp-chatbot?color=blue&label=Stars)](https://github.com/tjas/postgrad-ai-nlp-chatbot/stargazers)
[![Watchers](https://img.shields.io/github/watchers/tjas/postgrad-ai-nlp-chatbot?color=blue&label=Watchers)](https://github.com/tjas/postgrad-ai-nlp-chatbot/watchers)
[![Forks](https://img.shields.io/github/forks/tjas/postgrad-ai-nlp-chatbot?color=blue&label=Forks)](https://github.com/tjas/postgrad-ai-nlp-chatbot/forks)

[![Python](https://img.shields.io/badge/python-v3.8.X-darkgreen?label=Python)](https://www.python.org/)
[![Rasa](https://img.shields.io/badge/rasa-v2.8.14-blue?label=Rasa)](https://rasa.com/)

> ⭐ Marque o projeto com uma estrela. 👀 Acompanhe o projeto para receber novidades.
>
> 🇺🇸 Access this page in [US English](./README.md).

Exercício da disciplina *Computação Cognitiva: Chatbots* da pós-graduação em Inteligência Artificial utilizando Python e Rasa NLU Framework para construir um chatbot em Português do Brasil. O curso de pós-graduação foi realizado no [Centro de Educação Superior de Brasília (IESB)](https://www.iesb.br/) e a referida disciplina ocorreu em 2020.

## Exercício Proposto

Criar um chatbot utilizando o Rasa Framework, com as mesmas características do primeiro trabalho (realizado no Watson Assitant, para construir um chatbot semelhante ao construído neste projeto, mas não disponibilizado publicamente), atendendo aos seguintes requisitos:

* Estrutura básica: Saudação, Finalização, Ação, Outras perguntas (opcional);
* Executar ao menos uma ação customizada dentro de um fluxo de formulário que conecte em um serviço externo (usando requests do Python);
* A pipeline deve ser configurada permitindo o treinamento do chatbot em Português do Brasil;
* Não será cobrado excelência na configuração e treinamento, mas o treinamento deve ser suficiente para que os fluxos de diálogo sejam executados;
* Não é necessário integrar com nenhum mensageiro de Front-end, apenas entregar o projeto do Rasa Framework;
* Enviar a pasta do projeto do Rasa Framework sem os arquivos de modelo. Para entregar, apague os arquivos da pasta model, compacte e envie. Se desejar, podem versionar os arquivos no GitHub.

## Instruções para Rodar o Projeto Localmente

> Exemplo utilizando o sistema operacional Linux.

Este é um exemplo de como você pode configurar o projeto localmente no seu computador. Recomendamos fortemente que você utilize um ambiente virtual para rodar a aplicação, recomendamos a utilização do [Virtualenv](https://virtualenv.pypa.io/en/latest/) (ou qualquer outro de sua preferência). Leia a documentação, crie e ative o ambiente virtual dentro da pasta do projeto antes do passo 6.

Para obter uma cópia local funcionando, siga estas etapas:

1. Certifique-se de que você tem o Python 3.8 instalado ou verifique como fazê-lo em [Python.org](https://www.python.org/) ou por meio do [Anaconda](https://www.anaconda.com/);
2. Certifique-se de que você tem o Git instalado ou verifique como fazê-lo em [Git-scm.com](https://git-scm.com/);
3. Acesse a pasta na qual você deseja salvar o projeto, então, clone o repositório nesta pasta
    ```sh
    git clone https://github.com/tjas/postgrad-ai-nlp-chatbot
    ```
4. Acesse a pasta do projeto;
5. Crie e ative o ambiente virtual
    ```sh
    virtualenv venv --python=/usr/local/bin/python3.8 
    source venv/bin/activate
    ```
6. Instale as dependências do projeto
    ```py
    pip install -r requirements.txt
    ```
7. Treine o modelo
    ```sh
    rasa train
    ```
8. Rode o *Action Server*:
    ```sh
    rasa run actions
    ```
9. Rode o *Rasa Shell*:
    ```sh
    rasa shell
    ```

## Contato

**Thiago Jorge Almeida dos Santos**, autor e mantenedor do projeto.

[![LinkedIn](https://img.shields.io/badge/-LinkedIn-blue?style=flat-square&logoColor=white&link=https://www.linkedin.com/in/thiago-tjas)](https://www.linkedin.com/in/thiago-tjas) [![YouTube](https://img.shields.io/badge/-YouTube-FF0000?style=flat-square&logoColor=white&link=https://www.youtube.com/@thiago_tjas)](https://www.youtube.com/@thiago_tjas) [![Instagram](https://img.shields.io/badge/-Instagram-E4405F?style=flat-square&logoColor=white&link=https://www.instagram.com/thiago.tjas/)](https://www.instagram.com/thiago.tjas/) [![Website](https://img.shields.io/badge/-Website-888888?style=flat-square&logoColor=white&link=http://thiago-tjas.com/)](http://thiago-tjas.com/) [![GitHub](https://img.shields.io/badge/-GitHub-555555?style=flat-square&logoColor=white&link=https://github.com/tjas)](https://github.com/tjas)

## Licença

* Código distribuído sob a [Licença MIT](https://github.com/tjas/postgrad-ai-nlp-chatbot/blob/master/LICENCE).

