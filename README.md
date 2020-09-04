# Boas vindas ao repositório do projeto de Algorithms!

Você já usa o GitHub diariamente para desenvolver os exercícios, certo? Agora, para desenvolver os projetos, você deverá seguir as instruções a seguir. Fique atento a cada passo, e se tiver qualquer dúvida, nos envie por _Slack_! #vqv 🚀

Aqui você vai encontrar os detalhes de como estruturar o desenvolvimento do seu projeto a partir desse repositório, utilizando uma branch específica e um _Pull Request_ para colocar seus códigos.

---

## Instruções para entregar seu projeto:

### ANTES DE COMEÇAR A DESENVOLVER:

1. Clone o repositório

- `git clone git@github.com:tryber/sd-0x-algorithms.git`.
- Entre na pasta do repositório que você acabou de clonar:
  - `sd-0x-algorithms`

2. Crie o ambiente virtual para o projeto

- `python3 -m venv .venv && source .venv/bin/activate`

3. Crie uma branch a partir da branch `master`

- Verifique que você está na branch `master`
  - Exemplo: `git branch`
- Se não estiver, mude para a branch `master`
  - Exemplo: `git checkout master`
- Agora crie uma branch à qual você vai submeter os `commits` do seu projeto
  - Você deve criar uma branch no seguinte formato: `nome-github-nome-do-projeto`
  - Exemplo: `git checkout -b exemplo-algorithms`

4. Adicione as mudanças ao _stage_ do Git e faça um `commit`

- Verifique que as mudanças ainda não estão no _stage_
  - Exemplo: `git status` (deve aparecer listada a pasta _exemplo_ em vermelho)
- Adicione o novo arquivo ao _stage_ do Git
  - Exemplo:
    - `git add .` (adicionando todas as mudanças - _que estavam em vermelho_ - ao stage do Git)
    - `git status` (deve aparecer listado o arquivo _exemplo/README.md_ em verde)
- Faça o `commit` inicial
  - Exemplo:
    - `git commit -m 'iniciando o projeto algorithms'` (fazendo o primeiro commit)
    - `git status` (deve aparecer uma mensagem tipo _nothing to commit_ )

5. Adicione a sua branch com o novo `commit` ao repositório remoto

- Usando o exemplo anterior: `git push -u origin exemplo-project-name`

6. Crie um novo `Pull Request` _(PR)_

