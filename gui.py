import tkinter as tk
from functools import partial
import song


from PIL import Image, ImageTk


#possible_songs = song.get_possible_options(song.pre_game(r"C:\Users\Ariel\Desktop\RAZ\music"), 4)
#poss_names = song.get_song_names(possible_songs)

#correct_ans = poss_names[3]
correct_ans = "Hey you"
def print_selection(song_selected, correct):
    if (song_selected == correct):
        answer_value["text"] = "You're right!"
    else:
        answer_value["text"] = "You're wrong!"

window = tk.Tk()

canvas = tk.Canvas(window, width=500, height=300)
canvas.grid(columnspan=5)

def define_btn(song_name, btn_h, btn_w):
    new_btn = tk.Button(master=window, text=song_name, font="Cambria", bg="#20bebe", fg="white", height=btn_h, width=btn_w)
    new_btn['command'] = partial(print_selection, new_btn['text'], correct_ans)

    return new_btn

# Game Logo
logo = Image.open('logo.png')
logo = ImageTk.PhotoImage(logo)
logo_label = tk.Label(image=logo)
logo_label.image = logo
logo_label.grid(column=3, row=0)

# Button configurations
song_btn_h = 2
song_btn_w = 15

sng_lst = ["Hey you", "Scenes", "Try harder", "Not again"]
sng_lst = ["-", "-", "-", "-"]

song_buttons = list()
for idx,sng in enumerate(sng_lst):
    song_btn = define_btn(sng, song_btn_h, song_btn_w)
    #0 -> 1, 1
    #1 -> 1, 4
    #2 -> 4, 1
    #3 -> 4, 4
    if idx == 0:
        r = 1
        c = 1
    if idx == 1:
        r = 1
        c = 4
    if idx == 2:
        r = 4
        c = 1
    if idx == 3:
        r = 4
        c = 4
    song_btn.grid(row=r, column=c, sticky="nsew")
    song_buttons.append(song_btn)

start_btn = tk.Button(master=window, text="Start", font="Cambria", bg="#20bebe", fg="white", height = song_btn_h, width = song_btn_w - 10 )
start_btn.grid(row=4, column=3, sticky="nsew")
start_btn['command'] = partial(song.pre_game, r"C:\Users\Ariel\Desktop\RAZ\music")
# btn_opt_1 = tk.Button(master=window, text="Song 1", font="Cambria", bg="#20bebe", fg="white", height=song_btn_h, width=song_btn_w)
# btn_opt_1['command'] = partial(print_selection, btn_opt_1['text'],correct_ans)
# btn_opt_1.grid(row=1, column=1, sticky="nsew")
#
# btn_opt_2 = tk.Button(master=window, text="Song 2", font="Cambria", bg="#20bebe", fg="white", height=song_btn_h, width=song_btn_w)
# btn_opt_2['command'] = partial(print_selection, btn_opt_2['text'], correct_ans)
# btn_opt_2.grid(row=1, column=4, sticky="nsew")
#
# btn_opt_3 = tk.Button(master=window, text="Song 3", font="Cambria", bg="#20bebe", fg="white", height=song_btn_h, width=song_btn_w)
# btn_opt_3['command'] = partial(print_selection, btn_opt_3['text'],correct_ans)
# btn_opt_3.grid(row=4, column=1, sticky="nsew")
#
# btn_opt_4 = tk.Button(master=window, text="Song 4", font="Cambria", bg="#20bebe", fg="white", height=song_btn_h, width=song_btn_w)
# btn_opt_4['command'] = partial(print_selection, btn_opt_4['text'],correct_ans)
# btn_opt_4.grid(row=4, column=4, sticky="nsew")

answer_value = tk.Label(master=window, text="Waiting for selection", font="Cambria")
answer_value.grid(row=3, column=3)



window.mainloop()
#song.pre_game(r"C:\Users\Ariel\Desktop\RAZ\music")
