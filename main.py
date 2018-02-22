#! /usr/bin/env python
# coding: utf-8

from irc.bot import SingleServerIRCBot, ServerSpec

from lib.processing import Processing

class Bot(SingleServerIRCBot):
    def __init__(self, name, desc, passwd):
        sSpec = ServerSpec("irc_server", 6667, passwd)
        super().__init__([sSpec], name, desc)
   
    def on_welcome(self, serv, ev):
        serv.join("#tirage")
        serv.join("#conversation")
        serv.join("#admin")

    def on_kick(self, serv, ev):
        serv.join("#tirage")
        serv.join("#conversation")
        serv.join("#admin")

    def on_pubmsg(self, serv, ev):
        message = ev.arguments[0]
        Processing.processMessage(message, serv, ev.target)

if __name__ == "__main__":
    with open("/opt/key.secret", "r") as secret:
        myBot = Bot("MathsBot",
            "MathsBot, le robot du TFJM.",
            secret.readline())
        myBot.start()

