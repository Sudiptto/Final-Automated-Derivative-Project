import random # import the random number module and this will generator random numbers and can pick from a list of characters in an array
import time # importing the time which has the time.time() which grabs the time and this is used for all uses of time such as creating a timer 
start = input("Hello! Welcome to auto Derivative. Press Enter for more information") # start with an input that promts the user to enter for more info 

info = input("Note: ^ is a symbol for exponent so x^2 is x squared. Press enter to proceed. Also find the derivative then plug in the given x value ") # a derivative is a calculus concept that is used, it is the rate of change of a function given respect to time. 
name = input("Type name: ") # grabing the name of the user and storing it in a name variable
time_length = int(input("Please type the amount of seconds you want per question: ")) # Use an int since the user types in a number for the amount of time they want
options = input("Type either 'Chain', 'Exponent', 'Product' or 'Quotient' (not failure to do so properly will result in issues): ") # promts the user for different choices, each choice are different methods of finding the derivative based on the problem format. 
if options == 'Exponent': # if statement that will run if the user types in exponent 
  total_start = time.time() # starts the timer and it will save in total_start. This will be used to deterime the total amount of time the user spent doing problems
  num_questions = 0 # questions at 0 but will add +1 for each time the user does a question
  incorrect = 0 # if an answer is a wrong than +1 is added and this is the initial value
  correct = 0 # if an answer ia right than +1 is added and this is the initial value of the amount wrong 
  while True: # this is a while statement that will run infinetely since the boolean True cannot change so it will keep on running
    c = random.randint(1,4) # c means coefficent, generate random integers between 1 - 4, no decimal since it is randint 
    e = random.randint(1,4) # e means exponent, generate random integers between 1 - 4
    x = random.randint(1,3) # x value, assigns randon number
    start = time.time() # start the time and this will save it to this variable so each time it loops a new time will be recorded and this will be used to deteirme the amount of time per question 
    equation =  (str(c) + 'x' + '^' + str(e)) # this is the equation taht will randomly be generated and string concatenation is used, for example the variable c is a random integer so it cannot be added to a string so it has to be changed to a string 
    solution = (c * e) * ((x ** (e-1))) # deterimes the solution of the program because it uses power rule. (Calculus concept) By multiplying the coefficent to the exponenet and then multiply that to the x value by e -1
    correct_answers = [] # create an empty LIST that will collect all the correct answers that the user has 
    incorrect_answers = [] # empty list that will collect all the incorrect answers 
    answer = int(input("Find the derivative and then plug in the given x value: " + equation + " at x = " + str(x) + " Please type your answer: " )) # this will show the question and will grab the users answer which is an integer and it will stored in the answer variable to be used for comparison with the legitamte answer later on 
    end = time.time() # end the time when the user gets done withe problem
    total_time = int(end - start) # calculate the total time spent on problem by sub
    if (answer == solution) and (total_time < time_length): # deterimes if the answer set by the user equals the solution that was created earlier and the 'and' is a comparison operator, if the user is under their set time and correct than they will move on
      print("Congrats") # will print out if the got correct
      continue_derivative = input("Type 'Stop' if you want to stop the problems. If not ignore and press enter ") # if the user wants to stop they can type 'Stop', value stored in continue derivative if not they ignore
      correct +=  1 # add one since correct
      num_questions += 1 # add one since they got a question corret
      correct_answers.append(answer) # the .append() method will add the correct answers into the empty list everytime and since the list is outside of the while loop it will not be resent each time, this is helpful as it stores data hence being called a data structure.  Store all correct answers 
      if continue_derivative == 'Stop': # if they print stop than the next line will run, if statement. 
        break # will break out of the while loop and print out the statistics that are outside of the while loop
    else: # else if they get it incorrect or did not meet the time requriment 
      incorrect += 1 # add one to the talley since they got it wrong
      num_questions += 1 # add one since they did a questioj
      print("Try another! Make sure not to reach your time limit! ") # will print a statement out 
      print("The answer is: " + str(solution)) # state the solution and uses str due to string concatenation 
      print(" ") # create a space so it isn't crowded on the user side 
      incorrect_answers.append(answer) # the .append() method will add the correct answers into the empty list everytime and since the list is outside of the while loop it will not be resent each time, this is helpful as it stores data hence being called a data structure. This will store all the incorrect answers 
      print("How to solve: " + equation + "→ First multiply the exponent by the coefficient. Then subtract 1 from the exponent. This means completion of derivative. Then plug in x and simply use pemdas") # will give help to solve the equation. 
      continue_derivative = input("Type 'Stop' if you want to stop the problems. If not ignore and press enter ") # if they print stop than the next line will run, if statement. 
      if continue_derivative == 'Stop': # if they print stop than the next line will run, if statement
        break # will break out of the while loop and print out the statistics that are outside of the while loop
   
  def ratio(c, q): # ratio function 
    return c / q # return function, this will return the value of c / q and ca be used in future problems.
    


