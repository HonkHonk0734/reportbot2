from openpyxl import load_workbook
import discord
from discord.ext import commands
import datetime as dt


Token = 'ODg4MDYxNjQ4OTA3MTQ5MzMz.YUNN3A.obsdIOAfqFcCnFINdvdz47nR7MY'

wb = load_workbook('reported.xlsx')
ws = wb.active
ws.title = "reports"
client = discord.Client()

bot = commands.Bot(command_prefix='!')

@bot.command(pass_context=True)
async def clear(ctx, amount=100):
    channel = ctx.message.chanel
    messages = []
    async for message in client.logs_from(channel, limit=int(amount)):
        messages.append(message)
    await client.delete_messages(messages)



class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))


    async def on_message(self, message):
        print('Message from {0.author}: {0.content}'.format(message))

    async def on_message(self, message):
        args = message.content.split(" ")
        if args[0] == "!report":
            argument_length = len(args)
            if argument_length < 2:
                await message.channel.send('you need to specify a reason and a user like !report <user> <reason>')
            else:
                await message.channel.send('Making a report...')
                mentiond_user = args[1]
                print(mentiond_user)
                print(type(mentiond_user))
                if len(mentiond_user) != 22:
                    await message.channel.send('this is not a valid user')
                else:
                    reason_list = args[2:]
                reason_string = ' '.join(reason_list)
                current_date = dt.date.today()
                string_date = current_date.strftime('%Y-%m-%d')
                print(mentiond_user)
                print(reason_string)
                print(string_date)
                report = []
                report.append(mentiond_user)
                report.append(reason_string)
                report.append(string_date)
                ws.append(report)
                wb.save('test.xlsx')
                channel = client.get_channel(889217065083346965)
                print(mentiond_user)
                await channel.send('a new report has been made.\n'
                                   'The accused is: ' + mentiond_user + "\n"
                                   "The discription of the report is: " + reason_string + ".\n"
                                   "and the date that is was made was: " + string_date + ".")
                await message.author.send('Your report has been send wait for the moderators to review it')
                await message.channel.send('report has been made')

@bot.command()
async def displayembed():
    print('embed')
    embed = discord.Embed(
        title='Title',
        description="this is a discription",
    )

    embed.set_footer(text="this is an footer")
    embed.set_image(url='https://i.imgur.com/KiaZybi.png')
    embed.set_thumbnail(url='https://i.imgur.com/KiaZybi.png')
    embed.set_thumbnail(url='Honkhonk0734',
                        icon_url='https://cdn.discordapp.com/avatars/710433019407761498/751a3443d2c2d8cc2c5744acecc2132a.webp?size=128')
    embed.add_field(name='Fieldname', value="field value", inline=False)
    embed.add_field(name='Fieldname', value="field value", inline=True)
    embed.add_field(name='Fieldname', value="field value", inline=True)

    await client.say(embed=embed)



wb.save('reported.xlsx')
client = MyClient()
client.run(Token)