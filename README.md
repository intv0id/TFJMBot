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

### key.secret

Hashed (`HMAC-SHA256`) password for operator connection to the irc server.

To obtain this hash, use 

```irc
\quote /mkpasswd hmac-sha256 <password>
```

### channels.csv

Coma separated channels value.

**Example:**

```csv
channel1,channel2,channel3,
```

## License

MIT
