from matplotlib import pyplot as plt
plt.style.use("fivethirtyeight")

minutes = [1, 2, 3, 4, 5, 6, 7, 8, 8, 9]

player1 = [1, 2, 3, 3, 4, 4, 4, 4, 5, 5]
player2 = [1, 1, 1, 1, 2, 2, 2, 3, 3, 3]
player3 = [1, 1, 1, 2, 3, 4, 2, 3, 3, 4]


labels = ["Player 1", "Player 2", "Player 3"]
colr = ['#442193', '#610293', '#9f1240']

plt.stackplot(minutes, player1, player2, player3, labels=labels, colors=colr)
plt.legend(loc = 'upper right')
plt.title("My Stack plot")
plt.xlabel("Minutes")
plt.ylabel("Player Kill Count")
plt.grid(False)
plt.tight_layout()
plt.show()