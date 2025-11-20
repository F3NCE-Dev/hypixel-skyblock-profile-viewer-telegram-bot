import telebot
import requests
from config.config import *

bot = telebot.TeleBot(BOT_API)

@bot.message_handler(commands=['start'])
def main(m):
    bot.send_message(m.chat.id, 'Hi! How Can I help u??? 😺\nUse <b>"help"</b> for detailed information', parse_mode='html')

@bot.message_handler(commands=['help'])
def getHelp(m):
    bot.send_message(m.chat.id, '<b>My Commands:</b>'
                                '\n/user_profile - view user profile'
                                '\n/user_head - view the player’s avatar', parse_mode='html')

@bot.message_handler(commands=['user_profile'])
def user_profile(m):
    m_part = m.text.split()

    if len(m_part) == 2:
        user_name = m_part[1]
        res = requests.get(f"https://api.hypixel.net/player?key={HYPIXEL_API}&name={user_name}").json()
        if res.get('player') != None:
            bot.send_message(m.chat.id, f"I've found {user_name}")
            player_name = res['player']['playername']
            player_achievements = res["player"]["achievements"]
            bot.send_message(m.chat.id, f'<b>USERNAME IS:</b> {player_name}'
                                        f'\n\n{user_name} has the <b>{player_achievements["skyblock_sb_levels"]}</b> level on skyblock'
                                        f'\n\n<b>PLAYER SKILLS:'
                                        f'\n\n⚔️Combat level is {player_achievements["skyblock_combat"]}'
                                        f'\n\n💀Dungeon level is {player_achievements["skyblock_dungeoneer"]}'
                                        f'\n\n🌻Harvest level is {player_achievements["skyblock_harvester"]}'
                                        f'\n\n🌳Foraging level is {player_achievements["skyblock_gatherer"]}'
                                        f'\n\n🐟Fishing level is {player_achievements["skyblock_angler"]}</b>',
                             parse_mode='html')
        else:
            bot.send_message(m.chat.id, f"{user_name} hasn't been found.")
    else:
        bot.send_message(m.chat.id, 'Incorrect Input.\n/user_profile + "user name"')

@bot.message_handler(commands=['user_head'])
def user_head(m):
    m_part = m.text.split()

    if len(m_part) == 2:
        user_name = m_part[1]
        try:
            mojang_response = requests.get(f"https://api.mojang.com/users/profiles/minecraft/{user_name}")

            if mojang_response.status_code == 200:
                mojang_response.raise_for_status()
                uuid = mojang_response.json()["id"]
                head_url = f"https://crafatar.com/avatars/{uuid}?size={100}&overlay"

                try:
                    bot.send_photo(m.chat.id, f'{head_url}')
                except Exception:
                    bot.send_message(m.chat.id, 'Image not found')

        except requests.RequestException:
            bot.send_message(m.chat.id, f"{user_name} hasn't been found.")
    else:
        bot.send_message(m.chat.id, 'Incorrect input.\n/user_head + "user name"')

bot.polling(none_stop=True)
