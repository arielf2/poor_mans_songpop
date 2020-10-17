import os
from librosa import load
import numpy.random
import random
import glob
from mutagen.mp3 import MP3
from mutagen.id3 import ID3, TIT2, ID3NoHeaderError
from sounddevice import play
#

import warnings
warnings.filterwarnings("ignore")


def file_has_title_ID(song_path: str) -> bool:
   try:
       ID3(song_path)
   except ID3NoHeaderError:
      return False
   if not ID3(song_path).getall('TIT2'):
      return False
   return True

def collect_mp3_paths(music_folder: str):
   return glob.glob(f"{music_folder}\**\*.mp3", recursive=True)

def remove_invalid_ID3_songs(song_list: list):
   return [song for song in song_list if file_has_title_ID(song)]

def get_possible_options(song_list: list, num_of_songs: int):
   return [random.choice(song_list) for cnt in range(num_of_songs)]

def song_title_from_full_path(path: str):
   return ID3(path).getall('TIT2')[0]

def get_song_names(songs: list):
   return [song_title_from_full_path(song) for song in songs] 
          
def get_song_duration(song: str):
   return MP3(song).info.length

def pre_game(folder: str):
   song_paths_list = collect_mp3_paths(folder)
   song_paths_list = remove_invalid_ID3_songs(song_paths_list)
   main_game(song_paths_list, 3)

def print_round(current_round: int):
   round_string = f"Round {current_round + 1}"
   print("#" * 25)
   print("# {:^21} #".format(round_string))
   print("#" * 25)

def main_game(song_list: list, snippet_duration: int):

   game = True
   turns = 0
   wins = 0
   while (game):
      
      print_round(turns)
   
      # Generate 4 random songs
      possible_songs = get_possible_options(song_list, 4)

      # Pick one of them to play
      chosen_song = get_possible_options(possible_songs, 1)[0]

      # Fetch the real title from the ID3 of the file
      chosen_song_name = song_title_from_full_path(chosen_song)   
      song_names = get_song_names(possible_songs)

      # Generate a valid random offset from which to play the song          
      chosen_song_duration = get_song_duration(chosen_song)
      random_offset = numpy.random.randint(int(chosen_song_duration))

      # Load and Play
      chosen_song, sr = load(path=chosen_song, offset=random_offset, duration=snippet_duration)
      play(chosen_song, sr, blocking=True)

      # User menu
      choice = "-1"
      while (choice not in "12345"):
         for idx, title in enumerate(song_names):
            print(f"{idx + 1}. {title}")
         choice = input("What song is playing? (Or - press 5 to finish)\n")
           
      if (int(choice) == 5):
         game = False
      elif (int(choice) in [1, 2, 3, 4]):
            turns += 1
            if (song_names[int(choice) - 1] == chosen_song_name):
               print("You won!")
               wins += 1
            
            else:
               print("You lost!")     
               
                                    
      if (game == False):
         ratio = wins / turns
         print(f"Final score = {wins}/{turns} -> {100*ratio}%")

#m_folder = r"C:\Users\Ariel\Desktop\RAZ\music"
m_folder = r"C:\Users\Ariel\Downloads\Soulseek Downloads"


#pre_game(m_folder)
#main_game(folder)
