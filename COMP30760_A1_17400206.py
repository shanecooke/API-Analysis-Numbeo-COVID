#!/usr/bin/env python
# coding: utf-8

# Data Science in Python - Assignment 1
# Shane Cooke - 17400206
# 
# For this assignment, I read data from the numbeo API and the covid-19 API. I decided to analyse wether quality of life in a country had any influence on the number of covid-19 confirmed cases in that country, and also, wether the healthcare level in a country had any influence on the number of deaths from covid-19 in that country. I did this by reading the quality_of_life and healthcare data from the numbeo API and by reading the current confirmed cases and deaths data from the covid-19 API.

# In[ ]:


import requests
from pandas import json_normalize
import json
import matplotlib.pyplot as plot
from pylab import rcParams
import pandas as pd
import numpy as np
from functools import reduce

response = requests.get("https://www.numbeo.com/api/rankings_by_country_historical?api_key=n8ori93r58vx0s&section=12") #makes a https request for the API.
#print(response.status_code) #prints a response code, which is determined by wether the above request is succesful, if it is succesful 200 is printed.
file = open("country_standard_living.json", "w") #opens the json file, if there is no file in that name, it creates one.
file.write(response.text) #writes the data from the API to the file
file.close() #closes the file.

with open('country_standard_living.json') as data_file: #opens the json file that was just created as data_file.
   data = json.load(data_file) #loads the data from the json file into the variable data.
df = json_normalize(data['2020-mid']) #creates a dataframe from the '2020-mid' section of the json data.
#print(df) #prints the dataframe.

with open('country_standard_living.json') as data_file: #opens the original json file.
   data = json.load(data_file) #loads the data from the json file into the variable data.
df_edited = json_normalize(data['2020-mid']) #creates a new dataframe called df_edited.
cols = [0,2,3] #index for the columns we are interested in for the new dataframe.
df_edited = df_edited[df_edited.columns[cols]] #chooses the necessary columns from the unedited dataframe and removes all of the unecessary ones.
df_edited = df_edited.loc[[0,1,2,3,4,77,78,79,80,81]] #chooses the necessary rows from the unedited dataframe and removes all of the unecessary ones.
print(df_edited) #prints the cleaned dataframe.

with open('country_standard_living.json') as data_file:
   data = json.load(data_file)
df_healthcare = json_normalize(data['2020-mid']) #same steps as above in order to isolate the healthcare_index column in its own dataframe.
cols = [3]
df_healthcare = df_healthcare[df_healthcare.columns[cols]]
df_healthcare = df_healthcare.loc[[0,1,2,3,4,77,78,79,80,81]]
#print(df_healthcare) #prints the cleaned dataframe.

with open('country_standard_living.json') as data_file:
   data = json.load(data_file)
df_quality_of_life = json_normalize(data['2020-mid']) #same steps as above in order to isolate the quality_of_life_index in its own dataframe.
cols = [2]
df_quality_of_life = df_quality_of_life[df_quality_of_life.columns[cols]]
df_quality_of_life = df_quality_of_life.loc[[0,1,2,3,4,77,78,79,80,81]]
#print(df_quality_of_life) #prints the cleaned datframe.

rcParams['figure.figsize'] = 22, 5 #sets the parameters for the graph.
colors = ["b"] * 82 #fills the colors list with 82 values of blue.
colors[0] = 'y' #sets the first index in the color list to yellow.
colors[1] = 'y'
colors[2] = 'y'
colors[3] = 'y'
colors[4] = 'y'
colors[77] = 'y'
colors[78] = 'y'
colors[79] = 'y'
colors[80] = 'y'
colors[81] = 'y'
df.plot(kind='bar', x='country', y='quality_of_life_index', title="Quality of Life by quality_of_life_index", color=colors, edgecolor='black', label ='Countries of Interest') #plots the graph with all of the given parameters.

