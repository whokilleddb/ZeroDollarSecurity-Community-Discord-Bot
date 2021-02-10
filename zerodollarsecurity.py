import discord 
from discord.ext import commands
from better_profanity import profanity

TOKEN=""
GENERAL_ID=int(777585862124371988)
client=discord.Client()
PREFIX="!"

rules=["No mentors are to be contacted directly without permission. They can, however, mention them in the groups and ask their questions there.",
"Political discussions,  controversial topics, illegal and unethical dialogue are prohibited in the server. You can only have fun and share personal drama in the channels under 'Member Lounge', but within the boundaries of decency. Strict action shall be taken otherwise",
"No self-promotion or ads are to be shared in the server",
"Any form of abuse, racism, homophobia, discrimination or disrespect shown towards any community will result in a permanent ban without question.",
"If any test or assignment is provided, we expect honesty. You can ask for hints in the rooms under CTFs, in case we provide you with a CTF challenge. Cheating is prohibited. ",
"Make sure your words are clear cut and straight to the point. Unfortunately, we would not allow any other language except English. However, if you face difficulty with that, make sure you for permission to the community manager to express yourself in any language you deem comfortable."
"Distribution of illegally obtained materials within the server is not allowed.",
"Administrators have the right to change/add/deduct any rule later on.",
"Viruses and malware are not to be posted without explicit permission from the administrators themselves.",
"Spamming is prohibited, which includes repetitive texts or voice messages. You must not mislead others with malicious intent, especially in case of destruction of property. You can, however, get creative in the memes arena within ethical boundaries.",
"Do not take actions on any other members by yourself. That is the sole responsibility of the moderators. If you find any disturbing content from any individual on the server, make sure to contact and inform the moderators and they'll act accordingly. ",
"""Now, to familiarise with the system of our rooms. 

• #bot-commands - This room contains all the bot commands you'll need to use the bots in the server. You are only allowed to use them in the 'Members Lounge'(at the end). This rule must be followed.

• Under 'Learning', we'll be posting resources and materials relevant to the classes taken on a particular day and you'll be asking your doubts during a class in the room relevant to the topic. For example, if we are taking a class on Malware and you have a doubt, then you'll be posting your doubt in #malware room. 

• Under the CTF room, we'll be streaming live CTFs sometimes. You are free to join and take notes, but you won't be able to talk. It is only for viewing purposes. You can use the text channels for doubts regarding any CTF online. #zds-ctf is ZDS exclusive CTFs. 

• 'Community Text' will be the place for most of your discussions. We will be posting any relevant news or media postings on announcements (like our Youtube videos). We will post any general resources and study materials on #resources. You are free to converse with each other regarding any infosec topic or doubts first on #doubts channel. If it is not resolved there, then only you are liable to ask it on #cysec-talks. If we see that a particular doubt has not been asked in #doubts channel before, we have the right to refuse helping as you have not tried solving it by yourselves first (or in case of poor research). #advanced-topics is reserved for specific students who have shown more interest and enthusiasm than the rest and will be able to ask their doubts directly there for the administrators. 

• Under 'Community Voice', #topics-discussion is for you to solve your doubts via voice chat while #lounge is for relaxing. You can use the bot Groovy here. 

• 'Members Lounge' is for your enjoyment, exchange and networking. Use the channel names to figure out the relevant things you can do there.
"""]

@client.event
async def on_ready():
    general_channel=client.get_channel(GENERAL_ID)
    await general_channel.send("Zero Dollar Security Bot Is Live !")
    print("BOT IS LIVE !")
    

@client.event
async def on_member_join(member):
    general_channel=client.get_channel(GENERAL_ID)
    guild=member.guild
    message ='Hi {} ! '.format(member.mention)
    await general_channel.send(message)

@client.event
async def on_message(message):
	print(message)
	channel_name=client.get_channel(message.channel.category_id)
	if profanity.contains_profanity(message.content) :
		await message.delete()
		my_embed = discord.Embed(title="YOU HAVE BEEN BANNED", color=0xff0000)
		my_embed.add_field(name="Reason : ",value="Profane Language",inline=True)
		my_embed.set_footer(text="Please Contact A Moderator !")
		await message.channel.send(embed=my_embed)
		await message.guild.ban(message.author,reason="Profane Language")
	else :
		if message.author != client.user :
			text=message.content.lower()
			if text == "!rules" and len(text)==6:
				await message.channel.send("Server Rules")
				for i in range(len(rules)) : 
					await message.channel.send(f"Rule {i+1} : {rules[i]}\n")
			if text[:5]=="!rule" :
				id=text[5:]
				try :
					if(int(id))>0 and (int(id))< 13 :
						await message.channel.send(f"Rule {id} : {rules[int(id)-1]}")
				except ValueError :
					pass
        
client.run(TOKEN)
