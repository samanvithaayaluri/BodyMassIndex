# BMI and BMR Calculator and Diet and Exercise Planner

#Taking gender as input

gender=input("Enter your gender : M for Male and F for Female:")
print()

#Taking age as input

if gender == 'M' or gender =='F':
   age=int(input("Enter your age (in years):"))
   print()
else:
  print("Gender is invalid")
  exit()
  
#******************************************************************************************#

#Checking the age requirements

if age<18:
  print("Sorry, your age does not meet the defined requirements")
  exit()
else:

#Taking user height and user weight as inputs to calculate the BMI
  
  height=float(input("Enter your height in cm:"))
  print( )

  weight=float(input("Enter your weight in kgs:"))
  print( )

#Converting the height into meters for calculation
  
  hm=height/100

#***********************************************************************************#

#Calculating the BMI

  bmi=weight/(hm*hm)

#Displaying the BMI to the user
  
  print("Your Body Mass Index - BMI is :",f'{bmi:.2f}')
  print( )

#Displaying the category of BMI the user falls into
  
  if bmi <18.5:
    print("You fall in the category of UNDER WEIGHT ")
  
  elif bmi > 18.5 and  bmi < 24.9:
    print("You fall in the category of NORMAL WEIGHT")
  
  elif bmi > 25.0 and  bmi < 29.9:
    print("You fall in the category of PRE-OBESITY")
  
  elif bmi > 30.0 and  bmi < 34.9:
    print("You fall in the category of OBESITY CLASS 1")
  
  elif bmi > 35.0 and  bmi < 39.9:
    print("You fall in the category of OBESITY CLASS 2")
  
  else:
    print("You fall in the category of OBESITY CLASS 3")
  print( )

#***********************************************************************************#

#Displaying the BMI chart 
  
  print("Here is the chart displaying the BMI Ranges and the Weight Status")
  print( )

  from prettytable import PrettyTable

  myTable = PrettyTable(["BMI range", "Weight Status"])
  myTable.add_row(["Below 18.5","Underweight"])
  myTable.add_row(["18.5 - 24.9", "Normal Weight"])
  myTable.add_row(["25.0 - 29.9","Pre-Obesity"])
  myTable.add_row(["30.0 - 34.9", "Obesity Class 1"])
  myTable.add_row(["35.0 - 39.9", "Obesity Class 2"])
  myTable.add_row(["Above 40.0","Obesity Class 3"])

  print(myTable)
  print( )

#***********************************************************************************#

  if bmi >= 18.5 and  bmi <= 24.9:
    print("You are perfectly healthy 😀")
    exit()

#***********************************************************************************#

#Displaying the weight to reduce or gain
  
  max=(18.5*(hm*hm))
  min=(24.9*(hm*hm))

#***********************************************************************************#

# To Reduce
  
  if max < weight:
    maxi=weight-(18.5*(hm*hm))
    mini=weight-(24.9*(hm*hm))

    print("In order to come under the category of NORMAL WEIGHT, you need to lose at least a weight of",f'{mini:.2f}',"kgs and at most a weight of",f'{maxi:.2f}',"kgs")
    print( )

#***********************************************************************************#

# To Gain
  
  if max>weight:
    maxi=(18.5*(hm*hm))-weight
    mini=(24.9*(hm*hm))-weight
    
    print("In order to come under the category of NORMAL WEIGHT, you need to gain at least a weight of",f'{maxi:.2f}',"kgs and at most a weight of",f'{mini:.2f}',"kgs")
    print( )

#***********************************************************************************#

# BMR Calculation and Display
  
  if gender == 'M':
    bmr=66.47+(13.75*weight)+(5*height)-(4.7*age)
  else:
    bmr=655.09+(9.56*weight)+(1.85*height)-(4.68*age)

  print("Your BMR - Basic Metabolic Rate is : ",f'{bmr:.2f}')
  print()

#***********************************************************************************#

#Displaying the calories requirement per day
  
  print("Daily exercise schedule ")
  print()

  print("1.Little / No Exercise")
  print("2.Light Exercise / Sports (1-3 days per week)")
  print("3.Moderate Exercise / Sports (3-5 days per week)")
  print("4.Hard Exercise / Sports (6-7 days per week)")
  print("5.Very hard Exercise / Sports & Physical Job ")
  print()
  
  exe=input("Enter one of the choices from above based upon your daily schedule : ")
  print()

  exe = int(exe)

  if exe == 1:
    cals=bmr*1.2
  elif exe == 2:
    cals=bmr*1.375
  elif exe == 3:
    cals=bmr*1.55
  elif exe == 4:
    cals=bmr*1.725
  elif exe == 5:
    cals=bmr*1.9
  else:
    print("Please select from the above option")
    print()
    
  print("The amount of calories that you need to consume per day is: ",f'{cals:.2f}')
  print( )

