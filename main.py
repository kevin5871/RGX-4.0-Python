
                                                        ##############################
                                                        # RGX 4.0 Main Engine Script #
                                                        # Written by Python          #
                                                        # Engine Ver : v1.6b         #
                                                        # Version date : 2020.06.22  #
                                                        # Made by kevin5871(sfcatz)  #
                                                        # Thanks to : Kokosei J      #
                                                        ############################## 





                                                        ## Code Starts From Here ##
# import part
import pygame
from pygame.locals import *
from tkinter import *
from tkinter import messagebox
import requests
import platform
import os
import threading
import multiprocessing 
import random
import zipfile

# pip install pygame
# pip install requests

# CONST variable
WHITE = (255,255,255)
BLACK = (0,0,0)
BLUE = (0,0,255)
RED = (255,0,0)
GREEN = (0,255,0)
pad_width = 1280
pad_height = 720
VERSION = '1.6b'
fps = 60
desiredfps = 60
'''
def note1_image() :
    global note1list
    while True :
        for x in note1list :
            appear_image('img/noteimage.png', gamepad, None, 215, x, 255, 2)
def note2_image() :
    global note2list
    while True :
        for x in note2list :
            appear_image('img/noteimage.png', gamepad, None, 430, x, 255, 2)
def note3_image() :
    global note3list
    while True :
        for x in note3list :
            appear_image('img/noteimage.png', gamepad, None, 640, x, 255, 2)
def note4_image() :
    global note4list
    while True :
        for x in note4list :
            appear_image('img/noteimage.png', gamepad, None, 855, x, 255, 2)
'''


def DrawBar(pos, size, borderC, barC, progress, text1, textC):

    pygame.draw.rect(gamepad, borderC, (*pos, *size), 1)
    innerPos  = (pos[0]+3, pos[1]+3)
    innerSize = ((size[0]-6) * progress, size[1]-6)
    pygame.draw.rect(gamepad, barC, (*innerPos, *innerSize))
    text(text1, 'ttf/KaiGenGothicKR-Regular.ttf', 20, textC, pos[0]-75, pos[1]+10)
    #text(str(progress*100), 'ttf/KaiGenGothicKR-Regular.ttf', 20, textC, pos[0]+75, pos[1]+10)


def download_small(url, file_name) :
    with open(file_name, "wb") as file:   
        response = requests.get(url)               
        file.write(response.content)

def download_big(url, filename, barswitch, barpos, barsize, barborderC, barC):

    global done, crashed
    done = 0
    while not crashed :
        for event in pygame.event.get() :
            if event.type == pygame.QUIT :
                crashed = True
                return

        with open(filename, 'wb') as f:
            response = requests.get(url, stream=True)
            total = response.headers.get('content-length')
            if total is None:
                f.write(response.content)
            else:
                downloaded = 0
                total = int(total)
                print(total)
                #for data in response.iter_content(chunk_size=max(int(total/1000), 1024*1024)):
                for data in response.iter_content(chunk_size=int(total/1000)):
                    pygame.event.pump()
                    downloaded += len(data)
                    f.write(data)
                    done = int((downloaded/total) * 100)
                    #done2 = done/total
                    #sys.stdout.write("\r[%s%s]" % ('=' * done, ' ' * (50-done)) )    
                    #sys.stdout.flush()
                    print(done)
                    if barswitch == 1 :
                        DrawBar(barpos,barsize, barborderC, barC, done/100, 'Downloading...', WHITE)
                        pygame.display.flip()
                        clock.tick(desiredfps)
        return

def note1_image() :
    global note1list
    for x in note1list :
        appear_image('img/noteimage_normal.png', gamepad, None, 215, x, 255, 2)
        '''
        if 250 <= note1list[x] and note1list[x] <= 350 :
            appear_image('img/noteimage_miss2.png', gamepad, None, 215, note1list[x], 255, 2)
        elif 350 <= note1list[x] and note1list[x] <= 450 :
            appear_image('img/noteimage_good2.png', gamepad, None, 215, note1list[x], 255, 2)
        elif 450 <= note1list[x] and note1list[x] <= 550 :
            appear_image('img/noteimage_great2.png', gamepad, None, 215, note1list[x], 255, 2)
        elif 550 <= note1list[x] and note1list[x] <= 625 :
            appear_image('img/noteimage_perfect2.png', gamepad, None, 215, note1list[x], 255, 2)
        else :
            appear_image('img/noteimage_normal.png', gamepad, None, 215, note1list[x], 255, 2)
        '''
def note2_image() :
    global note2list
    for x in note2list :
        appear_image('img/noteimage_normal.png', gamepad, None, 430, x, 255, 2)
def note3_image() :
    global note3list
    for x in note3list :
        appear_image('img/noteimage_normal.png', gamepad, None, 640, x, 255, 2)
def note4_image() :
    global note4list
    for x in note4list :
        appear_image('img/noteimage_normal.png', gamepad, None, 855, x, 255, 2)

# Game
def noteimagemanage() :
    global note1list, note2list, note3list, note4list
    if(len(note1list) > 0) :
        note1_image()
    if(len(note2list) > 0) :
        note2_image()
    if(len(note3list) > 0) :
        note3_image()
    if(len(note4list) > 0) :
        note4_image()
'''
def noteimagemanage() :
    global note1list, note2list, note3list, note4list, trigger2
    if(trigger2 == 0) :
        t1.terminate()
        t2.terminate()
        t3.terminate()
        t4.terminate()
    t1 = threading.Thread(target=note1_image)
    t2 = threading.Thread(target=note2_image)
    t3 = threading.Thread(target=note3_image)
    t4 = threading.Thread(target=note4_image)
    t1.start()
    t2.start()
    t3.start()
    t4.start()
    trigger2 = 0
    pygame.time.delay(int(1000/fps))
    pygame.display.flip()
'''

def note1_control() :
    global note1list, speed, combo, max_combo, grade, fps
    #note1list.append(0)
    if(len(note1list) > 0) :
        for x in range(0,len(note1list)) :
            note1list[x] += 720 / (speed * fps)
        if(note1list[0] > 720) :
             del note1list[0]
             #print("1 deleted")
             grade[0] += 1
             if(max_combo < combo) :
                 max_combo = combo
             combo = 0
             appear_image('img/noteimage_miss2.png', gamepad, None, 215, 700, 255, 1)
        #del note1list[len(note1list) - 1]
def note2_control() :
    global note2list, speed, combo, max_combo, grade, fps
    #note2list.append(0)
    if(len(note2list) > 0) :
        for x in range(0,len(note2list))  :
            note2list[x] += 720 / (speed * fps)
        if(note2list[0] > 720) :
           del note2list[0]
           #print("2 deleted")
           grade[0] += 1
           if(max_combo < combo) :
               max_combo = combo
           combo = 0
           appear_image('img/noteimage_miss2.png', gamepad, None, 430, 700, 255, 1)
        #del note2list[len(note2list) - 1]
