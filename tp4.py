# -*- coding: utf-8 -*-
"""
Created on Thu Nov  1 13:08:17 2018

@author: Imen
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#question1
vitesse1=[50,100,150,200,250,300]
temps1=[1,2,3,4,5,6]
graphique11,=plt.plot(temps1,vitesse1,'r--')
graphique1,=plt.plot(temps1,vitesse1,'r--', linewidth=10)

#question2
plt.xlabel('Temps')
plt.ylabel('Vitesse')
plt.title('Courbe représentative du vitesse en fonction du temps')
#question3
#plt.axis(([1,10,50,200]))
#question4
vitesse2= [50,100,150,200,250,300]
temps2= [2,3,7,8,9,10]
graphique22,=plt.plot(temps2,vitesse2,'b*')
graphique2,=plt.plot(temps2,vitesse2,'b*',linewidth=3)
vitesse3= [50,100,150,200,250,300]
temps3= [2,3,4,7,9,10]
graphique33,=plt.plot(temps3,vitesse3,'g+')
graphique3,=plt.plot(temps3,vitesse3,'g+', linewidth=5)
#question5
plt.subplot(211)
plt.text(9,250,'Vitesse moyenne')
plt.plot(temps3,vitesse3,'g+')
plt.plot(temps2,vitesse2,'b*')
plt.plot(temps1,vitesse1,'r--')
plt.legend((graphique11, graphique22, graphique33), ('Vitesse1', 'Vitesse2', 'Vitesse3'))
plt.subplot(212)
plt.plot(temps1,vitesse1,'r',linewidth=10)
plt.plot(temps3,vitesse3,'g',linewidth=5)
plt.plot(temps2,vitesse2,'b',linewidth=3)
plt.legend((graphique1, graphique2, graphique3), ('Vitesse1', 'Vitesse2', 'Vitesse3'))

Catégorie = ['Catégorie1', 'Catégorie2', 'Catégorie3', 'Catégorie4']
Nombre = [5000, 26000, 21400, 12000]
plt.pie(Nombre,explode=[0.1,0.1,0.1,0.1],labels=Catégorie)

#exercice2/partie1
Date=pd.date_range(start='1/1/2017',periods=1000)
Val=np.random.randn(1000)
Série1=pd.Series(Val,Date)

Cumule1=np.cumsum(Série1)
plt.plot(Date,Cumule1)
Cumule1.plot()

#partie2
Val2=np.random.randn(1000,4)
Df2=pd.DataFrame(Val2,columns=['A','B','C','D'])
Cumule2=np.cumsum(Df2)
plt.figure()
Cumule2.plot()
#partie3
Val3=np.random.randn(1000,2)
Df3=pd.DataFrame(Val3,columns=['B','C'])
Cumule3=np.cumsum(Df3)
plt.figure()
Cumule3.plot()
Df3['A'] = pd.Series(list(range(len(Df3))))

Cumule4=np.cumsum(Df3)
plt.figure()
Cumule4['B'].plot()
plt.figure()
Cumule4['C'].plot()
#partie4
Val4=np.random.randn(5,4)
Df4=pd.DataFrame(Val4,columns=['A','B','C','D'])
Cumule5=np.cumsum(Df4)
plt.figure()
Cumule5.plot.bar()
plt.figure()
Cumule5.diff().hist(alpha=0.5,bins=50)
#partie5
Val5=np.random.randn(100,4)
Df5=pd.DataFrame(Val5,columns=['A','B','C','D'])
Cumule6=np.cumsum(Df5)
g1,=plt.plot(Cumule6['A'],Cumule6['B'],'*',color='#00035b')
g2,=plt.plot(Cumule6['C'],Cumule6['D'],'+',color='darkgreen')
plt.legend([g1,g2],['Groupe1','Groupe2'])
plt.figure()
series = pd.Series(3 * np.random.rand(4), index=['a', 'b', 'c', 'd'], name='series')
series.plot.pie(figsize=(6, 6))

