import pandas as pd

appearances_df = pd.read_csv('quiz/data/squad/appearances.csv')
players_df = pd.read_csv('quiz/data/squad/players.csv')

merged_df = appearances_df.merge(players_df[['player_id', 'position']], on='player_id', how='left')
merged_df.to_csv('merged_appearances.csv', index=False)