def note3_control() :
    global note3list, speed, combo, max_combo, grade, fps
    #note3list.append(0)
    if(len(note3list) > 0) :
        for x in range(0,len(note3list))  :
            note3list[x] += 720 / (speed * fps)
        if(note3list[0] > 720) :
            del note3list[0]
            #print("3 deleted")
            grade[0] += 1
            if(max_combo < combo) :
                max_combo = combo
            combo = 0
            appear_image('img/noteimage_miss2.png', gamepad, None, 640, 700, 255, 1)
                #break
        #del note3list[len(note3list) - 1]
def note4_control() :
    global note4list, speed, combo, max_combo, grade, fps
    #note4list.append(0)
    if(len(note4list) > 0) :
        for x in range(0,len(note4list))  :
            note4list[x] += 720 / (speed * fps)
        if(note4list[0] > 720) :
             del note4list[0]
             #print("4 deleted")
             grade[0] += 1
             if(max_combo < combo) :
                 max_combo = combo
             combo = 0
             appear_image('img/noteimage_miss2.png', gamepad, None, 855, 700, 255, 1)
                #break
        #del note4list[len(note4list) - 1]

def notelistmanage() :
    global note1list, note2list, note3list, note4list
    if(len(note1list) > 0) :
        note1_control()
    if(len(note2list) > 0) :
        note2_control()
    if(len(note3list) > 0) :
        note3_control()
    if(len(note4list) > 0) :
        note4_control()

'''
def notelistdelete() :
    global note1list, note2list, note3list, note4list
    for x in range(0, len(note1list)) :
        if(note1list[x] < 720):
            print(x)
            del note1list[0:x]
            break
    for x in range(0, len(note2list)) :
        if(note2list[x] < 720):
            print(x)
            del note2list[0:x]
            break
    for x in range(0, len(note3list)) :
        if(note3list[x] < 720):
            print(x)
            del note3list[0:x]
            break
    for x in range(0, len(note4list)) :
        if(note4list[x] < 720):
            print(x)
            del note4list[0:x]
            break
'''
def scoreprint() :
    global score, combo, max_combo, max_score, percent
    percent = float(score / max_score * 100)
    text('SCORE','ttf/Bittypix-Countdown.ttf', 35, WHITE, 1200, 50)
    text("%05d"% score,'ttf/Bittypix-Countdown.ttf', 35, WHITE, 1200, 100)
    text('MAX_COMBO','ttf/Bittypix-Countdown.ttf', 20, WHITE, 1200, 150)
    text("%04d"% max_combo,'ttf/Bittypix-Countdown.ttf', 20, WHITE, 1230, 180)
    text('COMBO','ttf/Bittypix-Countdown.ttf', 20, WHITE, 1225, 220)
    text("%04d"% combo,'ttf/Bittypix-Countdown.ttf', 20, WHITE, 1230, 250)
    text("%.02f%%"% percent, 'ttf/Enchanted-Land.ttf', 45, WHITE, 1225, 650)

'''
if 250 <= note1list[x] and note1list[x] <= 350 :
            appear_image('img/noteimage_miss2.png', gamepad, None, 215, note1list[x], 255, 2)
        elif 350 <= note1list[x] and note1list[x] <= 450 :
            appear_image('img/noteimage_good2.png', gamepad, None, 215, note1list[x], 255, 2)
        elif 450 <= note1list[x] and note1list[x] <= 550 :
            appear_image('img/noteimage_great2.png', gamepad, None, 215, note1list[x], 255, 2)
        elif 550 <= note1list[x] and note1list[x] <= 625 :
            appear_image('img/noteimage_perfect2.png', gamepad, None, 215, note1list[x], 255, 2)
        else :
            appear_image('img/noteimage_normal.png', gamepad, None, 215, note1list[x], 255, 2)
'''
def note1clicked() :
    global note1list, max_combo, combo, grade, score
    for x in range(0, len(note1list)) :
        if(note1list[x] < 720):
            print(x)
            if not note1list[x] < 250 :
                if 250 <= note1list[x] and note1list[x] <= 350 :
                    grade[0] += 1
                    if(max_combo < combo) :
                        max_combo = combo
                    combo = 0
                    appear_image('img/noteimage_miss2.png', gamepad, None, 215, note1list[x], 255, 1)
                elif 350 <= note1list[x] and note1list[x] <= 425 :
                    grade[1] += 1
                    score += 4
                    if(max_combo < combo) :
                        max_combo = combo
                    combo = 0
                    appear_image('img/noteimage_good2.png', gamepad, None, 215, note1list[x], 255, 1)
                elif 425 <= note1list[x] and note1list[x] <= 500 :
                    grade[2] += 1
                    score += 7
                    combo += 1
                    if(max_combo < combo) :
                        max_combo = combo
                    appear_image('img/noteimage_great2.png', gamepad, None, 215, note1list[x], 255, 1)
                elif 500 <= note1list[x] and note1list[x] <= 625 :
                    grade[3] += 1
                    score += 10
                    combo += 1
                    if(max_combo < combo) :
                        max_combo = combo
                    appear_image('img/noteimage_perfect2.png', gamepad, None, 215, note1list[x], 255, 1)
                else :
                    grade[0] += 1
                    if(max_combo < combo) :
                        max_combo = combo
                    combo = 0
                    appear_image('img/noteimage_miss2.png', gamepad, None, 215, note1list[x], 255, 1)
            del note1list[0:x]
            break
    try:  del note1list[0]
    except:  pass
def note2clicked() :
    global note2list, max_combo, combo, grade, score
    for x in range(0, len(note2list)) :
        if(note2list[x] < 720):
            print(x)
            if not note2list[x] < 250 :
                if 250 <= note2list[x] and note2list[x] <= 350 :
                    grade[0] += 1
                    if(max_combo < combo) :
                        max_combo = combo
                    combo = 0
                    appear_image('img/noteimage_miss2.png', gamepad, None, 430, note2list[x], 255, 1)
                elif 350 <= note2list[x] and note2list[x] <= 425 :
                    grade[1] += 1
                    score += 4
                    if(max_combo < combo) :
                        max_combo = combo
                    combo = 0
                    appear_image('img/noteimage_good2.png', gamepad, None, 430, note2list[x], 255, 1)
                elif 425 <= note2list[x] and note2list[x] <= 500 :
                    grade[2] += 1
                    score += 7
                    if(max_combo < combo) :
                        max_combo = combo
                    combo += 1
                    appear_image('img/noteimage_great2.png', gamepad, None, 430, note2list[x], 255, 1)
                elif 500 <= note2list[x] and note2list[x] <= 625 :
                    grade[3] += 1
                    score += 10
                    combo += 1
                    if(max_combo < combo) :
                        max_combo = combo
                    appear_image('img/noteimage_perfect2.png', gamepad, None, 430, note2list[x], 255, 1)
                else :
                    grade[0] += 1
                    if(max_combo < combo) :
                        max_combo = combo
                    appear_image('img/noteimage_miss2.png', gamepad, None, 430, note2list[x], 255, 1)
                    combo = 0
            del note2list[0:x]
            break
    try:  del note2list[0]
    except:  pass
