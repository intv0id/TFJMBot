#! /usr/bin/env python
# coding: utf-8

from irc.bot import SingleServerIRCBot, ServerSpec

from lib.processing import Processing

class Bot(SingleServerIRCBot):
    def __init__(self, name, desc, passwd, channels):
        sSpec = ServerSpec("irc_server", 6667, passwd)
        super().__init__([sSpec], name, desc)
        self.channels = channels
   
    def on_welcome(self, serv, ev):
        self.join_channels(serv)

    def on_kick(self, serv, ev):
        self.join_channels(serv)

    def on_pubmsg(self, serv, ev):
        message = ev.arguments[0]
        Processing.processMessage(message, serv, ev.target)

    def join_channels(self, serv):
        for chan in self.channels:
            try: serv.join(chan)
            except: 
                print("Failed to join {}".format(chan))

if __name__ == "__main__":
    with open("/opt/key.secret", "r") as secret, \
        open("/opt/channels.csv","r") as channels:
        myBot = Bot("MathsBot",
            "MathsBot, le robot du TFJM.",
            secret.readline(),
            filter(lambda a: a, channels.readline().split(",")))
        myBot.start()

