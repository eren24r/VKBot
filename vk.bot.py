@bot.message_handler(commands=['id_users'])
def cld(message):
	a = bot.send_message(message.chat.id, "send user id")
	bot.register_next_step_handler(a, get_usid)

@bot.message_handler(content_types=['text'])
def get_usid(message):
	my_tokenn = 'vk1.a.xi_kJmomSCaUnbo0uwSaGOdF69QQGNjKDxbIYs0ortJrofiJeoUoI0W5j77FvbTV14XwvL0amwMjn2ExWrDeZV_7JhZxLIylp3668qRTLo7zZf5xC5CDgNybxsFQSgTHteECo5YkGfLdKEZ74ArSf55Tqom_M-KY1dHTmnz-MrFhXxpHAke2PjH0YwhVVeST'
	try:
		session = vk_api.VkApi(token = my_tokenn)
		vk = session.get_api()
		uinfo = vk.users.get()
		uinfo = vk.users.get(user_ids=int(message.text),fields='bdate,about,counters,domain,sex')
		bot.send_message(message.chat.id, "VK token connected!")
		infou1 = ""
		infou1 = "id_user: " + str(uinfo[0]['id']) + "\n" + "name: " + str(uinfo[0]['first_name']) + " " + str(uinfo[0]['last_name']) + "\n" + "Date of Birthday: " + str(uinfo[0]['bdate']) + "\n"
		sx = ""
		if uinfo[0]['sex'] == 2:
			sx = "М"
		if uinfo[0]['sex'] == 1:
			sx = "Ж"
		if uinfo[0]['sex'] == 0:
			sx = "Na"
		infou2 = ""
		infou2 = "About: " + str(uinfo[0]['about']) + "\n" + "Sex: " + sx + "\n" + "Domain: " + str(uinfo[0]['domain']) + "\n"
		infou3 = ""
		infou3 = "albums: "	+ str(uinfo[0]['counters']['albums']) + "\n" + "photos: " + str(uinfo[0]['counters']['photos']) + "\n" + "videos: " + str(uinfo[0]['counters']['videos']) + "\n"
		infou4 = ""
		infou4 = "followers: " + str(uinfo[0]['counters']['followers']) + "\n" + "subscriptions: " + str(uinfo[0]['counters']['subscriptions']) + "\n" + "friends: " + str(uinfo[0]['counters']['friends']) + "\n"
		infou5 = ""
		infou5 = "groups: " + str(uinfo[0]['counters']['groups']) + "\n" + "audios: " + str(uinfo[0]['counters']['audios']) + "\n" + "user_photo: " + str(uinfo[0]['counters']['user_photos'])

		bot.send_message(message.chat.id, "Info:")
		bot.send_message(message.chat.id, str(infou1 + infou2 + infou3))
		bot.send_message(message.chat.id, "Counters:")
		bot.send_message(message.chat.id, str(infou4 + infou5))
		
		bot.send_message(message.chat.id, f"This account has got {vk.photos.getAll(owner_id=int(message.text))['count']} photos!")
		for i in vk.photos.getAll(owner_id=int(message.text))['items']:
			st = ""
			st = str(time.strftime("%H:%M:%S, %d.%B.%Y", time.gmtime(i['date'])))
			scm = ""
			scm = st + "\n" + "id_owner: " + str(i['owner_id']) + "\n" + "id_user: " + str(uinfo[0]['id']) + "\n" + "name: " + str(uinfo[0]['first_name']) + " " + str(uinfo[0]['last_name']) + "\n" "Text: " + str(i['text']) + "\n" + str(i['sizes'][len(i['sizes']) - 1]['url']) 
			bot.send_message(message.chat.id, str(scm))

	except:
		bot.send_message(message.chat.id, "Token Connection Eror! Send me again!")