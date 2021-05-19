import matplotlib.pyplot as plt
import seaborn as sns
from mplsoccer import Pitch, VerticalPitch
import pandas as pd
import cmasher as cmr

df = pd.read_csv("C:\Football Analytics\CSV Data\Kante.csv")

fig,ax = plt.subplots(figsize=(16,11))
fig.set_facecolor('black')
ax.patch.set_facecolor('black')

pitch = Pitch(pitch_type='opta', orientation='horizontal', line_zorder = 2,
              pitch_color='black', line_color='#cfcfcf', figsize=(16,11),
              constrained_layout=False, tight_layout=True)

pitch.draw(ax=ax)

kde = sns.kdeplot(df['x'], df['y'], levels = 800, thresh = 0.3, shade = True, shade_lowest = True, cmap = cmr.cosmic)

plt.xlim(0,100)
plt.ylim(0,100)
plt.title("Heatmap of N'Golo Kante against Real Madrid", color = 'white', size = 18)
plt.savefig("C:\Football Analytics\Visuals\Kante.png")