import random

destinations = ['Belgium', 'Switzerland', 'Germany', 'Ireland']
transportations = ['train', 'car', 'cab', 'bike']
entertainments = ['sightseeing', 'chocolate tasting',
                  'touring', 'immersing yourself in the culture']
restaurants = ['vegetarian food', 'traditional cuisine',
               'local cuisine', 'at a fancy restaurant']
name = input('Please enter your name: ')


def initial_greeting():
    print(
        f'Hello {name}! Welcome to the random trip generator. I will help assist you in planning your trip.')


initial_greeting()


def destination_choice(options, category):
    random_option = random.choice(options)
    response = input(
        f'We have chosen {random_option} for your {category}, is that okay? Enter Yes/No: ')

    while response != 'Yes':
        random_option = random.choice(options)
        response = input(
            f'How about {random_option} for your {category} instead? Enter Yes/No: ')
    else:
        print('Perfect! lets continue planning your trip!')
        return random_option


def transportation_choice(options, category):
    random_option = random.choice(options)
    response = input(
        f'We have chosen {random_option} for your {category}, is that okay? Enter Yes/No: ')

    while response != 'Yes':
        random_option = random.choice(options)
        response = input(
            f'How about {random_option} for your {category} instead? Enter Yes/No: ')
    else:
        print('Perfect! lets continue planning your trip!')
        return random_option


def entertainment_choice(options, category):
    random_option = random.choice(options)
    response = input(
        f'We have chosen {random_option} for your {category}, is that okay? Enter Yes/No: ')

    while response != 'Yes':
        random_option = random.choice(options)
        response = input(
            f'How about {random_option} for your {category} instead? Enter Yes/No: ')
    else:
        print('Perfect! lets continue planning your trip!')
        return random_option


def restaurant_choice(options, category):
    random_option = random.choice(options)
    response = input(
        f'We have chosen {random_option} for your {category}, is that okay? Enter Yes/No: ')

    while response != 'Yes':
        random_option = random.choice(options)
        response = input(
            f'How about {random_option} for your {category} instead? Enter Yes/No: ')
    else:
        print('Perfect! lets continue planning your trip!')
        return random_option


chosen_destination = destination_choice(destinations, 'destination')
chosen_transportation = transportation_choice(
    transportations, 'transportation')
chosen_entertainment = entertainment_choice(entertainments, 'entertainment')
chosen_restaurant = restaurant_choice(restaurants, 'restaurant')

print(
    f'Your trip will be going to {chosen_destination}, where you will travel by {chosen_transportation}, entertaining yourself by {chosen_entertainment}, and eating {chosen_restaurant}.')


def trip_completion():
    response = input(
        f'your trip has been completed {name}! Are you satisfied with your choices? Enter Yes/No: ')
    if response == 'Yes':
        print('You are all set, please enjoy your trip!')
    else:
        print('I am sorry, lets try again!')


trip_completion()
