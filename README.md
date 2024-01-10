# Fork changes
+ Translated into English
+ Optimized
 
### Functional
+ _Multithreading_
+ _Binding a proxy to a session_
+ _Auto-purchase of items if you have money (enery boost, speed boost, click boost)_
+ _Random sleep time between clicks_
+ _Random number of clicks per request_
+ _Support tdata / pyrogram .session / telethon .session_

### data/config.py  
_**API_ID / API_HASH** - Platform data from which to launch a Telegram session (stock - Android)
**MIN_CLICKS_COUNT** - Minimum number of clicks per request (counted without a multiplier, i.e. with a multiplier of x9: 1 click will equal 9 coins, not one)
**AUTO_BUY_ENERGY_BOOST** - Automatic purchase of Energy Boost when balance is reached (True / False)
**AUTO_BUY_SPEED_BOOST** - Automatic purchase of Speed ​​Boost when balance is reached (True / False)
**AUTO_BUY_CLICK_BOOST** - Automatic purchase of Click Boost when balance is reached (True / False)
**USE_PROXY_FROM_FILE** - Whether to use Proxy from the data/proxies.txt file for accounts that do not have Proxy attached (True / False)
**SLEEP_BETWEEN_CLICK** - Delay range between clicks (in seconds)
**SLEEP_BEFORE_BUY_MERGE** - Delay range before buying boosts (in seconds)
**SLEEP_BEFORE_ACTIVATE_FREE_BUFFS** - Delay range before activating daily boosts (in seconds)
**SLEEP_BEFORE_ACTIVATE_TURBO** - Delay range before activating Turbo (in seconds)_
