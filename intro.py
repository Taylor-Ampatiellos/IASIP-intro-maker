from moviepy.editor import *
import os, collections, sys, string

# black screen with theme song playing
intro = VideoFileClip("blank_intro.avi") 

# user-provided clip to play before the title card
clip = VideoFileClip(sys.argv[1])

# prompts the user to input their desired "episode" title
title = input("Input Title: ")

# creates clip of input text
txt_clip = ( TextClip(title, fontsize=30, color='white', font='Textile')
             .set_position('center')
             .set_duration(8) )

# adds the input title to the blank audio clip
punchline = CompositeVideoClip([intro, txt_clip]) 

# combines the initial video and "punchline"
complete = concatenate_videoclips([clip, punchline])

# writes the complete video
complete.write_videofile("my_intro.mp4", fps=60) 