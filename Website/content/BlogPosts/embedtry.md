Title: FBS Football Coach Salaries
Date: 2017-12-12 10:20
Modified: 2017-12-12 10:21
Category: Sports
Tags: web scraping, pandas, BeautifulSoup
Slug: FBS salaries
Authors: Rachel Ehlers
Summary: A look at FBS coach salary data scraped from USA Today. 


---------------------------
 
Coaching amateurs can be a lucrative endeavor. In 2016, the top-earning public employee in 27 states was an NCAA Division-I FBS football coach; in 12 others, it was a D-I college basketball coach. For those unfamiliar with the kind of money these individuals rake in: Alabama will have paid Nick Saban a whopping $11.125 million dollars by the end of the year. With the exception of 2016, he’s been the highest earner each year since 2012. The one hiccup in his would-be 7-year streak was the result of Jim Harbaugh’s $9 million deal with Michigan. While these salaries are arguably excessive (even Saban said, “probably not” when asked if he was worth $11 million this year), they provide insight on how far schools are willing to go to attract the top talent and keep them from straying. 


What about the rest of the staff? For years, each team has been allowed 9 paid assistant coaches. Starting in January, they'll be allowed 10. Curious about trends in salary distribution across teams and conferences, I began to search for a reliable source of data, and found one in USA Today. Since 2014, the publication has requested coaching staff compensation data from all FBS schools. Private schools are exempt from reporting such information, but data is available for almost every public FBS school. 

I attended an FCS school (University of Montana - go Griz!), so I'm much more familiar with football at that level. Here are a few things that stood out to me at first glance, coming from a place of naivete:
* 7 of the top 10 assistant coach salaries in 2017 were paid to coaches at SEC schools. LSU's Dave Aranda was the top earner, pulling in $1,800,000
* Coaches in the Power Five conferences are on another level compared to those at non-Power Five schools. 
* Assistant coaches in the Power Five 

The following plot consists of each school's head coach salary plotted against the school's assistant staff salaries totaled. Each blue point represents a non-Power Five head coach, and orange points represent Power Fives. I also included a line of equality for reference (where head coach salary would equal the staff total). The dropdown on the left allows you to switch what year's data is shown. Hovering over a point will reveal the corresponding coach, school, salary, and total staff salary. 

<iframe width="900" height="900" frameborder="0" scrolling="no" src="https://plot.ly/~rachehlers/0.embed"></iframe>













### Methodology

The most up-to-date salary data can be found at the links at the end of this post. I found data from 2014-2016 using the [Wayback Machine](http://archive.org/web/). I scraped and parsed the data using the Python libraries requests and BeautifulSoup. I structured and cleaned it using pandas. For visualization and analysis, I played around with both R and Python. I settled on using plotly for the following interactive. For runnable Python code, go check out my accompanying notebook.



#### Links
[Python notebook with methodology]


[Head coaches](http://sports.usatoday.com/ncaa/salaries/) 
[Assistant coaches](http://sports.usatoday.com/ncaa/salaries/football/assistant) 
[Strength coaches](http://sports.usatoday.com/ncaa/salaries/football/strength) 


For those who would like to follow along with the code and process of scraping, cleaning, and visualizing the data, check out my accompanying blog post. It's a Jupyter notebook, so the code is executable in your browser. Even if you've never coded before, I strongly encourage you to try it out. I provided step-by-step directions of how to run code, alter it, and then see what you built. 

Data 
I wrote CSV files of the data and posted them [here](https://github.com/rachelehlers11/FBScoachsalaries/tree/master/salaryfiles) if you would like to download and me



