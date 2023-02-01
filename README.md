<p align="center">
  <img src="./templates/static/autenticacao/img/logo.png" alt="Logo" width="300"/>
  <br>
</p>
<h3 align="center">
Seu novo lar está aqui!
</h3>

<p align="center">
  <img src="https://img.shields.io/static/v1?label=pythonando&message=imobi&color=blueviolet&style=for-the-badge"/>
  <img src="https://img.shields.io/github/license/MrRioja/pythonando-imobi?color=blueviolet&logo=License&style=for-the-badge"/>
  <img alt="GitHub top language" src="https://img.shields.io/github/languages/top/MrRioja/pythonando-imobi?color=blueviolet&logo=Python&logoColor=white&style=for-the-badge">
  <img alt="GitHub last commit" src="https://img.shields.io/github/last-commit/MrRioja/pythonando-imobi?color=blueviolet&style=for-the-badge">
</p>

<p align="center">
  <a href="#sobre">Sobre</a> •
  <a href="#imobi">Imobi</a> •
  <a href="#instalação">Instalação</a> •
  <a href="#tecnologias">Tecnologias</a> •
  <a href="#autor">Autor</a>  
</p>

## Sobre

Projeto desenvolvido durante a Pystack week 2.0 cujo objetivo foi criar uma aplicação com o framework Django.

## Imobi

O Imobi é uma aplicação imobiliária cujo objetivo é dar visibilidade para imoveis à venda e proporcionar um ambiente centralizado para interessados realizarem agendamentos de visitas aos imoveis.

Ao acessar a aplicação pela primeira vez o usuário deve realizar seu cadastro através da tela abaixo:

![Tela de cadastro](.github/cadastro.png)

Feito isso, basta realizar o login na plataforma para acessar os detalhes dos imoveis cadastrados. Ao criar a conta o usuário será direcionado para a tela de login automaticamente, aonde deverá informar seus dados de acesso, caso alguma informação esteja incorreta o formulário irá dar o feedback para o usuário conforme mostrado abaixo:

|            Tela de login            |     Tela de login - Preenchimento incorreto      |
| :---------------------------------: | :----------------------------------------------: |
| ![Tela de login](.github/login.png) | ![Tela de login - erro](.github/login-error.png) |

Após o login com os dados correto, o usuário terá acesso a homepage da aplicação, aonde inicialmente serão exibidos os imoveis disponíveis e uma opção para filtrar os resultados, conforme imagem a seguir:

![Home](.github/home.png)

Modal de filtros disponível na homepage:

![Home](.github/modal-filtros.png)

Ao clicar em um imóvel de interesse, os seus detalhes serão exibidos na tela abaixo, tais como: imagens, descrição e endereço, assim como um botão para realizar o agendamento de uma visita e imoveis semelhantes ao visualizado.

![Detalhes do imóvel](.github/imovel-detalhes.png)

Ao clicar no botão `Agendar visita` presente na pagina de detalhes do imóvel, o modal de agendamentos será aberto para o usuário escolher a data e horário de sua preferencia:

![Modal de agendamento](.github/modal-appointment.png)

Após concluir o agendamento (também acessível através do link `Agendamentos` presente no header da página) o usuário poderá ver seus agendamentos cadastrados e seus respectivos status, como exemplificado abaixo:

- **Agendamento Concluído**: Representa um agendamento realizado com sucesso.

![Agendamento concluído](.github/agendamentos-agendado.png)

- **Agendamento Finalizado**: Representa um agendamento cujo a visita já ocorreu.

![Agendamento finalizado](.github/agendamento-finalizado.png)

- **Agendamento Cancelado**: Representa um agendamento cancelado pelo usuário.

![Agendamento cancelado](.github/agendamentos-cancelado.png)

Com isso concluo a explicação sobre o projeto. Por razões de demonstração, deixo abaixo um GIF aonde navegado pelas interfaces explicadas acima e passo por todos os fluxos do app:

![Demonstração](.github/demo.gif)

## Instalação

Antes de começar, você vai precisar ter instalado em sua máquina as seguintes ferramentas:
[Git](https://git-scm.com), [Python](https://www.python.org/). Além disso é bom ter um editor para trabalhar com o código como [VSCode](https://code.visualstudio.com/).

### 🖥 Rodando o projeto

```bash
# Clone este repositório
$ git clone git@github.com:MrRioja/pythonando-imobi.git

# Acesse a pasta do projeto no terminal/cmd
$ cd pythonando-imobi

# Ative o ambiente virtual
$ source venv/bin/activate

# Execute a aplicação em modo de desenvolvimento
$ python3 manage.py runserver

# O servidor iniciará na porta 8000 - acesse <http://localhost:8000>
```

## Tecnologias

<img align="left" src="https://logos-world.net/wp-content/uploads/2021/10/Python-Symbol.png" alt="Python" height="75" />

<img align="left" src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTe_MTqBgu6g6VEe39__JSrc6j7i5JDspsxVH8rAU-9680X8zadKKWvjY6s2MT9cpomB2c&usqp=CAU" alt="Django" height="75"/>

<br><br><br>

## Autor

<div align="center">
<img src="https://images.weserv.nl/?url=avatars.githubusercontent.com/u/55336456?v=4&h=100&w=100&fit=cover&mask=circle&maxage=7d" />
<h1>Luiz Rioja</h1>
<strong>Backend Developer</strong>
<br/>
<br/>

<a href="https://linkedin.com/in/luizrioja" target="_blank">
<img alt="LinkedIn" src="https://img.shields.io/badge/linkedin-%230077B5.svg?style=for-the-badge&logo=linkedin&logoColor=white"/>
</a>

<a href="https://github.com/mrrioja" target="_blank">
<img alt="GitHub" src="https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white"/>
</a>

<a href="mailto:lulyrioja@gmail.com?subject=Fala%20Dev" target="_blank">
<img alt="Gmail" src="https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white" />
</a>

<a href="https://api.whatsapp.com/send?phone=5511933572652" target="_blank">
<img alt="WhatsApp" src="https://img.shields.io/badge/WhatsApp-25D366?style=for-the-badge&logo=whatsapp&logoColor=white"/>
</a>

<a href="https://join.skype.com/invite/tvBbOq03j5Uu" target="_blank">
<img alt="Skype" src="https://img.shields.io/badge/SKYPE-%2300AFF0.svg?style=for-the-badge&logo=Skype&logoColor=white"/>
</a>

<br/>
<br/>
</div>