- Vá até a página de _Pull Requests_ do [repositório no GitHub](https://github.com/tryber/sd-0x-algorithms/pulls)
- Clique no botão verde _"New pull request"_
- Clique na caixa de seleção _"Compare"_ e escolha a sua branch **com atenção**
- Clique no botão verde _"Create pull request"_
- Adicione uma descrição para o _Pull Request_ e clique no botão verde _"Create pull request"_
- **Não se preocupe em preencher mais nada por enquanto!**
- Volte até a [página de _Pull Requests_ do repositório](https://github.com/tryber/sd-0x-algorithms/pulls) e confira que o seu _Pull Request_ está criado

---

## Entregáveis

Para entregar o seu projeto você deverá criar um _Pull Request_ neste repositório. Este _Pull Request_ deverá conter os arquivos `...`, que conterão seu código `Python` e seus testes, respectivamente.

<!-- DEFINIR O NOME DOS ARQUIVOS -->

### ⚠️ É importante que seus arquivos tenham exatamente estes nomes! ⚠️

Você pode adicionar outros arquivos se julgar necessário. Qualquer dúvida, procure a monitoria.

Lembre-se que você pode consultar nosso conteúdo sobre [Git & GitHub](https://course.betrybe.com/intro/git/) sempre que precisar!

---

## O que deverá ser desenvolvido

Para fixar os conteúdos de algoritmos e estrutura de dados vistos até agora, você fará um projeto que tem como principal objetivo resolver problemas e otimizar algoritmos que fazem parte do cotidiano de uma pessoa desenvolvedora de software.

Pessoas desenvolvedoras de software, além de serem muito boas em implementações, devem, também, ser boas resolvendo problemas e otimizando algoritmos. No projeto de hoje, vamos treinar, ainda mais, a sua capacidade de resolução de problemas e otimização de código, que envolve algumas habilidades:

  - Lógica;

  - Capacidade de interpretação do problema;

  - Capacidade de interpretação de um código legado;

  - Capacidade de resolução do problema, de forma otimizada;

  - Resolver o problemas/Otimizar algoritmos mesmo sob pressão.

Tendo essas habilidades descritas acima, junto com algumas outras, farão de você uma pessoa desenvolvedora que terá muita facilidade em diversas situações problemáticas do dia-a-dia.

---

## Desenvolvimento e testes

Este repositório está dividido em duas pastas, `challenges` e `tests`. A pasta `challenges` contém todos os arquivos que você utilizá nesse projeto.

Cada arquivo `.py`, dentro da pasta `challenges`, representa um requisito. Ou seja, os arquivos não tem ligação uns com os outros. Logo, os problemas devem ser resolvidos de forma separada.

A pasta `tests` segue a mesma ideia da pasta `challenges`, contendo um arquivo de teste para cada requisito do projeto.

Este repositório já contém um _template_ com a estrutura de diretórios e arquivos, tanto de código quanto de teste criados. Veja abaixo:

```md
.
├── challenges
│   ├── challenge_
│   └── challenge_
├── tests
│   ├── test_
│   └── test_
├── README.md
├── requirements.txt
└── setup.cfg
```

Apesar do projeto já possuir uma estrutura base, você quem deve implementar tanto as funções quanto os testes. Novos arquivos podem ser criados conforme a necessidade.

Para executar os testes, lembre-se de primeiro **criar e ativar o ambiente virtual**, além de também instalar as dependências do projeto. Isso pode ser feito através dos comandos:

```bash
$ python3 -m venv .venv

$ source .venv/bin/activate

$ python3 -m pip install -r requirements.txt
```

O arquivo `requirements.txt` contém todos as dependências que serão utilizadas no projeto, ele está agindo como se fosse um `package.json` de um projeto `Node.js`. Com as dependências já instaladas, para executar os testes basta usar o comando:

```bash
$ python3 -m pytest
```

Se quiser saber mais sobre a instalação de dependências com `pip`, veja esse artigo: https://medium.com/python-pandemonium/better-python-dependency-and-package-management-b5d8ea29dff1

Para verificar se você está seguindo o guia de estilo do Python corretamente, execute o comando:

```bash
$ python3 -m flake8
```

Para executar cada arquivo separadamente, execute o comando:

```bash
$ python3 -m nome_do_arquivo.py
```

---

## Requisitos obrigatórios:



---

### DURANTE O DESENVOLVIMENTO

- Faça `commits` das alterações que você fizer no código regularmente

- Lembre-se de sempre após um (ou alguns) `commits` atualizar o repositório remoto

- Os comandos que você utilizará com mais frequência são:
  1. `git status` _(para verificar o que está em vermelho - fora do stage - e o que está em verde - no stage)_
  2. `git add` _(para adicionar arquivos ao stage do Git)_
  3. `git commit` _(para criar um commit com os arquivos que estão no stage do Git)_
  4. `git push -u nome-da-branch` _(para enviar o commit para o repositório remoto na primeira vez que fizer o `push` de uma nova branch)_
  5. `git push` _(para enviar o commit para o repositório remoto após o passo anterior)_

---

### DEPOIS DE TERMINAR O DESENVOLVIMENTO (OPCIONAL)

Para sinalizar que o seu projeto está pronto para o _"Code Review"_ dos seus colegas, faça o seguinte:

- Vá até a página **DO SEU** _Pull Request_, adicione a label de _"code-review"_ e marque seus colegas:

  - No menu à direita, clique no _link_ **"Labels"** e escolha a _label_ **code-review**;

  - No menu à direita, clique no _link_ **"Assignees"** e escolha **o seu usuário**;

  - No menu à direita, clique no _link_ **"Reviewers"** e digite `students`, selecione o time `tryber/students-sd-0x`.

Caso tenha alguma dúvida, [aqui tem um video explicativo](https://vimeo.com/362189205).

---

### REVISANDO UM PULL REQUEST

Use o conteúdo sobre [Code Review](https://course.betrybe.com/real-life-engineer/code-review/) para te ajudar a revisar os _Pull Requests_.

#VQV 🚀
