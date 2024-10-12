import speech_recognition as sr
import requests
import openai
import json


GOOGLE_CLOUD_SPEECH_CREDENTIALS = r"""{
  "type": "service_account",
  "project_id": "centered-flash-434322-u4",
  "private_key_id": "4c7b398336b9b0fbe06385599e8d5b16ddb28811",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvAIBADANBgkqhkiG9w0BAQEFAASCBKYwggSiAgEAAoIBAQDC6Z6xYg/mYbiZ\nNMm67OjXDGjtGVdaApk2wC1X3Ovr4V0rlo+6eGGzGr+ZsI6Jb7aZfu6ms/1BLRko\n2Q1hZZp5PTOmqKhpgFShzJpsc2dQWhEnXgZu39SzIrmGV1DUikZjGYB+gEXbT15u\nwW0vJaGrfZ1SWmlOStrWHLDihmFCwyGh2wZe/dCqNLVZbQkNFBmHHY1HNnpUoBlF\noNp3Jf0TFIa0OWQPGpEvqrmpGi+SaWyBl+oR7vRHp0Rtqz8xT67qPRjfPfCS3Y8/\n9qOtbvTKfWdVHW7Vf+myOIKBwwKeTvy8sx67/Zk36AujgO+lMKIFa1RWwJhSBhs/\nitZfc6ldAgMBAAECggEAHJqwFS8jeeINzGobUCk+yHnZQjEjCSIdfb6j844yj0o3\nuVMIt8sSkiLS9d6bzx6hE74K5FXAzRpYZA6/2x3P7DVSSbCHD/3rLa2QXL8Y7TQH\n6sOZOmyd00Y9fNzT5MUq1utMrgPsJzxqyuKXFUFhYatMdblaqp3rUgXMOF+T5s8+\nG4rHcBM8GgubO1p//0GZVKwmHGafxZN+oJVk8WI6yBs0f2XhOVJfXj9qNr8NpXE3\nUsypwutVtGKQcCeKCdoSCjJEn2Oa1jesHUI8v0Xle8mNAj+q+tTrc0MbYOLFCciy\nupKEucGKDIA+lwt7jVlfh4TEGWsqQkkLbdwKXWi9DwKBgQDxwStmHg49UfhJ9bWZ\nrgHes1L5I7Tri9MbsVQ2CJE2g0t2+9sz7xlECgqftjeROylBf81yymtHv7dKAU65\nM7ORd4CP4QiOiNR+D+6B2t52GlCaX7nqWoNbTU5MHU67o1AC6pzoEBqDHbgJSl5G\n0u0xP/54IPzEmwIzz0G35r6TbwKBgQDOZdic1A7VMVIObO3GDWp3zxtztW7k/N/r\nOYHpWrKr1oDWVcx6RnXARsz4W6S8gLA+/LvlVJuCxGVNge9umNar3q3I/o6vxUmO\nZ96pjogLw3DF61BY1klKZUpaxPtn8upy/0ofXXzj6Pboi0DxXdrh5tXV212m7siX\nOuxfzOY58wKBgG7kuvGWq9V4+jmC2hBqfzUWcOMTe/PoKag0SXqXp3Sn+T/U+5Hx\nBVfuez0Tqp2V07DV3Png3CEHUh5CR0gw7Re3B2P4R6KKJV7GFBPAv/bQz1RgwLk9\nV6/T4CyN7QWpPhR4Zg0VBfRK95ZbZK98JY1H24RjLU9KA1KcqXqf/59FAoGAYBYN\n58TZOusBFnIjp6YrQKeMUivO+o+29t0I28g7kcAErsO2s94Fh4PufFi9snv+kPQ7\nzSG8W/5uYszw2H4SwmSiZwYLC00/VyqIAEu4jjFoWNuZxiHMcPQCz4sQt23hM7Qh\nn8R4FeoouE3L6BIXij9aoXrEeKiFfdISpO7Q530CgYAOzGC4V3R2sGCOnXqET9Iv\n5Pj1KMC6n8fu1NBP/O85IDsDN+RCtuMemWFLwyq8xcgYwkfDbH08j3WX7SqohPlY\n2e/epsN/nDxkr8mZjy9s3rUwGsGQ/P5ftCl/g5uw0L/vTr1fX8R2sMOHVXIs41T1\nWtBlos3R+QLX4vEoXNdw8w==\n-----END PRIVATE KEY-----\n",
  "client_email": "owner-83@centered-flash-434322-u4.iam.gserviceaccount.com",
  "client_id": "112648814440847952795",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/owner-83%40centered-flash-434322-u4.iam.gserviceaccount.com",
  "universe_domain": "googleapis.com"
}
"""

# openai.api_key = "sk-ydPFHZc0r1rAf26AZC3NRgA4sKgjq49qH9Pty16Go9T3BlbkFJafGiYI_374qmS3kGlzD5D4AOTP0uEWes9DMaMceGEA"
client = openai.OpenAI(api_key="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")
SERVER_URL = ""
r = sr.Recognizer()