rcParams['figure.figsize'] = 15, 5
x = [u'Nigeria', u'Bangladesh', u'Kenya', u'Iran', u'Philippines', u'Netherlands', u'Australia', u'Finland', u'Switzerland', u'Denmark'] #list of the names of the countries of interest
y = [54.910851, 66.292369, 66.600304, 70.324953, 79.176957, 184.180997, 185.028664, 186.401587, 190.915900, 192.527603] #a list of all of the quality_of_life_index from the countries of interest.
colors2 = ['r','r','r','r','r','b','b','b','b','b'] #a new list of colors
fig, ax = plot.subplots() #creates a figure and a set of subplots.
width = 0.75 # the width of the bars 
ind = np.arange(len(y))  # the x locations for the groups
ax.barh(ind, y, width, color=colors2, edgecolor='black', alpha=0.3) #setting the parameters for the horizontal bar graph.
ax.set_yticks(ind+width/2)
ax.set_yticklabels(x, minor=False)
plot.title('Quality of Life : Countries of Interest') #plots the title.
plot.xlabel('quality_of_life_index') #plots the y axis label.
plot.ylabel('Countries') #plots the x axis label.
for i, v in enumerate(y):
    ax.text(v - 40, i - 0.1, str(v), color='black', fontweight='bold') #plots the individual index values on each of the bars.
plot.show() #prints the graph.

colors3 = ['b','b','b','b','b','r','r','r','r','r'] #a new list of colors
df_edited.plot.bar(x = 'country', y = 'healthcare_index', edgecolor = 'black', color=colors3, title = 'Healthcare : Countries of Interest', alpha=0.3) #plots the graph with all of the given parameters.

df_edited.plot.bar(x = 'country', edgecolor = 'black', color=['b','g'], title = 'Quality of Life compared to Healthcare in the Countries of Interest') #plots the graph with all of the given parameters


# I read the quality of life data from numbeo into a json file. I then plotted this data on a barchart and highlighted the countries which I had decided to analyse further, which I called the 'countries of interest'. The data was made up of multiple different factors which required cleaning, so I cleaned the dataframe until only country, quality_of_life_index and healthcare_index was left. I plotted the quality_of_life_index of the countries of interest on a horizontal bar chart and plotted the healthcare_index of the countries of interest on a vertical bar chart. Lastly, I decided to make a graph where both quality_of_life_index and healthcare_index where beside eachother in order to show the differences between the high quality of life countries and the low quality of life countries.

# In[ ]:


rcParams['figure.figsize'] = 8, 5 #sets the parameters for the figure.
response = requests.get("https://api.covid19api.com/total/country/Nigeria") #makes a https request for the API.
#print(response.status_code)
file = open("covid_Nigeria.json", "w") #opens the json file, if there is no file in that name, it creates one.
file.write(response.text) #writes the data from the API to the file.
file.close() #closes the file.

df1 = pd.read_json('covid_Nigeria.json') #reads the data from the json into a datframe.
#print(df1)
lastindex = df1.last_valid_index() #variable which will contain the value of the last index in the dataframe.
#print(lastindex) #prints the last index in the dataframe.

with open('covid_Nigeria.json') as data_file:
   data = json.load(data_file)
df1_edited = json_normalize(data) #creates a new dataframe from the original json file.
cols = [0,7,8,11] 
df1_edited = df1_edited[df1_edited.columns[cols]] #selects the necessary columns for the cleaned dataframe.
print(df1_edited) #prints the cleaned dataframe.

with open('covid_Nigeria.json') as data_file:
   data = json.load(data_file)
df1_confirmed = json_normalize(data)
cols = [7]
df1_confirmed = df1_confirmed[df1_confirmed.columns[cols]] #same steps as above, creates a dataframe with only confirmed in it.
df1_confirmed = df1_confirmed.loc[[lastindex]]
print(df1_confirmed)

with open('covid_Nigeria.json') as data_file:
   data = json.load(data_file)
