```text
 ______    _   _
|  ____|  | | | |
| |__ __ _| |_| |__   ___ _ __
|  __/ _` | __| '_ \ / _ \ '__|
| | | (_| | |_| | | |  __/ |
|_|  \__,_|\__|_| |_|\___|_|
```

# Random-Information-Generator
A command-line tool for randomly generating various kinds of information.

---

## Available generators

### Name generator

Generates randomly picked names using RandomProfile. Offers a choice between either full names, or just first or last ones.

### Address generator

Generates real, randomly picked addresses from the USA using Random Address and https://openaddresses.io. Offers a choice to pull either from a specific state or all states.

### Password generator

Generates passwords of the user's desired length. Passwords are generated using Python's secrets module.

### Email generator

Generates random emails. The emails are formed by combining a random name, either a user-selected domain or random one from RandomProfile, a set of random alphanumeric characters.

Example(s):
```text
mccall.albertIluG@mail.com
ferguson.damienl4YA@myself.com
guerrero.colton2Ll7@workmail.com
bentley.gregoryz1aeQoq@myself.com
zavala.kaisonr1n3nZU@aol.de
peters.landonrWD@planetmail.com
alfaro.connerLZ4jV@hotmail.com
hogan.lucanD9vyu@workmail.com
pennington.cain49YUp@myself.com
conley.neofBrFCs@gmx.net
```

### Profile generator

Generates a random fake identity using RandomProfile, including a name, address, phone number, job, height, etc.. Emphasis on fake, information is not guaranteed to be real or valid.

Example(s):

```text
first_name: Ty
last_name: Ventura
hair_color: yellow
blood_type: (O+)
full_name: Ty Ventura
DOB: 04/03/1971
age: 51
height: 154
weight: 50
phone: +1-466-915-9427
address: 116 Hill St. Vice City UT 58169
email: tyventura@usa.com
job_title: Game Designer
ip_address: 38.10.38.67
```

### Coordinate generator

Generates real, randomly picked coordinates from the USA using Random Address and https://openaddresses.io. Offers a choice to pull either from a specific state or all states.

### Coin flip generator

Generates coin flips, heads or tails.

### Random number generator

Generates random integer numbers between two number (inclusive) that you supply.

---

## How to build

Run the following commands in the project directory:

```console
python3 -m build
```

The built packages will appear in [dist/.](dist "Distributables folder.")

## Installation

Random-Information-Generator is avalible on [PyPi,](https://pypi.org/project/random-information-generator "Random-Information-Generator on PyPi") and can be installed by running the following command(s):

```console
pip install random-information-generator
```

Alternatively, You can download the latest package from [Releases,](https://github.com/FatherVonTayvious/Random-Information-Generator/releases "Random-Information-Generator releases.") or build from source, and install it using the following command(s):

```console
pip install <package name goes here>
```

## How to run

[Python 3](https://www.python.org "Python homepage") is required.

If Random-Information-Generator was installed via package, simply run the following command(s):

```console
randominformationgenerator
```

Alternatively, Random-Information-Generator is a stand-alone script and can be run by following these instructions:

The following dependencies are required:

- Colorama - https://pypi.org/project/colorama
- Random Address - https://pypi.org/project/random-address
- RandomProfile - https://pypi.org/project/random-profile

Which can be installed using the following command(s):
```console
pip install colorama random-address random-profile
```

The [stand-alone script](src/random_information_generator/Info.py "Random-Information-Generator") can then be run using either of the following commands in the project directory:
```console
python3 src/random_information_generator/Info.py
./src/random_information_generator/Info.py
```

---

## Changelog

- Fixed calls to functions from random_profile.
- Fixed printing of logo.
- Fixed packaging dependencies.
- Added license (GPLv3).