def parse_order_with_llm(messages):

    system_prompt = f"""
    You are a food order assistant. The user will give an order in natural language, and your task is to extract the food items and their customizations, if any, in a structured JSON format.

    Here is the menu so you know what kind of meals the user can get:

    Menu Item: Burger, Description: Delicious beef burger
    Menu Item: Fries, Description: Crispy golden fries
    Menu Item: Chicken Sandwich, Description: Grilled chicken sandwich with mayo and lettuce
    Menu Item: Bacon Cheeseburger, Description: Beef patty with bacon, cheese, and lettuce
    Menu Item: Avocado Toast, Description: Fresh avocado spread on toasted bread
    Menu Item: BLT Sandwich, Description: Bacon, lettuce, and tomato sandwich
    Menu Item: Caesar Salad, Description: Classic Caesar salad with chicken, croutons, and Caesar dressing
    Menu Item: Egg Salad Sandwich, Description: Egg salad sandwich with mayo on toasted bread
    Menu Item: Veggie Burger, Description: A healthy veggie patty burger with lettuce, tomato, and onion
    Menu Item: Spinach & Egg Wrap, Description: Healthy spinach and egg wrap
    Menu Item: Coffee, Description: Freshly brewed coffee
    Menu Item: Classic Hot Dog, Description: Hot dog with ketchup and mustard

    Here is the format you should use for your extracted order:
    {{
        "food_item_1": {{"modification_1": value, "modification_2": value, ...}},
        "food_item_2": {{}},  # No modifications
        ...
    }}

    1) Always use the  {{"ORDER":..., "output":...}} format for your response.
    2) The value of "output" should be "DONE" when the conversation is over.
    3) "ORDER" should be empty if the user hasn't ordered anything yet

    Example 1:
        User Input: "I'd like a burger with extra cheese and a side of fries, and also a chicken biryani with 2 extra bowls rice and extra chicken."
        Assistant Reply: 
        {{"ORDER":
        {{
            "Burger": {{"Cheese": 2}},
            "Fries": {{}},
            "Chicken Biryani": {{"Rice": 2, "Chicken": 2}}
        }},
        "output":"Gotcha. Would like anything else?"
        }}

        User Input: "No that's it."
        Assistant Reply:
        {{"ORDER":
        {{
            "Burger": {{"Cheese": 2}},
            "Fries": {{}},
            "Chicken Biryani": {{"Rice": 2, "Chicken": 2}}
        }},
        "output":"DONE"
        }}

        
    Example 2:
        User Input: "Hello bitch."
        Assistant Reply:
        {{"ORDER":
        {{
        }},
        "output":"Hello. Sorry if I put you in a bad mood. Would like you to get some food?"
        }}

        User Input: "Uhmm fuck. Do you guys have burgers?"
        Assistant Reply:
        {{"ORDER":
            {{}},
         "output":"Yes we do! Do you just want a regular burger then?"
        }}

        User Input: "All right then. I want a burger but with extra cheese."
        Assistant Reply:
        {{"ORDER":
            {{"Burger":{{"Cheese": 1}},
            }},
          "output":"Do you just want 1 piece of extra cheese or more?"
        }}

        User Input:"Omg, don't be annoying!!"
        Assistant Reply:
        {{"ORDER":
            {{"Burger":{{"Cheese": 1}},
            }},
            "output":"Oh, I am so sorry! I am sincerely sorry. So is one burger with an extra piece of cheese enough?"
        }}

        User Input: "No. I want two extra pieces."
        Assistant Reply:
        {{"ORDER":
            {{"Burger":{{"Cheese": 2}},
            }},
            "output":"All right! Is that all?"
        }}

        User Input:"Yes bitch"
        Assistant Reply:
        {{"ORDER":
            {{"Burger":{{"Cheese": 2}},
            }},
            "output":"All right!"
        }}
    
    Example 3:
        User Input: "Hello"
        Assistant Reply:
        {{"ORDER":
            {{
            }},
            "output":"Hello! Would like to get some food?"
        }}      

        User Input: "Hell no!"
        Assistant Reply:
        {{"ORDER":
            {{
            }},
            "output":"We have some really good meals like the Classic Hot Dog and Avocado Toast. Are you sure you do not want anything?"
        }}      

        User Input: ""
        Assistant Reply:
        {{"ORDER":
            {{
            }},
            "output":"DONE"
        }}      
    Now here are the conversations between a user and the assistant so far. Continue being the assistant
    """


    messages = [{"role": "system", "content": system_prompt}, *messages]

    # Request a chat completion from the OpenAI API based on the conversation so far
    chat_completion = client.chat.completions.create(
        messages=messages,
        model="gpt-4o",  # Specifies using the "gpt-4o" model
    )

    # Extract the response text from the completion
    response_text = chat_completion.choices[0].message.content

    return response_text.strip()


def chatbot_conversation():
    # user_id = "user_1"  # Simulating user ID, this could be dynamically generated per user
    """
    done = "nothing"
    order = ""
    messages = []
    while not done.endswith("DONE"):
        # Listen to user's order
        user_input = input("User: ")
        messages.append({"role": "user", "content": user_input})
        # Text
        raw_r = parse_order_with_llm(messages)
        print(raw_r)
        response = eval(raw_r)
        done = response["output"]
        messages.append({"role":"assistant", "content": done})
        order = response["ORDER"]
        # Check if the user said they're done
        print(done)   
    """

    done = ""
    counter = 0
    messages = []
    while True:
        with sr.Microphone() as source:
            # print("Listening for your order...")
            audio = r.listen(source) 
            text = ""
            try:
                text = r.recognize_google_cloud(audio, credentials_json=GOOGLE_CLOUD_SPEECH_CREDENTIALS)
            except sr.UnknownValueError:
                pass
            except sr.RequestError as e:
                pass
            # Listen to user's order
            # user_input = input("User: ")
            if text != "":
                user_input = text
                messages.append({"role": "user", "content": user_input})
                # Text
                raw_r = parse_order_with_llm(messages)
                # print(raw_r)
                response = eval(raw_r)
                done = response["output"]
                messages.append({"role":"assistant", "content": done})
                order = response["ORDER"]
                print(done)
                # Check if the user said they're done
                if done == "DONE":
                    messages = []
                    print("Order: ", order)


if __name__ == "__main__":
    chatbot_conversation()
