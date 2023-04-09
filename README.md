# Ouroboros copier
**Please don't use this for unleaked circles. This script may lead to key leaks when misformatted output is pasted.**

## Usage
Place a list of your joined circles in `circles/joined.txt`.

Place files containing `(LABEL) (KEY)` entries in `circles/X_keys.txt` where `X` can be an arbitrary name.
Place files containing join commands in `circles/X_commands.txt` where `X` can likewise be an arbitrary name.

Next run `main.py` to generate a list of join commands for circles you have not yet joined.

Keep updating `joined.txt` as you join more circles or they get betrayed.
