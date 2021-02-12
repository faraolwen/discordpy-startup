"""
from discord.ext import commands
import os
import traceback

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']


@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)


@bot.command()
async def ping(ctx):
    await ctx.send('pong')


bot.run(token)
"""
myth="""1 Alrund, God of the Cosmos (KHM) 40
1 Alrund, God of the Cosmos (KHM) 40
1 Orvar, the All-Form (KHM) 70
1 Resplendent Marshal (KHM) 22
1 Halvar, God of Battle (KHM) 15
1 Starnheim Unleashed (KHM) 33
1 Alrund's Epiphany (KHM) 41
1 Valki, God of Lies (KHM) 114
1 Esika, God of the Tree (KHM) 168
1 Quakebringer (KHM) 145
1 Goldspan Dragon (KHM) 139
1 Toralf, God of Fury (KHM) 154
1 Haunting Voyage (KHM) 98
1 Burning-Rune Demon (KHM) 81
1 Eradicator Valkyrie (KHM) 94
1 Tyvar Kell (KHM) 198
1 Battle Mammoth (KHM) 160
1 Vorinclex, Monstrous Raider (KHM) 199
1 Niko Aris (KHM) 225
1 Kaya the Inexorable (KHM) 218
1 Koma, Cosmos Serpent (KHM) 221""".split("\n")
rare="""1 Rally the Ranks (KHM) 20
1 Reidane, God of the Worthy (KHM) 21
1 Righteous Valkyrie (KHM) 24
1 Runeforge Champion (KHM) 26
1 Search for Glory (KHM) 27
1 Sigrid, God-Favored (KHM) 29
1 Glorious Protector (KHM) 12
1 Graven Lore (KHM) 61
1 Cosmos Charger (KHM) 51
1 Cosima, God of the Voyage (KHM) 50
1 Mystic Reflection (KHM) 69
1 Ascendant Spirit (KHM) 43
1 Rise of the Dread Marn (KHM) 107
1 Doomskar (KHM) 9
1 Reflections of Littjara (KHM) 73
1 Cyclone Summoner (KHM) 52
1 Dream Devourer (KHM) 90
1 Icebreaker Kraken (KHM) 63
1 Skemfar Avenger (KHM) 109
1 Egon, God of Death (KHM) 92
1 Varragoth, Bloodsky Sire (KHM) 115
1 Crippling Fear (KHM) 82
1 Draugr Necromancer (KHM) 86
1 Tergrid, God of Fright (KHM) 112
1 Blood on the Snow (KHM) 79
1 Calamity Bearer (KHM) 125
1 Tundra Fumarole (KHM) 156
1 Birgi, God of Storytelling (KHM) 123
1 Arni Brokenbrow (KHM) 120
1 Tibalt's Trickery (KHM) 153
1 Magda, Brazen Outlaw (KHM) 142
1 Dragonkin Berserker (KHM) 131
1 Reckless Crew (KHM) 146
1 Elvish Warmaster (KHM) 167
1 In Search of Greatness (KHM) 177
1 Jorn, God of Winter (KHM) 179
1 Old-Growth Troll (KHM) 185
1 Realmwalker (KHM) 188
1 Blessing of Frost (KHM) 161
1 Esika's Chariot (KHM) 169
1 Kolvori, God of Kinship (KHM) 181
1 Toski, Bearer of Secrets (KHM) 197
1 Hengegate Pathway (KHM) 260
1 The Raven's Warning (KHM) 227
1 Darkbore Pathway (KHM) 254
1 Immersturm Predator (KHM) 214
1 The Bloodsky Massacre (KHM) 207
1 Blightstep Pathway (KHM) 252
1 Battle of Frost and Fire (KHM) 204
1 King Narfi's Betrayal (KHM) 219
1 Firja's Retribution (KHM) 210
1 Sarulf, Realm Eater (KHM) 228
1 Harald Unites the Elves (KHM) 213
1 Waking the Trolls (KHM) 234
1 Showdown of the Skalds (KHM) 229
1 Battle for Bretagard (KHM) 203
1 Barkchannel Pathway (KHM) 251
1 The Bears of Littjara (KHM) 205
1 The World Tree (KHM) 275
1 Faceless Haven (KHM) 255
1 Tyrite Sanctum (KHM) 272
1 Pyre of Heroes (KHM) 241
1 Cosmos Elixir (KHM) 237
1 Maskwood Nexus (KHM) 240""".split("\n")
unc="""1 Spectral Steel (KHM) 30
1 Usher of the Fallen (KHM) 35
1 Rune of Sustenance (KHM) 25
1 Divine Gambit (KHM) 8
1 Colossal Plow (KHM) 236
1 Clarion Spirit (KHM) 6
1 Shepherd of the Cosmos (KHM) 28
1 Kaya's Onslaught (KHM) 18
1 Battershield Warrior (KHM) 2
1 Valkyrie's Sword (KHM) 36
1 Frost Augur (KHM) 56
1 Giant's Amulet (KHM) 59
1 Avalanche Caller (KHM) 45
1 Glimpse the Cosmos (KHM) 60
1 Rune of Flight (KHM) 75
1 Icebind Pillar (KHM) 62
1 Saw It Coming (KHM) 76
1 Inga Rune-Eyes (KHM) 64
1 Frostpyre Arcanist (KHM) 58
1 Bloodsky Berserker (KHM) 80
1 Draugr's Helm (KHM) 88
1 Rune of Mortality (KHM) 108
1 Return Upon the Tide (KHM) 106
1 Vengeful Reaper (KHM) 116
1 Skemfar Shadowsage (KHM) 110
1 Hailstorm Valkyrie (KHM) 97
1 Poison the Cup (KHM) 103
1 Tergrid's Shadow (KHM) 113
1 Dual Strike (KHM) 132
1 Fearless Liberator (KHM) 135
1 Frenzied Raider (KHM) 137
1 Rune of Speed (KHM) 148
1 Crush the Weak (KHM) 128
1 Dwarven Hammer (KHM) 133
1 Basalt Ravager (KHM) 122
1 Provoke the Trolls (KHM) 144
1 Doomskar Titan (KHM) 130
1 Boreal Outrider (KHM) 163
1 Rune of Might (KHM) 191
1 Path to the World Tree (KHM) 186
1 Fynn, the Fangbearer (KHM) 170
1 Elven Bow (KHM) 166
1 Blizzard Brawl (KHM) 162
1 Littjara Glade-Warden (KHM) 182
1 Spirit of the Aldergard (KHM) 195
1 Rootless Yew (KHM) 189
1 Gates of Istfell (KHM) 256
1 Niko Defies Destiny (KHM) 226
1 Vega, the Watcher (KHM) 233
1 Great Hall of Starnheim (KHM) 259
1 Ascent of the Worthy (KHM) 202
1 Firja, Judge of Valor (KHM) 209
1 Port of Karfell (KHM) 265
1 The Trickster-God's Heist (KHM) 232
1 Narfi, Betrayer King (KHM) 224
1 Skemfar Elderhall (KHM) 268
1 Kardur's Vicious Return (KHM) 217
1 Kardur, Doomscourge (KHM) 216
1 Immersturm Skullcairn (KHM) 263
1 Aegar, the Freezing Flame (KHM) 200
1 Invasion of the Giants (KHM) 215
1 Surtland Frostpyre (KHM) 271
1 Harald, King of Skemfar (KHM) 212
1 Binding the Old Gods (KHM) 206
1 Gnottvold Slumbermound (KHM) 258
1 Arni Slays the Troll (KHM) 201
1 Svella, Ice Shaper (KHM) 230
1 Axgard Armory (KHM) 250
1 Koll, the Forgemaster (KHM) 220
1 Forging the Tyrite Sword (KHM) 211
1 Bretagard Stronghold (KHM) 253
1 Fall of the Impostor (KHM) 208
1 Maja, Bretagard Protector (KHM) 222
1 Littjara Mirrorlake (KHM) 264
1 Weathered Runestone (KHM) 247
1 Bloodline Pretender (KHM) 235
1 Replicating Ring (KHM) 244
1 Runed Crown (KHM) 245
1 The Three Seasons (KHM) 231
1 Moritte of the Frost (KHM) 223""".split("\n")
common="""1 Battlefield Raptor (KHM) 3
1 Codespell Cleric (KHM) 7
1 Valor of the Worthy (KHM) 37
1 Wings of the Cosmos (KHM) 39
1 Beskir Shieldmate (KHM) 4
1 Giant Ox (KHM) 11
1 Revitalize (KHM) 23
1 Starnheim Courser (KHM) 32
1 Iron Verdict (KHM) 17
1 Invoke the Divine (KHM) 16
1 Goldmaw Champion (KHM) 14
1 Doomskar Oracle (KHM) 10
1 Bound in Gold (KHM) 5
1 Story Seeker (KHM) 34
1 Axgard Braggart (KHM) 1
1 Stalwart Valkyrie (KHM) 31
1 Master Skald (KHM) 19
1 Warhorn Blast (KHM) 38
1 Gods' Hall Guardian (KHM) 13
1 Annul (KHM) 42
1 Bind the Monster (KHM) 48
1 Brinebarrow Intruder (KHM) 49
1 Depart the Realm (KHM) 53
1 Disdainful Stroke (KHM) 54
1 Karfell Harbinger (KHM) 65
1 Mists of Littjara (KHM) 67
1 Pilfering Hawk (KHM) 71
1 Strategic Planning (KHM) 77
1 Littjara Kinseekers (KHM) 66
1 Frostpeak Yeti (KHM) 57
1 Behold the Multiverse (KHM) 46
1 Augury Raven (KHM) 44
1 Ravenform (KHM) 72
1 Mistwalker (KHM) 68
1 Draugr Thought-Thief (KHM) 55
1 Berg Strider (KHM) 47
1 Run Ashore (KHM) 74
1 Undersea Invader (KHM) 78
1 Duskwielder (KHM) 91
1 Village Rites (KHM) 117
1 Weigh Down (KHM) 118
1 Deathknell Berserker (KHM) 83
1 Demonic Gifts (KHM) 84
1 Elderfang Disciple (KHM) 93
1 Priest of the Haunted Edge (KHM) 104
1 Raise the Draugr (KHM) 105
1 Withercrown (KHM) 119
1 Grim Draugr (KHM) 96
1 Infernal Pet (KHM) 99
1 Karfell Kennel-Master (KHM) 101
1 Skull Raid (KHM) 111
1 Jarl of the Forsaken (KHM) 100
1 Draugr Recruiter (KHM) 87
1 Feed the Serpent (KHM) 95
1 Dogged Pursuit (KHM) 85
1 Koma's Faithful (KHM) 102
1 Dread Rider (KHM) 89
1 Fearless Pup (KHM) 136
1 Frost Bite (KHM) 138
1 Tormentor's Helm (KHM) 155
1 Axgard Cavalry (KHM) 121
1 Immersturm Raider (KHM) 141
1 Run Amok (KHM) 147
1 Vault Robber (KHM) 158
1 Breakneck Berserker (KHM) 124
1 Demon Bolt (KHM) 129
1 Open the Omenpaths (KHM) 143
1 Seize the Spoils (KHM) 149
1 Shackles of Treachery (KHM) 150
1 Tuskeri Firewalker (KHM) 157
1 Craven Hulk (KHM) 127
1 Dwarven Reinforcements (KHM) 134
1 Smashing Success (KHM) 151
1 Hagi Mob (KHM) 140
1 Squash (KHM) 152
1 Cinderheart Giant (KHM) 126
1 Jaspera Sentinel (KHM) 178
1 Broken Wings (KHM) 164
1 Sculptor of Winter (KHM) 193
1 Roots of Wisdom (KHM) 190
1 Masked Vandal (KHM) 184
1 Guardian Gladewalker (KHM) 174
1 Arachnoform (KHM) 159
1 Snakeskin Veil (KHM) 194
1 Glittering Frost (KHM) 171
1 Gnottvold Recluse (KHM) 172
1 Horizon Seeker (KHM) 175
1 Icehide Troll (KHM) 176
1 King Harald's Revenge (KHM) 180
1 Mammoth Growth (KHM) 183
1 Elderleaf Mentor (KHM) 165
1 Goldvein Pick (KHM) 239
1 Funeral Longboat (KHM) 238
1 Ravenous Lindwurm (KHM) 187
1 Grizzled Outrider (KHM) 173
1 Struggle for Skemfar (KHM) 196
1 Sarulf's Packmate (KHM) 192
1 Raven Wings (KHM) 243
1 Raiders' Karve (KHM) 242
1 Scorn Effigy (KHM) 246""".split("\n")
land="""1 Shimmerdrift Vale (KHM) 267
1 Glacial Floodplain (KHM) 257
1 Snowfield Sinkhole (KHM) 269
1 Ice Tunnel (KHM) 262
1 Volatile Fjord (KHM) 273
1 Sulfurous Mire (KHM) 270
1 Woodland Chasm (KHM) 274
1 Highland Forest (KHM) 261
1 Rimewood Falls (KHM) 266
1 Arctic Treeline (KHM) 249
1 Alpine Meadow (KHM) 248
1 Snow-Covered Forest (KHM) 285
1 Snow-Covered Forest (KHM) 284
1 Snow-Covered Mountain (KHM) 283
1 Snow-Covered Mountain (KHM) 282
1 Snow-Covered Plains (KHM) 276
1 Snow-Covered Plains (KHM) 277
1 Snow-Covered Island (KHM) 278
1 Snow-Covered Island (KHM) 279
1 Snow-Covered Swamp (KHM) 280
1 Snow-Covered Swamp (KHM) 281""".split("\n")
import random
from math import factorial as fact
def popen():
    pack=[]
    for x in [rare,myth,common,land,unc]:
        random.shuffle(x)
    random
    if random.random()>1/7.4:
        pack+=rare[:1]
    else:
        pack+=myth[:1]
    pack+=unc[:3]
    pack+=common[:10]
    pack+=land[:1]
    return(pack)

