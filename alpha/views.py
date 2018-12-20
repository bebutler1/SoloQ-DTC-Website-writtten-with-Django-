from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
import os.path, sys, os, time, csv, random
from os import path

from .forms import DataForm
# Create your views here.
def index(request):   
    return render(request, 'main.html',{'form': form})

def opt1(request):
    if request.method == 'POST':
        form = DataForm(request.POST)
        if form.is_valid():
#This section collects the info from the form and stores it into variables
            
            pname = form.cleaned_data['your_name'] #player's name
            champ = form.cleaned_data['champion'] #champoin name 
            role = form.cleaned_data['role'] #player's role
            tmate1 = form.cleaned_data['teammate_1'] #teammate 1's name
            tmate2 = form.cleaned_data['teammate_2'] #teammate 2's name 
            tmate3 = form.cleaned_data['teammate_3'] #teammate 3's name 
            tmate4 = form.cleaned_data['teammate_4'] #teammate 4's name
            outcome = form.cleaned_data['outcome'] #game's outcome 
            mute = form.cleaned_data['mute'] #whether the player muted anyone 
            ascore = form.cleaned_data['attitude_Score'] #player's attitude score 
            comments = form.cleaned_data['comments'] #player's comments 
            
#Now the Real fun begins. The following runs the functionality of option 1

            test = str(path.exists('games.csv')) #check if the storage file is exists or not
            if test == "True": #It does, so we will append, so we don't overwrite existing data 
                print("Great you've got the file on your computer!\n You can run any function you'd like to.\n\n")
                print("The program will begin in a moment")
                print("File Found....")
                print("Initializing....")
        
                with open('games.csv','a', newline = '') as file:
                    filewriter = csv.writer(file, delimiter=',',quotechar='|', quoting=csv.QUOTE_MINIMAL)
                    filewriter.writerow([pname, champ, role, tmate1, tmate2, tmate3, tmate4, outcome, mute, ascore, comments]) #output to the file
    
            else: #It doesn't, so we want to create it and set up a base line at the start, this else will only be run once, so long as the file isn't deleted
                print("I couldn't locate the appropriate file on your computer. I'll just create it")
                print("The program will begin in a moment")
                with open('games.csv','w', newline = '' ) as file:
                    filewriter = csv.writer(file, delimiter=',',quotechar='|', quoting=csv.QUOTE_MINIMAL)
                    filewriter.writerow(['Player_Name', 'Champion', 'Position', 'Teammate 1', 'Teammate 2', 'Teammate 3', 'Teammate 4', 'Outcome(Win/Loss)','Muted(Yes/No)' ,'Attitude Score','Comments'])
                    filewriter.writerow([pname, champ, role, tmate1, tmate2, tmate3, tmate4, outcome, mute, ascore, comments]) #output to the file

                                         
                    


            return HttpResponseRedirect('/run1/' )#redirects when the form is submitted, runs the run1 function down below...
        
    else:  #loads the initial page with a fresh form, just waiting to be filled out
        form = DataForm()

    return render(request, 'alpha/main.html',{'form': form})
    
def run1(request): #when redirect is called it comes here, this loads a page that changes the tabbed regions to their updated forms, so that you can review the data from the tabs

    #That wraps up what we needed to do for option one, now we move on to what's needed for part two
    games = [] #list that stores games
    wins = [] #list that stores wins
    scores = [] #list that stores attitude scores as strings
    ratings = [] #List to store attitude scores as integers
    low = 50.0  #if below, it's a low attitude score (lower bound)
    high = 75.0 #if above, it' a high attitude score (upper bound)

    win = 'win'
    Win = 'Win'

 # open file
    with open('games.csv', 'r') as f:
        reader = csv.reader(f)
        rowNr = 0
        for row in reader: #read file row by row
            if rowNr >= 1:
                games.append(row[7]) #adds the game to the games list 
                scores.append(row[9]) #adds the scores to the scores list
            rowNr = rowNr + 1

        totgames = len(games)    #Stores total number of items in games list

        #Make a new list with only the wins
        for x in games:
            if x == win:
                wins.append(x)
            elif x == Win:
                wins.append(x)

        totwins = len(wins) #stores the total number of items in wins list