df1_deaths = json_normalize(data)
cols = [8]
df1_deaths = df1_deaths[df1_deaths.columns[cols]] #same steps as above, creates a dataframe with only deaths in it.
df1_deaths = df1_deaths.loc[[lastindex]]
print(df1_deaths)
df1.plot(x='Date', y='Confirmed', color="green", title="Nigeria : Cases vs Date") #plots a graph with the given parameters.



response = requests.get("https://api.covid19api.com/total/country/Bangladesh") #same steps as above for Bangladesh.
#print(response.status_code)
file = open("covid_Bangladesh.json", "w")
file.write(response.text)
file.close()

df2 = pd.read_json('covid_Bangladesh.json')
#print(df2)

with open('covid_Bangladesh.json') as data_file:
   data = json.load(data_file)
df2_edited = json_normalize(data)
cols = [0,7,8,11]
df2_edited = df2_edited[df2_edited.columns[cols]]
print(df2_edited)

with open('covid_Bangladesh.json') as data_file:
   data = json.load(data_file)
df2_confirmed = json_normalize(data)
cols = [7]
df2_confirmed = df2_confirmed[df2_confirmed.columns[cols]]
df2_confirmed = df2_confirmed.loc[[lastindex]]
print(df2_confirmed)

with open('covid_Bangladesh.json') as data_file:
   data = json.load(data_file)
df2_deaths = json_normalize(data)
cols = [8]
df2_deaths = df2_deaths[df2_deaths.columns[cols]]
df2_deaths = df2_deaths.loc[[lastindex]]
print(df2_deaths)
df2.plot(x='Date', y='Confirmed', color="darkgreen", title="Bangladesh : Cases vs Date")



response = requests.get("https://api.covid19api.com/total/country/Kenya") #same steps as above for Kenya.
#print(response.status_code)
file = open("covid_Kenya.json", "w")
file.write(response.text)
file.close()

df3 = pd.read_json('covid_Kenya.json')
#print(df3)

with open('covid_Kenya.json') as data_file:
   data = json.load(data_file)
df3_edited = json_normalize(data)
cols = [0,7,8,11]
df3_edited = df3_edited[df3_edited.columns[cols]]
print(df3_edited)

with open('covid_Kenya.json') as data_file:
   data = json.load(data_file)
df3_confirmed = json_normalize(data)
cols = [7]
df3_confirmed = df3_confirmed[df3_confirmed.columns[cols]]
df3_confirmed = df3_confirmed.loc[[lastindex]]
print(df3_confirmed)

with open('covid_Kenya.json') as data_file:
   data = json.load(data_file)
df3_deaths = json_normalize(data)
cols = [8]
df3_deaths = df3_deaths[df3_deaths.columns[cols]]
df3_deaths = df3_deaths.loc[[lastindex]]
print(df3_deaths)
df3.plot(x='Date', y='Confirmed', color="black", title="Kenya : Cases vs Date")



response = requests.get("https://api.covid19api.com/total/country/Iran") #same steps as above for Iran.
#print(response.status_code)
file = open("covid_Iran.json", "w")
file.write(response.text)
file.close()

df7 = pd.read_json('covid_Iran.json')
#print(df7)

with open('covid_Iran.json') as data_file:
   data = json.load(data_file)
df7_edited = json_normalize(data)
cols = [0,7,8,11]
df7_edited = df7_edited[df7_edited.columns[cols]]
print(df7_edited)

with open('covid_Iran.json') as data_file:
   data = json.load(data_file)
df7_confirmed = json_normalize(data)
cols = [7]
df7_confirmed = df7_confirmed[df7_confirmed.columns[cols]]
df7_confirmed = df7_confirmed.loc[[lastindex]]
print(df7_confirmed)

with open('covid_Iran.json') as data_file:
   data = json.load(data_file)
df7_deaths = json_normalize(data)
cols = [8]
df7_deaths = df7_deaths[df7_deaths.columns[cols]]
df7_deaths = df7_deaths.loc[[lastindex]]
print(df7_deaths)
df7.plot(x='Date', y='Confirmed', color="red", title="Iran : Cases vs Date")



