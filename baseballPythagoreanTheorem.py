runsScored = int(input("Runs Scored: "))
runsAllowed = int(input("Runs Allowed: "))
wins = int(input("Wins: "))
losses = int(input("Losses: "))
exp = 1.9
r = runsScored/runsAllowed
percentageGamesWons = r ** exp/(r ** exp + 1)
totalGames = wins + losses
winRatio = wins/totalGames
absoluteError = percentageGamesWons - winRatio
if absoluteError < 0:
   absoluteError = absoluteError * (-1)

print(f'{round(percentageGamesWons, 3)} predicted win percentage')
print(f'{round(winRatio, 3)} win percentage')
print(f'{round(absoluteError, 3)} absolute error')

