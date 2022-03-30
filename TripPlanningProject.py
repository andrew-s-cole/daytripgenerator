import random

destinations = ['Belgium', 'Switzerland', 'Germany']
transportations = ['train', 'car', 'cab']
entertainments = ['sightseeing', 'chocolate tasting', 'touring']
restaurants = ['Vegetarian', 'traditional cuisine', 'local cuisine']
name = input('Please enter your name: ')
github = ('Checking...')


def initial_greeting():
    print(
        f'Hello {name}! Welcome to the random trip generator. I will help assist you in planning your trip.')


initial_greeting()


def destination_choice():
    print('I have chosen', random.choice(destinations),
          'for your trip location, is this selection okay? Enter Yes/No')
    while True:
        user_input = input()
        if user_input != 'Yes':
            print('I can pick another location instead, how about',
                  (random.choice(destinations)), 'for your trip location? Enter Yes/No')
        else:
            print('Perfect, lets continue planning your trip!')
            break


destination_choice()


def transportation_choice():
    print('I have chosen', random.choice(transportations),
          'for your mode of transportation, is this selection okay? Enter Yes/No')
    while True:
        user_input = input()
        if user_input != 'Yes':
            print('I can pick another mode of transportation instead, how about by',
                  random.choice(transportations), 'for your mode of transportation?')
        else:
            print('Perfect, lets continue planning your trip!')
            break


transportation_choice()


def entertainment_choice():
    print('I have chosen', random.choice(entertainments),
          'for your form of entertainment, is this okay? Enter Yes/No')
    while True:
        user_input = input()
        if user_input != 'Yes':
            print('I can pick another form of entertainment instead, how about',
                  random.choice(entertainments), 'for your entertainment choice?')
        else:
            print('Perfect, lets continue planning your trip!')
            break


entertainment_choice()


def restaurant_choice():
    print('I have chosen', random.choice(restaurants),
          'for your restaurant choice, is this okay? Enter Yes/No')
    while True:
        user_input = input()
        if user_input != 'Yes':
            print('I can pick another restaurant type instead, how about',
                  random.choice(entertainments), 'for your restaurant choice?')
        else:
            print('Perfect, lets continue planning your trip!')
            break


restaurant_choice()


def all_choices():
    print('We have finalized your trip, are you satisified with your current choices? Enter Yes/No')
    while True:
        user_input = input()
        if user_input != 'Yes':
            return destination_choice

        else:
            print('Your trip has been completed!')


all_choices()