response = requests.get("https://api.covid19api.com/total/country/Philippines") #same steps as above for Philippines.
#print(response.status_code)
file = open("covid_Philippines.json", "w")
file.write(response.text)
file.close()

df9 = pd.read_json('covid_Philippines.json')
#print(df9)

with open('covid_Philippines.json') as data_file:
   data = json.load(data_file)
df9_edited = json_normalize(data)
cols = [0,7,8,11]
df9_edited = df9_edited[df9_edited.columns[cols]]
print(df9_edited)

with open('covid_Philippines.json') as data_file:
   data = json.load(data_file)
df9_confirmed = json_normalize(data)
cols = [7]
df9_confirmed = df9_confirmed[df9_confirmed.columns[cols]]
df9_confirmed = df9_confirmed.loc[[lastindex]]
print(df9_confirmed)

with open('covid_Philippines.json') as data_file:
   data = json.load(data_file)
df9_deaths = json_normalize(data)
cols = [8]
df9_deaths = df9_deaths[df9_deaths.columns[cols]]
df9_deaths = df9_deaths.loc[[lastindex]]
print(df9_deaths)
df9.plot(x='Date', y='Confirmed', color="darkblue", title="Philippines : Cases vs Date")


# I then began reading the data from the covid-19 API into different json files for each country, I decided to focus on the low quality of life countries first. The API contains lots of irrelevant information which was placed in the first dataframe. I created an edited dataframe for each country which only contained the country, confirmed cases and deaths. I also created two datframes for each country which isolated confirmed cases and deaths on their own. I created a variable called lastindex, which will ensure that as the API updates its data, my dataframes and graphs will also be updated. I then plotted each countries 'Confirmed Cases' against 'Date'. I did this so that the reader could view the difference in shape between the 'low quality of life' countries graphs vs the 'high quality of life' countries graphs. As you can see, all of the 'low quality of life' graphs follow roughly the same shape.

# In[ ]:


response = requests.get("https://api.covid19api.com/total/country/Denmark") #makes a https request for the API.
#print(response.status_code)
file = open("covid_Denmark.json", "w") #opens the json file, if there is no file in that name, it creates one.
file.write(response.text) #writes the data from the API to the file.
file.close() #closes the file.

df4 = pd.read_json('covid_Denmark.json') #reads the data from the json into a datframe.
#print(df4)

with open('covid_Denmark.json') as data_file:
   data = json.load(data_file)
df4_edited = json_normalize(data) #creates a new dataframe from the original json file.
cols = [0,7,8,11]
df4_edited = df4_edited[df4_edited.columns[cols]] #selects the necessary columns for the cleaned dataframe.
print(df4_edited) #prints the cleaned dataframe.

with open('covid_Denmark.json') as data_file:
   data = json.load(data_file)
df4_confirmed = json_normalize(data)
cols = [7]
df4_confirmed = df4_confirmed[df4_confirmed.columns[cols]] #same steps as above, creates a dataframe with only confirmed in it.
df4_confirmed = df4_confirmed.loc[[lastindex]]
print(df4_confirmed)

with open('covid_Denmark.json') as data_file:
   data = json.load(data_file)
df4_deaths = json_normalize(data)
cols = [8]
df4_deaths = df4_deaths[df4_deaths.columns[cols]] #same steps as above, creates a dataframe with only deaths in it.
df4_deaths = df4_deaths.loc[[lastindex]]
print(df4_deaths)

rcParams['figure.figsize'] = 8, 5 #sets the parameters for the graph.
df4.plot(x='Date', y='Confirmed', color="darkred", title="Denmark : Cases vs Date") #plots a graph with the given parameters.



response = requests.get("https://api.covid19api.com/total/country/Switzerland") #same steps as above for Switzerland.
#print(response.status_code)
file = open("covid_Switzerland.json", "w")
file.write(response.text)
file.close()

df5 = pd.read_json('covid_Switzerland.json')
#print(df5)

with open('covid_Switzerland.json') as data_file:
   data = json.load(data_file)
