### Frequency Table Interpretation with Python
# by: Hernán Bareiro


"""
A logistics company has recorded the number of packages received according to weight ranges (in kilograms).
The following analysis aims to calculate:

1. The absolute frequency
2. The cumulative frequency 
3. The relative frequency
4. The cumulative relative frequency 

of packages in each weight range.


In order to optimize the distribution of space in the warehouse and detect load concentrations.
A statistical analysis of the data is then performed and visualizations are presented
to identify the most frequent ranges
and facilitate logistical decision making.

Weight ranges (kg):
1.00-2.99, 3.00-4.99, 5.00-7.99, 8.00-11.99, 12.00-14.99, 15.00-19.99

Number of registered packages (fi):
67, 124, 98, 23, 57, 21, 6

TOTAL packages (N);
390



*(fi) Absolute Frequency --- Number of packages that fall within a specific weight range
*(Fi) Cumulative Frecuency --- The total count of packages up to a certain weight range
*(hi) Relative Frequency ---   hi = fi / N
*(Hi) Cumulative Relative Frequency ---   Hi = Fi / N


| Weight (kg) | fi  | Fi  | hi   | Hi   |
| ----------- | --- | --- | ---- | ---- |
| 1.00-2.99   | 67  | 67  | 0.17 | 0.17 |
| 3.00-4.99   | 124 | 191 | 0.32 | 0.49 |
| 5.00-7.99   | 98  | 289 | 0.25 | 0.74 |
| 8.00-11.99  | 23  | 312 | 0.06 | 0.80 |
| 12.00-14.99 | 57  | 369 | 0.15 | 0.95 |
| 15.00-19.99 | 21  | 390 | 0.05 | 1.00 |
               {390}                    

"""


### To the Python train!

# We will use pandas and matplotlib libraries
import pandas as pd
import matplotlib.pyplot as plt


############################## PANDAS ##############################

# Data: Weight intervals and absolute frequency (fi)
data = {
    "Weight Range (kg)": ["1.00-2.99", "3.00-4.99", "5.00-7.99", "8.00-11.99", "12.00-14.99", "15.00-19.99"],
    "fi": [67, 124, 98, 23, 57, 21]
}
df = pd.DataFrame(data)  # pandas initialization!

# TOTAL number of packages (N)
N = df["fi"].sum()
print(f"Total Registered Packages: {N}\n")


# Cumulative Frequency (Fi)
df["Fi"] = df["fi"].cumsum() # .cumsum() calculates the cumulative sum of the "fi" column


# Relative Frequency (hi)
df["hi"] = (df["fi"] / N).round(2) #.round(2) makes sure we don’t get too many decimals... CLEAN!!


# Cumulative Relative Frequency (Hi)
df["Hi"] = (df["Fi"] / N).round(2)

print(df)


############################## matplotlib ##############################
 

#Create 4 vertically stacked subplots
fig, axs = plt.subplots(4, 1, figsize=(8, 10))

# Chart 1: Absolute Frequency (fi)
axs[0].bar(df["Weight Range (kg)"], df["fi"], color="skyblue", edgecolor="black")
axs[0].set_title("Absolute Frequency (fi)")
axs[0].set_ylabel("fi")
axs[0].grid(axis="y", linestyle="--", alpha=0.7)

# Chart 2: Cumulative Frequency (Fi)
axs[1].bar(df["Weight Range (kg)"], df["Fi"], color="orange", edgecolor="black")
axs[1].set_title("Cumulative Frequency (Fi)")
axs[1].set_ylabel("Fi")
axs[1].grid(axis="y", linestyle="--", alpha=0.7)

# Chart 3: Relative Frequency (hi)
axs[2].bar(df["Weight Range (kg)"], df["hi"], color="lightgreen", edgecolor="black")
axs[2].set_title("Relative Frequency (hi)")
axs[2].set_ylabel("hi")
axs[2].grid(axis="y", linestyle="--", alpha=0.7)

# Chart 4: Cumulative Relative Frequency (Hi)
axs[3].bar(df["Weight Range (kg)"], df["Hi"], color="violet", edgecolor="black")
axs[3].set_title("Cumulative Relative Frequency (Hi)")
axs[3].set_ylabel("Hi")
axs[3].set_xlabel("Weight Range (kg)")
axs[3].grid(axis="y", linestyle="--", alpha=0.7)

# Adjust spacing for a clean layout
plt.tight_layout()

# READY, STEADY, ACTION!
plt.show()



