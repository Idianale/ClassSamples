from enum  import IntEnum
class Stats(IntEnum):
     strenght = 0
     perception = 1
     endurance = 2
     rizz = 3 
     intel = 4 
     agility = 5 
     luck = 6
stats = [3,5,7,10,10,2,10]
print("PleWSE I'm strong I have " + str(stats[Stats.strenght]) + " strength")
