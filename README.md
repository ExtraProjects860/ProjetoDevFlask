# ProjetoDevFlask

## Descrição

ProjetoDevFlask é um projeto de desenvolvimento para criação rápida de aplicações web utilizando o microframework Flask. Este projeto fornece uma estrutura básica para iniciar o desenvolvimento de aplicações web de forma eficiente e organizada.

## Tecnologias Utilizadas

- **Python**: Linguagem de programação principal.
- **Flask**: Microframework para desenvolvimento web.
- **Bootstrap**: Framework CSS para design responsivo.
- **SQLAlchemy**: ORM para integração com banco de dados SQL.
- **SQLite**: Banco de dados utilizado na aplicação.

### Dependências (requirements.txt)

  ```plaintext
  bcrypt==4.1.3
  blinker==1.8.2
  click==8.1.7
  colorama==0.4.6
  dnspython==2.3.0
  email_validator==2.1.1
  Flask==3.0.0
  Flask-Bcrypt==1.0.1
  Flask-Login==0.6.3
  Flask-SQLAlchemy==3.1.1
  Flask-WTF==1.2.1
  greenlet==3.0.3
  idna==3.7
  itsdangerous==2.2.0
  Jinja2==3.1.4
  MarkupSafe==2.1.5
  Pillow==10.0.0
  SQLAlchemy==2.0.30
  typing_extensions==4.12.2
  Werkzeug==3.0.3
  WTForms==3.1.2
  ```

## Instalação

1. **Clone o repositório:**

   ```bash
   git clone https://github.com/seu-usuario/ProjetoDevFlask.git
   cd ProjetoDevFlask
   ```

2. **Crie um ambiente virtual e ative-o:**

   ```bash
   python -m venv venv
   source venv/bin/activate  # No Windows, use `venv\Scripts\activate`
   ```

3. **Instale as dependências:**

   ```bash
   pip install -r requirements.txt
   ```

## Estrutura do projeto

  ```bash
  ProjetoDevFlask/
  │
  ├── comunidade/
  │   ├── __pycache__/
  │   ├── templates/
  │   │   ├── base.html
  │   │   ├── contato.html
  │   │   ├── criarpost.html
  │   │   ├── editarperfil.html
  │   │   ├── home.html
  │   │   ├── login.html
  │   │   ├── navbar.html
  │   │   ├── perfil.html
  │   │   ├── post.html
  │   │   ├── usuarios.html
  │   ├── static/
  │   │   ├── fotos_perfil/
  │   │   ├── main.css
  │   ├── __init__.py
  │   ├── forms.py
  │   ├── models.py
  │   ├── routes.py
  │   ├── create.py
  │   └── main.py
  ├── instance/
  │   ├── commandRequirements.txt
  │   ├── requirements.txt
  └── .venv/
  ```

## Funcionalidades
- **Autenticação de Usuário**: Registro, login e logout de usuários.
- **Gerenciamento de Postagens**: Criação, visualização, edição e exclusão de postagens.
- **Perfil de Usuário**: Visualização e edição de perfis de usuário.
- **Contato**: Página de contato.

## Licença
- Este projeto está licenciado sob a Licença MIT - veja o arquivo LICENSE para mais detalhes.
