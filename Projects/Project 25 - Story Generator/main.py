## Write a story generator program which takes the user input sentences and identifies whether the 
# Added sentence is a question or an assertive sentence and format all these input data to get a story generated as the result

def format_sentence(u_input):
    capitalized = u_input.capitalize()
    q_words = ['What','Why','How','Where','When','Is']
    for word in q_words:
        if capitalized.startswith(word):
            if capitalized.endswith('?'):
                capitalized = capitalized.remove('?')
            return f"{capitalized}? "
    return f"{capitalized}. "

result = []
while True:
    
    u_input = input("Whats on yout mind ? -> ")
    if u_input == '\end':
        break
    else:
        complete_sentence = format_sentence(u_input)
        result.append(complete_sentence)

story = " ".join(result)
print(story)