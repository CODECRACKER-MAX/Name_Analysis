import os
import time
import webbrowser

def name_converter():
    #Data's required for converting the name to numbers!
    Data1 = "A","J","S"
    Data2 = "B", "K","T"
    Data3 = "C","L","U"
    Data4 = "D","M","V"
    Data5 = "E","N","W"
    Data6 = "F","O","X"
    Data7 = "G","P","Y"
    Data8 = "H","Q","Z"
    Data9 = "I","R"

    #Enter the Name !

    print("Note Only Enter Your First Name")
    name1 = input("Enter Your Name: ")
    name = "" # Initialization of the Name
    name = name1.upper()
    strings = len(name)

    # The Global Variables used in this module!
    global sum_of_numbers
    global length_of_the_numbers

    #############################


    sum_of_numbers = 0

    #Conversion of the name to number using the data mentioned,
    for x in range(len(name)):
        if (name[x] in Data1):
            sum_of_numbers = sum_of_numbers + 1
            print("String Found: {}, value = {}".format(name[x],"1"))
            pass
        if (name[x] in Data2):
            sum_of_numbers = sum_of_numbers + 2
            print("String Found: {}, value = {}".format(name[x],"2"))
            pass
        if (name[x] in Data3):
            sum_of_numbers = sum_of_numbers + 3
            print("String Found: {}, value = {}".format(name[x],"3"))
            pass
        if (name[x] in Data4):
            sum_of_numbers = sum_of_numbers + 4
            print("String Found: {}, value = {}".format(name[x],"4"))
            pass
        if (name[x] in Data5):
            sum_of_numbers = sum_of_numbers + 5
            print("String Found: {}, value = {}".format(name[x],"5"))
            pass
        if (name[x] in Data6):
            sum_of_numbers = sum_of_numbers + 6
            print("String Found: {}, value = {}".format(name[x],"6"))
            pass
        if (name[x] in Data7):
            sum_of_numbers = sum_of_numbers + 7
            print("String Found: {}, value = {}".format(name[x],"7"))
            pass
        if (name[x] in Data8):
            sum_of_numbers = sum_of_numbers + 8
            print("String Found: {}, value = {}".format(name[x],"8"))
            pass
        if (name[x] in Data9):
            sum_of_numbers = sum_of_numbers + 9
            print("String Found: {}, value = {}".format(name[x],"9"))
            pass
        if (name[x] == " "):
            continue
    print("The Sum of the number of '{}' is {}".format(name,sum_of_numbers))



    length_of_the_numbers = len(str(sum_of_numbers))
    print("The length of numbers: {}".format(length_of_the_numbers))



# To check the length of the sum!
def checking_the_length_of_the_sum():
    if(length_of_the_numbers == 1):
        print("Error! Your Name Cannot Be So, Short !!!")
        print("For Help Please Contact the Admin")

    if (length_of_the_numbers == 2):
        length_of_the_number_2()
    elif (length_of_the_numbers == 3):
        length_of_the_number_3()
    elif (length_of_the_numbers == 4):
        length_of_the_number_4()
    elif (length_of_the_numbers == 5):
        length_of_the_number_5()
    else:
        print("Error!!")
        print("Your Name Can't Be So Long !")
        print("Try Again, by entering your real name ;)")



# If the length of the numbers is "2", This Module will be working

def length_of_the_number_2():
    # Global variable for length_2 ####
    global power_number
    ####################


    power_number = ""
    sum_number_to_string = str(sum_of_numbers)
    for x in range(1):
        value1 = sum_number_to_string[x]
    for x in range(2):
        value2 = sum_number_to_string[x]
    print("Number 1 = {}".format(value1))
    print("Number 2 = {}".format(value2))
    final_sum_of_the_name = int(value1) + int(value2)
    print("Your Name has the power of: {}".format(str(final_sum_of_the_name)[0]))
    power_number = str(final_sum_of_the_name)[0]




# If the length of the numbers is "3", This Module will be working
def length_of_the_number_3():
    # Global variable for length_2 ####
    global power_number
    ####################

    sum_number_to_string = str(sum_of_numbers)
    for x in range(1):
        value1 = sum_number_to_string[x]
    for x in range(2):
        value2 = sum_number_to_string[x]
    for x in range(3):
        value3 = sum_number_to_string[x]
    print("Number 1 = {}".format(value1))
    print("Number 2 = {}".format(value2))
    print("Number 3 = {}".format(value3))
    final_sum_of_the_name = int(value1) + int(value2) + int(value3)
    power_number = str(final_sum_of_the_name)[0]



# If the length of the numbers is "4", This Module will be working
def length_of_the_number_4():
    # Global variable for length_2 ####
    global power_number
    ####################

    sum_number_to_string = str(sum_of_numbers)
    for x in range(1):
        value1 = sum_number_to_string[x]
    for x in range(2):
        value2 = sum_number_to_string[x]
    for x in range(3):
        value3 = sum_number_to_string[x]
    for x in range(4):
        value4 = sum_number_to_string[x]
    print("Number 1 = {}".format(value1))
    print("Number 2 = {}".format(value2))
    print("Number 3 = {}".format(value3))
    print("Number 4 = {}".format(value4))
    final_sum_of_the_name = int(value1) + int(value2) + int(value3) + int(value4)
    print("Your Name has the power of: {}".format(str(final_sum_of_the_name)[0]))
    power_number = str(final_sum_of_the_name)[0]



