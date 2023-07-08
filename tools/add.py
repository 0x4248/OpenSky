# Open sky add tool
# A repository of open source sky images.
# Github: https://www.github.com/lewisevans2007/opensky
# Licence: Unlicense

import os
import json
import random
logo = r"""
   ____  _____  ______ _   _    _____ _  ____     __
  / __ \|  __ \|  ____| \ | |  / ____| |/ /\ \   / /
 | |  | | |__) | |__  |  \| | | (___ | ' /  \ \_/ / 
 | |  | |  ___/|  __| | . ` |  \___ \|  <    \   /  
 | |__| | |    | |____| |\  |  ____) | . \    | |   
  \____/|_|    |______|_| \_| |_____/|_|\_\   |_|   """

if __name__ == '__main__':
    print(logo)
    #check if ADD_HERE folder exists
    print("Welcome to the open sky add tool. This tool will help you add photos to the dataset.")
    if os.path.exists("ADD_HERE"):
        print("The ADD_HERE folder already exists. Do you want to delete it? if you chose no the photos will be used (y/n)")
        if input() == "y":
            os.rmdir("ADD_HERE")
            os.mkdir("ADD_HERE")
            print("Please add your photos to the ADD_HERE folder once you are done press enter.")
            input()
        else:
            #count how many photos are in the folder
            print("There are currently "+str(len(os.listdir("ADD_HERE")))+" photos in the ADD_HERE folder.")
    else:
        os.mkdir("ADD_HERE")
        print("Please add your photos to the ADD_HERE folder once you are done press enter.")
        input()
    print("We now need to know what the conditions were like when you took the photos.")
    number_of_photos = len(os.listdir("ADD_HERE"))
    percentage_of_clouds = input("What percentage of the sky was covered in clouds? (0-100) (100 being like a white sky and 0 being a clear blue sky)")
    print("Now enter the condition of the weather.")
    print("1. Clear")
    print("2. Scattered Clouds")
    print("3. Broken Clouds")
    print("4. Overcast Clouds")
    print("5. Light Rain")
    print("6. Moderate Rain")
    print("7. Heavy Rain")
    print("8. Thunderstorm")
    while True:
        weather_condition = input("Enter the number of the weather condition: ")
        if weather_condition in ["1","2","3","4","5","6","7","8"]:
            if weather_condition == "1":
                weather_condition = "Clear"
            elif weather_condition == "2":
                weather_condition = "Scattered Clouds"
            elif weather_condition == "3":
                weather_condition = "Broken Clouds"
            elif weather_condition == "4":
                weather_condition = "Overcast Clouds"
            elif weather_condition == "5":
                weather_condition = "Light Rain"
            elif weather_condition == "6":
                weather_condition = "Moderate Rain"
            elif weather_condition == "7":
                weather_condition = "Heavy Rain"
            elif weather_condition == "8":
                weather_condition = "Thunderstorm"
            break
        else:
            print("Please enter a valid number.")
    print("Any notes about the photos?")
    notes = input("Notes: ")
    print("generating place in dataset...")
    while True:
        random_number = random.randint(10000,99999)
        print("trying "+str(random_number)+"...")
        if not os.path.exists("dataset/"+str(random_number)):
            os.mkdir("dataset/"+str(random_number))
            os.mkdir("dataset/"+str(random_number)+"/raw")
            os.mkdir("dataset/"+str(random_number)+"/processed")
            for photo in os.listdir("ADD_HERE"):
                os.rename("ADD_HERE/"+photo, "dataset/"+str(random_number)+"/raw/"+photo)
            print("done! the photos have been added to the dataset. (dataset/"+str(random_number)+"/raw/)")
            break
    print("generating json file...")
    data = {
        "number_of_photos": number_of_photos,
        "percentage_of_clouds": percentage_of_clouds,
        "weather_condition": weather_condition,
        "notes": notes
    }
    with open("dataset/"+str(random_number)+"/info.json", "w") as f:
        json.dump(data, f)
    print("done! the json file has been generated. (dataset/"+str(random_number)+"/info.json)")
    print("renaming photos...")
    i = 1
    for photo in os.listdir("dataset/"+str(random_number)+"/raw"):
        os.rename("dataset/"+str(random_number)+"/raw/"+photo, "dataset/"+str(random_number)+"/raw/"+str(i)+"."+photo.split(".")[-1])
        i += 1
    print("done! the photos have been renamed. (dataset/"+str(random_number)+"/raw/)")
    print("Deleting ADD_HERE folder...")
    os.rmdir("ADD_HERE")
    try:
        os.mkdir("tmp")
    except FileExistsError:
        pass

    with open("tmp/location.txt", "w") as f:
        f.write(os.getcwd()+"/dataset/"+str(random_number))
    with open("tmp/number.txt", "w") as f:
        f.write(str(random_number))
    print("Processing photos...")
