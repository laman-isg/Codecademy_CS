last_sem_gradebook = [["politics", 80], ["latin", 96], ["dance", 97], ["architecture", 65]]

# Your code below: 
subjects = ["physics", "calculus", "poetry","history"]
grades = [98, 97, 85, 88]
current_sem_gradebook = [
  ["physics",	98],
  ["calculus",	97],
  ["poetry",	85],
  ["history",	88]
]
print(current_sem_gradebook)

current_sem_gradebook.append(["computer science", 100])
print(current_sem_gradebook)
current_sem_gradebook.append(["visual arts", 93])
print(current_sem_gradebook)

current_sem_gradebook[5][1] += 5
print(current_sem_gradebook)

current_sem_gradebook[2].remove(current_sem_gradebook[2][1])
print(current_sem_gradebook)
current_sem_gradebook[2].append("Pass")
print(current_sem_gradebook)

full_gradebook = last_sem_gradebook + current_sem_gradebook
print(full_gradebook)
