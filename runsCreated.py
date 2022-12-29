hits = int(input("Hits: "))
bb = int(input("BB(Bases on balls - walks): "))
hbp = int(input("HBP(Hits By Pitcher): "))
#singles = int(input("Singles: "))
#twoBases = int(input("2B(Second Bases): "))
#threeBases = int(input("3B(Three Bases): "))
#hr = int(input("HR(Home Runs): "))
ab = int(input("AB(At bases): "))
actualRuns = int(input("Actual runs: "))
tb = int(input("TB(Total bases): "))
gidp = int(input("GIDP(Ground Into Double Plays): "))
sf = int(input("SF(Sacrifice Flies): "))
sac = int(input("SAC(Sacrifice Bunts): "))
cs = int(input("CS(Caught Stealing): "))

#tb = singles + 2*twoBases + 3*threeBases + 4*hr
runsCreated = ((hits + bb + hbp)*tb)/(ab+bb+hbp)

diference = runsCreated - actualRuns
if diference < 0:
    diference = diference * (-1)

outs = 0.982*(ab-hits)
extraOuts = gidp + sf + sac + cs

gamesOutsUsed = outs + extraOuts

runsCreatedPerGame = runsCreated/(gamesOutsUsed/26.72)

print(f'{runsCreated} runs created\n')
print(f'{actualRuns} actual runs\n')
print(f'{diference} runs diference\n')
print(f'{outs} outs\n')
print(f'{extraOuts} extra outs\n')
print(f'{gamesOutsUsed} games outs used\n')
print(f'{runsCreatedPerGame} runs created per game\n')