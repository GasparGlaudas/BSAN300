# scatter plots visually represents a data set as a collection

# %%
import matplotlib.pyplot as plt
import stats

#prepare the data
positions = list(range(1, 101))
numbers = stats.getRandomList(100, 1, 100, unique = True)

# set up and show the scatter
plt.scatter(positions, numbers, color = "purple", marker = ".")
plt.title("Scatter Plot of Unique Random Numbers from 1..100")
plt.xlabel("Position")
plt.ylabel("Random number")
plt.show()



# %%
