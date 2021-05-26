import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

plt.style.use('fivethirtyeight')

# for interactive visualizations
import plotly.offline as py
from plotly.offline import init_notebook_mode, iplot
import plotly.graph_objs as go
from plotly import tools
init_notebook_mode(connected = True)
import plotly.figure_factory as ff

df = pd.read_csv("Data.csv")
plt.rcParams['figure.figsize'] = (20, 10)
sns.heatmap(df.corr(),annot = True, cmap= 'coolwarm')
plt.title('Heatmap for the Data', fontsize = 20)
plt.show()
plt.savefig('correlation.png')