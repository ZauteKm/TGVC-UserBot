from os import environ

# import logging
from pyrogram import Client, idle

API_ID = int(environ["2103561"])
API_HASH = environ["c300704dc35521eda4f846a66aa53071"]
SESSION_NAME = environ["BQA6yUGQDwHE4ZCAwPgFMOOJOAGMyR2W4HI6fnEDeupbkOlrTGydnpmHOnxkDeNKd3BvslrpgVXZ24nvNJfPtIm_YTBrGNfCUQtSkkmALWfcETe7Kcn9N3NdhDc7NRFtJF4TmiXMCSLguEQ0-Afhd1zXr9eN_TypKd9Fa4gxO-l7IIWfgj97HtRZD6lc3D87yYTyox-qWRsQ55vDfXewmJepRVWZdG2BCTUuQcxRbeKy5sQu4CojW-Zs0wQdX6UhiJyOqkCK4q6w1eu3Z0evLtJYnzFESzgZ8MZtChsu-1ADOAJGYEQGQUCxD7g4-6kSQyyMZZOXXe8C5KS4ZriuephWRfBDyAA"]

PLUGINS = dict(
    root="plugins",
    include=[
        "vc." + environ["player"],
        "ping",
        "sysinfo"
    ]
)

app = Client(SESSION_NAME, API_ID, API_HASH, plugins=PLUGINS)
# logging.basicConfig(level=logging.INFO)
app.start()
print('>>> USERBOT STARTED')
idle()
app.stop()
print('\n>>> USERBOT STOPPED')
