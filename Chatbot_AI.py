import openai
import time


openai.api_key  = "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"
print("If you want end the interview type EXIT")

def get_completion_from_messages(messages, model="gpt-3.5-turbo", temperature=0):
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=temperature, # this is the degree of randomness of the model's output
    )
#     print(str(response.choices[0].message))
    return response.choices[0].message["content"]
messages =  [  
{'role':'system', 'content':'You are Expert javaScript Interviwer.'},    
{'role':'user', 'content':'Candidate'}  ]
response = get_completion_from_messages(messages, temperature=0)
print(response)
context = [ {'role':'system', 'content':"""
You are InterviewBot, an automated service to conduct expert-level JavaScript interviews. \
Your goal is to ask challenging yet fair questions to assess the candidate's proficiency in JavaScript. \
You start with a warm greeting, introduce yourself as the interviewer, and explain the interview format. \
You proceed with a series of coding challenges and conceptual questions related to JavaScript. \
Your questions may cover topics like closures, prototypes, async/await, ES6 syntax, and design patterns. \
You expect the candidate to respond in a clear and concise manner. \
Feel free to ask follow-up questions to delve deeper into their answers or clarify any ambiguities. \
You can also provide hints or guidance if the candidate seems stuck. \
Remember, the goal is to assess their expertise and problem-solving skills. \
After completing the technical questions, you may inquire about the candidate's experience and projects. \
Make sure to maintain a professional and respectful tone throughout the interview. \
Good luck with the interview process!
"""}
 ]  

while(True):
    try:
        prompt = input("Candidate : ")
        if prompt.strip().lower()=='bye':
            print(f"Interviewer : Thanks:) Your Interview is Over")
            break
        context.append({'role':'user', 'content':f"{prompt}"})
        response = get_completion_from_messages(context) 
        context.append({'role':'assistant', 'content':f"{response}"})
        print(f"Interviewer : {response}")
        
        
    except openai.error.ServiceUnavailableError as e:
        print("I want rest now!!")
        time.sleep(30)
    except openai.error.RateLimitError as e:
        print(f"due to {e} we are shutting down the system !!")
        time.sleep(120)


    
    
     
    
