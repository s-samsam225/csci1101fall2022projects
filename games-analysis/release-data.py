import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("game-ratings-by-release-dates.csv")

#Clean up the data
df["first_release_data"] = pd.to_datetime(df["first_release_date"])

#Analyze data through visulization
plt.scatter(df["first_release_data"], df["critic_rating_value"], color = "blue", label = "Critic ratings")
plt.scatter(df["first_release_data"], df["user_rating_value"], color = "red", label = "User Rating")

plt.legend(loc = "upper left")

plt.show()