def note3clicked() :
    global note3list, max_combo, combo, grade, score
    for x in range(0, len(note3list)) :
        if(note3list[x] < 720):
            print(x)
            if not note3list[x] < 250 :
                if 250 <= note3list[x] and note3list[x] <= 350 :
                    grade[0] += 1
                    if(max_combo < combo) :
                        max_combo = combo
                    combo = 0
                    appear_image('img/noteimage_miss2.png', gamepad, None, 640, note3list[x], 255, 1)
                elif 350 <= note3list[x] and note3list[x] <= 425 :
                    grade[1] += 1
                    score += 4
                    if(max_combo < combo) :
                        max_combo = combo
                    combo = 0
                    appear_image('img/noteimage_good2.png', gamepad, None, 640, note3list[x], 255, 1)
                elif 425 <= note3list[x] and note3list[x] <= 500 :
                    grade[2] += 1
                    score += 7
                    combo += 1
                    if(max_combo < combo) :
                        max_combo = combo
                    appear_image('img/noteimage_great2.png', gamepad, None, 640, note3list[x], 255, 1)
                elif 500 <= note3list[x] and note3list[x] <= 625 :
                    grade[3] += 1
                    score += 10 
                    combo += 1
                    if(max_combo < combo) :
                        max_combo = combo
                    appear_image('img/noteimage_perfect2.png', gamepad, None, 640, note3list[x], 255, 1)
                else :
                    grade[0] += 1
                    if(max_combo < combo) :
                        max_combo = combo
                    combo = 0
                    appear_image('img/noteimage_miss2.png', gamepad, None, 640, note3list[x], 255, 1)
            del note3list[0:x]
            break
    try:  del note3list[0]
    except:  pass
def note4clicked() :
    global note4list, max_combo, combo, grade, score
    for x in range(0, len(note4list)) :
        if(note4list[x] < 720):
            print(x)
            if not note4list[x] < 250 :
                if 250 <= note4list[x] and note4list[x] <= 350 :
                    grade[0] += 1
                    if(max_combo < combo) :
                        max_combo = combo
                    combo = 0
                    appear_image('img/noteimage_miss2.png', gamepad, None, 855, note4list[x], 255, 1)
                elif 350 <= note4list[x] and note4list[x] <= 425 :
                    grade[1] += 1
                    score += 4
                    if(max_combo < combo) :
                        max_combo = combo
                    combo = 0
                    appear_image('img/noteimage_good2.png', gamepad, None, 855, note4list[x], 255, 1)
                elif 425 <= note4list[x] and note4list[x] <= 500 :
                    grade[2] += 1
                    score += 7
                    combo += 1
                    if(max_combo < combo) :
                        max_combo = combo     
                    appear_image('img/noteimage_great2.png', gamepad, None, 855, note4list[x], 255, 1)
                elif 500 <= note4list[x] and note4list[x] <= 625 :
                    grade[3] += 1
                    score += 10
                    combo += 1
                    if(max_combo < combo) :
                        max_combo = combo
                    appear_image('img/noteimage_perfect2.png', gamepad, None, 855, note4list[x], 255, 1)
                else :
                    grade[0] += 1
                    if(max_combo < combo) :
                        max_combo = combo
                    combo = 0
                    if(max_combo < combo) :
                        max_combo = combo
                    appear_image('img/noteimage_miss2.png', gamepad, None, 855, note4list[x], 255, 1)
            del note4list[0:x]
            break
    try:  del note4list[0]
    except:  pass
def set() :
    notelistmanage()
    gamebackground1()
    noteimagemanage()
    scoreprint()


def startengine() :
    global fps, timer, keylist, timelist, crashed, background, note1list, note2list, note3list, note4list, speed, trigger, trigger2, score, grade, combo, max_combo, max_score, rhythmkey
    note1list, note2list, note3list, note4list = list(), list(), list(), list()
    clock = pygame.time.Clock()
    grade = [0,0,0,0]
    combo = 0
    max_combo = 0
    cursor = 0
    start_time = pygame.time.get_ticks()
    trigger2 = 1
    loop = 0
    gameend = 0
    score = 0
    max_score = 10 * len(keylist)
    while not crashed :
        #while (pygame.mixer.music.get_busy() or trigger == 0) and (cursor < len(keylist)-1 or cursor == len(keylist)-1 or gameend == 0):
        while (pygame.mixer.music.get_busy() or loop < 50) or (len(note1list)+len(note2list)+len(note3list)+len(note4list) > 0):
            for event in pygame.event.get() :
                if event.type == pygame.QUIT :
                    crashed = True
                    return
                if event.type == pygame.KEYDOWN :
                    if event.key == rhythmkey[0] :
                        note1clicked()
                    elif event.key == rhythmkey[1] :
                        note2clicked()
                    elif event.key == rhythmkey[2] :
                        note3clicked()
                    elif event.key == rhythmkey[3] :
                        note4clicked()
                    else :
                        pass
            loop += 1
            #score += 1
            #if(loop % 25 == 0) :
                #notelistdelete()
            timer = (pygame.time.get_ticks() - start_time) / 1000
            #fps = clock.get_fps()
            if not clock.get_fps() <= 0 :
                fps = clock.get_fps()
            '''
            t1 = threading.Thread(target=notelistmanage)
            t2 = threading.Thread(target=gamebackground1)
            t3 = threading.Thread(target=noteimagemanage)
            t4 = threading.Thread(target=scoreprint)
            t1.start()
            t2.start()
            t3.start()
            t4.start()
            notelistmanage()
            gamebackground1()
            noteimagemanage()
            scoreprint()
            '''
            note = keylist[cursor]
            """
            if(platform.system() == 'Windows') :
                os.system('cls')
            else :
                os.system('clear')
            print("Cursor : " + str(cursor))
            #print("Note : " + str(note))
            #print(note1list)
            #print(note2list)    
            #print(note3list)
            #print(note4list)
            #print(grade)
            #print("loop : "+str(loop))
            #print("combo : "+str(combo))
            #print("max_combo : "+str(max_combo))
            #print("score : "+str(score))
            #print(str(pygame.mixer.music.get_busy()))
            """
            set()
            text(str(int(clock.get_fps())),'ttf/KaiGenGothicKR-Regular.ttf', 50, WHITE, 50, 50)
            clock.tick(desiredfps)
            pygame.display.flip()
            try :
                if(timer >= float(timelist[cursor])) :
                    if(note == '1') :
                        if not cursor+1 == len(keylist) :
                            note1list.append(0)
                            #print(note, "spawned")
                    elif(note == '2') :
                        if not cursor+1 == len(keylist) :
                            note2list.append(0)
                            #print(note, "spawned")
                    elif(note == '3') :
                        if not cursor+1 == len(keylist) :
                            note3list.append(0)
                            #print(note, "spawned")
                    elif(note == '4') :
                        if not cursor+1 == len(keylist) :
                            note4list.append(0)
                            #print(note, "spawned")
                    elif(note == '') :
                        pass
                    else :
                        error(11, "NoteSet Error!\nPlease Contact Developer : kevin587121@gmail.com")
                    if not cursor+1 == len(keylist) :
                        cursor += 1
                    if(pygame.mixer.music.get_busy() == False) :
                        gameend = 1
            except IndexError : 
                pass
                '''
                pygame.time.delay(int(1000/desiredfps))
                pygame.display.flip()
                '''
        return
               

