play = True
couter = 5 

while play:
  while counter > 0:
    print (counter)
    counter -=1

play = input ("Would yoou like to play again? (y/n): ")
if play == "":
  play = True
  counter = 5
else:
  play = False
