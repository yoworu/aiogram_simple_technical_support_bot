from aiogram import html

START_MSG = (
    'Hello, I\'m {}'
    'To start asking your questions type /question'
).format(html.bold('technical support bot'))

QUESTION_START_MSG = (
    'Ok, I let\'s start feedback!\n\n'
    '{}'
).format(html.italic('Note: the message can contain no more than 250 characters'))


QUESTION_CANCEL_MSG = (
    'Question Cancelled'
)

QUESTION_SENT_MSG = (
    'Question sent'
)

QUESTION_LONG_MSG = (
    'Question is too long\n',
    'It is important that your message can not contain more than 250 characters\n',
    '{length}/250!'
)

ANSWER_SENT_MSG = (
    'Answer sent'
)
