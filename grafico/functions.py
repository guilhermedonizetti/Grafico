"""This module refers to the code to help main.py"""

import matplotlib.pyplot as plt

class Graphical(Exception):

    def __init__(self):
        pass

    def create_chart(datas):
        """Method for creating the graphic image.
        The method expects only 1 parameter of type list.
        \nThis is the sequence of data within the list:
        \ndates[dates_x, dates_y, type_chart, view, label_x, label_y, title]
        \nThis string cannot be changed."""

        try:
            plt.xlabel(datas[4]) if datas[4]!=None else ""
            plt.ylabel(datas[5]) if datas[5]!=None else ""
            plt.title(datas[6]) if datas[6]!=None else ""

            if datas[2]=='scatter':
                plt.scatter(datas[0], datas[1])
            if datas[2]=='bar':
                plt.bar(datas[0], datas[1])
            if datas[2]=='plot':
                plt.plot(datas[0], datas[1])

            plt.show() if datas[3] else plt.savefig("Grafico.png")
        except:
            raise Graphical("Error: failed to creat chart image.")


    def chech_regularity(datas_x, datas_y):
        """Function to check the regularities of the parameters.
        \nThis returns nothing. If something goes wrong the program will get an exception."""
        
        if type(datas_x)==type(datas_y)==list:
            if len(datas_x)!=len(datas_y):
                raise Graphical("Lists must be the same size.")
        else:
            raise Graphical("Expected to receive list as parameter.")