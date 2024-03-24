import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)
from colorama import Fore
from colorama import Style
import pyttsx3


engine = pyttsx3.init("sapi5")
voice = engine.getProperty("voices")
engine.setProperty("voice", voice[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

print("******************VITAL HEALTH STATS******************")

MaleFemale=str(input("Enter m/f: "))
if MaleFemale != "m" and MaleFemale != "f" :

    print(Fore.RED + Style.BRIGHT + "\tPlease Enter Male as (m) and Female as (f)")
    exit()
else:

    Height = float(input("Enter your height in centimeters: "))

    Weight = float(input("Enter your Weight in Kg: "))
    try:
        Height = Height / 100

        BMI = Weight / (Height * Height)

        print("your Body Mass Index is: ", BMI)

        if BMI > 0:

            if BMI <= 16:
                speak("you are severely underweight")
                print(Back.YELLOW + "you are severely underweight")

            elif BMI > 16 and BMI < 18.5:
                speak("you are underweight")
                print("you are underweight")

            elif BMI >= 18.5 and BMI < 24.9:
                speak("you are Healthy ")
                print(Back.GREEN + "you are Healthy ")

            elif BMI >= 24.9 and BMI < 29.9:
                speak("you are overweight")
                print("you are overweight")

            else:
                speak("you are severely overweight")
                print(Back.RED + "you are severely overweight")

        else:
            print("enter valid details")

    except ZeroDivisionError as e:
        print(Back.RED + "You have entered 0 in the height or weight")
        exit()


    def menu():
        print("")
        print("\/\/\/\/\MENU/\/\/\/\/")
        print("")
        print("\t[1] Diet sheet:")
        print("\t[2] Workout sheet:")
        print("\t[0] Exit the program.")
        print("")
        print("\/\/\/\/\END/\/\/\/\/\/")
        print("")


    menu()
    option = int(input("Enter your choice: "))

    if MaleFemale == "m":
        while option != 0:
            if option == 1:
                #  do option 1 stuff
                if BMI > 0:

                    if BMI <= 16:
                        print(
                            "\033[31m" + '''Since You Are severly Underweight according to the data you Entered , we recommend you to follow this diet => \033[39m"
                                         "\n Healthy Calories:-almonds, sunflower seeds, fruit, or whole-grain, wheat toast."
                                         "\n Nutrients:-Consider high-protein meats, which can help you to build muscle. Also, choose nutritious carbohydrates,\n such as brown rice and other whole grains"
                                         "\n Snacks:-Milk, protein bars or drinks, and crackers with hummus or peanut butter''')
                    elif BMI > 16 and BMI < 18.5:
                        print(
                            "\033[31m" + '''Since You Are Underweight according to the data you Entered , we recommend you to follow this diet => \033[39m"
                                         "\n Midmorning: It should be with tea or coffee with biscuits."
                                         "\n Lunch: It should be with whole grain cereals (like rice), vegetables..."
                                         "\n  Evening Tea: It should be with fruit juice (banana shake or milk shake etc.),..."
                                         "\n Dinner: It should start with soup. The dinner should consist of whole grain cereals, pulses,...''')

                    elif BMI >= 18.5 and BMI < 24.9:
                        print(Back.GREEN + "Since you are Healthy ")
                        print("")
                        print(Fore.YELLOW + Style.BRIGHT + "Follow Your daily Routine keep it up!!!"
                                          "\n 1- Avoid eating Bakery products"
                                          "\n 2- Eat fruits and vegetables"
                                          "\n 3- Avoid food that is high in sugar!! Follow Your daily Routine keep it up!!!")


                    elif BMI >= 24.9 and BMI < 29.9:
                        print(
                            "\033[31m" + '''Since you are overweight according to your entered data we recommend you to follow this diet =>\033[39m"
                                         "\n 1- Egg diet.
                                         "\n 2- Fruit diet. (General Motor’s diet).
                                         "\n 3- Salads.
                                         "\n 4- Refreshing drinks.
                                         "\n 5- Food diet – including raw food.
                                         "\n 6- Reduce food and drinks high in fat and sugar''')

                    else:
                        print(
                            "\033[31m" + '''Since you are severly overweight according to your entered data we recommend you to follow this diet =>\033[39m"
                                         "\n 1- Egg diet.
                                         "\n 2- Fruit diet. (General Motor’s diet).
                                         "\n 3- Salads.
                                         "\n 4- Refreshing drinks.
                                         "\n 5- Food diet – including raw food. ''')

            elif option == 2:
                # do option 2 stuff
                if BMI > 0:

                    if BMI <= 16:
                        print(
                            "\033[31m" + '''Since You Are severly Underweight according to the data you Entered , we recommend you to follow these simple workouts => \033[39m"
                                           "\n – Marching. Stand with your feet shoulder width apart. Now lift one leg up.
                                            "\n   1 –Pushups (10 reps * 3 sets)
                                            "\n  2– Plank    (30 sec * 2reps)
                                            "\n  3– Squats  (15 reps * 2 sets) 
                                            "\n  4– Lunges  (15 reps * 2 sets)
                                            "\n  5- Suryanamaskar (12 times)''')
                    elif BMI > 16 and BMI < 18.5:
                        print(
                            "\033[31m" + '''Since You Are Underweight according to the data you Entered , we recommend you to follow these simple workouts => \033[39m"
                                           "\n Push-ups (10 reps * 3 stes)
                                           "\n Plank    (30 sec * 2reps)"
                                           "\n Squats (15 reps * 2 sets)
                                           "\n Pull-ups (10 reps * 3 stes)
                                           "\n  Lunges  (15 reps * 2 sets)
                                           "\n Yoga  ''')

                    elif BMI >= 18.5 and BMI < 24.9:
                        print(Back.GREEN + "Since you are Healthy ")
                        print("")
                        print(Back.CYAN +
                              ''''\n  1- Pushups (15 reps * 3 sets) "
                              "\n  2- Burpees (10 reps * 4 sets)"
                              "\n  3- Squats  (15 reps * 3 sets)"
                              "\n  4- Lunges (12 reps * 3 sets)"
                              "\n  5- Jumping Jacks (20 reps * 4 sets)"
                              "\n  6- Crunches (12 reps * 4 sets)"
                              "Do yoga,cycling/running/jogging & Follow Your daily Routine keep it up!!!''')


                    elif BMI >= 24.9 and BMI < 29.9:
                        print(
                            "\033[31m" + '''Since you are overweight according to your entered data we recommend you to follow these simple workouts=>\033[39m"
                                            "\n – Marching. Stand with your feet shoulder width apart. Now lift one leg up , Hold as much as you can "
                                            "\n  1 –  Jumping Jacks , Cross Crawl...(10 reps * 4 sets)"
                                            "\n  2– Stick-Up , Crunches(10 reps * 3 sets)"
                                            "\n  3– Push ups , stretching(10 reps * 3 sets) "
                                            "\n  4– High knees( 45 sec * 3 sets)"
                                            "\n  5– Running / jogging. ''')

                    else:
                        print(
                            "\033[31m" + '''Since you are severly overweight according to your entered data we recommend you to follow these simple workouts=>\033[39m"
                                            "\n – Marching. Stand with your feet shoulder width apart. Now lift one leg up.
                                            "\n  1 – Cross Crawl. This movement is the next step after marching.(10 reps * 4 sets)
                                            "\n  2– Stick-Up. So far we have not done any upper body movements...(10 reps * 3 sets)
                                            "\n  3– Push ups. I know that’s a scary word for many people but you have to follow...(10 reps * 3 sets)
                                            "\n  4– High knees( 35 sec * 4 sets) 
                                            "\n  5– Running / jogging. (daily) ''')


            else:
                print("invalid option")

            print()
            menu()
            option = int(input("Enter your choice: "))

    elif MaleFemale == "f":
        while option != 0:
            if option == 1:
                #  do option 1 stuff
                if BMI > 0:


                    if BMI <= 16:
                        print(
                            "\033[31m" + '''Since You Are severly Underweight according to the data you Entered , we recommend you to follow this diet => \033[39m"
                                            "\n Healthy Calories:-almonds, sunflower seeds, fruit, or whole-grain, wheat toast."
                                            "\n Nutrients:-Consider high-protein meats, which can help you to build muscle. Also, choose nutritious carbohydrates,\n such as brown rice and other whole grains"
                                            "\n Snacks:-Milk, protein bars or drinks, and crackers with hummus or peanut butter''')
                    elif BMI > 16 and BMI < 18.5:
                        print(
                            "\033[31m" + '''Since You Are Underweight according to the data you Entered , we recommend you to follow this diet => \033[39m"
                                            "\n Midmorning: It should be with tea or coffee with biscuits."
                                            "\n Lunch: It should be with whole grain cereals (like rice), vegetables..."
                                            "\n  Evening Tea: It should be with fruit juice (banana shake or milk shake etc.),..."
                                            "\n Dinner: It should start with soup. The dinner should consist of whole grain cereals, pulses,...''')

                    elif BMI >= 18.5 and BMI < 24.9:
                        print(Back.GREEN + "Since you are Healthy ")
                        print("")
                        print(Fore.YELLOW + Style.BRIGHT + "Follow Your daily Routine keep it up!!!"
                                          "\n 1- Avoid eating Bakery products"
                                          "\n 2- Eat fruits and vegetables"
                                          "\n 3- Avoid food that is high in sugar!! Follow Your daily Routine keep it up!!!")


                    elif BMI >= 24.9 and BMI < 29.9:
                        print(
                            "\033[31m" + '''Since you are overweight according to your entered data we recommend you to follow this diet =>\033[39m"
                                            "\n 1- Egg diet.
                                            "\n 2- Fruit diet. (General Motor’s diet).
                                            "\n 3- Salads.
                                            "\n 4- Refreshing drinks.
                                            "\n 5- Food diet – including raw food.
                                            "\n 6- Reduce food and drinks high in fat and sugar''')

                    else:
                        print(
                            "\033[31m" + '''Since you are severly overweight according to your entered data we recommend you to follow this diet =>\033[39m"
                                            "\n 1- Egg diet.
                                            "\n 2- Fruit diet. (General Motor’s diet).
                                            "\n 3- Salads.
                                            "\n 4- Refreshing drinks.
                                            "\n 5- Food diet – including raw food. ''')

            elif option == 2:
                # do option 2 stuff
                if BMI > 0:

                    if BMI <= 16:
                        print(
                            "\033[31m" + '''Since You Are severly Underweight according to the data you Entered , we recommend you to follow these simple workouts => \033[39m"
                                              "\n – Marching. Stand with your feet shoulder width apart. Now lift one leg up.
                                               "\n   1 –Pushups (10 reps * 3 sets)
                                               "\n  2– Plank    (30 sec * 2reps)
                                               "\n  3– Squats  (15 reps * 2 sets) 
                                               "\n  4– Lunges  (15 reps * 2 sets)
                                               "\n  5- Suryanamaskar (12 times)''')
                    elif BMI > 16 and BMI < 18.5:
                        print(
                            "\033[31m" + '''Since You Are Underweight according to the data you Entered , we recommend you to follow these simple workouts => \033[39m"
                                              "\n Push-ups (10 reps * 3 stes)
                                              "\n Plank    (30 sec * 2reps)"
                                              "\n Squats (15 reps * 2 sets)
                                              "\n Pull-ups (10 reps * 3 stes)
                                              "\n  Lunges  (15 reps * 2 sets)
                                              "\n Yoga  ''')

                    elif BMI >= 18.5 and BMI < 24.9:
                        print(Back.GREEN + "Since you are Healthy ")
                        print("")
                        print(Back.CYAN +
                              ''''\n  1- Pushups (15 reps * 3 sets) "
                              "\n  2- Burpees (10 reps * 4 sets)"
                              "\n  3- Squats  (15 reps * 3 sets)"
                              "\n  4- Lunges (12 reps * 3 sets)"
                              "\n  5- Jumping Jacks (20 reps * 4 sets)"
                              "\n  6- Crunches (12 reps * 4 sets)"
                              "Do yoga,cycling/running/jogging & Follow Your daily Routine keep it up!!!''')


                    elif BMI >= 24.9 and BMI < 29.9:
                        print(
                            "\033[31m" + '''Since you are overweight according to your entered data we recommend you to follow these simple workouts=>\033[39m"
                                               "\n – Marching. Stand with your feet shoulder width apart. Now lift one leg up , Hold as much as you can "
                                               "\n  1 –  Jumping Jacks , Cross Crawl...(10 reps * 4 sets)"
                                               "\n  2– Stick-Up , Crunches(10 reps * 3 sets)"
                                               "\n  3– Push ups , stretching(10 reps * 3 sets) "
                                               "\n  4– High knees( 45 sec * 3 sets)"
                                               "\n  5– Running / jogging. ''')

                    else:
                        print(
                            "\033[31m" + '''Since you are severly overweight according to your entered data we recommend you to follow these simple workouts=>\033[39m"
                                               "\n – Marching. Stand with your feet shoulder width apart. Now lift one leg up.
                                               "\n  1 – Cross Crawl. This movement is the next step after marching.(10 reps * 4 sets)
                                               "\n  2– Stick-Up. So far we have not done any upper body movements...(10 reps * 3 sets)
                                               "\n  3– Push ups. I know that’s a scary word for many people but you have to follow...(10 reps * 3 sets)
                                m               "\n  4– High knees( 35 sec * 4 sets) 
                                               "\n  5– Running / jogging. (daily) ''')


            else:
                print("invalid option")

            print()
            menu()
            option = int(input("Enter your choice: "))

    else:
        print("Please Enter Male as (m) and Female as (f) ")