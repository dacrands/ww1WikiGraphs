# ww1WikiGraphs

Uses the data on [this wikipedia page](https://en.wikipedia.org/wiki/World_War_I_casualties) to create histograms 
of the military and civilian casualties for select nations.

## Background
I am a history buff, so I wanted to apply Python's data science libraries to visualize some simple WW1 data.
Wikipedia presents a very nice table of the war's casualties, so I figured I'd start there.

This is how I used Pandas to grab the data: 

```
url = 'https://en.wikipedia.org/wiki/World_War_I_casualties'
ww1_data = pd.read_html(url)
dframe = DataFrame(ww1_data[0])
```

