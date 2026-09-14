# 🦸‍♂️ HeroManager

Sistema web para gerenciamento de heróis, desenvolvido em **Python com Flask e MySQL**, permitindo ao usuário consultar heróis, visualizar seus atributos e montar uma equipe de até 5 personagens. Projeto desenvolvido para a disciplina de **Programação II**, do **3º ano do Ensino Médio Integrado**.

📅 **Desenvolvido em:** Novembro de 2025

---

## 🚀 Sobre o projeto

O **HeroManager** é um projeto acadêmico desenvolvido para a disciplina de **Programação II**, com o objetivo de aplicar, na prática, conceitos de desenvolvimento de sistemas web, programação em Python, integração com banco de dados e organização de aplicações.

A proposta do sistema é permitir que o usuário gerencie um grupo de heróis com diferentes classes, níveis e atributos. Cada usuário pode possuir até **5 heróis em sua equipe**, enquanto os demais personagens ficam armazenados em uma **base**.

O sistema permite consultar os heróis disponíveis, visualizar seus detalhes, criar uma conta, realizar login, editar informações do perfil e organizar sua equipe.

A proposta do projeto segue os requisitos definidos na atividade acadêmica, que prevê um sistema de gerenciamento de heróis com cadastro e login, consulta de personagens e gerenciamento de uma equipe limitada a cinco integrantes.

---

## 💼 Competências demonstradas

* Aplicação de conceitos de **Programação Orientada a Objetos (POO)**
* Desenvolvimento de aplicações web com **Python e Flask**
* Integração de aplicações Python com **MySQL**
* Implementação de operações de **cadastro, consulta, atualização e exclusão (CRUD)**
* Modelagem e relacionamento entre diferentes entidades do sistema
* Organização de projetos web com **templates, arquivos estáticos e banco de dados**
* Desenvolvimento colaborativo em dupla, com utilização de ferramentas de apoio, **materiais e modelos apresentados pelo professor em aula**, além de ferramentas de **Inteligência Artificial** no auxílio à resolução de problemas e dúvidas

---

## ⚙️ Funcionalidades

### 👤 Cadastro e Login

* Cadastro de usuário.
* Registro de nome, e-mail, CPF, senha e planeta.
* Autenticação por meio de e-mail e senha.
* Senhas armazenadas utilizando hash.
* Sistema de sessão para usuários autenticados.

### 🧑‍🚀 Perfil

* Visualização dos dados do usuário.
* Exibição do nome, e-mail, CPF e planeta.
* Edição das informações pessoais.
* Upload de foto de perfil.
* Visualização dos heróis pertencentes à equipe.

### 🦸 Consulta de Heróis

* Listagem dos heróis cadastrados.
* Busca de heróis por **nome ou ID**.
* Visualização dos detalhes de cada personagem.
* Exibição de informações como:

  * Nome;
  * Classe;
  * Nível;
  * Habilidades;
  * Força;
  * Defesa;
  * Velocidade;
  * Descrição;
  * Imagem.

### 🛡️ Gerenciamento da Equipe

* Adição de heróis à equipe.
* Limite de **5 heróis ativos**.
* Heróis adicionados após o limite são enviados para a base.
* Visualização da equipe atual.
* Visualização dos heróis armazenados na base.
* Troca de heróis entre equipe e base.
* Remoção de heróis.

---

## 🧱 Estrutura do projeto

```text
HeroManager/
│
├── app.py
├── config.py
├── models.py
├── README.md
│
├── sql/
│   └── heromanager.sql
│
├── static/
│   ├── css/
│   │   └── style.css
│   │
│   └── img/
│       ├── herois/
│       └── usuarios/
│
├── templates/
│   ├── base.html
│   ├── base_herois.html
│   ├── cadastro.html
│   ├── equipe.html
│   ├── herois.html
│   ├── heroi_detalhes.html
│   ├── home.html
│   ├── login.html
│   ├── perfil.html
│   └── resultados.html
│
└── docs/
    └── Roteiro-de-desenvolvimento.pdf
```

