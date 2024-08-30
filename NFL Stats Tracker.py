#Import libraries
import random
import time
import pandas as pd
import numpy as np

#Create list of seasons to download
seasons=[str(season) for season in range(2010,2023)]
print(f'number of seasons={len(seasons)}')

#Create lists of team abbreviations
team_abbrs=['crd','atl','rav','buf','car','chi','cin','cle','dal',
            'den','det','gnb','htx','clt','jax','kan','sdg','ram','rai',
            'mia','min','nwe','nor','nyg','nyj','phi','pit','sea','sfo','tam','oti','was']
print(f'number of teams={len(team_abbrs)}')

#Create an empty database to append
nfl_df=pd.DataFrame()

#Iterate through the seasons
for season in seasons:
    #Iterate through the teams
    for team in team_abbrs:

        #Step 1: Set the URL
        url='https://www.pro-football-reference.com/teams/'+team+'/'+season+'/gamelog/'
        print(url)

        #Step 2: Get offensive stats
        off_df=pd.read_html(url,header=1,attrs={'id':'gamelog'+season})[0]

        #Step 3: Get defensive stats
        def_df=pd.read_html(url,header=1,attrs={'id':'gamelog_opp'+season})[0]

        #Step 4: Concatenate the two dataframes
        team_df=pd.concat([off_df,def_df],axis=1)

        #Insert the season into the dataframe
        team_df.insert(loc=0,column='Season',value=season)

        #Insert team column
        team_df.insert(loc=2,column='Team',value=team.upper())

        #Step 5: Concatenate the team gamelog to the aggregate dataframe
        nfl_df=pd.concat([nfl_df,team_df],ignore_index=True)

        #Pause program to abide by website rules 
        time.sleep(random.randint(4,5))

        #Display dataframe
        print(nfl_df)

        #Save downloaded data to CSV file
        nfl_df.to_csv('NFL_Gamelogs_2010-2023.csv',index=False)

        #Display dataframe
        print(nfl_df)