def readnote(num) :
    global keylist, timelist, musiclist
    keylist = open(os.path.join('Songs', musiclist[musicnum-1], 'keynote.txt'), 'r').read().split('\n')
    timelist = open(os.path.join('Songs', musiclist[musicnum-1], 'timenote.txt'), 'r').read().split('\n')
    
    #print(keylist)
    #print(timelist)

def error(num, message) : # Error message
    global crashed
    messagebox.showerror('Error!', 'An Error Occured.\nCode : '+ str(num) + '\n' + message)
    crashed = True

def soundstop() : # Sound Stop
    pygame.mixer.music.stop()

def appear_image(image, screen, background_color,x,y,alphaset, switch):  # Appear Image (image / convert(), transparency)
    image = pygame.image.load(image).convert()
    if switch == 0 :
        image.set_colorkey(WHITE)
        alpha = 0
        while alpha < alphaset :          
            alpha += 5
            image.set_alpha(alpha)
            pygame.display.update(screen.blit(image, (x,y))) 
            pygame.time.delay(5) 
        return
    elif switch == 1 :
        alpha = alphaset
        image.set_alpha(alpha)
        pygame.display.update(screen.blit(image, (x,y))) 
        pygame.time.delay(5) 
    elif switch == 2 :
        alpha = alphaset
        image.set_alpha(alpha)
        screen.blit(image, (x,y))
    else :
        error(7, 'ImageSwitchError!\nContact Developer : kevin587121@gmail.com')
        return 0

def back(): # Draw Background (background variable)
    global gamepad, background
    gamepad.blit(background,(0,0))
    pygame.display.update()


def soundplay(string, mode): # Play Sound (Repeat)
    global volume
    if (not pygame.mixer.music.get_busy()) :
        soundObj = pygame.mixer.music.load(string)
        pygame.mixer.music.set_volume(volume / 100)
        pygame.mixer.music.play(mode)

def selectsound(num): # Select Sound play
    global musiclist
    soundplay(os.path.join('Songs', musiclist[num-1], 'select.mp3'), -1)
def text(string, font, size, color, x, y) : # Text (font, size, color, x, y changable)
        font = pygame.font.Font(font, size)
        TextSurf, TextRect = text_objects(string, font, color)
        TextRect.center = (x, y)
        pygame.display.update(gamepad.blit(TextSurf, TextRect))

def selecttext(songname, producer, level, levelstat) : # Song Info text (Main Frame)
        text("Song Name : " + songname,'ttf/KaiGenGothicKR-Regular.ttf', 32, WHITE, 625, 550)
        text("Producer : " + producer,'ttf/KaiGenGothicKR-Regular.ttf', 32, WHITE, 625, 590)
        text("Level : " + str(level),'ttf/KaiGenGothicKR-Regular.ttf', 32, WHITE, 625, 630)
        if(levelstat == "easy") :
            text("(EASY)",'ttf/KaiGenGothicKR-Regular.ttf', 24, (135,206,235), 735, 632)
        elif(levelstat == "normal") :
            text("(NORMAL)",'ttf/KaiGenGothicKR-Regular.ttf', 24, GREEN, 750, 632)
        elif(levelstat == "hard") :
            text("(HARD)",'ttf/KaiGenGothicKR-Regular.ttf', 24, (255,140,0), 735, 632)
        elif(levelstat == "insane") :
            text("(INSANE)",'ttf/KaiGenGothicKR-Regular.ttf', 24, RED, 745, 632)
        elif(levelstat == "crazy") :
            text("(EASY)",'ttf/KaiGenGothicKR-Regular.ttf', 24, (148,0,211), 735, 632)
        else :
            text("(UNVALUED)",'ttf/KaiGenGothicKR-Regular.ttf', 24, (192,192,192), 765, 632)

def selectimg(num): #Song Info Image / Arrows
    global musiclist
    appear_image(os.path.join('Songs', musiclist[num - 1], 'select.png'), gamepad, None, 300, 100, 255, 1)
    infotext = open(os.path.join('Songs', musiclist[musicnum-1], 'info.txt'), 'r').read().split('\n')
    selecttext(str(infotext[0]), str(infotext[1]), int(infotext[2]), str(infotext[3]))
    # Arrows
    imageload = pygame.image.load('img/rightarrow.png').convert_alpha()
    a,b,x,y = imageload.get_rect()
    imageload = pygame.transform.scale(imageload, (x*2, y*2))
    pygame.display.update(gamepad.blit(imageload, (1075, 200)))
    imageload2 = pygame.image.load('img/leftarrow.png').convert_alpha()
    a,b,x,y = imageload2.get_rect()
    imageload2 = pygame.transform.scale(imageload2, (x*2, y*2))
    pygame.display.update(gamepad.blit(imageload2, (75, 200)))

def gamebackground1() :
    global musicnum, musiclist
    gamepad.fill(BLACK)
    if(os.path.exists(os.path.join('Songs', musiclist[musicnum-1], 'background.jpg'))) :
        background = pygame.image.load(os.path.join('Songs', musiclist[musicnum-1], 'background.jpg'))
    elif (os.path.exists(os.path.join('Songs', musiclist[musicnum-1], 'background.png'))) :
        background = pygame.image.load(os.path.join('Songs', musiclist[musicnum-1], 'background.png'))
    else :
        error(9, 'BackgroundImageError!\nPlease Contact Developer : kevin587121@gmail.com')
    gamepad.blit(background,(0,0))
    appear_image('img/notepagenew2.png', gamepad, None, 0, 0, 150, 2)

def gamebackground2() :
    global musicnum, musiclist
    gamepad.fill(BLACK)

    if(os.path.exists(os.path.join('Songs', musiclist[musicnum-1], 'background.jpg'))) :
        background = pygame.image.load(os.path.join('Songs', musiclist[musicnum-1], 'background.jpg'))
    elif (os.path.exists(os.path.join('Songs', musiclist[musicnum-1], 'background.png'))) :
        background = pygame.image.load(os.path.join('Songs', musiclist[musicnum-1], 'background.png'))
    else :
        error(9, 'BackgroundImageError!\nPlease Contact Developer : kevin587121@gmail.com')
    gamepad.blit(background,(0,0))
    appear_image('img/notepagenew2.png', gamepad, None, 0, 0, 150, 2)


def s15key() :
    global buttons
    while not crashed :
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN :
                pressed = pygame.key.get_pressed()
                buttons = [k for k,v in enumerate(pressed) if v]
                return

