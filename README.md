# Celebramos

## Descrição

**Celebramos** é uma plataforma web que facilita a criação e gerenciamento de listas de desejos para eventos especiais, como casamentos, festas de 15 anos, chás de bebê e formaturas. Oferece uma solução prática para anfitriões criarem listas personalizadas e permite que convidados acessem e contribuam de maneira organizada, evitando presentes duplicados.

## Funcionalidades

- Criação de listas de desejos personalizadas.
- Gerenciamento de convidados e confirmações.
- Reserva de presentes para evitar duplicações.
- Adição de itens de lojas e fontes externas.
- Notificações para anfitriões e convidados.

## Tecnologias Utilizadas

- Frontend: HTML, CSS, JavaScript (React ou Vue.js)
- Backend: Python (Django ou Flask)
- Banco de Dados: PostgreSQL ou MySQL
- Autenticação: JWT ou OAuth
- Deploy: Heroku ou AWS

## Como Executar o Projeto

### Pré-requisitos

- Python 3.x
- Node.js (para o frontend)
- PostgreSQL ou MySQL

### Instalação

1. Clone o repositório:
   ```bash
   git clone https://github.com/seuusuario/celebramos.git
   cd celebramos
   ```

2. Configure o ambiente virtual:

   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate  # Windows
   ```
   
3. Instale as dependências:

   ```bash
   pip install -r requirements.txt
    ```
   
4. Configure o banco de dados no arquivo de configurações.

5. Execute as migrações:

   ```bash
   python manage.py migrate
   ```
6. Inicie o servidor:

   ```bash
   python manage.py runserver
   ```

7. Acesse a aplicação em seu navegador: 
   ```bash
   http://127.0.0.1:8000
   ```