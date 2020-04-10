import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data = pd.read_csv("us-states.csv")
a = data.groupby(data["date"]).aggregate({'cases':'sum'})

fig = plt.figure()

ax = fig.add_axes([0,0,2,2])
ax.set_xlabel("The # of days")
ax.set_ylabel("Cases")

x = np.arange(len(a["cases"]))
y = a["cases"]
ax.plot( x , y )
ax.scatter(x,y)

ax.set_title("The growth of coronavirus in america")
fig.savefig("corogrowth.png", bbox_inches="tight")