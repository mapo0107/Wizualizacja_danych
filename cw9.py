import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
############################################################################################
s = pd.Series(np.random.randn(1000), index=pd.date_range('01/01/2015', periods=1000))
s = s.cumsum()
line_plot = sns.relplot(kind='line', data=s)
line_plot.fig.set_size_inches(6, 6)
line_plot.fig.autofmt_xdate()
line_plot.set_xlabels('daty')
line_plot.set_ylabels('wartości')
plt.show()

############################################################################################
dane = {'wartosci' : np.random.randn(1000),
        'daty' : pd.date_range('01/01/2015', periods=1000)}
df = pd.DataFrame(dane)
df.wartosci = df.wartosci.cumsum()

line_plot = sns.relplot(x='daty', y='wartosci', kind='line', data=df)
line_plot.fig.set_size_inches(6, 6)
line_plot.fig.autofmt_xdate()
plt.show()
############################################################################################
data = {'a': np.arange(50),
        'c': np.random.randint(0, 50, 50),
        'd': np.random.randn(50)}
data['b'] = data['a'] +10 * np.random.randn(50)
data['d'] = np.abs(data['d']) * 100
df = pd.DataFrame(data)

plot = sns.relplot(data=df, x='a', y='b', hue='c', size='d',
                   palette='bright', legend=False)
plot.fig.set_size_inches(6, 6)
plt.show()
############################################################################################
data = {'Kraj':['Belgia', 'Indei', 'Brazylia', 'Polska'],
        'Stolica':['Bruksela', 'New Dehli', 'Brasilia', 'Warszawa'],
        'Kontynent':['Europa', 'Azja', 'Ameryka Południowa', 'Europa'],
        'Populacja':[1232324567, 6543232321, 53646756323, 647565453]}
df = pd.DataFrame(data)
plot = sns.catplot(kind='bar', data=df, x='Kontynent', y='Populacja', hue='Kontynent', dodge=False, ci=None)
plot.fig.set_size_inches(7, 6)
plot.set(title='Wykres słupkowy', ylim=(0, 140000000000))
plt.legend(loc='upper right', title='Populacja na kontynecncie')
plt.show()
############################################################################################
a = np.random.randn(10000)
histogram = sns.histplot(data=a, bins=50, color='g', stat='probability', alpha=0.75, kde=True, line_kws={'linewidth':4})
histogram.set(xlabel='x', ylabel='Prawdopodobienstow', title='Histogram')
plt.show()