df5_edited = json_normalize(data)
cols = [0,7,8,11]
df5_edited = df5_edited[df5_edited.columns[cols]]
print(df5_edited)

with open('covid_Switzerland.json') as data_file:
   data = json.load(data_file)
df5_confirmed = json_normalize(data)
cols = [7]
df5_confirmed = df5_confirmed[df5_confirmed.columns[cols]]
df5_confirmed = df5_confirmed.loc[[lastindex]]
print(df5_confirmed)

with open('covid_Switzerland.json') as data_file:
   data = json.load(data_file)
df5_deaths = json_normalize(data)
cols = [8]
df5_deaths = df5_deaths[df5_deaths.columns[cols]]
df5_deaths = df5_deaths.loc[[lastindex]]
print(df5_deaths)
df5.plot(x='Date', y='Confirmed', color="red", title="Switzerland : Cases vs Date")



response = requests.get("https://api.covid19api.com/total/country/Finland") #same steps as above for Finland.
#print(response.status_code)
file = open("covid_Finland.json", "w")
file.write(response.text)
file.close()

df6 = pd.read_json('covid_Finland.json')
#print(df6)

with open('covid_Finland.json') as data_file:
   data = json.load(data_file)
df6_edited = json_normalize(data)
cols = [0,7,8,11]
df6_edited = df6_edited[df6_edited.columns[cols]]
print(df6_edited)

with open('covid_Finland.json') as data_file:
   data = json.load(data_file)
df6_confirmed = json_normalize(data)
cols = [7]
df6_confirmed = df6_confirmed[df6_confirmed.columns[cols]]
df6_confirmed = df6_confirmed.loc[[lastindex]]
print(df6_confirmed)

with open('covid_Finland.json') as data_file:
   data = json.load(data_file)
df6_deaths = json_normalize(data)
cols = [8]
df6_deaths = df6_deaths[df6_deaths.columns[cols]]
df6_deaths = df6_deaths.loc[[lastindex]]
print(df6_deaths)
df6.plot(x='Date', y='Confirmed', color="blue", title="Finland : Cases vs Date")



response = requests.get("https://api.covid19api.com/total/country/Australia") #same steps as above for Australia.
#print(response.status_code)
file = open("covid_Australia.json", "w")
file.write(response.text)
file.close()

df8 = pd.read_json('covid_Australia.json')
#print(df8)

with open('covid_Australia.json') as data_file:
   data = json.load(data_file)
df8_edited = json_normalize(data)
cols = [0,7,8,11]
df8_edited = df8_edited[df8_edited.columns[cols]]
print(df8_edited)

with open('covid_Australia.json') as data_file:
   data = json.load(data_file)
df8_confirmed = json_normalize(data)
cols = [7]
df8_confirmed = df8_confirmed[df8_confirmed.columns[cols]]
df8_confirmed = df8_confirmed.loc[[lastindex]]
print(df8_confirmed)

with open('covid_Australia.json') as data_file:
   data = json.load(data_file)
df8_deaths = json_normalize(data)
cols = [8]
df8_deaths = df8_deaths[df8_deaths.columns[cols]]
df8_deaths = df8_deaths.loc[[lastindex]]
print(df8_deaths)
df8.plot(x='Date', y='Confirmed', color="darkblue", title="Australia : Cases vs Date")



response = requests.get("https://api.covid19api.com/total/country/Netherlands") #same steps as above for Netherlands.
#print(response.status_code)
file = open("covid_Netherlands.json", "w")
file.write(response.text)
file.close()

df10 = pd.read_json('covid_Netherlands.json')
df10.at[202,'Confirmed'] = 61000
df10.at[202, 'Deaths'] = 6180
#print(df10)

with open('covid_Netherlands.json') as data_file:
   data = json.load(data_file)
df10_edited = json_normalize(data)
cols = [0,7,8,11]
df10_edited = df10_edited[df10_edited.columns[cols]]
df10_edited.at[202,'Confirmed'] = 61000
df10_edited.at[202, 'Deaths'] = 6180
print(df10_edited)