#***********************************************************************************#

#Diet Plan

def diet (a):
  
  if a > 0 and a <=1000:
    
    print("The meal diet for you is a short-term, slightly extreme diet plan that requires you to slash the calories you’re eating and opt for high-protein , low-fat and low calorie foods to keep you full throughout the day.") 
    print( )
    
    print("The foods must replace the normal food routine with liquid supplements, meal replacement shakes and protein bars for a specific period. Few examples of foods that you can consume include oatmeal, eggs, berries, fish, fruits, chia seeds, nuts, meat and poultry, salads and cheese.")
    
  elif a>1000 and a<=1250:
    
    print("The meal plan for you can be achieved through a combination of protein, fiber, healthy fats, and complex carbohydrates while still including fun foods as well.You may need more or less at each meal and snack depending on your hunger levels.")
    print( )
    
    print("Including the right combination of foods at each meal and snack will keep you fuller for longer. Few examples of foods that you can consume include scrambled eggs, fruit salads, bread, lean proteins, whole grains, fruits and vegetables, low-fat dairy products, healthy fats ")

  elif a>1250 and a<=1500:
    
    print("Your diet plan typically involves consuming a balanced combination of protein, carbohydrates, and healthy fats while limiting calorie-dense foods and added sugars.")
    print( )

    print("It's also important to stay hydrated by drinking plenty of water and unsweetened beverages like herbal tea, and to limit or avoid sugary drinks like soda and juice. Example of foods that you can eat are lean meats ,low-fat dairy products, eggs, plant-based proteins such as tofu, tempeh, legumes, and beans ,whole grains, fruits and vegetables like leafy greens, broccoli, carrots, tomatoes.")
    
  elif a>1500 and a<=1750:
    
    print("Your customised calorie diet can include small servings of healthy snacks such as low-fat cheese, fruit, or nuts. It's important to stay hydrated by drinking plenty of water and unsweetened beverages like herbal tea, and to limit or avoid sugary drinks like soda and juice.")
    print( )

    print("Your plan typically involves consuming a balanced combination of macronutrients, including protein, carbohydrates, and healthy fats, while limiting high-calorie and high-sugar foods. Few foods which can be consumed by you are egg whites, yogurt, protein smoothie, sprouts salad, cottage cheese, protein breakfast burrito, mixed vegetables.")
    
  elif a>1750 and a<=2000:
    
    print("Your diet should consist of whole, unprocessed foods and be rich in fruits, vegetables, protein, whole grains, and healthy fats. You should think about each meal consisting of 400 to 500 calories and snacks providing about 150 to 300 calories. Including adequate balances of protein, fat, and carbohydrates at each meal and snack will keep you fuller for longer.")
    print( )

    print("You may need more or less at each meal and snack depending on your hunger levels. Few examples of foods that can be included in your diet are whole wheat bread, avacadoes, fried eggs, cherries, almonds, black beans, baby carrots, hummus, zucchini, greek yogurt.")
    
  elif a>2000 and a<=2250:
    
    print("Your diet plan should emphasize on vegetables, fruits, whole grains, and fat-free or low-fat dairy products, limited saturated and trans fats, sodium, and added sugars and controlled portion sizes")
    print( )
    
    print("Few examples of foods that can be included in your diet are scrambled eggs, blueberry yogurt, red pepper and tomatoes salad, protein shake, BBQ chicken salad, yogurt with avacado and basil, omelette, banana smoothie, peanut butter, cheesy chicken.")
    
  elif a>2250 and a<=2500:
    
   print("Individuals following this diet should aim to consume about 6.5 ounces of protein which should include various food items like seafood, poultry, lean meats, eggs, soy products, nuts and seeds including eggs, oats, cheese, whole grain toast are good options. Whey protein shakes, fruits and nuts are recommended.")
   print( )

   print("The main goal of this diet is to enhance body composition and maintain a balance in calorie intake of the body. This diet provides the necessary calories for proper functioning of the body. Few foods which can be consumed by people following this diet are aloo parantha, promogranete, chapatis, green tea, chicken stew, dal, soy milk, cornflakes, boiled rice, paneer.")
  
  elif a>2500 and a<=2750:
    
    print("The diet customised for you should be highly nutritious as you need a lot of calories that too which give plenty of energy and less amounts of fats and cholestrol. People following this diet must ensure they eat lots of good fats, proteins and vitamins and minerals so that they acquire less and less amonuts of fats even upon eating more and more calories.")
    print( )

    print("As mentioned above, the foods that you eat must contain all the mentioned qualities. A few examples of such foods include roasted peanuts, yogurt, omlette, cheese, eggs, avacado and cucumber, chicken, brown rice, broccoli, almond milk, fish, dairy, whole grains.")
    
  elif a>3000:
    
    print("The kinds of foods you should eat when consuming more than 3000 calories per day will depend on your individual dietary needs and goals. However, generally speaking, it's important to aim for a balanced diet that includes a variety of nutrient-dense foods from all the major food groups")
    print( )

    print("It's also important to pay attention to portion sizes and to make sure you're not consuming excessive amounts of added sugars, saturated fats, or sodium. A few foods which can satisfy your needs for the diet plan include whole grains, brown rice, quinoa, whole wheat bread, oats, chicken, turkey, fish, lean beef, tofu, nuts, seeds, avocados, olive oil, milk, yogurt, cheese, and fortified plant-based milks.")
  