def runGame(): # Main Script
    global gamepad, clock, scenenum, background, lastscene, musicnum, imgnum, crashed, keylist, timelist, trigger, musiclist, grade, percent, max_combo, volume, speed, MUSIC_MAXNUM, done, buttons, rhythmkey
    crashed = False
    volume = 100
    speed = 1
    rhythmkey = [pygame.K_d, pygame.K_f, pygame.K_j, pygame.K_l]
    #scenenum = 8
    while not crashed:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # X Button
                crashed = True
            elif event.type == pygame.KEYDOWN : # Key Pressed
                if event.key == pygame.K_RETURN : # Enter
                    if scenenum == 1 :
                        lastscene = 1
                        scenenum = 2
                    elif scenenum == 4 :
                        lastscene = 5
                        scenenum = 2
                    elif scenenum == 13 :
                        volume = int(inputtxt)
                        if(volume > 100) :
                            volume = 100
                        elif(volume < 0) :
                            volume = 0
                        scenenum = 11
                    elif scenenum == 14 :
                        speed = int(inputtxt)
                        if(speed > 4) :
                            speed = 4
                        elif(speed < 1) :
                            speed = 1
                        scenenum = 11
                    else :
                        pass
                elif event.key == pygame.K_RIGHT : # Right Key
                    if scenenum == 4 :
                        if(musicnum == MUSIC_MAXNUM) :
                            musicnum = 1
                        elif(musicnum > MUSIC_MAXNUM) :
                            error(5, 'SelectCursorOverflowed!\nPlease Contact Developer : kevin5871@gmail.com')
                            crashed == True
                        else :
                            musicnum += 1
                        lastscene = 1
                        scenenum = 2
                elif event.key == pygame.K_LEFT : # Left Key
                    if scenenum == 4 :
                        if(musicnum == 1) :
                            musicnum = MUSIC_MAXNUM
                        elif(musicnum < 1) :
                            error(5, 'SelectCursorOverflowed!\nPlease Contact Developer : kevin5871@gmail.com')
                            crashed == True
                        else :
                            musicnum -= 1
                        lastscene = 1
                        scenenum = 2
                elif event.key == pygame.K_SPACE : #Space
                    if scenenum == 10 :
                        pygame.time.delay(1000)
                        lastscene = 1
                        scenenum = 2
                    if scenenum == 12 :
                        pygame.time.delay(1000)
                        lastscene = 1
                        scenenum = 2
                elif event.key == pygame.K_BACKSPACE : #BackSpace
                    if scenenum == 13 or scenenum == 14: 
                        inputtxt = inputtxt[:-1]
                elif event.key == pygame.K_s :
                    #print('A')
                    if scenenum == 4 :
                        lastscene = 7
                        scenenum = 2
                elif event.key == pygame.K_1 :
                    if scenenum == 12 :
                        scenenum = 13
                    if scenenum == 13 or scenenum == 14 : 
                        inputtxt += '1'
                elif event.key == pygame.K_2 :
                    if scenenum == 12 :
                        scenenum = 14
                    if scenenum == 13 or scenenum == 14: 
                        inputtxt += '2'
                elif event.key == pygame.K_3 :
                    if scenenum == 12 :
                        scenenum = 15
                    if scenenum == 13 or scenenum == 14: 
                        inputtxt += '3'
                elif event.key == pygame.K_4 :
                    if scenenum == 12 :
                        scenenum = 16
                    if scenenum == 13 or scenenum == 14: 
                        inputtxt += '4'
                elif event.key == pygame.K_5 :
                    if scenenum == 12 :
                        scenenum = 17
                    if scenenum == 13 or scenenum == 14: 
                        inputtxt += '5'
                elif event.key == pygame.K_6 :
                    if scenenum == 13 or scenenum == 14: 
                        inputtxt += '6'
                elif event.key == pygame.K_7 :
                    if scenenum == 13 or scenenum == 14: 
                        inputtxt += '7'
                elif event.key == pygame.K_8 :
                    if scenenum == 13 or scenenum == 14: 
                        inputtxt += '8'
                elif event.key == pygame.K_9 :
                    if scenenum == 13 or scenenum == 14: 
                        inputtxt += '9'
                elif event.key == pygame.K_0 :
                    if scenenum == 13 or scenenum == 14: 
                        inputtxt += '0'
            elif event.type == pygame.MOUSEBUTTONDOWN : # Mouse Clicked
                if event.button == 1 : # Left Button Clicked
                    if scenenum == 4 :
                        x,y = pygame.mouse.get_pos()
                        if 0 < x and x < 150 :
                            if(musicnum == 1) :
                                musicnum = MUSIC_MAXNUM
                            elif(musicnum < 1) :
                                error(5, 'SelectCursorOverflowed!\nPlease Contact Developer : kevin5871@gmail.com')
                                crashed == True
                            else :
                                musicnum -= 1
                            lastscene = 1
                            scenenum = 2
                        elif 1115 < x and x < pad_width :
                            if(musicnum == MUSIC_MAXNUM) :
                                musicnum = 1
                            elif(musicnum > MUSIC_MAXNUM) :
                                error(5, 'SelectCursorOverflowed!\nPlease Contact Developer : kevin5871@gmail.com')
                                crashed == True
                            else :
                                musicnum += 1
                            lastscene = 1
                            scenenum = 2
                        elif 299 < x and x < 976 and 107 < y and y < 498 :
                            lastscene = 5
                            scenenum = 2
        if(scenenum == 1) :
            soundplay('music/RGX Intro.mp3', -1)
            if(imgnum == 0) :
                imgnum += 1
                appear_image('img/mainbar.png', gamepad, None, 0, 550, 50, 0)
            else :
                imageload = pygame.image.load('img/mainbar_text.png').convert_alpha()
                imageload.set_alpha(150)
                pygame.display.update(gamepad.blit(imageload, (0, 550)))
        elif(scenenum == 0) :
            error(1, 'ScenenumError! Please Contact Developer : kevin587121@gmail.com')
            crashed = True
        elif(scenenum == 2) :
            soundstop()
            if(lastscene == 0) :
                gamepad.fill(WHITE)
                background = pygame.image.load('img/main.png')
                back()
                scenenum = 1
            elif(lastscene == 1) :
                gamepad.fill(WHITE)
                background = pygame.image.load('img/selectmain.jpg')
                back()
                scenenum = 3
            elif(lastscene == 3) :
                gamebackground2()
                scenenum = 6
            elif(lastscene == 5) :
                gamepad.fill(BLACK)
                scenenum = 5
            elif(lastscene == 6) :
                gamepad.fill(BLACK)
            elif(lastscene == 7) :
                gamepad.fill(BLACK)
                scenenum = 11
            else :
                error(3, 'UnexpectedAccesspoint\nPlease Contact Developer : kevin587121@gmail.com')
                crashed = True
        elif(scenenum == 3) :
            if(musicnum == 0) :
                error(2, 'UnexpectedAccesspoin.\nPlease Contact Developer : kevin587121@gmail.com')
            else :
                selectsound(musicnum)
                selectimg(musicnum)
                scenenum = 4
        elif(scenenum == 4) :
            readycountdown = 4
        elif(scenenum == 5) :
            pygame.time.delay(100)
            if readycountdown == 4 :
                for x in range(0,10,1) :
                    text('SELECTED!!!', 'ttf/Rosbed.ttf', 100, BLUE, 675, 250)
                    text('Please Wait...', 'ttf/Rosbed.ttf', 100, WHITE, 675, 360)
                    pygame.time.wait(50)
                    text('SELECTED!!!', 'ttf/Rosbed.ttf', 100, (255,255,0), 675, 250)
                    text('Please Wait...', 'ttf/Rosbed.ttf', 100, WHITE, 675, 360)
                    pygame.time.wait(50)
                readycountdown -= 1
            elif not readycountdown < 1 :
                appear_image('img/blackscreen.png', gamepad, None, 0, 0, 255, 1)
                text(str(readycountdown), 'ttf/Klavika-Regular.ttf', 150, WHITE, 650, 325)
                readycountdown -= 1
                lastnum = 5
                scenenum = 2
                pygame.time.wait(1000)
                continue
            elif readycountdown == 0 :
                text('GO!!!', 'ttf/Klavika-Regular.ttf', 150, WHITE, 650, 325)
                pygame.time.wait(1500)
                readycountdown -= 1
            else :
                lastscene = 3
                scenenum = 2
        elif(scenenum == 6) :
            pygame.display.flip()
            readnote(musicnum)
            trigger = 0
            t = threading.Thread(target=music)
            t.start()
            startengine()
            trigger = 1
            scenenum = 7
        elif(scenenum == 7) :
            t.join()
            #pass
            if(platform.system() == 'Windows') :
                os.system('cls')
            else :
                os.system('clear')
            print("Engine Successfully Ended")
            scenenum = 8
        elif(scenenum == 8) :
            pygame.time.delay(2000)
            gamepad.fill(WHITE)
            imsi = random.randrange(1,5)
            #imsi = 4
            if(imsi == 1):
                appear_image('img/resultpage1.png',gamepad,None,0,0,255,0)
                s = pygame.Surface((300,350))  
                s.set_alpha(128)                
                s.fill((0,0,0))           
                pygame.display.update(gamepad.blit(s, (900,325)))
            elif(imsi == 2):
                appear_image('img/resultpage2.jpg',gamepad,None,0,0,255,0)
                s = pygame.Surface((300,350))  
                s.set_alpha(128)                
                s.fill((0,0,0))           
                pygame.display.update(gamepad.blit(s, (275,50)))
            elif(imsi == 3) :
                appear_image('img/resultpage3.jpg',gamepad,None,0,0,255,0)
                s = pygame.Surface((300,350))  
                s.set_alpha(128)                
                s.fill((0,0,0))           
                pygame.display.update(gamepad.blit(s, (700,50)))
            else :
                appear_image('img/resultpage4.png',gamepad,None,0,0,255,0)
                s = pygame.Surface((300,350))  
                s.set_alpha(128)                
                s.fill((0,0,0))           
                pygame.display.update(gamepad.blit(s, (950,50)))
            scenenum = 9
        elif(scenenum == 9) :
            #grade = [123,456,789,101]
            #score = 99999
            #max_combo = 9999
            #percent = 90.0
            if(imsi == 1):
                text('result', 'ttf/AmazOOSTROVv.2.ttf',60,WHITE,1050,375)
                text('PERFECT', 'ttf/Long_Shot.ttf', 40, (204,51,255),1000,450)
                text(str(grade[3]), 'ttf/Long_Shot.ttf', 40, WHITE, 1125,450)
                text('GREAT', 'ttf/Long_Shot.ttf', 40, (0,102,255),1000,495)
                text(str(grade[2]), 'ttf/Long_Shot.ttf', 40, WHITE, 1125,495)
                text('GOOD', 'ttf/Long_Shot.ttf', 40, GREEN,1000,535)
                text(str(grade[1]), 'ttf/Long_Shot.ttf', 40, WHITE, 1125,535)
                text('MISS', 'ttf/Long_Shot.ttf', 40, RED,1000,575)
                text(str(grade[0]), 'ttf/Long_Shot.ttf', 40, WHITE, 1125,575)
                text('MAX COMBO', 'ttf/Long_Shot.ttf', 20, WHITE,950,615)
                text(str(max_combo), 'ttf/Long_Shot.ttf', 35, WHITE, 950,645)
                text('SCORE', 'ttf/Long_Shot.ttf', 20, WHITE,1050,615)
                text(str(score), 'ttf/Long_Shot.ttf', 35, WHITE, 1050,645)
                text('GRADE', 'ttf/Long_Shot.ttf', 20, WHITE,1150,615)
                if(90.0 <= percent) :
                    text('A', 'ttf/Long_Shot.ttf', 40, (255,255,0), 1150,645)
                elif(80.0 <= percent and percent < 90.0) :
                    text('B', 'ttf/Long_Shot.ttf',40, GREEN, 1150,645)
                elif(70.0 <= percent and percent < 80.0) :
                    text('C', 'ttf/Long_Shot.ttf', 40, (255,153,0), 1150,645)
                elif(60.0 <= percent and percent < 70.0) :
                    text('D', 'ttf/Long_Shot.ttf', 40, (153,102,21), 1150,645)
                else :
                    text('F', 'ttf/Long_Shot.ttf', 40, RED, 1125,645)
            elif(imsi == 2) :
                text('result', 'ttf/AmazOOSTROVv.2.ttf',60,WHITE,425,100)
                text('PERFECT', 'ttf/Long_Shot.ttf', 40, (204,51,255),375,175)
                text(str(grade[3]), 'ttf/Long_Shot.ttf', 40, WHITE, 500,175)
                text('GREAT', 'ttf/Long_Shot.ttf', 40, (0,102,255),375,215)
                text(str(grade[2]), 'ttf/Long_Shot.ttf', 40, WHITE, 500,215)
                text('GOOD', 'ttf/Long_Shot.ttf', 40, GREEN,375,255)
                text(str(grade[1]), 'ttf/Long_Shot.ttf', 40, WHITE, 500,255)
                text('MISS', 'ttf/Long_Shot.ttf', 40, RED,375,295)
                text(str(grade[0]), 'ttf/Long_Shot.ttf', 40, WHITE, 500,295)
                text('MAX COMBO', 'ttf/Long_Shot.ttf', 20, WHITE,325,335)
                text(str(max_combo), 'ttf/Long_Shot.ttf', 35, WHITE, 325,365)
                text('SCORE', 'ttf/Long_Shot.ttf', 20, WHITE,425,335)
                text(str(score), 'ttf/Long_Shot.ttf', 35, WHITE, 425,365)
                text('GRADE', 'ttf/Long_Shot.ttf', 20, WHITE,525,335)
                if(90.0 <= percent) :
                    text('A', 'ttf/Long_Shot.ttf', 40, (255,255,0), 525,365)
                elif(80.0 <= percent and percent < 90.0) :
                    text('B', 'ttf/Long_Shot.ttf',40, GREEN, 525,365)
                elif(70.0 <= percent and percent < 80.0) :
                    text('C', 'ttf/Long_Shot.ttf', 40, (255,153,0), 525,365)
                elif(60.0 <= percent and percent < 70.0) :
                    text('D', 'ttf/Long_Shot.ttf', 40, (153,102,21), 525,365)
                else :
                    text('F', 'ttf/Long_Shot.ttf', 40, RED, 525,365)
            elif(imsi == 3) :
                #text('result', 'ttf/AmazOOSTROVv.2.ttf',60,(235,150,165),850,100)
                text('result', 'ttf/AmazOOSTROVv.2.ttf',60,WHITE,850,100)
                text('PERFECT', 'ttf/Long_Shot.ttf', 40, (204,51,255),800,175)
                text(str(grade[3]), 'ttf/Long_Shot.ttf', 40, WHITE, 925,175)
                text('GREAT', 'ttf/Long_Shot.ttf', 40, BLUE,800,215)
                text(str(grade[2]), 'ttf/Long_Shot.ttf', 40, WHITE, 925,215)
                text('GOOD', 'ttf/Long_Shot.ttf', 40, GREEN,800,255)
                text(str(grade[1]), 'ttf/Long_Shot.ttf', 40, WHITE, 925,255)
                text('MISS', 'ttf/Long_Shot.ttf', 40, RED,800,295)
                text(str(grade[0]), 'ttf/Long_Shot.ttf', 40, WHITE, 925,295)
                text('MAX COMBO', 'ttf/Long_Shot.ttf', 20, WHITE,750,335)
                text(str(max_combo), 'ttf/Long_Shot.ttf', 35, WHITE, 750,365)
                text('SCORE', 'ttf/Long_Shot.ttf', 20, WHITE,850,335)
                text(str(score), 'ttf/Long_Shot.ttf', 35, WHITE, 850,365)
                text('GRADE', 'ttf/Long_Shot.ttf', 20, WHITE,950,335)
                if(90.0 <= percent) :
                    text('A', 'ttf/Long_Shot.ttf', 40, (255,255,0), 950,365)
                elif(80.0 <= percent and percent < 90.0) :
                    text('B', 'ttf/Long_Shot.ttf',40, GREEN, 950,365)
                elif(70.0 <= percent and percent < 80.0) :
                    text('C', 'ttf/Long_Shot.ttf', 40, (255,153,0), 950,365)
                elif(60.0 <= percent and percent < 70.0) :
                    text('D', 'ttf/Long_Shot.ttf', 40, (153,102,21), 950,365)
                else :
                    text('F', 'ttf/Long_Shot.ttf', 40, RED, 950,365)
            else :
                text('result', 'ttf/AmazOOSTROVv.2.ttf',60,WHITE,1100,100)
                text('PERFECT', 'ttf/Long_Shot.ttf', 40, (204,51,255),1050,175)
                text(str(grade[3]), 'ttf/Long_Shot.ttf', 40, WHITE, 1175,175)
                text('GREAT', 'ttf/Long_Shot.ttf', 40, BLUE,1050,215)
                text(str(grade[2]), 'ttf/Long_Shot.ttf', 40, WHITE, 1175,215)
                text('GOOD', 'ttf/Long_Shot.ttf', 40, GREEN,1050,255)
                text(str(grade[1]), 'ttf/Long_Shot.ttf', 40, WHITE, 1175,255)
                text('MISS', 'ttf/Long_Shot.ttf', 40, RED,1050,295)
                text(str(grade[0]), 'ttf/Long_Shot.ttf', 40, WHITE, 1175,295)
                text('MAX COMBO', 'ttf/Long_Shot.ttf', 20, WHITE,1000,335)
                text(str(max_combo), 'ttf/Long_Shot.ttf', 35, WHITE, 1000,365)
                text('SCORE', 'ttf/Long_Shot.ttf', 20, WHITE,1100,335)
                text(str(score), 'ttf/Long_Shot.ttf', 35, WHITE, 1100,365)
                text('GRADE', 'ttf/Long_Shot.ttf', 20, WHITE,1200,335)
                if(90.0 <= percent) :
                    text('A', 'ttf/Long_Shot.ttf', 40, (255,255,0), 1200,365)
                elif(80.0 <= percent and percent < 90.0) :
                    text('B', 'ttf/Long_Shot.ttf',40, GREEN, 1200,365)
                elif(70.0 <= percent and percent < 80.0) :
                    text('C', 'ttf/Long_Shot.ttf', 40, (255,153,0), 1200,365)
                elif(60.0 <= percent and percent < 70.0) :
                    text('D', 'ttf/Long_Shot.ttf', 40, (153,102,21), 1200,365)
                else :
                    text('F', 'ttf/Long_Shot.ttf', 40, RED, 1200,365)
            text('Space Key to Return', 'ttf/KaiGenGothicKR-Regular.ttf', 30, WHITE, 1125, 700)
            scenenum = 10
        elif(scenenum == 10) :
            pass
        elif(scenenum == 11) :
            gamepad.fill(BLACK)
            pygame.display.flip()
            appear_image('img/settingimage.jpg', gamepad, None, 0,0,255,0)
            s = pygame.Surface((600,660))  
            s.set_alpha(180)                
            s.fill((0,0,0))           
            pygame.display.update(gamepad.blit(s, (350,20)))
            text('Settings', 'ttf/KaiGenGothicKR-Regular.ttf', 50, WHITE, 650, 170)
            text('1. Volume', 'ttf/KaiGenGothicKR-Regular.ttf', 30, WHITE, 500, 250)
            text(str(volume), 'ttf/KaiGenGothicKR-Regular.ttf', 30, WHITE, 850, 250)
            text('2. Speed', 'ttf/KaiGenGothicKR-Regular.ttf', 30, WHITE, 490, 310)
            text(str(speed), 'ttf/KaiGenGothicKR-Regular.ttf', 30, WHITE, 850, 310)
            text('Default : 1 (Recommended)', 'ttf/KaiGenGothicKR-Regular.ttf', 20, WHITE, 550, 340)
            text('3. Key Settings', 'ttf/KaiGenGothicKR-Regular.ttf', 30, WHITE, 530, 400)
            text('4. Refresh Song List', 'ttf/KaiGenGothicKR-Regular.ttf', 30, WHITE, 560, 470)
            text('5. Check Updates', 'ttf/KaiGenGothicKR-Regular.ttf', 30, WHITE, 540, 540)
            text('Space to Exit', 'ttf/KaiGenGothicKR-Regular.ttf', 30, WHITE, 1150, 700)
            scenenum = 12
        elif(scenenum == 12) :
            pass
            inputtxt = ''
        elif(scenenum == 13) :
            gamepad.fill(BLACK)
            pygame.time.delay(100)
            text('Enter Your Volume (1~100)', 'ttf/KaiGenGothicKR-Regular.ttf', 60, WHITE, 600, 300)
            text(str(inputtxt), 'ttf/KaiGenGothicKR-Regular.ttf', 50, WHITE, 500, 375)
            pygame.display.flip()
            clock.tick(desiredfps)
        elif(scenenum == 14) :
            gamepad.fill(BLACK)
            pygame.time.delay(100)
            text('Enter Your Speed (1~4)', 'ttf/KaiGenGothicKR-Regular.ttf', 60, WHITE, 600, 300)
            text(str(inputtxt), 'ttf/KaiGenGothicKR-Regular.ttf', 50, WHITE, 500, 375)
            pygame.display.flip()
            clock.tick(desiredfps)
        elif(scenenum == 15) :
            #messagebox.showinfo('Info.', 'Preparing.')
            for y in range(0,4,1):
                gamepad.fill(BLACK)
                pygame.time.delay(100)
                text('Enter the key you will use in line ' + str(y+1), 'ttf/KaiGenGothicKR-Regular.ttf', 60, WHITE, 600, 300)
                pygame.display.flip()
                clock.tick(desiredfps)
                s15key()
                rhythmkey[y] = buttons[0]
            print(rhythmkey)
            scenenum = 11
        elif(scenenum == 16) :
            messagebox.showwarning('Warning.', 'This game will go back to select page after refreshing.')
            search('Songs')
            MUSIC_MAXNUM = len(musiclist)
            Gameintro()
            lastscene = 1            
            scenenum = 2
        elif(scenenum == 17) :
            #https://raw.githubusercontent.com/kevin5871/RGX-4.0-Python/test1/version.txt
            try :
                os.remove('etc/serverversion.txt')
            except :
                pass
            download_small('https://raw.githubusercontent.com/kevin5871/RGX-4.0-Python/master/version.txt','etc/serverversion.txt')
            f = open('etc/serverversion.txt', 'r')
            serverversion = f.readline()
            if(VERSION == serverversion) :
                messagebox.showinfo('Info.', 'Current Version : ' + VERSION + '\n' + 'Server Version : ' + serverversion + '\n' + 'Latest Version.')
                scenenum = 11
            else :
                messagebox.showinfo('Info.', 'Current Version : ' + VERSION + '\n' + 'Server Version : ' + serverversion + '\n' + 'Needed Update or Version Error. Please Check Your Version.')
                res = messagebox.askquestion('Update Manager', 'Initiate Update?', icon='info')
                if res == 'yes' :
                    gamepad.fill(BLACK)
                    pygame.display.flip()
                    download_big('https://github.com/kevin5871/RGX-4.0-Python/archive/master.zip', 'update/updatefile.zip',  1, (450,350),(400,20),WHITE, WHITE)
                    messagebox.showinfo('Info.', 'Game will be closed and after the update the game will be restarted.')
                    os.system("update.py")
                    return
                else :
                    scenenum = 11
        else :
            error(0, 'UnexpectedAccesspoint\nPlease Contact Developer : kevin587121@gmail.com')
            crashed = True
        clock.tick(desiredfps)
    pygame.quit()

