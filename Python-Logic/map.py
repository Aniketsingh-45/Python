from matplotlib.lines import lineStyles
plt.plot(batsman['index'],batsman['V Kohli'],color="#00FF00", linestyle=':', linewidth=3, marker="o", markersize=5, label='virat')
plt.plot(batsman['index'],batsman['RG Sharma'],color='#00FFFF', linestyle='dashdot', linewidth=2, marker="*", label='Rohit')

plt.title('Rohit Sharma vs Virat Kohli') #give the title
plt.xlabel('season') #xlabel use for x axis label
plt.ylabel('Runs scored')
plt.legend(['Virat Kohli','Rohit Sharma'],loc=9)#LOC USE FOR LOCATION OF THE LEGEND 
plt.grid()
plt.show() #for showing the graph you have to use show function 