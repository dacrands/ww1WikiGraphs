# ww1WikiGraphs

Uses the data on [this wikipedia page](https://en.wikipedia.org/wiki/World_War_I_casualties) to create histograms 
of the military and civilian casualties for select nations.

## Background
I am a history buff, so I wanted to apply Python's data science libraries to visualize some simple WW1 data.
Wikipedia presents a very nice table of the war's casualties, so I figured I'd start there.

### Prerequisites
Along with Python 3+, you will need the following libraries for this script:
* matplotlib
* seaborn
* pandas
* re

### Getting the Data
This is how I used Pandas to grab the data: 

```
url = 'https://en.wikipedia.org/wiki/World_War_I_casualties'
ww1_data = pd.read_html(url)
dframe = DataFrame(ww1_data[0])
```

It's that easy! Getting the data to have the indices and data types you'd like, however, is a bit more difficult. Note this will give you
the data for every country, which while interesting, was beyond the scope of this little project.

### Organizing the data
To get the countries you'd like, pass their indices:
```
power_frame = dframe[[21,14,8,24,12,19,26,27]]
```

...then rename them:
```
power_frame['countries'] = [
                      'USA',
                      'Italy',
                      'UK',
                      'Aus-Hung',
                      'France',
                      'Russia',
                      'Germany',
                      'Ottoman'
                       ]
```