if options == 'Product': # if the user says 'Product' they will get th commands below 
  total_start = time.time() # starts the timer and it will save in total_start. This will be used to deterime the total amount of time the user spent doing problems
  num_questions = 0 # questions at 0 but will add +1 for each time the user does a question
  incorrect = 0 # if an answer is a wrong than +1 is added and this is the initial value
  correct = 0 # if an answer ia right than +1 is added and this is the initial value of the amount wrong 
  correct_answers = [] # create an empty LIST that will collect all the correct answers that the user has 
  incorrect_answers = [] # empty list that will collect all the incorrect answers 

  while True: # this is a while statement that will run infinetely since the boolean True cannot change so it will keep on running
    c = random.randint(1,3) # c means coefficent generate random integers between 1 - 3, no decimal since it is randint 
    e = random.randint(1,3) # e means exponent generate random integers between 1 - 3
    x = random.randint(1,3) # x value, assigns an random number
    c1 = random.randint(1,3) # second coefficent, will assign a random number for the second coefficient between a range of 1 - 3, only integer
    e1 = random.randint(1,3) # second exponent, will assign the value e1 a random number from 1 - 3, only integers
    start = time.time() # start the time and this will save it to this variable so each time it loops a new time will be recorded and this will be used to deteirme the amount of time per question 
    equation = ('(' +str(c) + 'x^' + str(e) + ')(' + str(c1) + 'x^' + str(e1) + ')') # this is the equation taht will randomly be generated and string concatenation is used, for example the variable c is a random integer so it cannot be added to a string so it has to be changed to a string 
    solution = ((c * e) * ((x ** (e-1)))) * ((c1 * (x ** e1))) + ((c * (x ** e)) * (c1 * e1 * (x ** (e1 -1)))) # solution to the problem and it uses product rule which is more advanced as it deals with multiple values istead of one like the other program 
    
    answer = int(input("Find the derivative and then plug in the given x value(use product rule): " + equation + " at x = " + str(x) + " Please type your answer: " )) # this will show the question and will grab the users answer which is an integer and it will stored in the answer variable to be used for comparison with the legitamte answer later on 
    end = time.time()  # end the time when the user gets done withe problem
    total_time = int(end - start) # calculate the total time by subracting the end by the start since end is greater and then running it through an int so it gets rounded
    if (answer == solution) and (total_time < time_length): # deterimes if the answer set by the user equals the solution that was created earlier and the 'and' is a comparison operator, if the user is under their set time and correct than they will move on
      print("Congrats") # will display Congrats
      continue_derivative = input("Type 'Stop' if you want to stop the problems. If not ignore and press enter ") # if the user wants to stop they can type 'Stop', value stored in continue derivative if not they ignore
      correct += 1 # add one since the user got it correct 
      num_questions += 1 # add one since the user did question 
      correct_answers.append(answer) # the .append() method will add the correct answers into the empty list everytime and since the list is outside of the while loop it will not be resent each time, this is helpful as it stores data hence being called a data structure. 
      if continue_derivative == 'Stop': # if they print stop than the next line will run, if statement.
        break # will break out of the while loop and print out the statistics that are outside of the while loop
    else: # else statement if the answer was not correct or the duration the user said was greater 
      incorrect += 1 # add one since it was wrong 
      num_questions += 1 # add one since it was question 
      print('Solution: ' + str(solution)) # state the solution and uses str due to string concatenation 
      print("Try another! Make sure not to reach your time limit! ") # encouragmenet and gives typs, will display taht emssage on the screen 
      incorrect_answers.append(answer) # the .append() method will add the correct answers into the empty list everytime and since the list is outside of the while loop it will not be resent each time, this is helpful as it stores data hence being called a data structure. This will store all the incorrect answers 
      continue_derivative = input("Type 'Stop' if you want to stop the problems. If not ignore and press enter ") # if they print stop than the next line will run, if statement.
      if continue_derivative == 'Stop':# if they print stop than the next line will run, if statement
        break# will break out of the while loop and print out the statistics that are outside of the while loop


