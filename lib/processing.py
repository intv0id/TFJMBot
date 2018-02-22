#! /usr/bin/env python3
# coding: utf-8

from .actions import randomAction, adminAction

import re

class Processing():
    @staticmethod
    def processMessage(message, serv, channel):
        if re.match( r'^!choose (.*)$', message):
            matchingExp = re.match( r'!choose (.*)$', message)
            elements = matchingExp.groups()[0].split(",")
            randomAction.elementChoice(elements, serv, channel)
        elif re.match(r'^!flipcoin$', message, channel):
            randomAction.flipCoin(serv, channel)
        elif re.match(r'^!rolldie ([0-9]*)$', message, channel):
            n = int(re.match( r'!rolldie ([0-9]*)$', message).groups()[0])
            randomAction.rolldie(n, serv, channel)
        elif re.match(r'^!gm (.*?)$', message, channel):
            fwMessage = re.match(r'!gm (.*?)$', message).groups()[0]
            adminAction.sendAll(serv, channel)
