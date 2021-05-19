import pandas as pd
import matplotlib.pyplot as plt
from mplsoccer import Pitch, VerticalPitch
import seaborn as sns
import cmasher as cmr

df = pd.read_csv('C:\Football Analytics\CSV Data\Cavani.csv')

# Create Pitch
fig, ax = plt.subplots(figsize=(16, 11))
fig.set_facecolor('#22312b')
ax.patch.set_facecolor('#22312b')

pitch = Pitch(pitch_type='opta', orientation='horizontal', line_zorder=2,
              pitch_color='#22312b', line_color='#cfcfcf', figsize=(16, 11),
              constrained_layout=False, tight_layout=True)

pitch.draw(ax=ax)

# Creating False label variables because if plotting through loop, keys of legend repeat themselves
label_added1 = False
label_added2 = False
label_added3 = False
label_added4 = False

# Loop and Plot
for n in range(len(df['x'])):
    if df['outcome'][n] == 'Goal':
        if not label_added1:
            plt.scatter(df['x'][n], df['y'][n], color='yellow', s=200, marker='x', linewidth=4, label='Goals')
            label_added1 = True
        else:
            plt.scatter(df['x'][n], df['y'][n], color='yellow', s=200, marker='x', linewidth=4)
    if df['outcome'][n] == 'Assist':
        if not label_added2:
            plt.plot([df['x'][n], df['endx'][n]], [df['y'][n], df['endy'][n]], color='#6495ed', linewidth=4,
                     label='Assists')
            label_added2 = True
            plt.scatter(df['x'][n], df['y'][n], color='#6495ed', s=200)
        else:
            plt.plot([df['x'][n], df['endx'][n]], [df['y'][n], df['endy'][n]], color='blue', linewidth=4)
            plt.scatter(df['x'][n], df['y'][n], color='#6495ed', s=200)
    if df['outcome'][n] == 'Successful':
        if not label_added3:
            plt.plot([df['x'][n], df['endx'][n]], [df['y'][n], df['endy'][n]], color='green', label='Successful Passes',
                     linewidth=3)
            label_added3 = True
            plt.scatter(df['x'][n], df['y'][n], color='green')
        else:
            plt.plot([df['x'][n], df['endx'][n]], [df['y'][n], df['endy'][n]], color='green', linewidth=3)
            plt.scatter(df['x'][n], df['y'][n], color='green')
    if df['outcome'][n] == 'Unsuccessful':
        if not label_added4:
            plt.plot([df['x'][n], df['endx'][n]], [df['y'][n], df['endy'][n]], color='red', label='Unsuccessful Passes',
                     linewidth=3)
            label_added4 = True
            plt.scatter(df['x'][n], df['y'][n], color='red')
        else:
            plt.plot([df['x'][n], df['endx'][n]], [df['y'][n], df['endy'][n]], color='red', linewidth=3)
            plt.scatter(df['x'][n], df['y'][n], color='red')

plt.legend(loc='upper left')
plt.xlim(0, 100)
plt.ylim(0, 100)

plt.title('Cavani against Roma - First Leg', color='white', size=18)
plt.savefig('C:\Football Analytics\Visuals\Player Summary - Cavani.png')