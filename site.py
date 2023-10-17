from pywebcopy import save_webpage, save_website
from pywebcopy.configs import get_config
import validators

token = 'vk1.a.xi_kJmomSCaUnbo0uwSaGOdF69QQGNjKDxbIYs0ortJrofiJeoUoI0W5j77FvbTV14XwvL0amwMjn2ExWrDeZV_7JhZxLIylp3668qRTLo7zZf5xC5CDgNybxsFQSgTHteECo5YkGfLdKEZ74ArSf55Tqom_M-KY1dHTmnz-MrFhXxpHAke2PjH0YwhVVeST'

def send(msg):
		vk.messages.send(user_id = 741770870, message = msg, random_id = 0)

def website(url, folder, name):
	save_website(
		url=url,
		project_folder=folder,
		project_name=name,
		bypass_robots=True,
		debug=True,
		open_in_browser=True,
		delay=None,
		threaded=False,
  )

config = get_config('https://vk.com/')
wp = config.create_page()
wp.get(config['project_url'])
form = wp.get_forms()[1]
form.inputs['email'].value = 'nemadzonrahmatov2004@mail.ru' # etc
form.inputs['pass'].value = 'No10no20no30' # etc
wp.submit_form(form)
print(wp.get_links())




url = 'https://vk.com/eren24r'
download_folder = '/site/'    

kwargs = {'bypass_robots': True, 'project_name': 'site_vk'}

save_webpage(url, download_folder, **kwargs)