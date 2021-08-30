# Graphic

The package applies for generating graphics that, although they are simple graphics, need many lines of code to be generated.
Licensed: free to use for any purpose, subject only to copyright conservation and license.

### Usage:

To include the package the command is:<br>
<code>from grafico.main import Grafico</code><br>
There is only 1 method to meet the need, the generate_chart method. This method has the following parameters:<br>

dates_x = Required. Receives a list of values ​​for the X axis of the graph.<br>
dates_y = Required. Receives a list of values ​​for the Y axis of the graph.<br>
type_chart = Optional. Receives the graph model, possible values ​​are bar, scatter and plot. If no value is entered, by default it will be plot.<br>
view = Optional. Receive True if you want the graph to be displayed when it has finished generating, and False if you want the graph to be saved locally as a .PNG file. If nothing is given, by default it will be True.<br>
label_x = Optional. Receives the text to be displayed on the X axis. If nothing is informed, it will be empty.<br>
label_y = Optional. Receives the text to be displayed on the Y axis. If nothing is informed, it will be empty.<br>
title = Optional. Receives a title for the chart. It is empty if nothing is informed.