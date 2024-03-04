import database as db
import datetime
import pandas as pd

def timestamp_conversion(value):
    if(len(value) == 0):
        return "No Data Found"
    display = pd.DataFrame(value)
    display["release_date"] = pd.to_datetime(display["release_date"], unit = 's')  #if for loop use .fromtimestamp(value[i]).strftime("%d %b %y")
    return display

def add_view():
    title = input("Please! Enter the Title:")
    timestamp = datetime.datetime.strptime(input("Enter the Date in dd-mm-yy !"),"%d-%m-%y").timestamp()
    db.add(title,timestamp)
    print("\n\nSuccessfully Added\n\n")

def data_view(watched=False,upcoming=False):
    movie = ""
    test = ""
    if watched:
        test = "watched"
        movie = db.get_watched_movie()
    elif upcoming:
        test = "upcoming"
        movie = db.display_movie(upcoming)
    else:
        test = "view_all"
        movie = db.display_movie(upcoming)
    
    print(f"\n\n{timestamp_conversion(value=movie)}\n\n")

def update_view():
    print(f"\n{timestamp_conversion(value=db.unwatched_movie())}\n")
    get_id = input("Please Enter any one ID to update watchlist to 1 :")
    final_id = ((lambda x:int(x)) (get_id) if(len(get_id)==1) else "Terminated - WrongID!!")
    db.update_watched(final_id)
    print(f"\n\n\tWatch List Updated to 1!!\n\n")