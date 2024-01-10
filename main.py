from itertools import cycle
from better_proxy import Proxy
from os.path import isdir
import asyncio
from os import listdir
from os import mkdir
from os.path import exists
from sys import stderr

from loguru import logger

from core import create_sessions, start_farming
from database import on_startup_database
from utils import monkeypatching

logger.remove()
logger.add(stderr, format='<white>{time:HH:mm:ss}</white>'
                          ' | <level>{level: <8}</level>'
                          ' | <cyan>{line}</cyan>'
                          ' - <white>{message}</white>')


async def main() -> None:
    await on_startup_database()

    match user_action:
        case 1:
            await create_sessions()

            logger.success('Sessions added successfully')

        case 2:
            tasks: list = [
                asyncio.create_task(coro=start_farming(session_name=current_session_name,
                                                       proxy=next(proxies_cycled) if proxies_cycled else None))
                for current_session_name in session_files
            ]

            await asyncio.gather(*tasks)

        case _:
            logger.error('Action selected incorrectly')


if __name__ == '__main__':
    if not exists(path='sessions'):
        mkdir(path='sessions')

    with open(file='data/proxies.txt',
              mode='r',
              encoding='utf-8-sig') as file:
        proxies: list[str] = [Proxy.from_str(proxy=row.strip()).as_url for row in file]

    if proxies:
        proxies_cycled: cycle = cycle(proxies)

    else:
        proxies_cycled: None = None

    session_files: list[str] = [current_file[:-8] if current_file.endswith('.session')
                                else current_file for current_file in listdir(path='sessions')
                                if current_file.endswith('.session') or isdir(s=f'sessions/{current_file}')]

    logger.info(f'Discovered {len(session_files)} sessions / {len(proxies)} proxy')

    user_action: int = int(input('\n1. Create a session'
                                 '\n2. Launch the bot from existing sessions'
                                 '\nSelect your action:'))
    print()

    try:
        import uvloop

        uvloop.run(main())

    except ModuleNotFoundError:
        asyncio.run(main())

    input('\n\nPress Enter to Exit..')