if options == 'Chain': # if the user says 'Chain' they will get th commands below 
  total_start = time.time() # starts the timer and it will save in total_start. This will be used to deterime the total amount of time the user spent doing problems
  num_questions = 0 # variable that stores the number of questions correct, starts off at 0 since no problem yet
  incorrect = 0  # if an answer is a wrong than +1 is added and this is the initial value
  correct = 0 # if an answer ia right than +1 is added and this is the initial value of the amount wrong 
  correct_answers = [] # create an empty LIST that will collect all the correct answers that the user has 
  incorrect_answers = [] # empty list that will collect all the incorrect answers 
  while True:# this is a while statement that will run infinetely since the boolean True cannot change so it will keep on running
    c = random.randint(1,2) # c means coefficent, generate random number between 1 and 2, random integer specifically using the randint method
    e = random.randint(1,2) # e means exponent, generate random number between 1 and 2, random integer specifically using the randint method
    x = random.randint(1,2) # x value, assigns, generate random number between 1 and 2, random integer specifically using the randint method
    d = random.randint(1,2) # d means outside coefficent, generate random number between 1 and 2, random integer specifically using the randint method
    m = random.randint(1,2) # m means outside exponent, generate random number between 1 and 2, random integer specifically using the randint method
    equation = (str(d) + '(' + str(c) + 'x' + '^' + str(e) + ')' + '^' + str(m)) # this is the equation taht will randomly be generated and string concatenation is used, for example the variable c is a random integer so it cannot be added to a string so it has to be changed to a string 
    solution = ((d * m) * (c * (x ** e))) * ((c * e) * ((x ** (e-1)))) # solution to the problem and it uses product rule which is more advanced as it deals with multiple values istead of one like the other program, uses chain rule to solve
    start = time.time()
    user_chain_answer = int(input("Make sure to use chain rule then plug in x after finding derivative! Type the answer to " + equation + " when x is " + str(x) + ": ")) # this will show the question and will grab the users answer which is an integer and it will stored in the answer variable to be used for comparison with the legitamte answer later on 
    end = time.time() # end the time when the user gets done withe problem andn store it in a variable called end
    duration = int(end - start) # calculate the total time by subracting the end by the start since end is greater and then running it through an int so it gets rounded
    
    if (user_chain_answer == solution) and (duration < time_length): # deterimes if the answer set by the user equals the solution that was created earlier and the 'and' is a comparison operator, if the user is under their set time and correct than they will move on
      print('Congrats') # will display Congrats
      correct += 1 # add one since the user got it correct
      num_questions += 1 # add one since a problem was solved 
      correct_answers.append(user_chain_answer) # the .append() method will add the correct answers into the empty list everytime and since the list is outside of the while loop it will not be resent each time, this is helpful as it stores data hence being called a data structure. 
      continue_derivative = input("Type 'Stop' if you want to stop the problems. If not ignore and press enter ") # if the user wants to stop they can type 'Stop', value stored in continue derivative if not they ignore
      if continue_derivative == 'Stop': # if they print stop than the next line will run, if statement.
        break # will break out of the while loop and print out the statistics that are outside of the while loop
    
    else:# else statement if the answer was not correct or the duration the user said was greater 
      print("Try another! Make sure not to reach your time limit! ") # print out a re-assurance using the print()
      print('This is the solution → ' + str(solution)) # print out the solution which is an int type so it has to be converted to a string type 
      incorrect += 1 # add one since it was incorrect
      num_questions += 1 # add one since a question was answered 
      incorrect_answers.append(user_chain_answer) # the .append() method will add the correct answers into the empty list everytime and since the list is outside of the while loop it will not be resent each time, this is helpful as it stores data hence being called a data structure. This will store all the incorrect answers 
      continue_derivative = input("Type 'Stop' if you want to stop the problems. If not ignore and press enter ") # if they print stop than the next line will run, if statement.
      if continue_derivative == 'Stop': # if they print stop than the next line will run, if statement
        break # will break out of the while loop and print out the statistics that are outside of the while loop
  
