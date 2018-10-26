# TCC Inatel 2018: SSR vs CSR
Este repositório contém o script de autamatização usado para extrair as métricas dos sites.

# Branchs
- lighthouse: Contém o código principal para uso no TCC.

# Configurar ambiente
- Instalar o [Python2](https://www.python.org/downloads/release/python-2715/), versão mais recente.
- Instalar o [Node](https://nodejs.org/en/download/) no PC, versão mais recente.
- Executar no bash: pip install numpy && pip install scipy
- Executar no bash: npm install lighthouse -g

# Executar script
Para rodar o projeto, basta executar o script lighthouse.py informando a quantidade de iterações desejada.

    pyhton lighthouse.py 1000
Executa 1000 vezes

    python lighthouse.py
Executa a mesma quantidade de vezes definida no arquivo constants.py

# Adicionar URLs para teste
Dentro do arquivo constants.py:
- Adicionar a URL desejada na lista URLS
- Adicionar um nome para o resulta na listas NAMES
***(Manter a URL e o nome na mesma ordem/posição nas duas listas)***
