"""This module refers to the code responsible for calling the functions and generating the graph."""

from .functions import Graphical

class Grafico(Graphical):

    def __init__(self):
        pass

    def generate_chart(self, datas_x, datas_y, type_chart='plot', view=True, label_x=None, label_y=None, title=None):
        """Method to generate the graph.
        Mandatory parameters: x-dates, y-dates.
        To change the chart format, in type_chart enter:
        plot, scatter or bar.
        Enter False in view= for the graph not to be displayed but saved."""

        Graphical.chech_regularity(datas_x, datas_y)
        datas = [datas_x, datas_y, type_chart, view, label_x, label_y, title]
        self.criar(datas)
        
    def criar(self, datas):
        Graphical.create_chart(datas)