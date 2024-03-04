import database as db
import views as fn

menu = """Please Select one of the Options:
1) Add new movie.
2) View upcoming movies.
3) View all movies.
4) Update Watched movie.
5) View Watched movies.
6) Search Movie Info using Title.
7) Exit.

(Please Select in Numbers)
Your Selection : """

print("Welcome to the Watchlist APP")

db.create()

#functions

while(True):
    get = int(input(menu))
    if(get == 1):
        fn.add_view()
    elif(get == 2):
        fn.data_view(upcoming=True)
    elif(get == 3):
        fn.data_view(upcoming=False)
    elif(get == 4):
        fn.update_view()
    elif(get == 5):
        fn.data_view(watched=True)
    elif(get == 6):
        search = input("Enter the Title Partially to Search : ")
        print(f"\n\n{fn.timestamp_conversion(db.search_movie(search))}\n\n")

    elif(get == 7):
        break
    else:
        print("Please Enter Proper Value !!\n Try again\n")