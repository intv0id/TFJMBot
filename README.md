# TFJMBot
An IRC Chatbot for the TFJM Tournament team draw.

https://intv0id.github.io/TFJMBot/

## Commands

* `!gm message`
> Diffuse message to all participants.
* `!rolldie n`
> Choose number in range `[|1, n|]`.
* `!flicoin`
> Flip a coin (tail, heads).
* `!choose a,b,c`
> Choose element (coma separated, same probability).

## Configuration

### Docker-compose

Example:

```yml
ircbot:
  build: ./TFJMBot
  volumes:
    - "/etc/ircbot.docker/:/config"
  container_name: ircbot
```

Both `key.secret` and `channels.csv` should be in `/config` within the container.

### key.secret

Hashed (`SHA256`) password for operator connection to the irc server.

To obtain this hash, use 

```irc
/quote mkpasswd sha256 <password>
```

### channels.csv

Coma separated channels value.

**Example:**

```csv
channel1,channel2,channel3,
```

## License

MIT