with open('covid_Netherlands.json') as data_file:
   data = json.load(data_file)
df10_confirmed = json_normalize(data)
cols = [7]
df10_confirmed = df10_confirmed[df10_confirmed.columns[cols]]
df10_confirmed = df10_confirmed.loc[[lastindex]]
print(df10_confirmed)

with open('covid_Netherlands.json') as data_file:
   data = json.load(data_file)
df10_deaths = json_normalize(data)
cols = [8]
df10_deaths = df10_deaths[df10_deaths.columns[cols]]
df10_deaths = df10_deaths.loc[[lastindex]]
print(df10_deaths)
df10.plot(x='Date', y='Confirmed', color="orange", title="Netherlands : Cases vs Date")


# I carried out the same steps for the high quality of life countries as I did in the above cell for the low quality of life countries. I plotted all of these on graphs as well, so that the reader can see the difference between the shapes of the 'high quality of life' countries graphs vs the 'low quality of life' countries graphs. As you can see, all of the 'high quality of life' graphs follow roughly the same shape.

# In[ ]:


rcParams['figure.figsize'] = 8, 5 #sets parameters for graph.
ax = df6.plot(x='Date', y='Confirmed', color='blue', label='Finland') #plots a line to represent cases vs date in Finland
df3.plot(ax=ax, x='Date', y='Confirmed', color='black', label ='Kenya', title='Fnland vs Kenya : Confirmed Cases') #plots a line on the same graph to represent cases vs date in Kenya.


ax = df4.plot(x='Date', y='Confirmed', color='darkred', label='Denmark')
df7.plot(ax=ax, x='Date', y='Confirmed', color='darkgreen', label='Iran', title='Denmark vs Iran : Confirmed Cases')


ax = df5.plot(x='Date', y='Confirmed', color='red', label='Switzerland')
df9.plot(ax=ax, x='Date', y='Confirmed', color='darkblue', label='Philippines', title='Switzerland vs Philippines : Confirmed Cases')


ax = df10.plot(x='Date', y='Confirmed', color='orange', label='Netherlands')
df2.plot(ax=ax, x='Date', y='Confirmed', color='green', label='Bangladesh', title='Netherlands vs Bangladesh : Confirmed Cases')


ax = df8.plot(x='Date', y='Confirmed', color='purple', label='Australia')
df1.plot(ax=ax, x='Date', y='Confirmed', color='gray', label='Nigeria', title='Australia vs Nigeria : Confirmed Cases')


combined_df = reduce(lambda x,y: pd.merge(x,y, on='Date', how='inner'), [df1_edited,df4_edited,df3_edited,df6_edited,df9_edited,df2_edited,df5_edited,df7_edited,df8_edited,df10_edited]) #combines all of the cleaned dataframes into one large dataframe.
print(combined_df) #prints the combined cleaned dataframe.

rcParams['figure.figsize'] = 15, 15
combined_df.plot(x = 'Date',y = ['Confirmed_x','Confirmed_y'], title = 'Comparison : Countries have same colour as in above graphs', color=['gray','black','darkblue','red','purple','darkred','blue','green','darkgreen','orange'], legend=None) #plots the graph of all of the cases in the countries of interest.


# I decided to graph all of the 'high quality of life' countries against all of the 'low quality of life' countries. I decided the fairest way to do this was to graph the lowest population 'high quality of life' country vs the lowest population 'low quality of life' country and the highest population 'high quality of life' country vs the highest population 'low quality of life' country. I colour coded these graphs in line with the nations flags and followed this colour code when plotting all 10 countries against eachother. I hoped that the reader would be able to see that regardless of the numbers, all of the plots follow roughly the same shape, which illustrates the difference between both types of country. For all of the graphs, countries are on the x-axis and confirmed cases are on the y-axis.

# In[ ]:


