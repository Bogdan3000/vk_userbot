import vk_api
import time

vk = vk_api.VkApi(token='your own token to control profile')
vk.get_api()

wait = 0.8
long_wait = 1.5

owner_id = 'Your profile id'

exmark = '&#10071;'   #Воскл. знак

smile = '&#128522;'   #Улыбающийся
wink = '&#128521;'    #Подмигивающий

sad = '&#128546;'     #Грусный
crying = '&#128557;'  #Плачущий

normal = '&#128528;'  #Нормальный
bigeyes = '&#128563;' #Большеглазый

cat_sad = '&#128575;' #Кот грусный
cat_fun = '&#128569;' #Кот смешньй
cat_love = '&#128571;'#Кот с сердечками
cat_wow = '&#128576;' #Кот с белыми глазами



def edit(peer_id, msg, msg_id):
	vk.method('messages.edit', {
	'peer_id': peer_id,
	'message': msg,
	'message_id': msg_id})
  
def get_msgs():
  return 	vk.method('messages.getConversations', {'filter': 'all', 'count': 3})
  
print('Userbot v1')

while True:
  msgs = get_msgs()
	for i in msgs['items']:

		from_id = i['last_message']['from_id']
		peer_id = i['last_message']['peer_id']
		text = i['last_message']['text']
		full_msg = text
		msg_id = i['last_message']['id']
		fun = ''
		if text == 'stop':
			edit(peer_id, exmark+'Userbot stopped'+exmark, msg_id)
			time.sleep(wait)
			sys.exit()
		elif text[0:5] == 'slide' and from_id == owner_id:
			text = text[6:]
			for i in text:
				fun += i
				try:
					edit(peer_id, fun, msg_id)
					time.sleep(wait)
				except:
					break
		elif text[0:6] == 'scroll' and from_id == owner_id:
			text = text[7:]
			text = text[::-1]
			err = False
			for i in text:
				fun = i + fun
				try:
					edit(peer_id, fun, msg_id)
					time.sleep(wait)
				except:
					print('Complete capcha')
					err = True
					break
			if not err:
				text = text[::-1]
				for i in range(1, len(text)):
					try:
						edit(peer_id, text[:i-i-i], msg_id)
						time.sleep(wait)
					except:
						print('Complete capcha')
						break
				edit(peer_id, full_msg[7:], msg_id)

		elif text == 'warning' and from_id == owner_id:
			for i in range(4):
				try:
					edit(peer_id, exmark+'Warning, warning'+exmark, msg_id)
					time.sleep(long_wait)
					edit(peer_id, exmark+'Important information'+exmark, msg_id)
					time.sleep(long_wait)
				except:
					print('Введите капчу')
					break
		elif text == 'post' and from_id == owner_id:
			for i in range(4):
				try:
					edit(peer_id, exmark+'Warning, warning'+exmark, msg_id)
					time.sleep(long_wait)
					edit(peer_id, exmark+'New post'+exmark, msg_id)
					time.sleep(long_wait)
				except:
					print('Complete capcha')
					break
		elif text == 'wink' and from_id == owner_id:
			for i in range(4):
				try:
					edit(peer_id, smile, msg_id)
					time.sleep(wait)
					edit(peer_id, wink, msg_id)
					time.sleep(wait)
				except:
					print('Complete capcha')
					break
		elif text == 'rain' and from_id == owner_id:
			for i in range(4):
				try:
					edit(peer_id, sad, msg_id)
					time.sleep(wait)
					edit(peer_id, crying, msg_id)
					time.sleep(wait)
				except:
					print('Complete capcha')
					break
		elif text == 'bigeyes' and from_id == owner_id:
			for i in range(4):
				try:
					edit(peer_id, normal, msg_id)
					time.sleep(wait)
					edit(peer_id, bigeyes, msg_id)
					time.sleep(wait)
				except:
					print('Complete capcha')
					break
		elif text == 'catty' and from_id == owner_id:
			for i in range(3):
				try:
					edit(peer_id, cat_sad, msg_id)
					time.sleep(wait)
					edit(peer_id, cat_fun, msg_id)
					time.sleep(wait)
					edit(peer_id, cat_love, msg_id)
					time.sleep(wait)
				except:
					print('Complete capcha')
					break
		elif text == 'catwow' and from_id == owner_id:
			for i in range(4):
				try:
					edit(peer_id, cat_wow, msg_id)
					time.sleep(wait)
					edit(peer_id, cat_love, msg_id)
					time.sleep(wait)
				except:
					print('Complete capcha')
					break
	time.sleep(0.1)
  
  
  
