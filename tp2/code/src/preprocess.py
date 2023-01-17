'''
    Contains some functions to preprocess the data used in the visualisation.
'''
import pandas as pd
from modes import MODE_TO_COLUMN


def summarize_lines(my_df):
    
    '''
        Sums each player's total of number of lines and  its
        corresponding percentage per act.

        The sum of lines per player per act is in a new
        column named 'PlayerLine'.

        The percentage of lines per player per act is
        in a new column named 'PlayerPercent'

        Args:
            my_df: The pandas dataframe containing the data from the .csv file
        Returns:
            The modified pandas dataframe containing the
            information described above.
    '''
    # TODO : Modify the dataframe, removing the line content and replacing
    # it by line count and percent per player per act
    my_df['PlayerLine'] = my_df.groupby(by=['Player', 'Act'])['Line'].transform('count')
    my_df['PlayerPercent'] = my_df.groupby(by=['Act'])['Line'].transform('count')
    my_df['PlayerPercent'] = my_df['PlayerLine'] / my_df['PlayerPercent'] * 100
    my_df = my_df.drop_duplicates(subset=['Player', 'Act']).reset_index(drop=True)

    return my_df


def replace_others(my_df):
    '''
        For each act, keeps the 5 players with the most lines
        throughout the play and groups the other players
        together in a new line where :

        - The 'Act' column contains the act
        - The 'Player' column contains the value 'OTHER'
        - The 'LineCount' column contains the sum
            of the counts of lines in that act of
            all players who are not in the top
            5 players who have the most lines in
            the play
        - The 'PercentCount' column contains the sum
            of the percentages of lines in that
            act of all the players who are not in the
            top 5 players who have the most lines in
            the play

        Returns:
            The df with all players not in the top
            5 for the play grouped as 'OTHER'
    '''
    # TODO : Replace players in each act not in the top 5 by a
    # new player 'OTHER' which sums their line count and percentage

    # Get the top 5 players per act
    my_df.drop(columns=['Scene', 'Line'], inplace=True)
    top_5 = my_df.groupby(by=['Player'])['PlayerLine'].sum().sort_values(ascending=False).head(5)
    my_df['Player'] = my_df['Player'].apply(lambda x: x if x in top_5 else 'OTHER')
    my_df = my_df.groupby(by=['Act', 'Player']).sum().reset_index()
    my_df['LineCount'] = my_df['PlayerLine']
    my_df['LinePercent'] = my_df['PlayerPercent']
    my_df.drop(columns=['PlayerLine', 'PlayerPercent'], inplace=True)
    return my_df

def clean_names(my_df):
    '''
        In the dataframe, formats the players'
        names so each word start with a capital letter.

        Returns:
            The df with formatted names
    '''
    # TODO : Clean the player names
    my_df['Player'] = my_df['Player'].apply(lambda x: x.capitalize())
    return my_df
