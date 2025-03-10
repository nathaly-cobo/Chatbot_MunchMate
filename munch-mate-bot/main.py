# 
# @Author: Seven Yaoching-Chi 
# @Date: 2024-05-23 20:30:11 
# @Last Modified by:   Seven Yaoching-Chi 
# @Last Modified time: 2024-05-23 20:30:11 
# 

import re
import os
import sys
import time
from dotenv import load_dotenv
from openai import OpenAI 
import uuid
import json
from contents import SYS_CONTENT, RESTAURANTS, TOOLS
from helper.common import gen_assistant_msg, gen_system_msg, gen_user_msg

if load_dotenv():
    print('Env file ready\n')
else:
    print('Can\'t load the env file, exit.')
    sys.exit(1)

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

def chat_complete_prompt_with_msg(messages, tools=None, tool_choice=None):
    print('Thinking...')
    time.sleep(1)
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo-1106",
            # model="gpt-4o",
            messages=messages,
            temperature=0, # this is the degree of randomness of the model's output
            tools=tools,
            tool_choice=tool_choice,
        )

        return response.choices[0].message
    except Exception as e:
            print("Unable to generate ChatCompletion response")
            print(f"Exception: {e}")
            return e
    


def get_restaurants(location, type):
    """Get the restaurants in a given location and type"""
    if location.lower() in RESTAURANTS:
        restaurants_info = {
            "location": location,
            "restaurants": [item for item in RESTAURANTS[location.lower()] if item.get("type") == type.upper()]
            
        }
        return json.dumps(restaurants_info)
    else:
        return json.dumps({
            "location": location,
            "restaurants": []
        })

available_functions = {
    "get_restaurants": get_restaurants,
}

def function_call(messages, response_message, tool_calls, available_functions):
    messages.append(response_message)  # extend conversation with assistant's reply
    # print("added response:", messages)

    for tool_call in tool_calls:
        function_name = tool_call.function.name
        print("function name is: ", function_name)
        function_to_call = available_functions[function_name]
        function_args = json.loads(tool_call.function.arguments)
        #print("function_args:", function_args)
        
        function_response = function_to_call(
            location=function_args.get("location"),
            type=function_args.get("type"),
        )
        messages.append(
            {
                "tool_call_id": tool_call.id,
                "role": "tool",
                "name": function_name,
                "content": function_response,
            }
        )

    second_response_message = chat_complete_prompt_with_msg(messages, tools=TOOLS, tool_choice="auto")  
    return second_response_message


response = {}
isFinish = False
isInit = True
random_uuid = ''

while not isFinish:
    if isInit:
        print(random_uuid)
        
        random_uuid = uuid.uuid4()
        response[random_uuid] = [gen_system_msg(SYS_CONTENT)]
        responseInit = chat_complete_prompt_with_msg(response[random_uuid])
        print("ChatBot: ", responseInit.content)
        response[random_uuid].append(gen_assistant_msg(responseInit.content))
        isInit = False

    user_input = input("You: ")
    if user_input:
        response[random_uuid].append(gen_user_msg(user_input))
        responseUser = chat_complete_prompt_with_msg(response[random_uuid], tools=TOOLS, tool_choice="auto")
        if responseUser.content:
            print("ChatBot: ", responseUser.content)        
        tool_calls = responseUser.tool_calls
        if tool_calls:
            print('Looking for the pre-defined functions......')
            responseUser = function_call(response[random_uuid], responseUser, tool_calls, available_functions)
            print(responseUser.content)
        
        response[random_uuid].append(gen_assistant_msg(responseUser.content))

        if any(s in responseUser.content for s in ["Thanks for coming", "have a nice day"]):
            isRestart = input("Would you want to start a new order? (Y/n)").strip().lower()
            if isRestart == '' or isRestart == 'y':
                isInit = True
            else:
                isFinish = True
