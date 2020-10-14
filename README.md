# mlb-analysis

# Overview
The 2020 MLB season was cut shortened from 162 games to just 60 games due to Covid. I wanted to build a model to project how the teams would have done if they were able to play the remaining 102 games. This was my first experience using web scraping to gather data, as well as my first time building linear regression models with python. 

# Workflow
I scraped data from [Baseball Reference](https://www.baseball-reference.com/), grabbing yearly statistics from every team since 1950. I used these stats to create and analyze different linear regression models for predicting MLB win totals. I used "pure stats" like singles, doubles, triples, stolen bases etc. as well as "engineered stats" like On-Base Percentage, Batting Average, and Slugging Percentage. I then used this model to project out the remainder of the 2020 MLB season. 

# Repo
All of the Work is done in Python notebooks within the `work_and_analysis` folder. The web scraping was done in the [Scraping File](./work_and_analysis/Team_Season_Data_Scraping.ipynb). The main workflow can be found and followed within the [Main_WorkFlow File](./work_and_analysis/Main_WorkFlow.ipynb). I experimented with different models and analysis methods within the [Scratch Work Folder](./work_and_analysis/scratch_work), feel free to explore that if you want, but all the important stuff made it into the main workflow file. 

A presentation of my findings can be found in a pdf file inside of the presentation folder.

# Findings
Ultimately I was able to create a model using a teams Batting Average, On Base Percentage, and Slugging Percentage to predict their win total within 4 wins on average. I found that the Marlins were the luckiest team of 2020, and if it weren't for the shortened season and expanded playoff bracket they would have likely had a sub .500 record and missed the playoffs. Also my model predicted the Dodgers to finish 2020 with 119 wins, which would have been a Major League record.

I made an web application for one of my models (using just pure stats), you can play around with it [here](https://mlb-model-app.herokuapp.com/).
