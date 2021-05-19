import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.spatial import ConvexHull
from scipy import stats
import matplotlib as mpl
from mplsoccer import Pitch, VerticalPitch
from highlight_text import fig_text

df = pd.read_csv("C:\Football Analytics\CSV Data\BrunoPogba.csv")

# Create Pitch
fig, ax = plt.subplots(figsize=(16, 11))
fig.set_facecolor('black')
ax.patch.set_facecolor('black')

pitch = Pitch(pitch_type='opta', orientation='horizontal', line_zorder=2,
              pitch_color='black', line_color='#cfcfcf', figsize=(16, 11),
              constrained_layout=False, tight_layout=True)

pitch.draw(ax=ax)

# Get a list of players from data frame as it will help with loops while plotting for more than one player
players = df['player']

# Filter according to player, then eliminate outliers from the pass data set, and plot passes within limits
df1 = df[df['player'] == 'Bruno Fernandes']
df1 = df1[(np.abs(stats.zscore(df1[['x', 'y']])) < 2)]
plt.scatter(df1['x'], df1['y'], c='white', label='Fernandes Pass Points')

# After filtering all pass values, put them in a list that can later be used to loop when defining boundaries of Hull
points = df1[['x', 'y']].values

# Importing stats into indices of Hull
hull = ConvexHull(df1[['x', 'y']])

# Plotting Hull
for i in hull.simplices:
    plt.plot(points[i, 0], points[i, 1], '#dc143c')
    plt.fill(points[hull.vertices, 0], points[hull.vertices, 1], c='#dc143c', alpha=0.02)

# Plotting for another player without comments -

df2 = df[df['player'] == 'Paul Pogba']
df2 = df2[(np.abs(stats.zscore(df2[['x', 'y']])) < 2)]
plt.scatter(df2['x'], df2['y'], c='#ffd700', label='Pogba Pass Points')

pog_points = df2[['x', 'y']].values

hull2 = ConvexHull(df2[['x', 'y']])

for n in hull2.simplices:
    plt.plot(pog_points[n, 0], pog_points[n, 1], '#ee82ee')
    plt.fill(pog_points[hull2.vertices, 0], pog_points[hull2.vertices, 1], c='#ee82ee', alpha=0.02)

fig_text(s="Territory covered by <Fernandes> and <Pogba> against Aston Villa", x=0.27, y=0.9, fontsize=20,
         color='white',
         highlight_textprops=[{"color": '#dc143c'}, {"color": '#ee82ee'}])
ax.text(0.03, 0.0061, '@PanditMUFC x @TheUnitedDevils', verticalalignment='bottom', horizontalalignment='left',
        transform=ax.transAxes, color='#6495ed', fontsize=14)
plt.legend(loc='upper left', frameon=True, facecolor='black', labelcolor='white')
plt.savefig("C:\Football Analytics\Visuals\BrunoPogba.png")