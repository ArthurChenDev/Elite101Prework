# Where I learned about how to find if the string contains array elements: https://realpython.com/python-string-contains-substring/ 


hoursList=["hours", "open", "days", "when", "time", "closed"]
locationList=["store", "location", "place", "map", "where", "address","closest"]
productsList=["inventory", "products", "stock", "item", "available", "have"]
priceList=["how much", "price", "dollars", "money", "cash", "card", "prices"]

time="We are open from 7am to 10pm every day."
location="Currently, we only have one location. Our address is 123 sesame street."
inv="We currently have milk, eggs, several meats, and high quality tables for sale."
cost="Our milk is $3.48 per gallon, eggs are $5 for 18 eggs, all meats are $7 per pound, and tables are $1500."

def mainInteraction():
  response=""
  while True:
    count=0;
    response= input("\nWhat can I help you with today?\n").lower()
    if response=="q":
      print("Thank you for using Shop Bot! Bye!")
      break
    if response == "list commands":
      listCommands()
      count+=1
    for hours in hoursList:
      if hours in response:
        print(time)
        count+=1
        break
    for places in locationList:
      if places in response:
        print(location)
        count+=1
        break
    for item in productsList:
      if item in response:
        print(inv)
        count+=1
        break
    for price in priceList:
      if price in response:
        print(cost)
        count+=1
        break


    if count == 0:
      print("I'm sorry. I was unable to understand your request. Please enter \"list commands\" to view a full list of commands. ")
    

def listCommands():
  print("Enter \"q\" to quit \nEnter \"prices\" for prices \nEnter \"inventory\" for a list of our inventory\nEnter \"hours\" for our hours\nEnter \"location\" for our locations")

def welcome():
  name=input("Hi! What is your name? ")
  print(f"Hi {name}! Welcome to Store Chatbot!\n\nI can help with store hours, our locations, available products, and prices.")
  print("\nWhen you would like to exit, please enter \"q\" to quit \n")
  mainInteraction()



welcome()