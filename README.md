<h1 align="center">Grafico</h1>
<p align="center">
<a href="https://pypi.org/project/Grafico/">Pacote para gerar gráficos simples.</a>
</p>

<b>Objetivo: </b>O objetivo é aprender sobre criação de pacotes em Python e publicação no <a href="https://pypi.org/project/Grafico/">PyPI</a>, por isso a ideia do pacote <b>Grafico</b> é uma coisa simples: gerar gráficos básicos.

<b>Instalação: </b><code>pip3 install Grafico</code><br>

<b>Uso: </b><br>
from grafico.main import Grafico<br>
gf = Grafico()<br>

gf.generate_chart(datas_x, datas_y, type_chart, view, label_x, label_y, title)

<br>
<b>datas_x = </b>obrigatoriamente recebe uma lista de valores para o eixo X.<br>
<b>datas_y = </b>obrigatoriamente recebe uma lista de valores para o eixo Y.<br>
<b>type_chart = </b>opcionalmente informa o tipo de gráfico. Por padrão será plot, mas também aceita bar ou scatter.<br>
<b>view = </b>opcionalmente informa se deseja abrir o gráfico quando for gerado. Por padrão é True, mas pode ser False. Caso seja False o gráfico seráarmazenado em imagem .PNG.<br>
<b>label_x = </b>opcionalmente informa um texto para o eixo X. Por padrão ele será vazio.<br>
<b>label_y = </b>opcionalmente informa um texto para o eixo Y. Por padrão ele será vazio.<br>
<b>title = </b>opcionalmente informa um título para o gráfico.<br>

<br>

<img src="https://github.com/guilhermedonizetti/Grafico/blob/main/image/grafico_1.png" width="400" height="230">&nbsp;&nbsp;<img src="https://github.com/guilhermedonizetti/Grafico/blob/main/image/grafico2.png" width="400" height="230">
