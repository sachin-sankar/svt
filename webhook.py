from discord_webhook import DiscordWebhook, DiscordEmbed

fileWebHookUrl = 'https://discord.com/api/webhooks/1118384790245216326/ST3L9-YLhn447LB1NTQAjguXaHGWX1EvzcmAGgKEXUfdt5bGQuotq4UYLvPNpEaJewxF'
notifyWebHookUrl = 'https://discord.com/api/webhooks/1118392177207287858/KvzG4E_nlIfeVaXtRHL5Nm3XUZRy6CjAkU0hjdrJp4-mHFamkG-BSVhdPXiFNJclJKOa'
userName = 'Viswa Cars Backend'



def sendError(fields):
  webhook = DiscordWebhook(url=notifyWebHookUrl,username=userName,avatar_url='https://upload.wikimedia.org/wikipedia/commons/thumb/6/62/Solid_red.svg/512px-Solid_red.svg.png?20150316143248')
  embed = DiscordEmbed('System Error Notification','The following system error has occured.',color='FF0000')
  for i in fields.items():
    embed.add_embed_field(i[0],i[1],False)
  webhook.add_embed(embed)
  webhook.execute()

def sendBackup():
  webhook = DiscordWebhook(url=fileWebHookUrl,username=userName,content='Scheduled Backup System')
  with open("svt.db", "rb") as f:
      webhook.add_file(file=f.read(), filename='svt.db')
  r = webhook.execute()
  if r.status_code != 200:
    sendError({'Error Type':'HTTP Error','Error Code':str(r.status_code),'Error Impact':'Failure of scheduled Backup'})