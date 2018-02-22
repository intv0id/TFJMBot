#! /usr/bin/env python3
# coding: utf-8

import random as rd

class randomAction():
    @staticmethod
    def rolldie(n:int, serv, channel):
        try:
            assert type(n) is int
            assert n > 0
        except AssertionError:
            return

        serv.privmsg(channel, "---- Tirage [|{}, {}|] ----".format(1, n))
        serv.privmsg(channel, str(rd.randint(1, n)))

    @staticmethod
    def elementChoice(stringList, serv, channel):
        try:
            assert all(map(lambda x: type(x) is str, stringList))
        except AssertionError:
            return

        serv.privmsg(channel, "--- Tirage au sort ---")
        serv.privmsg(channel, "----------------------")
        serv.privmsg(channel, "---- Possibilités ----")
        for i,j in enumerate(stringList):
            serv.privmsg(channel, "{} - {}".format(str(i+1), j))
        serv.privmsg(channel, "------ Résultat ------")
        serv.privmsg(channel, str(rd.choice(stringList)))

    @staticmethod
    def flipCoin(serv, channel):
        serv.privmsg(channel, "---- Pile ou Face ----")
        serv.privmsg(channel, rd.choice(("Pile","Face")))

class adminAction():
    @staticmethod
    def sendAll(fwMessage, serv, channel):
        serv.privmsg(channel, "---- Diffusion ----")
        serv.privmsg(channel, "")
        serv.privmsg(channel, fwMessage)
        serv.privmsg(channel, "")
        serv.privmsg(channel, "-------------------")
