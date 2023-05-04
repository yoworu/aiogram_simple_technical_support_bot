from aiogram.types import BotCommand

commands_descs = (
    ('/help', 'Get help'),
    ('/question', 'Ask some question')
)

commands_list = [BotCommand(command=cmd[0], description=cmd[1]) for cmd in commands_descs]
