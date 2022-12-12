import os, requests, random,  lxml, re, json, urllib.request
from helper_functions import slugify, make_dir_if_not_exists
from image_scraper import get_images
from chat_gpt_interface import get_video_script, save_script
from tts_converter import save_audio
from moviepy.editor import *


# For the config please go here:
# https://github.com/acheong08/ChatGPT/wiki/Setup
session_token = "eyJhbGciOiJkaXIiLCJlbmMiOiJBMjU2R0NNIn0..4Obp_ZHwiXExkYgV.gcflVHPdxnmFaJUrO72vmEJlCTttdwhTUMdlP1DsPWYN7ki9CVU7_nNj-yGsfr7yfG3G0PbvmHnNVd7Bk6CUl65OzxKfUcGilYQBhTf0FInzRPbmvoCZUFGUxfpv6n1RbIFmj2vsOAsIV3NmO36ejaqAl4FgGZXA0y_oJ_0-WnBMRgOel6x3qVQXNhejkmNnQxyliXFmJfCUqLZK9uHJR7msWsTQxFcUmCNShQc75D1BQ6PrhsPhOvkpuLuve7WSp8SrIoZ-ePW2sfgXtooA1Xx5MsQDyiqIbRy_AdMK3RIn6dz37CKR78KLRqrEVeIbTDj-U32Ss4CxFrDBfb_IuUVlC1OJL-BtQ9Ax5J_wk2MzshV2BV-Pl-mN_pOcE-VYMwsvndan1mtMgu77pvzYXhMbJmL4IFKmulqWlKre9lF69emEUGTTHGTnQSMugRutgZF4R955kHuTBoFzCWUuvkK3EHZz-pRiYINf7E6Vz3sQa3_vHAYQUY5xvgaHw2gP3YMonumMEshjHNjSq1yRgfKq2LLViCT4A_1yFWL8HLpdkJfz81VRYYtVwpVaU00nT9hn1TLfbuuDZXd7tDCRO0YoDwQEXUwywkgl3_2cM5mLVA5N6bJBSr8l3XxCJsVAMCFBuotegqMvrT1B_vD2MU3q6xRcw1rRPIU-XV4gcNJEqyvGWZZ_uRarKVwMsmAUWYjUxsHhyWItCdDdnT-RKZuFsqVfSc9VktOEdwRcxnHVRC4FSC0yRygWaVE-Tbx3AV9XsdtJNGZ3_5jHZt_wtXMLBsZQOn3_dBG_J8973EId9RgSMJrEYJG3nIPImzAdEXxPdetlZM71Es3amuNKMFSZKQwZEpCjpCWj1uxjpniNPjoh8Gw1Xi5A-N_xAxb1faU7UFaSvHKjS2NOx3nnxPKTEvKqcgzSH2_cHBxwaIkAAAn250Lrh_c4cX29a1J1QKbXRuo5ewfXoAX4EFFebX2V8F5AR1MVnpLQv6CTiqTqWfyavyi912kCQioJOwqquSIWdp-8ByvtRVeTCBHOV4BoyHDRGRcSmpVFRJKbAEVxynSAlVRskwfahmPkvaIrqStqpDr4vLzYjW8ReL1KWO9d97iCzmU0FXLpMfO59dXSac6ad4cDmsrfikY2i5iVMYoi_toySOSMJZn80ku29rzRhHer2HytP8P8-PL23uLkgX6fas6DvnXpynh6mI6HB4nMwkJAyN9U32SoLEMBlLwxAKzzmW0m7IC-fARsKUndgCfNrdxe_mAA0htfCt40b1SqO22gm_-tpEjvDUc-USMmTxMD3aa1oSzspsOfVdtcqhDFHXQR1dW6mPfe9gFXjvH7wvZRLnMAePMb2uEA604KCCuYU1xKjUv2a_FyIXqKeypJB69mFDIP2DVTnFYb8K2FwPnlFTN0jMMomDBRjC1-udxAcWTjWPtRhbgdxMmWXutvPb3hjy4nhob2pZqGYFqrQNw9Eq1BvXHdH0BugbVnqF1TTOZXOqJ4fjyhYK02UKiH2kuV6sxajM58s56S-mJJ2G3JlYHkvdxac9_geJQuuSIVqJMMaBPvZKVYq5tS2fIWKAjdf8ggA8pLVR56htto2HhZfgr4c1_UhIZEF3HhmoKdbZduObnZO42h0SUSY5tl68qKFkvKLHQxG7QhJJEfSNqC-F6AisMq4xL7vwguXTQ1lQoZn0n-LU8DKifhN_uMTxCNOBAmfIUV8SgCg_e8SE727-GPLLZCPVD9V7Y8zKdhbgJDygjkZNqoyUrVWbQ_Tapxpj7HwSGIJsJGNfJHTRaUWC54ya7Sxl2d3FDljT84M10JlVZ38KvP57c4RvVNyX9KMRG-wjSKEERkIaGyjRXLLl5keyaVHm9GG_yLFIgMf4O51tk4KWj46ZiSZt00YHYWDQNaYCcNPgTdTDxJStuJ981iHFEqEJjOis68QPwcsOVKEzoHCaVOx0YacQxAmS_ayNBf0VdlB9zJlNg5Ws7PYDaBcxJ_HVW_XDHAE98n-gKruZNZXvu6xtE-jDHl5A7raEebMTrAaTUZ1gPHuoNF6dkKJhUPTDJAzCY7NmKef1QDYu4321mcUvHuF-m1DgzruMiovfpbji5Ji6DI26bOoo7Pgsi4WphX9UqL3qiGulaGIxP96sG9HOFSA7LeblE_OsmZCqFSLE71dvk6Q0P4P0U8DA8TwzYPSXKqkhzJxg0liePDZxc8BLUK2scGi3JDKUj9l8Tkk24G3-6YN-IQ9hmIcgfsLb8smz84yee4ZdrXXdrSHE_Hwnexex3qOkUuAIp5X1ML3GYa05o0qjG_agMzNYGS89zTHItPJSRBHyygRaZVu8Bv-w.lCUlsopUa6w460FLKUvaDw"

topics = ["DIY craft ideas",    "Hacks and tips for everyday life",    "Comedy sketches and skits",    "Dance challenges and routines",    "Life hacks for students",    "Beauty and makeup tips",    "Travel vlogs and destination guides",    "Relationship advice and tips",    "Cooking and recipe videos",    "DIY fashion and style tips",    "Comedy challenges and games",    "Fitness and workout routines",    "Life hacks for parents",    "Pranks and practical jokes",    "DIY home decor ideas",    "Life hacks for the workplace",    "Animal videos and pet tricks",    "Comedy monologues and stand-up",    "DIY beauty and skincare products",    "Travel hacks and packing tips",    "Relationship advice for couples",    "Food challenges and taste tests",    "DIY project ideas for kids",    "Comedy duets and lip sync battles",    "Fitness challenges and workouts",    "Life hacks for saving money",    "Animal videos and pet care tips",    "Comedy parodies and satire",    "DIY home organization ideas",    "Life hacks for saving time",    "Travel vlogs and adventure stories",    "Relationship advice for singles",    "Cooking challenges and food experiments",    "DIY gift ideas and tutorials",    "Comedy interviews and Q&A sessions",    "Fitness tips and healthy eating advice",    "Life hacks for everyday problems",    "Animal videos and pet adoptions"]
video_tones = ["funny", "informative", "romantic", "motivational", "inspirational", "educational", "scary", "sad", "happy", "angry"]


video_topic = random.choice(topics)
video_tone = random.choice(video_tones)
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



