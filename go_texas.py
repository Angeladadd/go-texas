#!/usr/bin/env python

import argparse
import os
import json
from datetime import datetime
import cnlunar
from wuxing import texas_advice, texas_fortune


happy_texas = '纳财'

def main():

    parser = argparse.ArgumentParser(description='Texas fortune for today')
    subparsers = parser.add_subparsers(dest='who')
    me_parser = subparsers.add_parser('me', help='Test the fortune for yourself')
    friend_parser = subparsers.add_parser('friend', help='Test the fortune for a friend')
    friend_parser.add_argument('name', help='Friend\'s name')
    # it should be optional after we can predict 五行 by name
    friend_parser.add_argument('birthday', help='Friend\'s birthday')
    parser.add_argument('-s', dest='source', help='Source file path')
    args = parser.parse_args()

    config_path = os.path.join(args.source or os.curdir, 'config.json')
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
    lunar_advice = happy_texas in lunar.goodThing
    me_advice, friend_advice = False, False

    if args.who == 'me':
        user_birthday = datetime.strptime(config['me']['birthday'], '%d-%m-%Y')
        suitability, _ = texas_fortune(user_birthday)
        me_advice = lunar_advice and texas_advice(suitability)
    elif args.who == 'friend':
        # TODO: save friend's birthday to config
        friend_birthday = datetime.strptime(args.birthday, '%d-%m-%Y')
        suitability, _ = texas_fortune(friend_birthday)
        friend_advice = lunar_advice and texas_advice(suitability)
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


if __name__ == '__main__':
    main()