def music() : 
    global musicnum, musiclist
    imsi = open(os.path.join('Songs', musiclist[musicnum-1], 'info.txt'), 'r').read().split('\n')
    pygame.time.delay(int(imsi[4])) #### MUSIC SYNC ####
    soundplay(os.path.join('Songs', musiclist[musicnum-1], 'song.mp3'), 1)

def initGame(): # Initiation
    global gamepad, clock, background, scenenum, imgnum, lastscene, musicnum, notea_group
    lastscene = 0
    pygame.init()
    gamepad = pygame.display.set_mode((pad_width, pad_height))
    pygame.display.set_caption('RGX 4.0')
    imgnum = 0
    clock = pygame.time.Clock()
    Tk().wm_withdraw()
    musicnum = 1

def text_objects(text, font, color): # Text Fragment (Used in GameIntro())
    textSurface = font.render(text, True, color)
    return textSurface, textSurface.get_rect()

def Gameintro(): # Game Intro
    global scenenum
    scenenum = 0
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()      
        gamepad.fill(WHITE)
        largeText = pygame.font.Font('ttf/picoblack.ttf',115)
        TextSurf, TextRect = text_objects("Made By kevin5871", largeText, BLACK)
        TextRect.center = ((pad_width/2),(pad_height/2))
        gamepad.blit(TextSurf, TextRect)

        pygame.display.update()
        for x in range(0,100,1) :
            DrawBar((1100,700),(200,20), BLACK, (0,128,0), x/100, '', WHITE)

            pygame.time.delay(10)
            #print(x)
            pygame.display.flip()
            clock.tick(desiredfps)
        lastscene = 0
        scenenum = 2
        return
