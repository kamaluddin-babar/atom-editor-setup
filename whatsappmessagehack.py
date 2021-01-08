import pywhatkit
count = 0
hour = 9
min = 2
rashed = 'Kashmir is the northernmost geographical region of the Indian subcontinent. Until the mid-19th century, the term "Kashmir" denoted only the Kashmir Valley between the Great Himalayas and the Pir Panjal Range. Today, the term encompasses a larger area that includes the Indian-administered territories of Jammu and Kashmir and Ladakh, the Pakistani-administered territories of Azad Kashmir and Gilgit-Baltistan, and Chinese-administered territories of Aksai Chin and the Trans-Karakoram Tract.'
while count <14:
    pywhatkit.sendwhatmsg('+8801816159700', rashed, hour, min)
    count = count +1
    min = min + 4
