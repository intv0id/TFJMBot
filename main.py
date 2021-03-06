#! /usr/bin/env python
# coding: utf-8

from irc.bot import SingleServerIRCBot, ServerSpec

from lib.processing import Processing

class Bot(SingleServerIRCBot):
    def __init__(self, name, desc, passwd, channels_list):
        sSpec = ServerSpec("irc_server", 6667)
        super().__init__([sSpec], name, desc)
        self.channels_list = channels_list
        self.passwd = passwd.split("\n")[0]

    def on_welcome(self, serv, ev):
        self.join_channels(serv)

    def on_kick(self, serv, ev):
        self.join_channels(serv)

    def on_pubmsg(self, serv, ev):
        message = ev.arguments[0]
        Processing.processMessage(message, serv, ev.target)

    def join_channels(self, serv):
        #serv.send_items("OPER", "MathsBot", self.passwd)
        for chan in self.channels_list:
            try: 
                serv.join(chan)
                #serv.send_items("SAMODE", chan, "+o", "MathsBot")
            except:
                print("Failed to join {}".format(chan))

if __name__ == "__main__":
    with open("/config/key.secret", "r") as secret, \
        open("/config/channels.csv","r") as chan_file:
        myBot = Bot("MathsBot",
            "MathsBot, le robot du TFJM.",
            secret.readline(),
            [ c for c in chan_file.readline().split(",") if c ])
        myBot.start()

