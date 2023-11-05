import json
import os
from time import sleep
from dotenv import load_dotenv
import openai
import tiktoken
import re

def num_tokens_from_string(string: str, encoding_name: str) -> int:
    encoding = tiktoken.encoding_for_model(encoding_name)
    num_tokens = len(encoding.encode(string))
    return num_tokens


def summarize_chunks(text_chunks, prompt):
    context = ""
    output = []
    tokens_called = 0
    for chunk in text_chunks:
        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            temperature=0.2,
            max_tokens=1000,
            messages=[
                {
                    "role": "system",
                    "content": context + prompt
                },
                {
                    "role": "user",
                    "content": chunk[0]
                }
            ]
        )
        # response is an OpenAI object get the text from it
        response = completion.choices[0]['message']['content']
        context = "Here is a summary of the previous text: " + response + " "
        output.append(response)
        tokens_called += chunk[1]
        if tokens_called > 80000:
            sleep(60)
            tokens_called = 0
    return output

def clean_json(string):
    string = re.sub(",[ \t\r\n]+}", "}", string)
    string = re.sub(",[ \t\r\n]+\]", "]", string)

    return string

def create_lessons(lesson_chunks, prompt):
    lessons = []
    for chunk in lesson_chunks:
        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            temperature=0.2,
                max_tokens=1000,
                messages=[
                    {
                        "role": "system",
                        "content": prompt
                    },
                    {
                        "role": "user",
                        "content": chunk
                    }
                ]
        )
        #turn the response into a json object
        lesson = json.loads(clean_json(completion.choices[0]['message']['content']))
        lessons.append(lesson)
    return lessons

def create_chunks_from_string(string, encoding_name, chunk_size):
    chunks = []
    chunk = ""
    for word in string.split(" "):
        if num_tokens_from_string(chunk + word, encoding_name) > chunk_size:
            chunks.append((chunk, num_tokens_from_string(chunk, encoding_name)))
            chunk = ""
        chunk += word + " "
    chunks.append((chunk, num_tokens_from_string(chunk, encoding_name)))
    return chunks

def gpt_caller(input_object):
    # load API key from .env file
    load_dotenv()
    openai.api_key = os.getenv("OPENAI_API_KEY")
    
    lessons = []
    for k in input_object:
        all_text = input_object[k]
        # add all the texts together
        text = ""
        for t in all_text:
            text += all_text[t] + "\n"
        prompt = ""
        #remove newlines
        text = text.replace("\n", " ")
        # split text into chunks of 2000 tokens
        text_chunks = create_chunks_from_string(text, "gpt-3.5-turbo", 2000)
        
        # Summarize each chunk and use previous summary as context for next chunk
        output = summarize_chunks(text_chunks, "Using the context of the previous text, summarize the new text: ")
        
        # Add up chunks from outputs such that each chunk is less than 3500 tokens
        lesson_chunks = []
        chunk = ""
        for summary in output:
            if num_tokens_from_string(chunk + summary, "gpt-3.5-turbo") > 3500:
                lesson_chunks.append(chunk)
                chunk = ""
            chunk += summary + " "
        lesson_chunks.append(chunk)
        
        # Now create a lesson plan based on the summary
        prompt = "Using the following summary create a lesson plan that helps students understand the text. The lesson plan should be written in a way that is easy for students to understand. Do not include any explanations, only provide a RFC8259 compliant JSON response with the following structure. "
        prompt += '''{
            "Title": "The title of the lesson",
            "Objective": "A brief description of the lesson objective",
            "Materials": "A brief description of the materials needed for the lesson",
            "Procedure": {
                "Step One": "Procedure step description",
                "Step Two": "Procedure step description",
                "...": "..."
            },
            "Assessment": "A brief description of how the student will be assessed"
        }'''
        lessons += create_lessons(lesson_chunks, prompt)
    
    lessons = [json.dumps(lesson) for lesson in lessons]
        
    return lessons