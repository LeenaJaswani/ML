# The example function below keeps track of the opponent's history and plays whatever the opponent played two plays ago. It is not a very good player so you will need to change the code to pass the challenge.


steps = {}

def player(prev_play, opponent_history=[]):


  n = 6

  if prev_play in ["R","P","S"]:
    opponent_history.append(prev_play)

  guess = "R" 

  if len(opponent_history)>n:
    move = "".join(opponent_history[-n:])

    if "".join(opponent_history[-(n+1):]) in steps.keys():
      steps["".join(opponent_history[-(n+1):])]+=1
    else:
      steps["".join(opponent_history[-(n+1):])]=1

    possible =[move+"R", move+"P", move+"S"]

    for i in possible:
      if not i in steps.keys():
        steps[i] = 0

    predict = max(possible, key=lambda key: steps[key])

    if predict[-1] == "P":
      guess = "S"
    if predict[-1] == "R":
      guess = "P"
    if predict[-1] == "S":
      guess = "R"


  return guess