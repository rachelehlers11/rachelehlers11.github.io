Title: Deadly Brotherhoods- Hazing Deaths in the United States
Date: 2017-12-18 10:20
Modified: 2017-12-18 10:20
Category: Social Trends
Tags: web scraping, pandas, BeautifulSoup
Slug: Hazing Deaths
Authors: Rachel Ehlers
Summary: A look at hazing deaths on record in the United States


A year ago, Tim Piazza was a regular Penn State sophomore, searching for a sense of belonging. He chose to pledge Beta Theta Pi, a fraternity held in high regard, complete with a beautiful house renovated with a $10 million donation 10 years earlier. 

 On February 3rd, Tim Piazza downed an estimated 18 drinks in a two-hour span as part of a hazing ritual. He proceeded to stumble around the house, knocking his head on multiple occasions. He tumbled down the stairs at the fraternity. Tim, who just hours before was healthy, coherent and presumably excited about his new friends, suffered a ruptured spleen, collapsed lung, and irrecoverable brain injuries. His friends placed his limp body on a couch, "Jansported" him (put a backpack on him with enough weight to keep him from rolling on his back and choking on vomit) and left him alone after unsuccessful attempts to wake him. 

The story got even darker after video surveillance revealed the extent of his brothers' negligence; it took 12 hours for anyone to call for help. By then, it was too late, and Piazza died in the ICU. Further investigation showed members of Beta had attempted to cover up their involvement in his death by erasing surveillance footage, text messages, and other evidence related to Piazza's death. 

The disturbing story isn't all that unusual. Deaths attributed to hazing date back to the 1800s. 
Tim was nowhere near the first to suffer an untimely death as the result of a hazing ritual, and he won't be the last. In fact, his story is all too common. Reading his story made me wonder about hazing practices. I decided to scrape [this Wikipedia page](https://en.wikipedia.org/wiki/List_of_hazing_deaths_in_the_United_States) for information on hazing deaths on record in the United States. I used the requests Python library to scrape the data and BeautifulSoup to parse it. 


The purpose of this post is not to discuss the morality of hazing, but rather to gain a better understanding of the rituals practiced over time. Has hazing become more or less prevalent over time? How have rituals changed over time? Unfortunately, the answers to those questions aren't as simple to find as they might seem. 

Drawing valuable insights about hazing proves particularly challenging, considering the following: 

- Victims are sworn to secrecy(whether by threat of nonmembership or further physical abuse as retaliation)
- The U.S. population has increased considerably over the time period studied, but proportional comparisons are inappropriate, considering changing media coverage of hazing over time. 
- There exists no official centralized database for data on hazing deaths. 

For the reasons above, comparing the quantity of hazing deaths over time isn't particularly useful. Instead I decided to compare trends in rituals leading to deaths. 

Before doing any type of analysis, I like to take note of any glaring trends. At first glance, a few things were clear: 

- Males account for an overwhelming majority of deaths attributed to hazing.
- The types of rituals leading to fatalities have changed in over time. 
- Alcohol consumption as the focal point of hazing rituals is a relatively recent concept. 






If you or someone you know feels physically, emotionally, mentally, or sexually violated as a result of hazing, please reach out. 






I was talking to my dad about the sudden shift, speculating on the possible cause. He reminded me that when he was in college, states were required to increase the legal drinking age to 21. Noncomplying states would be penalized by a 10% cut in highway funding. I decided to look back at the data I'd collected and make note of the share of hazing deaths attributed to alcohol intoxication (including, but not limited to alcohol poisoning, asphyxiation by )

I was particularly disturbed when I read the story of Tim Piazza, 
