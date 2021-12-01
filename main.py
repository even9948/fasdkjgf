from numpy import empty
import plotly.figure_factory as ff 
import plotly.graph_objects as go
import random
import statistics
import pandas as pd
import csv

df = pd.read_csv("data.csv")
data = df["temp"].tolist()
#population_mean = statistics.mean(data)
population_std_deviation = statistics.stdev(data)
#print("Population mean: ", population_mean)
print("Std_deviation: ", population_std_deviation)

#fig = ff.create_distplot([data],["temp"],show_hist = False)
#fig.add_trace(go.Scatter(x=[population_mean,population_mean],y=[0,1],mode="lines",name="MEAN"))
#fig.show()

#dataset= []
#for i in range(0,100):
#    random_index = random.randint(0,len(data))
#    value = data[random_index]
#    dataset.append(value)
#mean = statistics.mean(dataset)
#std_deviation = statistics.stdev(dataset)

#print("Mean of sample: ",mean)
#print("Std deviation of sample: ", std_deviation)

##  code to find the mean of 100 data points 1000 times and plot it
#function to get the mean of the given data samples
# pass the number of data points you want  as counter
def random_set_of_mean(counter):
    dataset = []
    for i in range(0,counter):
        random_index = random.randint(0,len(data)-1)
        value = data[random_index]
        dataset.append(value)
    mean = statistics.mean(dataset)
    return mean

#function to plot the mean on the graph
def show_fig(mean_list):
    df=mean_list
    mean=statistics.mean(df)
    fig = ff.create_distplot([df],["temp"],show_hist = False)
    fig.show()

# Pass the number of time you want the mean of the data points as a parameter in range function in for loop
def setup():
    mean_list=[]
    for i in range(0,1000):
        set_of_means=random_set_of_mean(100)
        mean_list.append(set_of_means)
    show_fig(mean_list)

    mean=statistics.mean(mean_list)
    
    print("mean of sampling dis :", mean)

setup()

# code to find the standard deviation of the sample data
def standard_deviation():
    mean_list=[]
    for i in range(0,1000):
        set_of_means=random_set_of_mean(100)
        mean_list.append(set_of_means)
    std_deviation=statistics.stdev(mean_list)
    print("standard dev of sampling dis: ", std_deviation)
    
standard_deviation()

#std deviation of sampling distribution = std deviation of population / sqrt (number of data in each sample)