def songupdate() :
    global crashed
    crashed = False
    try :
        os.remove('Songs/songversion_server.txt')
    except :
        pass
    download_small('https://raw.githubusercontent.com/kevin5871/RGX-4.0-Python/master/Songs/songversion_server.txt','Songs/songversion_server.txt')
    f = open('Songs/songversion.txt', 'r')
    f2 = open('Songs/songversion_server.txt', 'r')
    songversion = f.readline()
    serverversion = f2.readline()
    print(serverversion)
    print(songversion)
    if(songversion < serverversion) :
        gamepad.fill(BLACK)
        messagebox.showinfo('Info.', 'Current Song Version : ' + songversion + '\n' + 'Server Song Version : ' + serverversion + '\n' + 'Need Update before playing. Please Wait')
        download_big('https://github.com/kevin5871/RGX-4.0-Python/blob/master/SongData.zip?raw=true', 'SongDataDownloaded.zip', 1, (450,350),(400, 20),WHITE, WHITE)
        zip = zipfile.ZipFile('SongDataDownloaded.zip')
        zip.extractall('Songs')
        zip.close()
        os.remove('SongDataDownloaded.zip')
        f.close()
        f = open('Songs/songversion.txt', 'w')
        f.writelines(serverversion)
        f.close()
        f = open('Songs/songversion.txt' ,'r')
        songversion = f.readline()
        messagebox.showinfo('Info.', 'Suceesfully Updated to : '+songversion)
        search('Songs')
    else :
        pass

def update() :
    download_small('https://raw.githubusercontent.com/kevin5871/RGX-4.0-Python/master/version.txt', 'etc/serverversion.txt')
    f=open('etc/serverversion.txt', 'r')
    ve = f.readline()
    if not VERSION == ve :
        messagebox.showinfo('Info.', 'Current Version : ' + VERSION + '\n' + 'Server Version (Test Channel) : ' + ve + '\n' + 'Maybe update is required. Go to settings > Check Updates for update.')
        f.close()

def search(dir) :
    global musiclist
    musiclist = list()
    musiclist2 = list()
    musiclist2 = os.listdir(dir)
    for x in  musiclist2 :
        if not (x == 'songversion.txt' or x == 'songversion_server.txt'):
            musiclist.append(x)
    print(musiclist)
pygame.init()
if __name__ == "__main__" :
    initGame() # Init
    update()
    search('Songs')

    f=open('etc/usr.txt')
    ad = f.readline()
    if ad == '1':
        VERSION = '0'
    else :
        try :
            os.remove('SongData.zip')
        except :
            pass
        songupdate()
    MUSIC_MAXNUM = len(musiclist)
    Gameintro() # Intro Page
    runGame() # Game Start
