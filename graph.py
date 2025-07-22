#unit-5 [overview of data scinence]

#visulising the data
#bar graph:-
# import pandas as pd 
# import matplotlib.pyplot as plt 
# df=pd.read_excel('pop.xlsx')
# print(df)

# x=df['year']
# y=df['Population']
# plt.bar(x,y)
# plt.xlabel=('Year')
# plt.ylabel=('Population')
# plt.title('Population in billion')
# plt.legend()
# plt.show()

#pie chart:-
# import matplotlib.pyplot as plt 
# sales_perc=[15,20,25,30,10]
# prod=['pencil','eraser','sharpner','scale','pen']
# col=['blue','green','red','yellow','pink']
# plt.pie(sales_perc,lables=prod,colors=col)
# plt.title('scales of product in percentage')
# plt.legend()
# plt.show()

#line chart

# import matplotlib.pyplot as plt 
# years=['2020','2021','2022','2023','2024']
# incr_pop_ind=[10,15,11,19,25]
# incr_pop_chin=[9,12,8,21,15]
# plt.plot(years,incr_pop_ind,color='red')
# plt.plot(years,incr_pop_chin,color='blue')
# plt.title('population growth of india')
# plt.xlabel('years')
# plt.ylabel('increase of population in lakhs')
# plt.show()

#scatter plot

# import matplotlib.pyplot as plt
# x=[2,9,7,6,3,4,8,10]
# y=[8,2,4,9,6,3,2,5]
# plt.scatter(x,y)
# plt.xlabel('x-axis')
# plt.ylabel('y-axis')
# plt.title('scatter diagram')
# plt.show()

#area plot

import matplotlib.pyplot as plt
import numpy as np
x=range(1,6)
y=[1,4,6,2,4]
plt.fill_between(x,y)
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('area plot')
plt.show()

