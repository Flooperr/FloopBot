from bardapi import Bard
DiscordNames = {'flooperrr': 'Ariel', 'flamingoish': 'Devin', 'lazyrus123': 'Cameron', 'notjewish': 'Grady', 'illegal_mexico21': 'Erick', 'yizzzz69': 'Yiz'}
# Set your Bard API key (the __Secure-1PSID cookie value)
token = 'BARD TOKEN HERE' 

# Create a Bard instance
bard = Bard(token=token)

def answer(question, person):
    user_prompt = f'The person asking this question is {person}: {question}'
    response = bard.get_answer(user_prompt)

    # Access the response content
    content = response['content']
    print("Bard's response:")
    print(content)
    return content



