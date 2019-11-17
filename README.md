# deep_learning_university_course
Repository to store all related files to the Deep Learning university course, especially implementation and the source files for the big (semester) homework.
 
 Summary of the chosen task:
 
 EUR to HUF exchange rate prediction based on daily news.
 
 Given a fixed number of headlines of different newsletters on a day, what shall be the average EUR/HUF exchange rate the next day?
 - **datasets/eur_huf_exch_rate**: contains EUR/HUF exchange rates from 2010 (source: https://www.histdata.com)
 - **datasets/daily_news**: contains news headlines from Reddit WorldNews Channel (/r/worldnews). They are ranked by reddit users' votes, and only the top 25 headlines are considered for a single date. (Range: 2008-06-08 to 2016-07-01) 
 (source: https://www.kaggle.com/aaron7sun/stocknews#)
 - **datasets/glove_embedding:** contains pre-trained word vectors (aka word embeddings) provided by the Stanford University (souce: https://nlp.stanford.edu/projects/glove/)
 
In the future, I might try to improve the performance of the model by parsing news from additional websites, like:
- https://inshorts.com/en/read/ 
- https://dailynewshungary.com/
- https://www.kormany.hu/en/news?page=1  