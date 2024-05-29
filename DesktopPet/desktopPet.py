import random
import tkinter as tk
import pyautogui
x = 1400
cycle = 0
check = 1
idle_num =[1,2,3,4]
sleep_num = [10,11,12,13,15]
walk_left = [6,7]
walk_right = [8,9]
event_number = random.randrange(1,3,1)
impath = 'C:\Users\e\Documents\GitHub\funthings\DesktopPet'
window = tk.Tk()

# call buddy's action .gif to an array
idle = [tk.PhotoImage(file=impath + 'idle.gif', format = 'gif -index %i'%(i)) for i in range(5)] # idle gif for 5 frames
idle_to_sleep = [tk.PhotoImage(file = impath + 'idle to sleep.gif', format = '.gif -index %i' %(i))for i in range(8)] # falling asleep up gif for 8 frames
sleep = [tk.PhotoImage(file = impath + 'sleep.gif', format = '.gif -index %i' %(i))for i in range(8)] # sleeping gif for 8 frames
sleep_to_idle = [tk.PhotoImage(file = impath + 'sleep to idle.gif', format = '.gif -index %i' %(i))for i in range(8)] # waking up gif for 8 frames
walk_positive = [tk.PhotoImage(file = impath + 'walking left.gif', format = '.gif -index %i' %(i))for i in range(8)] # walk left gif for 8 frames
walk_negative = [tk.PhotoImage(file = impath + 'walking right.gif', format = '.gif -index %i' %(i))for i in range(8)] # walk right gif for 8 frames

window.config(highlightbackground='black')
window.overrideredirect(True)
window.wm_attributes('-transparentcolor','black')

label = tk.Label(window, bd = 0, bg = 'black')
label.pack()
window.mainloop()

# function that makes the gif move
def gif_work(cycle, frames, event_number, first_num, last_num):
    if cycle < len(frames) -1:
        cycle+=1
    else:
        cycle = 0
        event_number = random.randrange(first_num, last_num + 1, 1)
        return cycle, event_number

def update(cycle, check, event_number, x):
    # idle
    if check == 0:
        frame = idle[cycle]
        cycle ,event_number = gif_work(cycle, idle, event_number, 1, 9)
        
    # falling asleep
    elif check == 1:
        frame = idle_to_sleep[cycle]
        cycle ,event_number = gif_work(cycle, idle_to_sleep, event_number, 10, 10)
        
    # sleeping
    elif check == 2:
        frame = sleep[cycle]
        cycle, event_number = gif_work(cycle, sleep, event_number, 10, 15)
        
    # waking up
    elif check == 3:
        frame = sleep_to_idle[cycle]
        cycle, event_number = gif_work(cycle, sleep_to_idle, event_number, 1, 1)
        
    # walking left
    elif check == 4:
        frame = walk_positive[cycle]
        cycle, event_number = gif_work(cycle, walk_positive, event_number, 1, 9)
        x -=3
        
    # walking right
    elif check == 5:
        frame = walk_negative[cycle]
        cycle, event_number = gif_work(cycle, walk_negative, event_number, 1, 9)
        x -= -3
        
    window.geometry('100x100+' + str(x) + '+1050')
    label.configure(image = frame)
    window.after(1, event, cycle, check, event_number, x)
    
    idle_num = [1, 2, 3, 4, 5]
    sleep_num = [10, 11, 12, 13, 14, 15]
    walk_left = [6,7]
    walk_right = [8,9]
    
    def event(cycle, check, event_number, x):
        if event_number in idle_num:
            check = 0
            print('idle')
            window.after(400, update, cycle, check, event_number, x)
            
        elif event_number == 5:
            check = 1
            print('from idle to sleep')
            window.after(100, update, cycle, check, event_number, x)
        
        elif event_number in walk_left:
            check = 4
            print('walking towards left')
            window.after(100, update, cycle, check, event_number, x)
            
        elif event_number in walk_right:
            check = 5
            print('walking towards right')
            window.after(100, update, cycle, check, event_number, x)
            
        elif event_number in sleep_num:
            check = 2
            print('sleep')
            window.after(1000, update, cycle, check, event_number, x)
        
        elif event_number == 14:
            check = 3
            print('sleep to idle')
            window.after(100, update, cycle, check, event_number, x)
            
        