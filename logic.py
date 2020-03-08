from google.cloud import translate_v2 as translate
client = translate.Client()
import random


def get_languages(client):
    languages = []
    for language in client.get_languages():
        languages.append(language)
    return languages


def target_language(languages):
    l_index = random.randint(0, len(languages) - 1)
    to_language = languages[l_index]
    return to_language


def get_answer(languages, answer_index, score):
    choices = []
    while len(choices) == 0 or answer_index in choices:
        choices = random.sample(range(0, len(languages) - 1), 4)

    target = random.randint(0, 4)
    choices.insert(target, answer_index)

    print('')
    print('Guess the language: ')
    marker = 1
    for choice in choices:
        index = int(choice)
        print(str(marker) + ') ' + languages[index]['name'])
        marker += 1
        
    print('')
    user_response = input('Select a number: ')
    if user_response.lower() == 'q':
        close_game(score)
    user_selection = int(user_response)
    print('***')
    if user_selection == target + 1:
        score[0] += 1
        print('Correct!')
    else:
        print('Sorry, the correct answer was ' + languages[answer_index]['name'])
    return score


def translatetext(message, score):
    client = translate.Client()
    languages = get_languages(client)

    from_language = client.detect_language(message)
    for l in languages:
        if l['language'] == from_language['language']:
            languages.remove(l)
            
    to_language = target_language(languages)
    result = client.translate(message, to_language['language'])

    print('***')
    print(result['translatedText'])
    print('***')

    answer_index = languages.index(to_language)
    score = get_answer(languages, answer_index, score)


def run(score):
    print('***')
    message = input('Type something in any language: ')
    if message.lower() == 'q':
        close_game(score)
    translatetext(message, score)
    score[1] += 1
    print('Your current score is ' + str(score[0]) + ' out of ' + str(score[1]))
    print('')
    return score


def close_game(score):
    print('***')
    if score[1] > 0:
        print('Final score: ' + str(score[0]) + ' out of ' + str(score[1]) + ' (' + str(round((score[0]/score[1]) * 100)) + '%)')
    quit()
