##################################################################################################################################################################
# Computer Project #5 
#
# Algorithm
#   define function called open_file() which takes no arguments and it returns a file-pointer of a file
#   define function called find_max() which takes 4 arguments and compares and returns max value and corresponding title
#   define function called find_min() which takes 4 arguments and compares and returns min value and corresponding title
#   define function called read_file() which takes one argument (it itself calls find_min() and find_max() functions inside) and returns 7 values after comparison
#   define function callled search_anime() which takes 2 arguments - file-pointer and a string to search
#   define function main() which is like the starting point for everything and it displays menu and goes according to the user
#   calls menu only when name is main(kind of a special way)
##################################################################################################################################################################


def open_file():  #Here starts the function definition of open_file()
    """
    Prompts user to enter a file name and and does not leave user until the 
    person enters a valid file name
    
    Parameters
    -------
    None

    Returns
    -------
    file_pointer : It is the file object which is used to navigate through
                   the connection made between the Python Shell and the file in
                   the user's computer
    """
    file_name=input("\nEnter filename: ") #inputting file name from the user
    while True:       #a while loop looping till the user enters the one which exists
        try:          #which exists -- here try except
            file_pointer=open(file_name,"r",encoding="utf-8")
            break
        except FileNotFoundError:  #This except will only catch FileNotFoundError
            print("\nFile not found!")  #this error will be displayed
            file_name=input("\nEnter filename: ")  #for input of the filename
    return file_pointer    #returning filepointer afte all of this
    
def find_max(value,name,max_value,max_name):   #func definition fin_max() starts
    """
    It makes a single-time comparison to find the maximum value and the 
    corresponding title as passed by the user.

    Parameters
    ----------
    value : float
           The value to be compared
    name : string
           The corresponding title of the value
    max_value : float
                The maximum value to be compared with as inputted by the user
    max_name : string
               The corresponding title of the max_value  

    Returns
    -------
    float type
        It returns the maximum value that is obtained after comparison
    string type
        It returns the corresponding maximum title after comparison
        
    """
    if value<max_value:        #1st comparison being made between value and max_val 
        return max_value, max_name       #returning the correct maxval and maxname
    elif value>max_value:          #if the above didn't satify then this
        return value, "\n\t{}".format(name)   #returning the correct maxval and maxname
    else:                          #if the above didn't satify then this
        max_name=max_name+"\n\t"+name  
        return max_value,max_name   #returning the correct maxval and maxname
    
    
def find_min(value,name,min_value,min_name):   #func definition fin_min() starts
    """
    It makes a single-time comparison to find the minimum value and the 
    corresponding title as passed by the user.    

    Parameters
    ----------
    value : float
            The value which is to be compared as inputted by the user
    name : string
           The corresponding title of the value
    min_value : float
                The minimum value to be compared with as inputted by the user
    min_name : string
               The corresponding title of the min_value 

    Returns
    -------
    float type
        It returns the minimum value that is obtained after comparison
    string type
        It returns the corresponding minimum title after comparison

    """
    if value>min_value:
        return min_value,min_name
    elif value<min_value:
        return value,"\n\t{}".format(name)
    else:
        min_name=min_name+"\n\t"+name
        return min_value,min_name

def read_file(data_fp):  #Here starts the function definition of read_file()
    """
    It goes through the file, reading the file line by line and compares values
    to finally find the highest scoring title, the highest episode count title,
    and the lowest scoring title
    
    Parameters
    ----------
    data_fp : The file pointer object
              It is the file pointer of the file

    Returns
    -------
    ini_max : float
              It is the highest score after all the comparisons through 
              the data of the file
    
    ini_max_name : string
                   It is the corresponding title of the highest
                   value found out
        
    ini_max_ep : float
                 It is the highest total episode count after going though all 
                 the data line by line thoughout the file
        
    ini_max_epname : string
                     It is the corresponding highest total episode count
                     anime title
        
    ini_min : float
              It is the lowest score after all the comparisons through the data
              of the file
        
    ini_min_name : string
                   It is the corresponding title of the lowest
                   value found out                   
        
    avg_score : float
                It is the computed average value of the scores
        
    """
    ini_min=10**7              #initializing all the values
    ini_min_name='z'* 100
    ini_max_ep=0
    ini_max_epname=''
    ini_max=0
    ini_max_name=""
    avg_sum=0
    num=0
    for line in data_fp:       #going through line by line through the file
        title=line[0:100].strip()    #stripping out the extra spaces
        try:             #now this try except is to make sure that I don't convert 
            score=float(line[100:105].strip())   #N/A to float
            num+=1                     #for average score calculation usage
        except ValueError:
            score=line[100:105].strip()
        try:             #same concept applied here for episodes as well       
            episodes=float(line[105:110].strip())  
        except ValueError:                   
            episodes=line[105:110].strip()
        if score=="N/A" and episodes!="N/A":   #1st if case
            ini_max_ep,ini_max_epname=find_max(episodes,title,ini_max_ep,\
ini_max_epname)
        elif score!="N/A" and episodes=="N/A": #2nd if case(elif)
            ini_min,ini_min_name=find_min(score,title,ini_min,ini_min_name)
            ini_max,ini_max_name=find_max(score,title,ini_max,ini_max_name)
            avg_sum+=score
        elif score!='N/A' and episodes!="N/A": #3rd (elif)
            ini_min,ini_min_name=find_min(score,title,ini_min,ini_min_name)
            ini_max,ini_max_name=find_max(score,title,ini_max,ini_max_name)
            avg_sum+=score
            ini_max_ep,ini_max_epname=find_max(episodes,title,ini_max_ep,\
ini_max_epname)
    if num==0:           #condition as specified in the documentation
        avg_score=0.0
    else:
        avg_score=avg_sum/num         #calculating avg score
        avg_score=round(avg_score,2)   #ounding to 2 decimal places
    return ini_max,ini_max_name,ini_max_ep,ini_max_epname,ini_min,\
