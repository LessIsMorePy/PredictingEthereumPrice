# Modules
import glob
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

plt.style.use('ggplot')

class Price:

    def __init__(self):
        self.df = pd.read_csv(glob.glob("*.csv")[0])
        assert pd.notnull(self.df).all().all()

    def cleaning(self, array_type):
        '''
            Acording to investing.com data, array_type must be a string name like;
            'Apertura', 'Cierre', 'Máximo' and 'Mínimo'.

            :param array_type: 'Apertura', 'Cierre', 'Máximo' and 'Mínimo'
            :return: an array with data you chose.
        '''
        return np.array(self.df[array_type].apply(lambda x: float(x.replace(',', '').replace('.', '.'))))

    def opening(self):
        """
            Return an array with the opening price data
        """
        return self.cleaning('Apertura')

    def close(self):
        """
            Return an array with the close price data
        """
        try:
            return self.cleaning('Cierre')
        except:
            return self.cleaning('Último')

    def maximum(self):
        """
            Return an array with the maximum price data
        """
        return self.cleaning('Máximo')

    def minimum(self):
        """
            Return an array with the minimum price data
        """
        return self.cleaning('Mínimo')

    def date(self, kind='DataFrame'):
        """
        return  Data Frame or an array data

        :param kind: 'DataFrame' or 'array'
        :return:
        """
        """
        :param kind: 
        :return: 
        """
        if kind.lowe() == 'dataframe':
            return self.df['Fecha']
        elif kind.lower() == 'array':
            return np.array(self.df['Fecha'])
        else:
            print('kind must be equal to: "DataFrame" or "Array"')

    def plot(self):

        clean_data = lambda x: float(x.replace(',', '').replace('.', '.'))

        self.df['Apertura'].apply(clean_data).plot(color='red', label='Opening', alpha=0.4)
        self.df['Máximo'].apply(clean_data).plot(color='green', label='Maximum', ls=':')
        self.df['Mínimo'].apply(clean_data).plot(color='purple', label='Minimum', ls=':')
        self.df['Cierre'].apply(clean_data).plot(color='blue', label='Close', alpha=0.5)

        plt.legend()
        plt.title('Cryptocurrency price')
        plt.xlabel('Days number')
        plt.ylabel('USD price')
        plt.show()
