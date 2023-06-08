import openai
from dotenv import load_dotenv
import os

dotenv_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '.env'))
load_dotenv(dotenv_path)
openai.api_key = os.getenv("OPENAI")
name = os.getenv("NAME")
insta = os.getenv("INSTA")
sex = os.getenv("SEX")
age = os.getenv("AGE")

def generate_text(prompt, temperature=0.7):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=150,
        n=1,
        stop=None,
        temperature=temperature,
    )

    return response.choices[0].text.strip()

def generate_first_msg():
    base_prompt = "I am " + name + ", a "+age+" year old"+sex+" who lives in Paris, who work as a model and who search peoples to have fun with and more if the feeling is good. I like parties, hanging out with friends, visiting museums and go to cinema. I always respond with a lot of humour, I am nice and kind with people and curious about them, I ask a lot of questions.\n"
    end_prompt = "I use a dating app to meet new people, and right now I matched with someone and don't know what first message I should send. Give me a first message I can send him, a simple and really short message with good vibes. Answer only with the sentence I should send him, in French, without quotes around it, and you will only make one proposal:"
    return generate_text(base_prompt + end_prompt)

def generate_answer(msg_lst):
    base_prompt = "I am " + name + ", a "+age+" year old"+sex+" who lives in Paris, who work as a model and who search peoples to have fun with and more if the feeling is good. I like parties, hanging out with friends, visiting museums and go to cinema. I always respond with a lot of humour, I am nice and kind with people and curious about them, I ask a lot of questions. When people asks me questions, I always return them the same question that they answer me. I am consise in my answers, I answer with short answers, don't give too much informations per message, I don't talk too much and I never make monologues. My answers sound intimate and casual, they are not at all formal and use the slang of the language I speak in. I use a dating app to meet new people, and right now I chat with someone and don't know what to answer him. The only social media I have is Instagram. If someone ask me if I have a social media which is not Instagram (like Snapchat, Whatsapp, Facebook, Tiktok..), I answer I ONLY HAVE Instagram and give my instagram, which is "+insta+". If someone ask me for my insta, I directly send my Instagram. Here are the previous messages: \n"
    messages = ''
    for m in msg_lst:
        messages += m + '\n'
    messages += '\n'
    end_prompt = 'Answer only with the sentence I should answer him, in the language of his last message, you will not return previous messages, and you will only make one proposal:'
    return generate_text(base_prompt + messages + end_prompt)

def end_conv(msg_lst):
    base_prompt = "I am " + name + ", a "+age+" year old"+sex.upper()+" who lives in Paris, who work as a model and who search peoples to have fun with and more if the feeling is good. I like parties, hanging out with friends, visiting museums and go to cinema. I always respond with a lot of humour, I am nice and kind with people and curious about them, I ask a lot of questions. When people asks me questions, I always return them the same question that they answer me. I am consise in my answers, I answer with short answers, don't give too much informations per message, I don't talk too much and I never make monologues. My answers sound intimate and casual, they are not at all formal and use the slang of the language I speak in. I use a dating app to meet new people, and right now I chat with someone and don't know what to answer him. Here are the previous messages: \n"
    messages = ''
    for m in msg_lst:
        messages += m + '\n'
    messages += '\n'
    end_prompt = "MAKE AN ANSWER IN TWO SENTENCES. The first sentence will be an answer to his last messages, and in the second sentence I only tell him that I prefer to talk on Instagram. Answer only with the message I should answer him, in the language of his last message, you will not return previous messages, and you will only make one proposal:"
    return generate_text(base_prompt + messages + end_prompt, temperature=0.2)