---

## 🗄️ Banco de dados

O projeto utiliza o **MySQL** para armazenar os dados da aplicação.

O banco de dados possui as seguintes tabelas principais:

* `usuario` — armazena os dados dos usuários.
* `classe` — armazena as classes disponíveis para os heróis.
* `heroi` — armazena os dados e atributos dos personagens.
* `usuario_heroi` — realiza o relacionamento entre usuários e heróis, indicando se o personagem está na equipe ou na base.

O projeto também possui dados iniciais cadastrados, incluindo **30 heróis** distribuídos entre diferentes classes.

---

## ▶️ Como executar o projeto

### 🔹 Passo a passo

### 1. Baixar o projeto

Baixe ou clone o repositório do projeto.

### 2. Abrir no VS Code

Abra a pasta do projeto no **Visual Studio Code**.

### 3. Configurar o XAMPP

Abra o **XAMPP Control Panel** e inicie:

* Apache
* MySQL

### 4. Criar o banco de dados

No XAMPP, clique em **Admin** no módulo MySQL para abrir o phpMyAdmin.

Depois:

1. Acesse a opção **Importar**.
2. Selecione o arquivo:

```text
sql/heromanager.sql
```

3. Execute a importação.

O script cria o banco `heromanager`, suas tabelas, classes e os heróis iniciais.

### 5. Configurar a conexão com o banco

No arquivo `config.py`, verifique as informações da conexão:

```python
DB_CONFIG = {
    "host": "localhost",
    "user": "root",
    "password": "",
    "database": "heromanager"
}
```

Caso o MySQL esteja configurado com uma senha para o usuário `root`, altere o campo `password`.

### 6. Instalar as dependências

No terminal do VS Code, execute:

```bash
pip install flask
pip install mysql-connector-python
pip install werkzeug
```

### 7. Executar o sistema

Dentro da pasta que contém o arquivo `app.py`, execute:

```bash
python app.py
```

Depois, acesse no navegador o endereço exibido pelo Flask, normalmente:

```text
http://127.0.0.1:5000
```

---

## 📄 Contexto acadêmico, Regras de Negócio e Documentação

O **HeroManager não é um projeto comercial**, sendo desenvolvido exclusivamente para fins **acadêmicos**, como parte das atividades da disciplina de **Programação II**, no ano de **2025**.

O sistema possui algumas regras de negócio importantes:

* Cada usuário pode possuir vários heróis.
* Apenas **5 heróis podem permanecer na equipe ativa**.
* Quando a equipe já possui 5 personagens, novos heróis são direcionados para a base.
* Um herói pode ser movimentado entre a equipe e a base.
* O usuário pode remover heróis de sua coleção.
* O sistema exige autenticação para acessar as funcionalidades relacionadas ao usuário.

O projeto foi desenvolvido com base em um roteiro acadêmico contendo as demais instruções, requisitos e critérios de avaliação, disponível em:

```text
docs/Roteiro-de-desenvolvimento.pdf
```

---

## 🤖 Uso de Inteligência Artificial

O desenvolvimento do projeto contou com a utilização de **ferramentas de Inteligência Artificial** como apoio durante o processo de desenvolvimento.

Essas ferramentas foram utilizadas principalmente para:

* Esclarecimento de dúvidas sobre programação.
* Auxílio na resolução de problemas.
* Apoio na identificação e correção de erros.
* Consulta de conceitos relacionados às tecnologias utilizadas no projeto.

---

## 👥 Autores

**Emily Luciani**
**Amanda Pazianoti Horst**

Projeto desenvolvido em dupla para a disciplina de **Programação II**, no ano de **2025**.

---

## 📄 Observação

Este projeto foi desenvolvido para fins **educacionais e acadêmicos**, não possuindo finalidade comercial.
