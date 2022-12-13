import os, requests, random,  lxml, re, json, urllib.request
from helper_functions import has_selected_yes, slugify, make_dir_if_not_exists
from image_scraper import get_images
from chat_gpt_interface import get_video_script, save_script
from tts_converter import save_audio
from moviepy.editor import *


# For the config please go here:
# https://github.com/acheong08/ChatGPT/wiki/Setup
session_token = "ADD YOUR TOKEN HERE"

user_is_providing_topic = input("Would you like to provide a topic for the video? (y/n) ")

if has_selected_yes(user_is_providing_topic):
    video_topic = input("What topic would you like to write about? ")
else: 
    topics = ["DIY craft ideas",    "Hacks and tips for everyday life",    "Comedy sketches and skits",    "Dance challenges and routines",    "Life hacks for students",    "Beauty and makeup tips",    "Travel vlogs and destination guides",    "Relationship advice and tips",    "Cooking and recipe videos",    "DIY fashion and style tips",    "Comedy challenges and games",    "Fitness and workout routines",    "Life hacks for parents",    "Pranks and practical jokes",    "DIY home decor ideas",    "Life hacks for the workplace",    "Animal videos and pet tricks",    "Comedy monologues and stand-up",    "DIY beauty and skincare products",    "Travel hacks and packing tips",    "Relationship advice for couples",    "Food challenges and taste tests",    "DIY project ideas for kids",    "Comedy duets and lip sync battles",    "Fitness challenges and workouts",    "Life hacks for saving money",    "Animal videos and pet care tips",    "Comedy parodies and satire",    "DIY home organization ideas",    "Life hacks for saving time",    "Travel vlogs and adventure stories",    "Relationship advice for singles",    "Cooking challenges and food experiments",    "DIY gift ideas and tutorials",    "Comedy interviews and Q&A sessions",    "Fitness tips and healthy eating advice",    "Life hacks for everyday problems",    "Animal videos and pet adoptions"]
    video_topic = random.choice(topics)

user_is_providing_tone = input("Would you like to provide a tone for the video? (y/n) ")

if has_selected_yes(user_is_providing_tone):
    video_tone = input("What tone would you like to write about? ")
else:
    video_tones = ["funny", "informative", "romantic", "motivational", "inspirational", "educational", "scary", "sad", "happy", "angry"]
    video_tone = random.choice(video_tones)

user_is_specifying_length = input("Would you like to specify the length of the video? (y/n) ")

if has_selected_yes(user_is_specifying_length):
    video_length = input("How long should the video be? (in seconds) ")
else:
    video_length = str(random.randint(60, 90))

print('Topic: ' + video_topic)
print('Tone: ' + video_tone)
print('Length: ' + video_length + ' seconds')


video_script = get_video_script(session_token, video_topic, video_tone, video_length) # Get the video script from the AI.


topic_slug = slugify(video_topic)

# The path where the content will be saved
main_path = os.getcwd() + "/content" # Gets the "content" folder in the current working directory of the script
current_working_dir = main_path + "/" + topic_slug # The path to the folder for the current topic.

# Create the directory if it doesn't exist
make_dir_if_not_exists(current_working_dir)


### Save the content to the current working directory ###
get_images(topic_slug, current_working_dir, 10) # Download the images and save them to the cwd.
save_script(video_script['message'], current_working_dir, topic_slug + ".txt") # Save the video script to the cwd.
save_audio(video_script['message'], current_working_dir, topic_slug) # Save the audio to the cwd.

### Create the video

# Get all the image file names in the "images" folder and store them in an array
image_file_names = []

for file in os.listdir(current_working_dir + '/images'):
    if file.endswith(".jpg"):
        image_file_names.append(file)
    else:
        continue

## Loop through the image file names and create an ImageClip for each one.
clips = [ImageClip(current_working_dir + '/images/' + m).set_duration(10).set_fps(24) # https://stackoverflow.com/questions/44732602/convert-image-sequence-to-video-using-moviepy
            for m in image_file_names]

## Concatenate the ImageClips into a single VideClip            
concat_clip = concatenate_videoclips(clips, method="compose") # Returns a VideoClip instance that concatenates the clips in the list clips. https://zulko.github.io/moviepy/ref/VideoClip/concatenate_videoclips.html

## Create an AudioFileClip from the TTS audio and set it up as the audio for the video.
audio_clip = AudioFileClip(current_working_dir + '/audio/'  + topic_slug + '.mp3') # https://zulko.github.io/moviepy/ref/AudioClip/AudioFileClip.html
new_audio_clip = CompositeAudioClip([audio_clip]) # https://zulko.github.io/moviepy/ref/AudioClip/CompositeAudioClip.html
concat_clip.audio = audio_clip # This is the sound for the VideoClip

concat_clip.resize( (1080,1920) ) 

# Write the video to a file
concat_clip.write_videofile(current_working_dir + '/video/' + topic_slug + '.mp4')