#Let's create a dictionary to map the values to return the data to html

        #outputs = { "winrate": winrate, "attitute_score": avg_score, "response": response }

        #Test to see if there are any wins
                
        if totwins == 0: #no wins
            winrate = "0"
        else: #there are wins
            base = totwins/totgames #stores the winrate as a decimal by dividing the two numbers
            floatt = 100 * base  #multiply by 100 to get the decimal to be a whole number
            whole = int(floatt)
            winrate = str(whole) + "%"

        #Let's make a list of all the scores as numbers not strings

        for y in scores:
            num = int(y)
            ratings.append(num) #add it to the list for scores

        rate = 0 #this will be the sum of all the scores
        divisor = len(ratings) #stores the total number of items in the list

        for val in ratings: #a loop that adds them all up
             rate += val #continually updated rate

        score = rate / divisor
        avg_score = int(score)

        if avg_score < low:
            response = "Your score could mean that you aren't having a very good time with League of Legends at the moment.You may be prone to tilting, flaming your teammates, and overall you could be spreading your negative attitude, and hurting you, and your teammate's gameplay.One suggestion I have for you is to take a break. There's no sense in playing if you're not enjoying it.Improve your play and improve your attitude. Muteall at the start of every game turn the ping volume down, and focus on your own play."
                
        elif low < avg_score < high:  
            response = "Your score could mean that you're not having a horrible time with the game, but that you might be getting a bit bored with it. Remember to that climbing happens as you improve, so just try to improve. If you're bored, play different champs, try a different lane. Practice in a normal game or ARAM. Even take a break for a bit play something else."

        elif avg_score > high:
            response = "Wow, you're having a great time. Keep up the good work. I'm sure you're climbing and having a great time with your teammates, so keep doing what you're doing, and have fun out there on the rift."
                    

#Onward to part 3's code, originally it had a search feature, but as of right now this doesn't, so it'll only output the people who are in more than 1/4 of the game's winrate's anyway....

    #declare the variable that are needed 
        entry = ""
        y = 0
        store =[]
        wins_per_teammates = []
        keys = []
        duplicates = 0
        exceptions = 0
        dgames = []
        dwins = []
        team1 =[]
        team2 = []
        team3 = []
        team4 = []
        players = [] # list for player that meet criteria
        drates = []
        counter = 0;
        team_wins = []
        with open('games.csv', 'r') as f:
            reader = csv.reader(f)
            rowNr = 0
            for row in reader:
        # Skip the header row.
                if rowNr >= 1:
                    dgames.append(row[7]) #store the game outcomes
                    team1.append(row[3])  #store teammate 1
                    team2.append(row[4])  #store teammate 2
                    team3.append(row[5])  #store teammate 3
                    team4.append(row[6])  #store teammate 4
 
        # Increase the row number
                rowNr = rowNr + 1
        zipped = zip(team1,dgames)
        zipped2 = zip(team2,dgames)
        zipped3 = zip(team3,dgames)
        zipped4 = zip(team4, dgames)
        big_brain = team1 + team2 + team3 + team4
        length = len(big_brain) - 1 #a large lists of all of the teammates, this includes duplicates that might occur if the same player appears in a different column
        #We zip the two lists together because this allows us to create a value called 'key' the key is a player's name and the word win, we only care about wins, and the loses are bad keys 
        for c, value in enumerate(zipped):
            store.append(value)#store the zipped values into a list called store
        for c, value in enumerate(zipped2):
            store.append(value)#store the zipped values into a list 
        for c, value in enumerate(zipped3):
            store.append(value)#store the zipped values into a list 
        for c, value in enumerate(zipped4):
            store.append(value)#store the zipped values into a list
        threshold = len(team1)/2 /2 #establish the amount of games needed (all lists are the same length, and the length is also the same as the total amount of games
        print("this is threshold" + str(threshold))
        while y <= length:
            entry = big_brain[y] #this is the players name inside big_brain
            key = (entry, 'Win')
            if entry not in keys:
                keys.append(entry) #store only the unique names, not duplicates
                occurs = store.count(key) #stores the number of occurences of the current key inside our list of keys
                #this is done from within this if so that duplicates aren't counted. Only the good keys are counted as we specified what key was outside, so loses aren't counted at all, but all the names are stored
                wins_per_teammates.append(occurs) #add it to the list of wins, only teammates with wins will be stored here
                if threshold >=1:
                    if occurs >= threshold: #the player's played enough games
                        result = occurs / len(team1) * 100 #the winrate as decimal
                        quarter_wins = int(result) #make that decimal round
                        names = str(entry)
                        players_rate = str(quarter_wins)
                        print(players_rate)
                        players.append(names)
                        drates.append(players_rate + '%')
                        print("Your winrate with " + str(entry) + " is: " + str(int(result)))

                    else:
                        exceptions += 1
                else:
                    words = "There's not enough data, add more and try again"
            else:
                duplicates +=1 #bump the duplicates counter

            y +=1 #continue the while loop 
                    

        

    return render(request, 'alpha/submission.html',{'winrate':winrate, 'attitude':avg_score, 'response': response, 'players':players, 'rates':drates, 'threshold':threshold})

            
                
