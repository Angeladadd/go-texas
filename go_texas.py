#!/usr/bin/env python

import argparse
import os
import json
from datetime import datetime
import cnlunar
from wuxing import texas_fortune


happy_texas =  ['纳财', '出师', '庆赐']
sad_texas = ['施恩', '入学']

def get_lunar_advice(goodThing):
    return (any([thing in goodThing for thing in happy_texas]) - any([thing in goodThing for thing in sad_texas])) >= 0

def get_wuxing_advice(suitability):
    return suitability >= 5

def main():

    parent_parser = argparse.ArgumentParser(add_help=False)
    parent_parser.add_argument(
        '-e', '--explain', 
        dest='explain', 
        action='store_true',
        help='Explain the fortune'
    )
    parser = argparse.ArgumentParser(description='Texas fortune for today')
    subparsers = parser.add_subparsers(dest='who')
    me_parser = subparsers.add_parser('me', parents=[parent_parser], help='Test the fortune for yourself')
    friend_parser = subparsers.add_parser('friend', parents=[parent_parser], help='Test the fortune for a friend')
    friend_parser.add_argument('name', help='Friend\'s name')
    # it should be optional after we can predict 五行 by name
    friend_parser.add_argument('birthday', help='Friend\'s birthday')
    args = parser.parse_args()

    config_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'config.json')
    config = {}
    if os.path.exists(config_path):
        config = json.load(open(config_path))
    else:
        user_name = input('What is your name? ')
        user_birthday = input('What is your birthday? In the format of DD-MM-YYYY ')
        config['me'] = {
            'name': user_name,
            'birthday': user_birthday
        }
    
    today = datetime.now()
    lunar = cnlunar.Lunar(today, godType='8char')
    lunar_advice = get_lunar_advice(lunar.goodThing)
    me_advice, friend_advice = False, False
    elements = {}

    if args.who == 'me':
        user_birthday = datetime.strptime(config['me']['birthday'], '%d-%m-%Y')
        suitability, elements = texas_fortune(user_birthday)
        me_advice = lunar_advice and get_wuxing_advice(suitability)
    elif args.who == 'friend':
        # TODO: save friend's birthday to config
        friend_birthday = datetime.strptime(args.birthday, '%d-%m-%Y')
        suitability, elements = texas_fortune(friend_birthday)
        friend_advice = lunar_advice and get_wuxing_advice(suitability)
    else:
        print('Command unsupported: ', args.who)

    # save config back
    with open(config_path, 'w') as file:
        json.dump(config, file)

    if args.who == 'me':
        if me_advice:
            print('Today is a lucky day for you! GO TEXAS!')
        else:
            print('DO NOT GO TEXAS!')
    elif args.who == 'friend':
        if friend_advice:
            print('Your friend has a lucky day. DO NOT GO TEXAS WITH THEM!')
        else:
            print('Your friend has a bad day. GO TEXAS WITH THEM!')
    
    if args.explain:
        print('Good thing for today:', lunar.goodThing)
        print('Texas fortune:', elements)


if __name__ == '__main__':
    main()