#***********************************************************************************#

#Exercise Plan

def exercise (b):
  
  if b <= 18.5:
    
    print("If you are underweight, it's important to focus on exercises that build muscle mass and promote weight gain. Strength training exercises such as weightlifting, resistance band exercises, and bodyweight exercises like push-ups, squats, and lunges can help you build muscle. Additionally, incorporating healthy sources of protein and healthy fats into your diet can help support muscle growth.")

  if b > 18.5 and b <= 24.9:
    
    print("If you have a normal BMI, it's important to focus on maintaining a healthy weight and improving your overall fitness level. Aim for at least 150 minutes of moderate-intensity aerobic exercise or 75 minutes of vigorous-intensity aerobic exercise per week. This can include activities such as running, cycling, swimming, or brisk walking. Additionally, incorporating strength training exercises 2-3 times per week can help build and maintain muscle mass.")

  if b > 25 and  b <=29.9:
    
    print("If you are overweight, it's important to focus on exercises that burn calories and promote weight loss. Aim for at least 150-300 minutes of moderate-intensity aerobic exercise or 75-150 minutes of vigorous-intensity aerobic exercise per week. This can include activities such as running, cycling, swimming, or brisk walking. Additionally, incorporating strength training exercises 2-3 times per week can help build and maintain muscle mass.")

  if b >30.0:
    
    print("If you are obese, it's important to focus on exercises that promote weight loss and improve overall health. Aim for at least 300 minutes of moderate-intensity aerobic exercise or 150 minutes of vigorous-intensity aerobic exercise per week. This can include activities such as running, cycling, swimming, or brisk walking. Additionally, incorporating strength training exercises 2-3 times per week can help build and maintain muscle mass.")

#************************************************************************#

# Diet and Exercise Plan

def dietexercise (c):

  if c< 18.5:
    
    print("You are underweight. To gain weight, try incorporating the following into your diet:")
    print()
    
    print("- High-calorie, nutrient-dense foods such as nuts, seeds, avocados, and whole grains.")
    print()
    
    print("- Lean proteins such as chicken, fish, and beans.")
    print()
    
    print("- Strength training exercises such as weightlifting or bodyweight exercises like push-ups, squats, and lunges.")
    print()

  elif 18.5 <= c < 25:
    
    print("You are at a healthy weight. To maintain your weight and improve your overall fitness, try the following:")
    print()
    
    print("- A balanced diet that includes plenty of fruits, vegetables, lean proteins, and whole grains.")
    print()
    
    print("- Cardio exercises such as running, cycling, swimming, or brisk walking.")
    print()
    
    print("- Strength training exercises 2-3 times per week to build and maintain muscle mass.")
    print()

  elif 25 <= c < 30:
    
    print("You are overweight. To promote weight loss and improve overall health, try the following:")
    print()

    print("- A balanced diet that is low in processed foods and high in fruits, vegetables, and lean proteins.")
    print()
    
    print("- Cardio exercises such as running, cycling, swimming, or brisk walking.")
    print()
    
    print("- Strength training exercises 2-3 times per week to build and maintain muscle mass.")
    print()

  else:
    
    print("You are obese. To promote weight loss and improve overall health, try the following:")
    print()
    
    print("- A balanced diet that is low in processed foods and high in fruits, vegetables, and lean proteins.")
    print()
    
    print("- Cardio exercises such as running, cycling, swimming, or brisk walking.")
    print()
    
    print("- Strength training exercises 2-3 times per week to build and maintain muscle mass.")
    print()

#******************************************************************************************#

#Asking the input to choose their suitable plan

print("These are the different choices available for plans:")
print( )

print("1 for Only Diet plan")
print("2 for Only Exercise plan")
print("3 for both diet and exercise plan")
print( )

ch=int(input("Enter one choice from the above:"))
print( )

print("The following is a suitable plan for you:")
print()

if ch==1:
  diet(cals)
elif ch==2:
  exercise(bmi)
elif ch==3:
  dietexercise(bmi)