frames = [df4_deaths, df5_deaths, df6_deaths, df8_deaths, df10_deaths, df1_deaths, df2_deaths, df3_deaths, df7_deaths, df9_deaths] #creates a list of all of the 'deaths' dataframes.
df_total_deaths = pd.concat(frames) #combines all of these datframes into one large cleaned dataframe.
#print(df_total_deaths) #prints the cleaned dataframe.
frames3 = [df4_confirmed, df5_confirmed, df6_confirmed, df8_confirmed, df10_confirmed, df1_confirmed, df2_confirmed, df3_confirmed, df7_confirmed, df9_confirmed] #creates a list of all of the 'confirmed' dataframes.
df_total_confirmed = pd.concat(frames3) #combines all of these dataframes into one large cleaned dataframe.
#print(df_total_confirmed) #prints the cleaned dataframe.

df_total_deaths.reset_index(drop=True, inplace=True) #resets the index for the given dataframe.
df_total_confirmed.reset_index(drop=True, inplace=True)
df_healthcare.reset_index(drop=True, inplace=True)
df_quality_of_life.reset_index(drop=True, inplace=True)
frames2 = [df_total_deaths,df_healthcare]
df_result2 = pd.concat(frames2, axis=1) #combines the two dataframes.
country = ['Denmark','Switzerland','Finland','Australia','Netherlands','Nigeria','Bangladesh','Kenya','Iran','Philippines'] #list of all of the countries of interest.
population = [5.806,8.545,5.518,24.990,17.280,195.900,161.400,51.390,81.800,106.700] #list of poulations for all of the countries of interest.
percentage_of_population_infected = [0.0102,0.0293,0.0033,0.0011,0.0253,0.0003,0.0026,0.0012,0.0088,0.0037]#list of percentages of population infected.
deaths_per_1m = [131,387,67,1083,495,6,37,23,492,71]
df_result2['country'] = country #adds in the country column.
frames4 = [df_result2,df_total_confirmed]
df_result2 = pd.concat(frames4, axis=1)  #combines the two dataframes.
frames5 = [df_result2,df_quality_of_life]
df_result2 = pd.concat(frames5, axis=1) #combines the two dataframes.
cols = df_result2.columns.tolist()
cols = cols[+2:] + cols[:+2] #changes the order of the columns in the datframe in order to make it more readable.
df_result2 = df_result2[cols]
df_result2['population_in_millions'] = population #adds the population column to the dataframe.
df_result2['percentage_of_population_infected'] = percentage_of_population_infected #adds the percentage_of_population_infected column to the dataframe.
df_result2['deaths_per_1m'] = deaths_per_1m
print(df_result2) #prints the final cleaned and reformatted datframe.

colors3 = ['b','b','b','b','b','r','r','r','r','r'] #new list of colors.
rcParams['figure.figsize'] = 5, 10
df_result2.plot.bar(x = 'country', y = 'Confirmed', edgecolor = 'black', color=colors3, title = 'Confirmed in Countries of Interest', alpha=0.3, legend=None) #plots graph of confirmed cases.
df_result2.plot.bar(x = 'country', y = 'Deaths', edgecolor = 'black', color=colors3, title = 'Deaths in Countries of Interest', alpha=0.3, legend=None) #plots graph of deaths.
df_result2.plot.bar(x = 'country', y = 'percentage_of_population_infected', edgecolor = 'black', color=colors3, title = 'Percentage of population that are infected in Countries of Interest', alpha=0.3, legend=None) #plots graph of percentage of population infected.
df_result2.plot.bar(x = 'country', y = 'deaths_per_1m', edgecolor = 'black', color=colors3, title = 'Deaths per 1 million population in Countries of Interest', alpha=0.3,legend=None)

plot.figure(figsize=(40,20))
ax1 = plot.subplot(121, aspect='equal')
df_result2.plot(kind='pie', y = 'Confirmed', ax=ax1, autopct='%1.1f%%', 
 startangle=90, shadow=False, labels=df_result2['country'], legend = False, fontsize=12) #plots the pie chart and specifies the parameters for the figure.


