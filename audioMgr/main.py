#imports
from display import print_menu, print_header, clear
from album import Album
from song import Song
import pickle


#globals
catalog = []
album_count = 0
next_id = []



#functions
def serialize_data():
    try:
        writer = open('songMngr.data', 'wb')  # wb = write binary
        pickle.dump(catalog, writer)
        writer.close()
        print("** Data serialized!")

    except:
        print("** Error, data not saved")

def deserialize_data():
    global next_id

    try:
        reader = open('songMngr.data', 'rb')  # rb = read binary
        temp_list = pickle.load(reader)
        reader.close()

        for prod in temp_list:
            catalog.append(prod)

        # get the last used id, and increase by 1
        last = catalog[-1]
        album_count = last.id + 1

        how_many = len(catalog)
        print("** Read: " + str(how_many) + " albums")

    except:
        print("** Error, no data file found")


def register_album():
    global album_count
    print_header("Register a new Album")

    try:  
        #title, genre, artist, release_year, price, album_art, related_artist, record_label
        title = input("Please provide Title: ")
        genre = input("Please privide Genre: ")
        artist= input("Please provide Artist: ")
        release_year = int(input("Please provide Release Year: "))
        price = float(input("Please provide Price: $"))
        album_art = input("Please provide AlbumArt: ")
        related_artist = input("Please provide Related Artist: ")
        record_label = input("Please provide Record Label: ")

        album_count += 1

        album = Album(album_count, title, genre, artist, release_year, price, album_art, related_artist, record_label)
        catalog.append(album)
        print(album)

        # push the album into the ist
        catalog.append(album)
        print("** Album created!")

    except ValueError:
        print("** Error: Invalid Number.. Try again")

    
    except:
        print('** Unexpected Error. Try again later')

def print_albums():
    print_header("you current albums")

    for album in catalog:
        print(f"{album.id} | {album.title}| {album.release_year}")

def register_song():

    #let the user choose an album
    print_albums()
    album_id = int(input("Please choose the album Id: "))

    #find the album with that id
    found = False
    for album in catalog:
        if(album.id == album_id):
            found = True
            the_album = album

    if(not found):
        print("**Error: Wrong id. Try again")
        return

    #create the song
    print_header("Register a new Song")

    title = input("Please provide a Title: ")
    feature_artist = input("Please provide a Featured Artist: ")
    length_of_song = input("Please provide the Length in Seconds:")
    written_by = input("Please provide the song Author: ")

    song = Song(1, title, feature_artist, length_of_song, written_by)

    # push the song to the album list
    the_album.add_song(song)

    print("** Song Registered")


def count_songs():
    print_header("Your total number of songs")

    total = 0
    for album in catalog:
        songs_catalog = len(album.songs)
        total += songs_catalog

    print(f"There are: {total} songs in the system")


#instructions

deserialize_data()
input("Please Enter to continue...")

opc = ''
while(opc != 'q' and opc != 'x'):
    clear()
    print_menu()
    opc = input("Please select an option: ")

    if(opc == '1'):
        register_album()
        serialize_data()

    elif(opc == '2'):
        register_song()
        serialize_data()

    elif(opc == '3'):
        print_albums()
        
    input("press Enter to continue...")