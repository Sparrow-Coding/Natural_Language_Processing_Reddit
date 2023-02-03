Problem Statement:
The goal of this project is to use data collected from two subreddits(AmITheAsshole and RelationshipAdvice)
and predict which subreddit a post is most likely to be based off it's keywords. The models to be used will be
Naive bayes, Logistic Regression, KNN. The determintion of success will be based on how accurate our models
can predict and this can be used for reddit moderators who may feel like content is misguided and is better suited 
for another subreddit.

Data Collection: 
The goal is to use a minimum of 10,000 post so initally 10,000 post were scraped from each subreddit. 
This was a useful approach as I was able to use about 6,000 post for my data analysis. 
The data was initally stored as a csv file
and read in later to be concated into a final csv file that will be used for my analysis. A function was written
to scrape the data and pipelines were used for model devlopment. Data scraping was conducted every 5 seconds to
not overwhelem the server.

Data Cleaning & EDA:
Missing values were attempted to be found using unditt.com 
1 post per author was allowed but overall, empty values were ultimately dropped. I will be able to
predict either AmITheAsshole or RelationShip advice as these subreddits have common words in their post but
a few unique words. Polarity will also play a role in helping predict the subreddit.

Preprocessing & Modeling: 
Data was converted into a dataframe so it can be read and analyzed. Methods such as CountVectorizing with stop words, 
lemmatization were implemented to find signifcant words that can help predict the subreddit.

Evaluation and Conceptual Understanding:
KNN had the highest accuracy score which will be a better model to use for future projects. Some reddits can 
fit int multiple categories so it will be a nice feature to have a reddit post become eligible for multiply 
comments if a polarity or word score is hit.

Conclusion and Recommendations:
In summation, KNN yielded the best results as to predicting 
AmItheAsshole or RelationshipAdvice. Although both reddits had 14000 common words, based on their unquie words 
and polarity, it is possible to accurately predict a subreddit.
In the future, these predictions can help a clustering problem in terms of providing data of a post and seeing
if it is similiar to it's original subreddit. This can create growth for other reddit accounts and introuduce 
users to other subreddits thus making the platform more expolarable.