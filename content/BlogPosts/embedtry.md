Title: FBS Coach Salaries
Date: 2018-1-14 
Category: Sports
Tags: web scraping, pandas, BeautifulSoup
Slug: FBS salaries
Authors: Rachel Ehlers
Summary: A look at FBS coach salary data scraped from USA Today. 


---------------------------
Before reading: Know the interactive plots in this post are made to be viewed on a laptop or desktop.


Coaching amateur athletes can be a lucrative endeavor. In 2016, the top-earning public employee in 27 states was an NCAA Division-I FBS coach (and a D-I basketball coach in 12 others). In 2017, Alabama paid Nick Saban a whopping $11.132 million salary. With the exception of 2016, he’s been the top earner each year since 2012. The one hiccup in his would-be 7-year streak was the result of Jim Harbaugh’s $9 million deal with Michigan. While these salaries are arguably excessive (even Saban said, “probably not” when asked if he was worth $11 million this year), they provide insight on how far schools are willing to go to attract the top talent and keep them from straying. 


I attended an FCS school, and before looking into this data, I was much more familiar with that level of play and coach pay. My knowledge of FBS coach salaries was limited to what headlines I'd seen about Saban and Harbaugh. I was curious about trends in pay distribution and searched for a reliable source of data, finding one in USA Today(links at the end of this post). Since 2014, the publication has requested and released coach compensation data from all FBS schools.  Public schools are required to release such information, but private schools are exempt. Read on to learn a few things I found interesting about the available data. 

#### Head Coach Salaries Across Conferences
-------------------------------------------------
First, let's take a look at head coach salaries. Below is a plot displaying head coach salaries by conference. Hovering over a point will reveal the corresponding coach, salary, and school. If you want to zoom in on a specific part of the plot (for example, to get a closer look at salaries in the MAC, which appear to be grouped very closely due to scaling), use your mouse to drag a box around the area. To zoom back out, double-click anywhere in the plot area. Please note that "Ind." does not represent a conference, but rather the limited data available from independent schools.  

<iframe width="800" height="600" frameborder="0" scrolling="no" src="https://plot.ly/~rachehlers/133.embed"></iframe>

For each year in question, SEC coaches made the most, followed by the Big Ten. These two conferences are members of the Power Five, along with the ACC, Pac-12, and Big 12. Teams outside of these conferences are either in the Group of Five (American Athletic Conference, Conference USA, Mid-American Conference, Mountain West Conference, and the Sun Belt) or are independent (Notre Dame, Massachusetts, Brigham Young, and Army). 

Now, let's put the salaries of the highest earners in perspective. 
Of the Group of Five, three conferences had complete head coach salary data: the Mid-American Conference, Sun Belt, and Conference USA. The 38 head coach salaries in these conferences sum to $24.276 million. The top three individual earners overall (Nick Saban, Dabo Swinney, and Jim Harbaugh), collectively earned $26.64 million. **That means their 3 salaries could cover the salaries of all 38 head coaches in these 3 conferences, with more than $2.3 million to spare**. 


#### Assistant Coach Salaries Across Conferences
------------------------------------------------------

The following boxplots display assistant coach salaries by conference. The points to the left of each boxplot display the underlying data. 


<iframe width="800" height="600" frameborder="0" scrolling="no" src="https://plot.ly/~rachehlers/143.embed"></iframe>

Like their head coaches, assistants in the SEC tend to earn more than those in other conferences. In 2017, seven of the top 9 assistant salaries went to SEC coaches. LSU's defensive coordinator, Dave Aranda, was the top-earning assistant, making $1.8 million. His defensive counterpart, Matt Canada, was fourth on the list with $1.505 million. Alabama and Michigan each employed a pair of assistants in the top 10. 



#### Comparing Head Coach Pay to Staff Pay
------------------------------------------

The following plot consists of each school's head coach salary plotted against their staff's salaries totaled. 

For each year from 2014-2017, about 50% of Power Five head coaches made a salary greater than their 9 assistants' salaries totaled. This was only true for about 5% of schools outside of Power Five conferences each year. 

<iframe width="800" height="600" frameborder="0" scrolling="no" src="https://plot.ly/~rachehlers/0.embed"></iframe>




### My Methodology

The most up-to-date salary data can be found at the links at the end of this post. I found data from 2014-2016 using the [Wayback Machine](http://archive.org/web/). I scraped and parsed the data using the Python libraries requests and BeautifulSoup, then cleaned and structured it using pandas. For the visualizations in this post, I used plotly. Code for scraping the data is on [my GitHub](https://github.com/rachelehlers11/FBScoachsalaries/blob/master/dataframebuilder.py). The files in CSV form (all years included) are at [this link](https://github.com/rachelehlers11/FBScoachsalaries/tree/master/salaryfiles). 



### Current Data Links

USA Today's site only keeps live the most current data (2017). Refer to "My Methodology" for past years' data.

- [Head coaches](http://sports.usatoday.com/ncaa/salaries/) 

- [Assistant coaches](http://sports.usatoday.com/ncaa/salaries/football/assistant) 

- [Strength coaches](http://sports.usatoday.com/ncaa/salaries/football/strength) 

### Yearly USA Today Methodology Links

2014

- [Head coaches](http://sports.usatoday.com/2014/11/19/2014-ncaa-football-head-coach-salaries-methodology/)
- [Assistants](http://sports.usatoday.com/2014/12/10/2014-ncaa-football-assistant-coaches-methodology/)

2015

- [Head coaches](http://sports.usatoday.com/2015/10/08/2015-ncaa-football-head-coach-salaries-methodology/)
- [Assistants](http://sports.usatoday.com/2015/12/08/2015-ncaa-football-assistant-coach-salaries-methodology/)

2016

- [Head coaches](http://sports.usatoday.com/2016/10/25/2016-ncaa-football-head-coach-salaries-methodology/)
- [Assistants](http://sports.usatoday.com/2016/12/06/2016-ncaa-football-assistant-coach-salaries-methodology/)
- [Strength coaches](http://sports.usatoday.com/2016/12/06/2016-ncaa-football-strength-coach-salaries-methodology/)

2017

- [Head coaches](http://sports.usatoday.com/2017/10/25/2017-ncaa-football-head-coach-salaries-methodology/)
- [Assistants](http://sports.usatoday.com/2017/12/06/2017-ncaa-football-assistant-coach-salaries-methodology/)
- [Strength coaches](http://sports.usatoday.com/2017/12/06/2017-ncaa-football-strength-coach-salaries-methodology/)