ini_min_name,avg_score           #returning 7 values 
    
        
def search_anime(data_fp,search_str):  #func def for search_anime() function
    """
    It's purpose is to find out the animes which contain a particular string
    in their title and also to find out the number of animes which have them

    Parameters
    ----------
    data_fp : file pointer object
              It is the file pointer
    
    search_str : string
                 It is the string to be searched for in the titles of the
                 animes

    Returns
    -------
    str_count : Integer
                It is the count of the number of animes which have the
                search_str in their titles
                
    str_title : String
                These are the title(s) which contain the search_str in their
                titles

    """
    str_count=0              #initializing values
    str_title=""
    for line in data_fp:     #going through the file line by line
        title=line[0:100].strip()     #getting rid of extra spaces
        release_season=line[110:122].strip()   #getting rid of extra spaces
        if search_str in title:
            str_count+=1         #incrementing count by 1    
            str_title+="\n\t{:100}{:12}".format(title,release_season)
    return str_count,str_title   #returning 2 values

def main():          #function definition starts here for main()
    """
    This is the main function which displays the various menu options and 
    performs the activities(calling the above written functions accordingly)
    which the user asks for and loops until the user wants to break.
    
    Parameters
    ----------
    None.

    Returns
    -------
    None.

    """
    
    BANNER = "\nAnime-Planet.com Records" \
             "\nAnime data gathered in 2022"
    print(BANNER)                     #printing the banner
    while True:                       #a loop until the user wants to break
        MENU ="Options" + \
              "\n\t1) Get max/min stats" + \
              "\n\t2) Search for an anime" + \
              "\n\t3) Stop the program!"
        print(MENU)                   #printing the menu
        choice=input("\tEnter option: ")       #user input for choice
        if choice!="1" and choice!="2" and choice!="3": #if invalid, we go here
            while choice!="1" and choice!="2" and choice!="3": #loop until valid one
                print("\nInvalid menu option!!! Please try again!")
                print(MENU)           #printing the menu once again    
                choice=input("\tEnter option: ") #asking for user input
        if choice=="1":                 #if choice is 1, then we go here
            file_object=open_file()     #for valid filename and file pointer
            max_score,max_sc_title,max_ep,max_epname,min_score,min_sc_title,\
avg_score_here=read_file(file_object)   #getting all values
            
            print("\n\nAnime with the highest score of {}:\n{}".format(\
max_score,max_sc_title))                #printing in the right format
            print("\n\nAnime with the highest episode count of \
{:,.0f}:\n{}".format(max_ep,max_epname))
            print("\n\nAnime with the lowest score of {:.2f}:\n{}".format(\
min_score,min_sc_title))
            print("\n\nAverage score for animes in file is {}".format(\
avg_score_here))
            file_object.close()         #closing file pointer
            
        elif choice=="2":               #if choice is 2, then we go here
            file_obj=open_file()        #for valid filename and file pointer 
            anime_search=input("\nEnter anime name: ")  #user input for search
            anime_count,anime_titles= search_anime(file_obj,anime_search)
            if anime_count==0:       #if string not found in titles, we go here
                print("\nNo anime with '{}' was found!".format(anime_search))
            else:
                print("\nThere are {} anime titles with '{}'\n{}".format(\
anime_count,anime_search,anime_titles))
            file_obj.close()         #closing file pointer 
        elif choice=="3":            #if choice is 3, user can exit 
            print("\nThank you using this program!")  #bidding goodbye
            break                    #breaking the loop 

if __name__ == "__main__":           #special condition for this main
    main()
    
    
