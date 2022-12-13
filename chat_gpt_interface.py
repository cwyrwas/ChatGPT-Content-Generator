from revChatGPT.revChatGPT import Chatbot
import os

def get_video_script(token, video_topic, tone = "funny", length = "60"):
    # For the config please go here:
    # https://github.com/acheong08/ChatGPT/wiki/Setup
    config = { "session_token": token }
    prompt = "Write me a " + length + " second TikTok video script about " + video_topic + " with a " + tone + " "
    
    if tone == "funny":
        prompt += "Please include a specific punchline and a joke."
    elif tone == "informative":
        prompt += " Please include a specific fact and a tip."
    elif tone == "romantic":
        prompt += "Please include a specific compliment and a love quote."
    elif tone == "motivational":
        prompt += "Please include a motivational quote from a well-liked personality and a wellness tip."
    elif tone == "inspirational":
        prompt += "Please include an inspiring quote from a celebrity and a tip about how to achieve your dreams."
    elif tone == "educational":
        prompt += "Please include a specific fact and a tip about how to learn more about " + video_topic + "."
    elif tone == "scary":
        prompt += "Please include a specific scary fact and a scary quote from someone who is not well-liked in the eyes of the public."
    elif tone == "sad":
        prompt += "Please include a sad fact about " + video_topic + " and a sad quote from a well-liked celebrity or personality."
    elif tone == "happy":
        prompt += "Please include a happy fact about " + video_topic + " and a happy quote from a well-liked personality."
    elif tone == "angry":
        prompt += " with an angry tone. Please include a fact that most people would generally consider to be frustrating about " + video_topic + "."
    
    prompt += " Please include a transition phrase at the end of each sentence. Also, please include a call to action at the end of the script, such as 'subscribe to @AI_TikTok_Bot' or 'follow @AI_TikTok_Bot for more videos like this. Also, create a clever title for the video, and introduce the title at the beginning of the script. Please make the title something catchy and attention-grabbing, such as 'The Most Dangerous Animal in the World' or 'The Most Dangerous Animal in the World is...'. Don't label things like 'Title: ', 'Opening: ', 'Ending: ', etc. Simply write the title, opening, and ending as if they were part of a cohesive script."


    chatbot = Chatbot(config, conversation_id=None)

    response = chatbot.get_chat_response(prompt, output="text")
    print(response) 

    return response


def save_script(script, current_working_dir, file_name):
    file_path = os.path.join(current_working_dir + '/script', file_name)

    # create a text file and write the script to it
    with open(file_path, "w") as f:
        f.write(script)
        print("Saved script to " + file_path)
    