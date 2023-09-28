from termcolor import cprint
import emoji

print('Hello from CMD')

cprint('hello, world', 'green', 'on_red', attrs=["bold", "underline"])
print(emoji.emojize('Python is :thumbs_up:'))
print('hello')