# If the length of the numbers is "5", This Module will be working
def length_of_the_number_5():

    # Global variable for length_2 ####
    global power_number
    ####################

    sum_number_to_string = str(sum_of_numbers)
    for x in range(1):
        value1 = sum_number_to_string[x]
    for x in range(2):
        value2 = sum_number_to_string[x]
    for x in range(3):
        value3 = sum_number_to_string[x]
    for x in range(4):
        value4 = sum_number_to_string[x]
    for x in range(5):
        value5 = sum_number_to_string[x]
    print("Number 1 = {}".format(value1))
    print("Number 2 = {}".format(value2))
    print("Number 3 = {}".format(value3))
    final_sum_of_the_name = int(value1) + int(value2) + int(value3) + int(value4) + int(value5)
    print("Your Name has the power of: {}".format(str(final_sum_of_the_name)[0]))
    power_number = str(final_sum_of_the_name)[0]




def identify_the_power():
    if (power_number == "1"):
        number1_power()

    elif (power_number == "2"):
        number2_power()

    elif (power_number == "3"):
        number3_power()

    elif (power_number == "4"):
        number4_power()

    elif (power_number == "5"):
        number5_power()

    elif (power_number == "6"):
        number6_power()

    elif (power_number == "7"):
        number7_power()

    elif (power_number == "8"):
        number8_power()

    elif (power_number == "9"):
        number9_power()

    else:
        print("Verified, the incorrect !!!!!!")

def number1_power():
    print("So, your power is: {}".format("1"))
    print("Which says, you are:'Initiator of action, pioneering, leading, independent, attaining, individualistic' \n")
    Note()

def number2_power():
    print("So, your power is: {}".format("2"))
    print("Which says, you are: 'Cooperation, adaptability, consideration of others, partnering, mediating'\n")
    Note()

def number3_power():
    print("So, your power is: {}".format("3"))
    print("Which says you are: 'Expression, verbalization, socialization, you also have a lot of art with you naturally, your the joy of living'\n ")
    Note()

def number4_power():
    print("So, your power is: {}".format("4"))
    print("Which say you are: 'Values of foundation, your the order, and your the service, you will struggle against limits, your the steady growth'\n ")
    Note()

def number5_power():
    print("So, your power is: {}".format("5"))
    print("Which says you are: 'Expansiveness, visionary, adventurous, the constructive use of freedom'\n ")
    Note()

def number6_power():
    print("So, your power is: {}".format("6"))
    print("Which say's you are: 'Good With Responsibility, protective, nurturing, community (social being), your balanced, and sympathy'\n")
    Note()

def number7_power():
    print("So, your power is: {}".format("7"))
    print("Which say's you are: 'Analytical, understanding, you will have good knowledge, awareness, studious, meditating'\n")
    Note()

def number8_power():
    print("So, your power is: {}".format("8"))
    print("Which say's you are: 'Practical endeavors, status-oriented, power-seeking, high-material goals'\n")
    Note()

def number9_power():
    print("So, your power is: {}".format("9"))
    print("Which say's you are: 'Humanitarian, nature giving, selflessness, obligations, creative expression'\n")
    Note()

def Note():
    print("This is only the analysis of your name, so some how this will match with your personality,")
    print("BUT, it's not deeply analyzed, You should visit a good astrologist inorder to get the most out astrology")
    print("But, I will refer you a good site, where you should enter your details and it will deeply analyze your birth chart! ")
    print("- And one more thing, Even Lord Krishna said that 'Even God's Does Not Know The Exact Future Of Humans So, Work Hard, \nYou Never Know When Your Good Luck Will Start!")
    print("Opening the astrology website :)")
    print("\nPlease Wait.........")
    time.sleep(15)
    print("\nDo you want me to open the site for you ? y/n")
    site_open = input("Enter your choice: ")
    if (site_open == "Y" or site_open == "y"):
        print("Opening the site please wait..............")
        time.sleep(6)
        webbrowser.open("https://www.astrosage.com/")
        pass

    elif (site_open == "N" or site_open == "n"):
        print("As you say I will not open the site, Hope you liked my python script :) ")
        pass

    else:
        print("Sorry, I didn't understood what you mean by: '{}'".format(site_open))
        print("But I Guess you are insterested, opening the site for you, please wait.......")
        time.sleep(5)
        webbrowser.open("https://www.astrosage.com/")
        pass

    print("Signing Out Stefen, Hope To See You Soon ;)")
    print("Press Any Key TO EXIT!")
    input()


#Calling the required Moudels!
name_converter()
checking_the_length_of_the_sum()

print("Analyzing your number")
print("Please Wait..................")
time.sleep(6)
os.system('cls') # Note this will only work for windows os!
identify_the_power()
