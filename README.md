# Automação de Envio de Email com Análise de Ações

Este projeto é um script em Python que utiliza várias bibliotecas para buscar dados históricos de uma ação específica, realizar análises e enviar os resultados por email usando automação.

## Contexto

Este script permite ao usuário digitar o código de uma ação desejada, obter dados históricos dessa ação, calcular valores de fechamento máximo, mínimo e médio, e enviar esses dados por email. Ele usa as bibliotecas `yfinance` para buscar dados de ações, `pyautogui` e `pyperclip` para automação do navegador e envio de email, e `webbrowser` para abrir o Gmail.

## Configuração

Para configurar o ambiente para executar este script, siga os seguintes passos:

1. **Instale o Python**: Certifique-se de ter o Python instalado em sua máquina. Você pode baixá-lo em [python.org](https://www.python.org/).

2. **Clone o repositório**:
    ```bash
    git clone https://github.com/leopxz/automacao_de_email.git
    cd automacao_de_email
    ```

3. **Instale as bibliotecas necessárias**:
    ```bash
    pip install yfinance pyautogui pyperclip
    ```
    
4. **Configuração do Gmail**: Certifique-se de estar logado na sua conta do Gmail e, se necessário, permita o acesso a aplicativos menos seguros ou configure uma senha de aplicativo para permitir o envio de emails via automação.

## Execução

Para executar o script, siga os passos abaixo:

1. **Execute o script**:
    ```bash
    python bolsa_de_valores.py
    ```
    OU SE preferir, clique com o botão direito do mouse no código e clique em RUN PYTHON > RUN PYTHON FILE in TERMINAL

2. **Digite o código da ação** quando solicitado.

O script irá abrir o navegador, acessar o Gmail, compor um email com as análises da ação e enviá-lo automaticamente.

## Estrutura

A estrutura do projeto é simples e consiste em um único arquivo de script:

automacao_de_email/<br>
│<br>
├── README.md --> Este arquivo, que fornece informações sobre o projeto e instruções de configuração e execução.<br>
├── bolsa_de_valores.py --> Contém o código principal que realiza a busca de dados da ação, análise e envio de email.<br>
└── cod_no_jupter.ipynb --> Contém a estrutura do projeto de forma organizada antes de passar o codigo para o arquivo .py<br>

## Contribuição

Se você deseja contribuir para este projeto, siga estas etapas:

1. Faça um fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Empurre para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