# In this cell, I created one large dataframe which contains all of the revelant data from both APIs. This dataframe contains all of the cleaned data from the dataframes which where created in the cells at the beginning of the notebook. I then re-ordered this dataframes columns in order to make it more readable. I also added in population and percentage_of_population_infected, which I calculated myself, because I felt as though it was necessary information in order to analyse the dataset and the covid-19 API did not contain this information. I visualised this data with a bar chart showing the confirmed cases across all of the countries, a bar chart showing the deaths across all of the countries, a bar chart showing the percentage of the population infected across all of the countries and a graph showing the deaths per 1 million population across all countries. Finally, I created a pie chart showing the distribution of the total cases for all 10 countries. The 360 degrees come from the total cases added up between each country of interest, and each slice represents how much a country added to that total.

# Conclusion:
#     
# At first, I thought that maybe I was answering an obvious question by doing this analysis. I believed that it was obvious that the higher quality of life countries would have less confirmed cases overall, and that the higher quality of healthcare countries would have less deaths overall. However, after analysing all of the data I read in from both API's, I don't believe this to be true.
# 
# At first, when looking at the cases vs date graphs for the low quality of life countries, I believed that due to the constant and almost linear increase of cases, and no 'flattening of the curve', that the low quality of life countries where indeed performing very badly. This belief was solidated when I looked at the graphs for the high quality of life countries. All of the graphs for these countries show a sharp increase in the early months of this year, then a flattening of the curve, and then another increase beginning around September. Because of this long period of flatness in the graphs, I believed that these countries must be performing much better (in terms of cases) than the low quality of life countries.
# 
# I then looked at the graphs where I compare a high quality of life country to a low quality of life country. In 4 out of 5 of these graphs, the low quality of life country has more cases than the high quality of life country. These graphs really show the difference in line shape between the two 'classes' of country. The graph which shows all 10 countries lines on the same graph shows that the only high quality of life country with cases like the low quality of life countries is the Netherlands which I was very suprised to see.
# 
# Upon creating the fully cleaned and optimized dataframe for the analysis, I began to graph different metrics against eachother in order to further compare the two 'classes', and mainly focus on healthcare vs deaths. By looking at the 'Deaths in Countries of Interest' graph, I realized that there was not a huge difference between the two 'classes of country' (apart from Iran) in terms of number of deaths due to covid-19. This stands in stark contrast to the above graph 'Confirmed in Countries of Interest' which shows that the low quality of life countries have much more cases on average than the high quality of life countries. I then allowed for population in each of the countries and plotted the percentage of the population that are infected on the graph, 'Percentage of population that are infected in Countries of Interest. I found the populations of the countries on Google and calculated the percentage infected myself, as the covid-19 API did not contain this information and I felt as though it was necessary for my analysis. In this graph, it is clear to see that in fact, the high quality of life countries actually had a much higher percentage infected than the lower quality of life countries on average. Switzerland and the Netherlands are clear and obvious outliers in the dataset. I then plotted a graph called 'Deaths per 1 million population in Countries of Interest'. This graph illustrates that in fact, on average, the high healthcare countries are having a lot more deaths than the low healthcare countries per population. I calculated the deaths per million polulation myself by reading data from the API, as the API itself did not have this metric.
# 
# My analysis has shown me that higher quality of life does not in fact reduce the covid-19 cases in a country and that lower quality of life does not increase the covid-19 cases in the countries in my dataset. It has also shown me that the higher standard of healthcare in the countries in my dataset does not necessarily translate to less deaths, and that the lower standard of healthcare also does not translate to more deaths. It is however clear to me that the higher quality of life countries succesfully flattened the curve, if only for a period of months, which none of the lower quality of life countries in my dataset managed to do. I also noticed that in almost every high quality of life country, transmission of the disease began long before it did in many of the lower quality of life countries which may be a contribution to more cases and more deaths per population.
# 
# For further analysis, I would like to take a lot more countries into account on both sides of the scale, and I would also like to include many more variables, such as age of the population, geographical variables, age of confirmed cases, age of deaths, abilty to access testing and tests carried out thus far.
