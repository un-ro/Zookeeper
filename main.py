from zoo import *

if __name__ == "__main__":
   zoo = zoo()
   animals = [zoo.camel(), zoo.lion(), zoo.deer(), zoo.goose(), zoo.bat(), zoo.rabbit()]
   user_input = input("Please enter the number of the habitat you would like to view: > ")
   while user_input != "exit":
      try:
         print(animals[int(user_input)])
      except IndexError:
         print("Empty Animals")
      user_input = input("Please enter the number of the habitat you would like to view: > ")
   print("See you later!")
   