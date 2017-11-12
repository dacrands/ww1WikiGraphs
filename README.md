# WWI Wiki Graphs

Uses the data from [this wikipedia page](https://en.wikipedia.org/wiki/World_War_I_casualties) to create histograms 
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

## Data Cleaning and Organization
### Use of regex
The data from the table came in a strange string (e.g, ```56,639[18] to 64,996 [9]```, ```1,700,000[33] to
2,254,369[51]```) when I wanted integers, so I needed some regex magic.
I created a function to grab the lower estimates (i.e., ```56,639``` instead of ```64,996```), the heart of which is this mess:
```
int(re.compile(r'\d{2,}').search(i.replace(',','')).group())
```

### Getting the Data
This is how I used Pandas to grab the data: 

```
url = 'https://en.wikipedia.org/wiki/World_War_I_casualties'
ww1_data = pd.read_html(url)
dframe = DataFrame(ww1_data[0])
```
In the code I pass the URL directly to ```read_html()``` since there was only one (See how I handle multiple urls over in [this](https://github.com/dacrands/BigMenGraphs/blob/master/basketball_ref_data.py) .py file located in my BigMenGraphs repo), though this may not be best practice (I will investigate!).
Note this will give you the data for all of the WWI beligerents, which while interesting, is beyond the scope of this little project.

### Organizing the data
I created a new data frame by passing the indices of the countries I wanted (view the data frame to see indices):
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



