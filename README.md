# postgrad-ai-nlp-chatbot

[![Status](https://img.shields.io/badge/status-active-brightgreen.svg?label=Status)](./README.md)
[![Hits](https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fgithub.com%2Ftjas%2Fpostgrad-ai-nlp-chatbot&count_bg=%2379C83D&title_bg=%23555555&title=Hits&edge_flat=false)](https://hits.seeyoufarm.com)
[![Licence](https://img.shields.io/github/license/tjas/postgrad-ai-nlp-chatbot?color=orange&label=Licence)](https://github.com/tjas/postgrad-ai-nlp-chatbot/blob/master/LICENCE)
[![Commits](https://img.shields.io/github/commit-activity/t/tjas/postgrad-ai-nlp-chatbot?label=Commits)](https://github.com/tjas/postgrad-ai-nlp-chatbot/graphs/commit-activity)
![Last commit](https://img.shields.io/github/last-commit/tjas/postgrad-ai-nlp-chatbot?color=blue&label=Last%20commit)
![Repo size](https://img.shields.io/github/repo-size/tjas/postgrad-ai-nlp-chatbot?color=888888&label=Repo%20size)
![Code size](https://img.shields.io/github/languages/code-size/tjas/postgrad-ai-nlp-chatbot?color=888888&label=Code%20size)
[![Stars](https://img.shields.io/github/stars/tjas/postgrad-ai-nlp-chatbot?color=blue&label=Stars)](https://github.com/tjas/postgrad-ai-nlp-chatbot/stargazers)
[![Watchers](https://img.shields.io/github/watchers/tjas/postgrad-ai-nlp-chatbot?color=blue&label=Watchers)](https://github.com/tjas/postgrad-ai-nlp-chatbot/watchers)
[![Forks](https://img.shields.io/github/forks/tjas/postgrad-ai-nlp-chatbot?color=blue&label=Forks)](https://github.com/tjas/postgrad-ai-nlp-chatbot/forks)

[![Python](https://img.shields.io/badge/python-v3.8.X-darkgreen?label=Python)](https://www.python.org/)
[![Rasa](https://img.shields.io/badge/rasa-v2.8.14-blue?label=Rasa)](https://rasa.com/)

> ⭐ Mark the project with a star. 👀 Watch the project for receive news.
>
> 🇧🇷 Acesse esta página em [Português do Brasil](./README_pt-br.md).

Artificial Intelligence postgraduation's *Cognitive Computing: Chatbots* discipline exercise using Python and Rasa NLU Framework to build a Brazilian Portuguese chatbot. The postgraduate course was held at [Centro de Educação Superior de Brasília (IESB)](https://www.iesb.br/) and the referred discipline took place in 2020.

## Proposed Exercise

Create a chatbot using the Rasa Framework, with the same characteristics as the first exercise (performed in Watson Assitant, to build a chatbot similar to the one built in this project, but not publicly available), meeting the following requirements:

* Basic structure: Greeting, Ending, Action, Other questions (optional);
* Run at least one custom action within a form flow that connects to an external service (using Python requests);
* The pipeline must be configured allowing training of the chatbot in Brazilian Portuguese;
* Excellence in configuration and training will not be charged, but the training must be sufficient for the dialog flows to be executed;
* It is not necessary to integrate with any Front-end messenger, just deliver the Rasa Framework project;
* Submit the Rasa Framework project folder without the model files. To deliver, delete the files from the model folder, zip and send it. If you wish, you can version the files on GitHub.

## Instructions to Run the Project Locally

> Example using Linux operational system.

This is an example of how you may set up the project locally in your computer. We strongly recommended that you use virtual environments to run the application, we recommend [Virtualenv](https://virtualenv.pypa.io/en/latest/) (or any other of your choice). Read documentation, create and activate the virtual environment inside the project folder before steps 6.

To get a local copy up and running follow these steps:

1. Make sure you have Python 3.8 installed or do it from [Python.org](https://www.python.org/) or from [Anaconda](https://www.anaconda.com/);
2. Make sure you have Git installed or do it from [Git-scm.com](https://git-scm.com/);
3. Access the folder you want to save the project, then clone the repo there
    ```sh
    git clone https://github.com/tjas/postgrad-ai-nlp-chatbot
    ```
4. Access the project folder;
5. Create and activate the virtual environment
    ```sh
    virtualenv venv --python=/usr/local/bin/python3.8
    source venv/bin/activate
    ```
6. Install the project dependencies
    ```py
    pip install -r requirements.txt
    ```
7. Train the model
    ```sh
    rasa train
    ```
8. Run the *Action Server*:
    ```sh
    rasa run actions
    ```
9. Run the *Rasa Shell*:
    ```sh
    rasa shell
    ```

## Contact

**Thiago Jorge Almeida dos Santos**, project author and maintainer.

[![LinkedIn](https://img.shields.io/badge/-LinkedIn-blue?style=flat-square&logoColor=white&link=https://www.linkedin.com/in/thiago-tjas)](https://www.linkedin.com/in/thiago-tjas) [![YouTube](https://img.shields.io/badge/-YouTube-FF0000?style=flat-square&logoColor=white&link=https://www.youtube.com/@thiago_tjas)](https://www.youtube.com/@thiago_tjas) [![Instagram](https://img.shields.io/badge/-Instagram-E4405F?style=flat-square&logoColor=white&link=https://www.instagram.com/thiago.tjas/)](https://www.instagram.com/thiago.tjas/) [![Website](https://img.shields.io/badge/-Website-888888?style=flat-square&logoColor=white&link=http://thiago-tjas.com/)](http://thiago-tjas.com/) [![GitHub](https://img.shields.io/badge/-GitHub-555555?style=flat-square&logoColor=white&link=https://github.com/tjas)](https://github.com/tjas)

## Licence

* Code distributed under [MIT License](https://github.com/tjas/postgrad-ai-nlp-chatbot/blob/master/LICENCE).
