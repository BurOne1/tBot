import asyncio

from data import config
from utils.db_api import quick_commands as commands
from utils.db_api.db_gino import db


async def db_test():
    await db.set_bind(config.POSTGRES_URI)
    #await db.gino.drop_all()
    #await db.gino.create_all()

    #await commands.fun_for_get_my_data('uuu', 'Ivan', 'Burvan', 'ii', 'mmmmm')
    # await commands.add_user(2, 'Alex', 'Nane is update')
    # await commands.add_user(3, 'Sergey', '6')
    # await commands.add_user(4, 'vlad', '7')

    # users = await commands.select_all_users()
    # print(users)
    #
    # count = await commands.count_users()
    # print(count)
    #
    # user = await commands.select_user(3)
    # print(user)
    #
    # await commands.update_status(2, 'kosta')
    #
    # user = await commands.select_user(2)
    # print(user)


loop = asyncio.get_event_loop()
loop.run_until_complete(db_test())

