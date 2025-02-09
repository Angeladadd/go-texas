#!/usr/bin/env python

import argparse
import os
import json
from datetime import datetime
import cnlunar


happy_texas = '纳财'

def main():

    # TODO: predict by 五行八字
    # parser = argparse.ArgumentParser(description='Texas fortune for today')
    # subparsers = parser.add_subparsers(dest='who')
    # me_parser = subparsers.add_parser('me', help='Test the fortune for yourself')
    # friend_parser = subparsers.add_parser('friend', help='Test the fortune for a friend')
    # friend_parser.add_argument('name', help='Friend\'s name')
    # friend_parser.add_argument('--birthday', help='Friend\'s birthday')
    # args = parser.parse_args()

    # TODO: save name and birthday to config file
    # source_dir = os.path.dirname(os.path.abspath(__file__))
    # config_path = os.path.join(source_dir, 'config.json')
    # config = {}
    # if os.path.exists(config_path):
    #     config = json.load(open(config_path))
    # else:
    #     user_name = input('What is your name? ')
    #     user_birthday = input('What is your birthday? In the format of DD-MM-YYYY ')
    #     config['me'] = {
    #         'name': user_name,
    #         'birthday': user_birthday
    #     }
    
    today = datetime.now()
    lunar = cnlunar.Lunar(today, godType='8char')
    if happy_texas in lunar.goodThing:
        print('Today is a lucky day for you! GO TEXAS!')
    else:
        print('DO NOT GO TEXAS!')
    
    # TODO: predict by different users
    # if args.command == 'me':
    #     pass
    # elif args.command == 'friend':
    #     pass
    # else:
    #     print('Command unsupported: ', args.command)


if __name__ == '__main__':
    main()