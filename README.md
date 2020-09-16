# popular-repositories-github-information
Informations about popular repositories on GitHub extracted by GitHub api

Este projeto é uma atividade prática da disciplina Laboratório de Medição e Experimentação em Engenharia de Software do curso de Engenharia de Software da PONTIFÍCIA UNIVERSIDADE CATÓLICA DE MINAS GERAIS.

## Objetivo
O objetivo dessa atividade é introduzir conceitos práticos de mineração de dados a partir da mineração de informações de repositórios de software do GitHub.

## Descrição da Atividade
Analisar sistemas populares open source, coletando informações dos 1.000 repositórios com maior número de estrelas no GitHub.

## Questões de Pesquisa (proposto pelo Prof. Laerte Xavier)
- RQ 01. Sistemas populares são maduros/antigos? Métrica: idade do repositório (calculado a partir da data de sua criação)
- RQ 02. Sistemas populares recebem muita contribuição externa? Métrica: total de pull requests aceitas
- RQ 03. Sistemas populares lançam releases com frequência? Métrica: total de releases
- RQ 04. Sistemas populares são atualizados com frequência? Métrica: tempo até a última atualização (calculado a partir da data de última atualização)
- RQ 05. Sistemas populares são escritos nas linguagens mais populares? Métrica: linguagem primária de cada um desses repositórios
- RQ 06. Sistemas populares possuem um alto percentual de issues fechadas? Métrica: razão entre número de issues fechadas pelo total de issues

## Requisitos do projeto
- Python 3.8.2
- pip 20.1

## Como executar
Clone o projeto
```
git clone https://github.com/raviassis/popular-repositories-github-information.git
```
Acesse o diretório raiz do projeto
```
cd popular-repositories-github-information
```
Crie um arquivo .env para as variáveis de ambiente
```
cp .env.example .env
```
Insira sua token de autenticação da api do github no arquivo .env
```
TOKEN=paste your key here
```
Instale as dependências do projeto
```
pip install -r requirements.txt
```
Execute o projeto
```
python .
```
