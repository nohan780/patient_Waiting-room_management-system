class Patient:
  def __init__(self, elem, next, prev):
    self.elem = elem
    self.next = next
    self.prev = prev



class WRM:
  def __init__(self):
    self.n = Patient(None, None, None)
    self.n.next = self.n
    self.n.prev = self.n
    self.tail = self.n
    print("**Welcome to Waiting Room Management System** \n")
  def RegisterPatient(self, id, name, age, blood):
    new = Patient(name, self.n, self.tail)
    self.tail.next = new
    self.tail = self.tail.next
    self.n.prev = self.tail
    print("Successfully registered a patient \n")
    return self.n
  def ServePatient(self):
    if self.n.next == self.n:
      print("No patient to be served!!! \n")
    else:
      delt_node = self.n.next
      delt_prev = delt_node.prev
      delt_next = delt_node.next
      delt_prev.next = delt_next
      delt_next.prev = delt_prev
      delt_node.next = None
      delt_node.prev = None
      print(f"{delt_node.elem} is served! \n")
  def CancelAll(self):
    if self.n.next == self.n:
      print("There's no patient in the Waiting room!!! \n")
    else:
      self.n.next = self.n
      self.n.prev = self.n
      self.tail = self.n
      print("All appointments are cancelled!!!! \n")

  def CanDoctorGoHome(self):
    if self.n.next == self.n and self.n.prev == self.n:
      print("Yes \n")
    else:
      print("No \n")


  def ShowAllPatient(self):
    temp = self.n.next
    if temp == self.n:
      print("No patient in the waiting room!!! \n")
    else:
      while temp != self.n:
        print(temp.elem, end= " ")
        temp = temp.next
      print("\n")
  def ReverseTheLine(self):
    if self.n.next == self.n:
      print("There's no patient!!! \n")
    else:
      self.n.next, self.n.prev = self.n.prev, self.n.next
      temp = self.n.next
      while temp != self.n:
        temp.next, temp.prev = temp.prev, temp.next
        temp = temp.next
      print("done! \n")

chck = True
a = WRM()
while chck:
  print("==Choose an option==")
  print("1. Register Patient")
  print("2. Serve a patient")
  print("3. Show all patient")
  print("4. Can doctor go home?....")
  print("5. Cancel all appointment...")
  print("6. Reverse the line....")
  print("7. Exit")
  print("************************")
  num = int(input("Enter your choice: "))
  if num == 1:
    print("executing Register Patient...")
    id = int(input("Enter ID: "))
    name = input("Enter Name: ")
    age = int(input("Enter Age: "))
    blood = input("Enter blood group: ")
    new = a.RegisterPatient(id,name,age,blood)
  elif num == 2:
    print("executing Serve a patient...")
    serve = a.ServePatient()
  elif num == 3:
    print("executing Show all patient...")
    show = a.ShowAllPatient()
  elif num == 4:
    print("executing Can doctor go home?...")
    can = a.CanDoctorGoHome()
  elif num == 5:
    print("executing Cancel all appointment...")
    cancel = a.CancelAll()
  elif num == 6:
    print("executing Reverse the line....")
    r = a.ReverseTheLine()
  elif num == 7:
    print("Thank you for using Waiting room management system!!!")
    print("EXITING!!!! \n")
    break
  else:
    print("No such option!!! \n")



