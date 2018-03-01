# Player-python

Código de player de video em Python, onde reproduz todos os videos presente em uma pasta especifica automaticamente. Pode ser usado no Raspberry pi. 

Este projeto foi utilizado para criação de um player para empresa Inter Construtora, para que os funcionário possam enviar video pelo Google Drive e automaticamente o código python presente no Raspberry pi execute os videos presente na pasta do drive, controlando o que é exibido pela TV/Monitor instalado em qualquer local.

Para isso foi usado o drive OverDrive para linux, que faz acesso ao Google Drive importando e exportando arquivos. 

Foi também utilizado o TeamViwer para que possamos fazer manutenção, a distância do raspberry pi.

Foi colocado também para que o raspberry execute o script `player3.py` ao inicializar, para que caso ocorrar alguma falta de energia durante o funcionamento do sistema, o video video execute automaticamente sem a necessidade de interferência externa.

Abaixo algumas instruções de como colocar o sistema em prática.

# Requisitos 

#### Instalar biblioteca omxplayer para python:


> % pip install omxplayer-wrapper  

#### Irá precisar também da biblioteca pathlib

> pip install pathlib

Existem outras biblioteca utilizadas no código, porém na maioriadas vezes já vem instalado como padrão.
Caso de erros de importação de modulo, baixem todas as biblioteca usadas.

Nesse 

###### continua...
