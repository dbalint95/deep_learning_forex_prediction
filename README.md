**EUR to HUF exchange rate prediction based on daily news. 
 
 Given a number of daily news headlines of different newsletters on a day, what shall be the average EUR to HUF exchange rate the next day?

Structure of the repository:

- **datasets**: contains all the resource files that I have used and that can be used to reproduce my results

  - **datasets/eur_huf_exch_rate**: contains EUR/HUF exchange rates from 2010 (source: https://www.histdata.com)
     - raw: original downloaded .csv files
     - processed: the output of the **forex_preprocessing.ipynb** Jupyter notebook. This .csv file can be passed as an **input to the forex_predictor.ipynb** notebook
  - **datasets/daily_news**: contains daily news headlines from Reddit WorldNews Channel (/r/worldnews). They are ranked by reddit users' votes, and only the top 25 headlines are considered for a single date. (Range: 2008-06-08 to 2016-07-01) 
 (source: https://www.kaggle.com/aaron7sun/stocknews#)
  - **datasets/glove_embedding:** contains pre-trained word vectors (alias word embeddings) provided by the Stanford University (souce: https://nlp.stanford.edu/projects/glove/)
 
- **forex_preprocessing.ipynb:** serves the purpose of preprocessing the foreign exchange rate data
    - input: datasets/eur_huf_exch_rate/raw
    - output: datasets/eur_huf_exch_rate/processed
    
- **forex_predictor.ipynb:** contains the implementation of the chosen task:
    - processing of the daily news data
    - synchronization between the daily news and forex datasets
    - data analysis
    - deep learning model train, validation and test

- **doc:** contains the documentation and the slideshow files


# To reproduce the training and testing of the model:
- open the **forex_predictor.ipynb**
- if you want to **provide the input** files from your **google drive**, mount your drive by executing the first code cell, **otherwise ignore it**
- in the second code cell, set the path to the 3 input files:
    - **DAILY_NEWS_PATH** (file can be found in the repo: **datasets/daily_news/daily_news.csv**)
    - **FOREX_PATH** (file can be found in the repo: **datasets/eur_huf_exch_rate/processed/forex_data.csv**)
    - **GLOVE_PATH** (file can be found in the repo: **datasets/glove_embedding/glove.6B.100d.txt**)
- execute the notebook
