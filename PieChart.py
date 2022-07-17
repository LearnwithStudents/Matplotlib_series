import matplotlib.pyplot as plt

plt.style.use('seaborn')

plt.title('Student Details', fontdict={'size': 30}, pad=30)

# student Details
marks = [70, 66, 10]
corresponding_Subject_names = ['physics', 'Maths', 'Biology']

colors = ['#CAF0F6', '#EDFFEF', '#FDF1CA']

# for highlighting particular individual data and in this we are highlighting "biology"
explode = [0.0, 0.0, 0.3] # These values are corresponding to the marks list i.e 0.0==70, 0.0==66, 0.3==10

# plotting pie
plt.pie(marks, labels=corresponding_Subject_names, colors=colors, wedgeprops={'edgecolor': 'black',
       'linewidth': 2}, startangle=67, explode=explode)

plt.show()
