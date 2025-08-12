-----

## Salão de Beleza: Sistema de Gerenciamento de Agendamentos

Este projeto é um sistema de gerenciamento para salões de beleza, desenvolvido com Django. Ele foi projetado para atender às necessidades de negócio de um salão, incluindo o cadastro de clientes, serviços e profissionais, gestão de agendamentos e geração de relatórios de desempenho.

### 📋 **Pacotes e Ferramentas**

  * **Django**: `5.2.5`
  * **Python**: `3.11.9`
  * **pip**: `24.0`
  * **VSCode**: `1.103.0`
  * **Sistema Operacional**: Windows 11

### 📁 **Estrutura de Pastas e Funcionalidades**

O projeto é organizado na seguinte estrutura principal, com rotas (URLs) bem definidas para cada funcionalidade:

  * **`Salao`** (diretório principal)
      * **Home (`home/`)**: Página inicial com um menu de botões para navegação nas áreas de gerenciamento.
      * **Clientes (`clientes/`)**:
          * `clientes/cadastrar/`: Formulário para cadastro de novos clientes.
      * **Profissionais (`profissionais/`)**:
          * `profissionais/cadastrar/`: Formulário para cadastro de profissionais do salão.
      * **Serviços (`servicos/`)**:
          * `servicos/criar/`: Cadastro dos tipos de serviços oferecidos pelo salão.
          * `servicos/associar/`: Associa um profissional a um tipo de serviço, definindo o valor cobrado por ele.
      * **Agendamentos (`agendamentos/`)**:
          * `agendamentos/criar/`: Cria um novo agendamento para um cliente com um profissional.
          * `agendamentos/gerenciar/`: Permite a alteração do status de um agendamento (agendado, concluído, cancelado).
          * `agendamentos/relatorio/concluidos/`: Gera um relatório de serviços concluídos em um período específico.
      * **`templates/base/base.html`**: O layout principal do site, utilizando **Bootstrap** e CSS para estilização.

-----

### ⚙️ **Regras de Negócio Implementadas**

Para garantir a integridade e a correta operação do sistema, as seguintes regras foram implementadas:

  * **Restrições de Cadastro**: Não é permitido cadastrar um cliente ou profissional com o mesmo **CPF**.
  * **Validação de Agendamento**:
      * A data do agendamento não pode ser anterior à data atual.
      * A hora de término do agendamento deve ser posterior à hora de início.
      * Um agendamento não pode ser criado se o profissional já tiver um compromisso para a mesma data e horário.
      * Agendamentos com status 'cancelado' são excluídos da verificação de conflitos de horário.
  * **Gerenciamento de Serviços**: A associação entre profissionais e serviços é flexível. Um profissional pode realizar múltiplos serviços, e o valor cobrado pode variar entre profissionais para o mesmo serviço, simulando a tabela de preços de um salão.
  * **Status de Agendamento**: Um agendamento pode ter um dos seguintes status: **agendado**, **concluido** ou **cancelado**.
  * **Otimização de Consultas**: Para garantir a performance, as consultas ao banco de dados para a validação de regras de negócio são otimizadas utilizando o método `filter` do Django.

-----

### 🏛️ **Modelo de Entidades**

O banco de dados é estruturado com as seguintes entidades:

  * **`Cliente`**: `id`, `nome`, `cpf`, `data_de_nascimento`, `telefone`, `email`
  * **`Profissional`**: `id`, `nome`, `cpf`, `data_de_nascimento`, `telefone`, `email`
  * **`Servico`**: `id`, `descricao`
  * **`ProfissionalServico`**: `id`, `valor`, `profissional_id`, `servico_id` (Tabela de relacionamento entre profissionais e serviços)
  * **`Agendamento`**: `id`, `data_de_agendamento`, `hora_inicio`, `hora_fim`, `status`, `cliente_id`, `profissional_servico_id` (Tabela de relacionamento entre clientes e a relação `ProfissionalServico`)

-----

### 🚀 **Como Rodar o Projeto**

Siga os passos abaixo para executar o projeto em sua máquina local:

1.  Verifique a versão do Python instalada:

    ```bash
    python --version
    ```

2.  Crie um ambiente virtual para o projeto:

    ```bash
    python -m venv venv
    ```

3.  Ative o ambiente virtual:

    ```bash
    source venv/Scripts/Activate
    ```

4.  Instale o Django e as dependências necessárias:

    ```bash
    pip install django
    ```

5.  Execute as migrações para criar o banco de dados:

    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

6.  Inicie o servidor de desenvolvimento:

    ```bash
    python manage.py runserver
    ```

    O sistema estará acessível em `http://127.0.0.1:8000/`.