if options == "Quotient": # if the user says 'Chain' they will get th commands below 
  total_start = time.time()  # starts the timer and it will save in total_start. This will be used to deterime the total amount of time the user spent doing problems
  num_questions = 0 # number of questions is at 0 and this will be added on 
  incorrect = 0 # number of questions incorrect is at 0 and will be added by +1 for everytime a question is solved incorrectly
  correct = 0 # number of questions correct is at 0 and will be addewd by +1 for everytime a question is solved correctly 
  correct_answers = [] # create an empty LIST that will collect all the correct answers that the user has 
  incorrect_answers = [] # empty list that will collect all the incorrect answers 
  while True:
      x = random.randint(1,2) # random x value. 
      c1 = random.randint(1,2) # random coefficient generate random number between 1 and 2, random integer specifically using the randint method
      c = random.randint(1,2) # random coefficient generate random number between 1 and 2, random integer specifically using the randint method
      e1 = random.randint(1,2) # random exponenet generate random number between 1 and 2, random integer specifically using the randint method
      e = random.randint(1,2) # random exponenet generate random number between 1 and 2, random integer specifically using the randint method

      equation = ('(' + str(c) + 'x^' + str(e) + ') / ') +  ('(' + str(c1) + 'x^ ' + str(e1) + ')') 
      #print(equation) # this is the equation taht will randomly be generated and string concatenation is used, for example the variable c is a random integer so it cannot be added to a string so it has to be changed to a string, this is value over value 
      solution = (((((c * e) * (x ** (e-1))) * (c1*(x**e1)))) - (((c1 * e1) * ((x ** (e1-1)))) * (c*(x**e)))) / ((c1 * (x ** e1)) ** 2) # solution to the problem and it uses product rule which is more advanced as it deals with multiple values istead of one like the other program, uses chain rule to solve
      start = time.time() # start the time and this will save it to this variable so each time it loops a new time will be recorded and this will be used to deteirme the amount of time per question 
      user_quotient_answer = float(input("Make sure to use chain rule then plug in x after finding derivative! Type the answer to " + equation + " when x is " + str(x) + ": "))# this will show the question and will grab the users answer which is an integer and it will stored in the answer variable to be used for comparison with the legitamte answer later on 
      
      end = time.time()  # end the time when the user gets done withe problem andn store it in a variable called end, this value stores the time as of now 
      duration = int(end - start) # calculate the total time by subracting the end by the start since end is greater and then running it through an int so it gets rounded
      
      if (user_quotient_answer == solution) and (duration < time_length): # deterimes if the answer set by the user equals the solution that was created earlier and the 'and' is a comparison operator, if the user is under their set time and correct than they will move on
        print('Congrats') # will print out congrats on the screen
        correct += 1 # add one to the count since it is correct
        num_questions += 1 # add one to questions since a question has been solved 
        correct_answers.append(solution) # the .append() method will add the correct answers into the empty list everytime and since the list is outside of the while loop it will not be resent each time, this is helpful as it stores data hence being called a data structure. 
        continue_derivative = input("Type 'Stop' if you want to stop the problems. If not ignore and press enter ") # if the user wants to stop they can type 'Stop', value stored in continue derivative if not they ignore
        if continue_derivative == 'Stop': # if they print stop than the next line will run, if statement.
          break # will break out of the while loop and print out the statistics that are outside of the while loop
      else: # else statement if the answer was not correct or the duration the user said was greater 
        print("Try another! Make sure not to reach your time limit! ") # print out a re-assurance using the print() 
        print('This is the solution → ' + str(solution)) # print out the solution that was defined earlier since solution is an integer it needs to be converted into a string 
        incorrect_answers.append(user_quotient_answer) # the .append() method will add the correct answers into the empty list everytime and since the list is outside of the while loop it will not be resent each time, this is helpful as it stores data hence being called a data structure. This will store all the incorrect answers 
        incorrect += 1 # add one since it was incorrect
        num_questions += 1 # add one to questions since a question has been solved 
        continue_derivative = input("Type 'Stop' if you want to stop the problems. If not ignore and press enter ") # if the user wants to stop they can type 'Stop', value stored in continue derivative if not they ignore
        if continue_derivative == 'Stop':  # if they print stop than the next line will run, if statement.
          break # will break out of the while loop and print out the statistics that are outside of the while loop

