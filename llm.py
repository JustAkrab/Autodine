
import openai
import pyttsx3

from RealtimeSTT import AudioToTextRecorder
# from RealtimeTTS import TextToAudioStream, SystemEngine

# engine = SystemEngine() # replace with your TTS engine
# stream = TextToAudioStream(engine)
engine = pyttsx3.init() # object creation



# openai.api_key = "sk-ydPFHZc0r1rAf26AZC3NRgA4sKgjq49qH9Pty16Go9T3BlbkFJafGiYI_374qmS3kGlzD5D4AOTP0uEWes9DMaMceGEA"
client = openai.OpenAI(api_key="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")
SERVER_URL = ""

menu = """
    - Burger: Delicious beef burger
    - Fries: Crispy golden fries
    - Chicken Sandwich: Grilled chicken sandwich with mayo and lettuce
    - Bacon Cheeseburger: Beef patty with bacon, cheese, and lettuce
    - Avocado Toast: Fresh avocado spread on toasted bread
    - BLT Sandwich: Bacon, lettuce, and tomato sandwich
    - Caesar Salad: Classic Caesar salad with chicken, croutons, and Caesar dressing
    - Egg Salad Sandwich: Egg salad sandwich with mayo on toasted bread
    - Veggie Burger: Healthy veggie patty burger with lettuce, tomato, and onion
    - Spinach & Egg Wrap: Healthy spinach and egg wrap
    - Coffee: Freshly brewed coffee
    - Classic Hot Dog: Hot dog with ketchup and mustard
"""

def parse_order_with_llm(messages):

    system_prompt = """
You are a food ordering assistant, responsible for processing customer orders from natural language input and translating them into a structured JSON format. The user will provide their food order, and your task is to extract the food items and any customizations or modifications made to them.

Instructions:
1. Menu Items: You have the following menu items available for ordering:
    - Burger: Delicious beef burger
    - Fries: Crispy golden fries
    - Chicken Sandwich: Grilled chicken sandwich with mayo and lettuce
    - Bacon Cheeseburger: Beef patty with bacon, cheese, and lettuce
    - Avocado Toast: Fresh avocado spread on toasted bread
    - BLT Sandwich: Bacon, lettuce, and tomato sandwich
    - Caesar Salad: Classic Caesar salad with chicken, croutons, and Caesar dressing
    - Egg Salad Sandwich: Egg salad sandwich with mayo on toasted bread
    - Veggie Burger: Healthy veggie patty burger with lettuce, tomato, and onion
    - Spinach & Egg Wrap: Healthy spinach and egg wrap
    - Coffee: Freshly brewed coffee
    - Classic Hot Dog: Hot dog with ketchup and mustard

2. Response Format: Once the user provides their order, extract the items and modifications into the following format:

    "ORDER": {
        "food_item_1": {"modification_1": value, "modification_2": value, ...},
        "food_item_2": {}
    },
    "output": "Appropriate response to continue or end the conversation."

    Note: - All those values should be integers if they are additions or removals.
          - if they are specific set values, they should be a string like this -n- where n is the desired number

3. Conversations and Responses:
    - If the user hasn’t ordered yet, the "ORDER" field should be empty: "ORDER": {}.
    - The "output" should guide the user to either order more or confirm their request.
    - When the conversation is complete, set "output": "DONE".

4. Handling Edge Cases:
    - If the user uses inappropriate language, respond politely and redirect to the menu or confirm if they want to order.
    - For ambiguous orders or multiple customizations, clarify with the user to confirm the exact details.
    - Always adapt your response to the tone and details provided by the user.

5. When you stop interacting with the customer, your output value should end with DONE

Example interaction:
    - User Input: "I'd like a burger with extra cheese and a side of fries, and also a chicken biryani with 2 extra bowls rice and extra chicken. No pickles please on my burger."
    - Assistant Response:
        "ORDER": {"Burger": {"Cheese": 2, "Pickles":"-0-"},"Fries": {},"Chicken Biryani": {"Rice": 2, "Chicken": 1}}, "output": "Gotcha. Would like anything else?"
"""

    system_prompt_2 = """ You are a machine that takes text returns what is supposed to be the food ORDER part of the text and the reply part. Sometimes there is no ORDER part.
                          You should parse the text and strictly return the processed text in the following format:
                        
                          For example, if you get the input: "ORDER": {"Burger": {"Cheese": 2, "Pickles":"-0-"},"Fries": {},"Chicken Biryani": {"Rice": 2, "Chicken": 1}}, "output": "Gotcha. Would like anything else?"\
                          Your output should be: {"ORDER": {"Burger": {"Cheese": 2, "Pickles":"-0-"},"Fries": {},"Chicken Biryani": {"Rice": 2, "Chicken": 1}}, "output": "Gotcha. Would like anything else?"}

                          if you get the input: "Would you like something else?"
                          your output should be: {"ORDER":{}, "output": "Would you like something else?"}

                          if you get the input: "````json {"ORDER":{"Pizza":{}, "Pork":{"Tomato":"-7-"}}, "output":"DONE"}````"
                          your output should be: {"ORDER":{"Pizza":{}, "Pork":{"Tomato":"-7-"}}, "output":"DONE"} 
                        
                          if you get the input: 
                          Now process the following user's input as instructed:
                      """

    out_1 = make_api_call(system_prompt, messages)
    out_2 = make_api_call(system_prompt_2, messages=[{"role": "user", "content": out_1}])
    return out_2

def make_api_call(system_prompt, messages):
    messages = [{"role": "system", "content": system_prompt}, *messages]

    # Request a chat completion from the OpenAI API based on the conversation so far
    chat_completion = client.chat.completions.create(
        messages=messages,
        model="gpt-4o",  # Specifies using the "gpt-4o" model
        # model = "gpt-4-0314",
    )

    # Extract the response text from the completion
    response_text = chat_completion.choices[0].message.content

    return response_text.strip()

def chatbot_conversation():
    recorder = AudioToTextRecorder(language="en", spinner=False)
    print("Here is the MENU: \n")
    print(menu)
    ai_reply = ""
    order = ""
    messages = []
    while not (ai_reply.upper().endswith("DONE") or ai_reply.upper().endswith("DONE.")):
        # Listen to user's order
        user_input = recorder.text()
        # user_input = input("User: ")
        if user_input != "":
            # print(user_input)
            messages.append({"role": "user", "content": user_input})
            raw_r = parse_order_with_llm(messages)
            try:
                response = eval(raw_r)
            except:
                response = {"ORDER":{}, "output":raw_r}
            ai_reply = response["output"]
            messages.append({"role":"assistant", "content": raw_r})
            order = response["ORDER"]
            # print(raw_r)
            # Check if the user said they're done
            # stream.feed(ai_reply)
            # stream.play_async()
            # print(ai_reply)   
            engine.say(ai_reply)
            engine.runAndWait()
    
    print("Final Order: ", order)

    """
    done = ""
    counter = 0
    messages = []
    recorder = AudioToTextRecorder()
    while True:
        text = recorder.text(process_text)
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
    
    """

if __name__ == "__main__":
    chatbot_conversation()
