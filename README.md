# chatgpt content generator
 Uses Python to automatically generate TikTok videos/short-form content using ChatGPT.

 ## Installation / Requirements
 Make sure you have Python 3+ and Chrome installed, then simply clone this repository.

 ## Getting Started
 To get started, you need to log in to ChatGPT and get your `__Secure-next-auth.session-token` cookie value. You can do this by logging in to ChatGPT and then going to the [Chrome DevTools](https://developers.google.com/web/tools/chrome-devtools) and going to the Application tab. Then, go to the Cookies section and copy the value of the `__Secure-next-auth.session-token` cookie.

 Once you have the cookie value, edit `content_gen.py` and replace the value of the `session_token` variable with your cookie value.

 ## Usage / Parameters

 ### Video Topics
 This script utilizes an array of different video topics. To add more topics, simply add them to the `topics` array in `content_gen.py`. I generated the topics using ChatGPT, so feel free to ask it for more of them or use your own.

 ### Video Tones
 The `video_tones` array functions similarly to the `topics` array, but it contains different video tones. Depending on the tone, the script will generate text with a different style. For example, if the tone is `funny`, the script will generate text that is more comedic in nature. This simply modifies the prompt that is sent to ChatGPT. To use your own, or add more, simply edit the `video_tones` array in `content_gen.py` and then modify the conditional in `chat_gpt_interface.py` to include your new tone(s).
 Play around with the prompts to see what works best. I've found that the `sad` tone tends to generate the most interesting results. I'm sure the prompts could be improved, so please open a PR or issue if you have any suggestions.

 ### Video Length
The `video_length` variable in `content_gen.py` (sort of) determines how long the video will be. All this does is modify the prompt to ask for a X second long video script, so it's not super reliable but the larger the number, the more text you will receive.

# How does this work?
It uses [@aechong08's ChatGPT API](https://github.com/acheong08/ChatGPT) to communicate with the OpenAI servers. Once a prompt has been generated, the resulting text is stored inside of the `content` directory. It will slugify the video topic and create the corresponding directories if it does not exist already. For each video, a subdirectory is created containing directories for 4 separate components of the video. 
The directory structure looks like this:
```
content/diy-craft-ideas/
    /images/
    /script/
    /audio/
    /video
```
Once the script has been saved, it gets stored into a text file in the subdirectory. Additionally, 10 images are then scraped from Unsplash using `image_scraper.py`. Finally, we use `pyttsx3` to generate an audio file from the script. The audio file is then saved in the `audio` directory. To build the video, `content_gen.py` uses `moviepy` to parse the video's /images/ directory. It creates an ImageCollection to function as a slideshow. Lastly, the audio file is added to the video and the video is saved in the `video` directory.

## How can I run this script?
You can run this script by simply running `python content_gen.py` in the root directory of the project. This will generate your video and save it to the `content` directory. You can then use the video however you want.

## Notes:
This is highly experimental, and there is a solid chance that this will break at some point given that ChatGPT is actively changing on a day-to-day basis. I'm not responsible for anything in regards to your OpenAI account resulting from using this script. Use at your own risk.