def ratio(c, q): # ratio function 
    return (c / q) * 100 # return function, this will return the value of c / q and ca be used in future problems. The types * 100 converts it to a percent 
    
ratio = ratio(correct, num_questions)  # this is the function that calls the ratio, ratio(correct,num_questions) the ratio is how it is called and the values inside the parenthesis are the paramaters that get calculated into a ratio inside the function definition.
total_end = time.time() # ends the total amount of time, it grabs the current time as of now and saves it to a variable
elapsed = int(total_end - total_start) # subtracts the time the user first opened and used the application to when the user pressed 'Stop' 
converted_elapsed = elapsed / 60 # converts the seconds into minutes dividing it by 60
minutes = round(converted_elapsed, 2) # rounds to the second number
print("                              ") # acts as a seperator in order to clearly seperate the main thing with the statistics
print(name +' Statistics') # type out statistics onto the screen 
print('Total Questions Completed: ' + str(num_questions)) # prints out the number of questions that were completed and the variable 'num_questions' was convereted from an int to a string so it can be concatenated
print('Total Questions Correct: ' + str(correct)) #prints out the number of questions that were correct and the variable 'correct' was convereted from an int to a string so it can be concatenated
print('Total Questions Incorrect: ' + str(incorrect)) #prints out the number of questions that were incorrect and the variable 'incorrect' was convereted from an int to a string so it can be concatenated
print('Percent Correct: ' + str(ratio) + '%') # this will print out the ratio and since the ratio value is a float it needs to be converted into a string so it can be concatenated to a string
print('Total Time: ' + str(minutes) + ' minute') # this will print out the total amount of times in minute, minutes is a variable that is an integer so it cannot be added to a string so it has to concatenated 
print("All questions correct: " + str(correct_answers)) # this will print out a list that contains all the correct answers that the user has typed in. correct_answers is a list type so it has to be converted into a string so it can be concatenaed so str() method is used. 
print("All incorrect questions: " + str(incorrect_answers)) # this will print out a list that contains all the incorrect answers that the user has typed in. incorrect_answers is a list type so it has to be converted into a string so it can be concatenaed so str() method is used. 
  
    





    

  