def c(n,m):
    if n-m<0:
        return 0
    return fact(n)/fact(m)/fact(n-m)


# インストールした discord.py を読み込む
import discord

# 自分のBotのアクセストークンに置き換えてください
TOKEN = 'ODA5Mzc3ODgzNDgzMDEzMTQx.YCUN5A.5bA24b5TLPMxLzYT5BIJdR7s6Co'

# 接続に必要なオブジェクトを生成
client = discord.Client()

# 起動時に動作する処理
@client.event
async def on_ready():
    # 起動したらターミナルにログイン通知が表示される
    print('ログインしました')

# メッセージ受信時に動作する処理
@client.event
async def on_message(message):
    # メッセージ送信者がBotだった場合は無視する
    if message.author.bot:
        return
    if message.content == '!khmseald':
        await message.channel.send('Deck')
        for _ in range(2):
            await message.channel.send('\n'.join(popen()+popen()+popen()))
    if "!comp" in message.content:
        await message.channel.send(eval(message.content.split()[1]))
    if "!range" in message.content:
        _,ran,com = message.content.split()
        res=[]
        a,b = list(map(int,ran.split("to")))
        for i in range(a,b+1):
            res.append(str(i)+" "+str(eval(com.replace("x",str(i)))))
        await message.channel.send("\n".join(res))




# Botの起動とDiscordサーバーへの接続
client.run(TOKEN)
