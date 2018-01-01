Title: Deadly Brotherhoods- Hazing Deaths in the United States
Date: 2017-12-18 10:20
Modified: 2017-12-18 10:20
Category: Social Trends
Tags: web scraping, pandas, BeautifulSoup
Slug: Hazing Deaths
Authors: Rachel Ehlers
Summary: A look at hazing deaths on record in the United States


A year ago, Tim Piazza was a regular Penn State sophomore, searching for a sense of belonging. He chose to pledge Beta Theta Pi, a fraternity held in high regard, complete with a beautiful house renovated with a $10 million donation 10 years earlier. 

On February 3rd, Piazza downed an estimated 18 drinks in two hours as part of a hazing ritual. He proceeded to stumble around the fraternity house, knocking his head on multiple occasions. His most violent fall was a tumble down the stairs. Tim, who just hours before was healthy, coherent and presumably excited about his new friends, suffered a ruptured spleen, collapsed lung, and irrecoverable brain injuries. His new friends placed his limp body on a couch, "Jansported" him (put a backpack on him with enough weight to keep him from rolling on his back and choking on vomit) and left him alone after unsuccessful attempts to wake him. It wasn't until 12 hours later, when Tim's skin had turned gray, that anyone called for medical help. It was too late, and he died in the ICU.   

Surveillance cameras had been installed in the $10 million house renovation. It was by watching their footage that authorities determined how much Tim drank that night. The footage also revealed members' negligence as Tim stumbled around and repeatedly harmed himself. Some tried to cover their tracks but were caught. This included deletion of surveillance footage, text messages, and other relevant evidence. Their efforts were unsuccessful; though originally 14 members were charged with various crimes, police review of footage recovered 6 months after its deletion resulted in criminal charges for 12 more members (story [here](http://6abc.com/dozens-of-new-charges-filed-in-penn-state-frat-death/2640425/)).

Tim's story made me more curious about hazing. To get a better understanding of hazing practices (not limited to fraternities), I searched for historical data. Unfortunately, there exists no centralized database for hazing data. I scraped Wikipedia's ["List of hazing deaths in the United States"](https://en.wikipedia.org/wiki/List_of_hazing_deaths_in_the_United_States) tables with Python, using [requests](https://github.com/requests/requests) and [BeautifulSoup](https://github.com/waylan/beautifulsoup). Incomplete stories were supplemented with data from Hank Nuwer's [site](http://www.hanknuwer.com/hazing-deaths/) where applicable. 

Since the data includes only instances of hazing resulting in fatalities, it provides an incomplete picture of hazing traditions and is insufficient in measuring the prevalence of hazing as a whole. But collecting reliable data on hazing is already challenging to start with, considering victims are usually sworn to secrecy. Certainly victims of hazing are silenced the overwhelming majority of the time, but they usually survive. What's much harder to silence than a survivor is an unnecessary death. Perhaps the incomplete picture is more complete than one might think.  

My first step after finding data to scrape is to take a few minutes to identify any glaring trends. A few things stood out to me after scanning through the Wikipedia page: 
- Males account for an overwhelming majority of deaths attributed to hazing.
- Over time, traditions tend to wax and wane in their popularity. 
- Alcohol consumption as the focal point of hazing rituals is a relatively recent concept. 


Each death in the dataset is accompanied by a paragraph-long story but lack a succinct cause of death. So though many stories are very similar, it's hard to tell without reading through each one individually. I decided to add another variable, a "categorization" of the death. Categorizations were carefully chosen to reflect the nature of the rituals while avoiding overgeneralization. 




If you or someone you know feels physically, emotionally, mentally, or sexually violated as a result of hazing, please reach out. 






I was talking to my dad about the sudden shift, speculating on the possible cause. He reminded me that when he was in college, states were required to increase the legal drinking age to 21. Noncomplying states would be penalized by a 10% cut in highway funding. I decided to look back at the data I'd collected and make note of the share of hazing deaths attributed to alcohol intoxication (including, but not limited to alcohol poisoning, asphyxiation by )

I was particularly disturbed when I read the story of Tim Piazza, 
