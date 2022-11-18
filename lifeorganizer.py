import time, os

toDoList = []

def prettyPrint(priority):
  newPrintList = []
  print()
  
  if priority == "all":
    for row in toDoList:
      length = len(row) - 1
      for i in row:
        if i != row[length]:
          print(f"{i:^7}", end = " | ")
        else:
          print(f"{i:^7}")
    print()
        
  elif priority == "low":
    for row in toDoList:
      length = len(row) - 1
      for i in row:
        if i == "low":
          newPrintList.append(row)

    for row in newPrintList:
      for i in row:
        if i != row[length]:
          print(f"{i:^7}", end = " | ")
        else:
          print(f"{i:^7}")
    print()
          
  elif priority == "medium":
    for row in toDoList:
      length = len(row) - 1
      for i in row:
        if i == "medium":
          newPrintList.append(row)

    for row in newPrintList:
      for i in row:
        if i != row[length]:
          print(f"{i:^7}", end = " | ")
        else:
          print(f"{i:^7}")
    print()
          
  elif priority == "high":
    for row in toDoList:
      length = len(row) - 1
      for i in row:
        if i == "high":
          newPrintList.append(row)
          
    for row in newPrintList:
      for i in row:
        if i != row[length]:
          print(f"{i:^7}", end = " | ")
        else:
          print(f"{i:^7}")
    print()
  
  time.sleep(2)
  os.system("clear")

while True:
  print("🌟Life Organizer🌟")
  print()
  menu = input("1.Add\n2.View\n3.Remove\n4.Edit\n\n> ").strip().capitalize()
  
  if menu == "1":
    newTask = []
    task = input("What is the task? > ").strip().capitalize()
    date = input("What is the due date? > ").strip().capitalize()
    priority = input("What is the priority? ").strip().capitalize()

    newTask = [task, date, priority]

    toDoList.append(newTask)

    prettyPrint("all")
    
  elif menu == "2":
    whichView = input("1.View All\n2.View Priority\n\n> ").strip().capitalize()

    if whichView == "1":
      prettyPrint("all")
    elif whichView == "2":
      type = input("Which priority > ").strip().lower()
      if type == "low":
        prettyPrint("low")
      elif type == "medium":
        prettyPrint("medium")
      elif type == "high":
        prettyPrint("high")

    time.sleep(1)
    os.system("clear")
  
  elif menu == "3":
    removeEntry = input("Which task do you want to remove? > ").strip().lower()
    for row in toDoList:
      if row[0] == removeEntry:
        toDoList.remove(row)
    time.sleep(1)
    os.system("clear")
        
  elif menu == "4":
    prettyPrint("all")
    edit = input("Which task would you like to edit? > ").strip().lower()
    editList = []
    for row in toDoList:
      if edit in row:
        task = input("New task: ")
        date = input("New Due Date: ")
        priority = input("New Priority: ")

        editList = [task, date, priority]
        
        toDoList.remove(row)

        toDoList.append(editList)

  time.sleep(1)
  os.system("clear")
