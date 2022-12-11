# Exbitron API CLI

# ![Exbitron](https://cdn.discordapp.com/attachments/994252098571079740/1051226477875691660/image.png)

Command line interface to the website [Exbitron](https://www.exbitron.com/)

---

Translations | [EN](README.md) | [NO](README_NO.md) |

# Innhold
- [API documentation](#api-documentation)
- [Setup and Run](#setup-and-run)
- [Commands](#commands)
- [TODO](#todo)
- [Contribute](#contribute)
- [Contributors](#contributors)
- [License](#licence)

# API Documentation

The API that is used is based upon the API [Exbitron](https://www.exbitron.com/kb/api.html) has. All information and statistics are coming from here. To build out this CLI to every function they have, a person just need to add more endpoints. It just takes time, so if your feature is not here, make a issue under this project and we will take a look at it.

# Setup and Run 

1. Clone this project `git clone git@github.com:danielboye/exbitron-cli.git`
2. Follow the [API](api.md) guide to get access to your API keys.
3. Run `./setup.shy`
4. Run `python cli.py`

# Commands

More commands are comming. Everything can be implimented, it just takes time. 

### Wallet
- `oversikt` - Main menu with overview over active orders and your wallet.
- `wallet` - Returns the value of your wallet. 
- `exit` - Close the program.

### Price

- `price <ticker>` - Price of a trading pair.
- `ask <ticker>` - Ask price from the orderbooks to a optional trading pair.
- `bid <ticker>` - Bid price from the orderbooks to a optional trading pair.
- `spread <ticker>` - Spread showes in % on a optional trading pair.

Example:


```shell
spread btc
```
Output

```shell
Spread on btc is: 2.44 %
```

### Other
- `kontakt` - Contact information to the author.

# TODO

- Get a better wallet overview
- Execute trades
- Stop, create and edit live orders
- Better design for closing the script with ctrl c without printing out "KeyboardInterrupt"
- More features from the API
- Rewrite the project into English
- Rewrite the program in C++
- Convert the program into a bash command in linux with the help of a bash script. As "neofetch" only as "exbitron" that launches the client

Big changes that are cool but a little bit more difficult

- Get trading data represented as a chart in the terminal 
- Have a more persistent program that rather asks you once for the keys, and remembers them after that

# Contribute

## Pull request

I appreciate all contributions whether they are small changes such as documentation of source code to major improvement of
code. The easiest way is to create a fork and then make a pull request to our master branch.

More features will come eventually, and it's just a matter of creating new "issues" for any features you want, and I'll take a look at them

# Contributors

The following contributors have either helped start this project, have contributed
code, actively maintain it (including documentation), or in other ways
be wonderful contributors to this project. **We'd like to take a moment to recognize them.**

[<img src="https://github.com/danielboye.png?size=72" alt="danielboye" width="72">](https://github.com/danielboye)

# License

The license is MIT
