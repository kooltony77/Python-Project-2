 # Hero's: Knight , Blacksmith , Young King
print()
# Intro:
print("Our story takes place in a Kingdom known as 'Yaggsil' where three warriors must choose the right decisions..You decide will the hero's fail or succeed!!! ")

print()

# choose scene
print("The dark king army of orcs has broke into the castle , you...")
print()
print("A. Grab your sword and join your fellow knights to fight off the orcs.")
print()
print("B. Go to the blacksmith and grab the ancient sword of elves. ")
print()
print("C. Run and grab your horse to lead the charge with your king.")
scenario = input("Which option will you choose? Please select option A - C: ")

print()

# Knight Story
if(scenario == "a"):
  print("You grabbed your sword and start fighting. ")
  knightSelection = input("How many orcs do you kill?: ")
  if knightSelection == "100":
    print("Well done, you won the battle!!")
  else:
    print("The orcs survived and eat you!")

  print()
  
  #Blacksmith presents a challenge
elif (scenario == "b"):
  print("You grab the ancient sword but notice you need to solve the riddle. ")
  blackSmith = input("What is 2 + 4? ")
  if blackSmith == "6":
   print("You unlocked the full power of the sword destroying the entire orc army.")
  else:
   print("You were unable to unlock the full power of the sword so you died in battle.")

print()

if (scenario == "c"):
  print("You run and grab your armor and your hourse but the stable is locked. ")
  king = input("Please enter 9: ")
  if king == "9":
    print("You unlocked the stable and join the charge with your king destroying all invading orcs. ")
  else:
    print("You was unable to unlock the stable thus burning alive. ")