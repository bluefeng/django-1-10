#!/usr/bin/env python
import os
import sys
import traceback
import configparser
import platform
CurDir = os.path.dirname(os.path.abspath(__file__))
NginxInfo = """
server {{
    listen 80;

    server_name www.iwill.fun iwill.fun; 
    charset UTF-8;

    location / {{
        {0}
    }}
    location /static/ {{
        expires 30d;
        autoindex off; 
        add_header Cache-Control private;
        alias {1};
    }}
    # end mipush 
}}
"""

def isDebugSys():
	return 'Linux' not in platform.system()

#修改 ini 路径
def refreshIniDir():
	cfg = configparser.ConfigParser()
	cfg.read('uwsgi.ini')
	chdir = cfg.get('uwsgi', 'chdir')
	if CurDir != chdir :
		cfg.set("uwsgi", "chdir", CurDir)
		cfg.set("uwsgi", "home", os.path.join(os.path.dirname(CurDir), "py_env/django_1_10"))
		with open('uwsgi.ini', 'w') as f :
			cfg.write(f)
			f.close()




def refreshNginxInfo():
	serverInfo = NginxInfo.format("""
		include uwsgi_params;
        uwsgi_pass 127.0.0.1:8000;
        uwsgi_connect_timeout 30;
		""", os.path.join(CurDir, 'static/'))
	with open('nginx.conf', 'w') as f :
		f.write(serverInfo)
		f.close()
		
def refreshNginxInfoWin():
	serverInfo = NginxInfo.format("proxy_pass http://127.0.0.1:8000;" 
		, os.path.join(CurDir, 'static/'))
	with open('nginx.conf', 'w') as f :
		f.write(serverInfo)
		f.close()


if __name__ == "__main__":
	if isDebugSys() :
		refreshNginxInfoWin()
		os.system('python manage.py runserver --setting blogproject.settings.local')
	else:
		try:
			if sys.argv[1] == "start" :
				refreshIniDir()
				refreshNginxInfo()
				os.system('python manage.py collectstatic --setting blogproject.settings.production')
				os.system('uwsgi --ini uwsgi.ini')
			elif sys.argv[1] == "stop" :
				os.system('uwsgi --stop uwsgi/uwsgi.pid')
			elif sys.argv[1] == "reload" :
				os.system('uwsgi --reload uwsgi/uwsgi.pid')
			elif sys.argv[1] == "status" :
				a = os.popen('uwsgi --connect-and-read uwsgi/uwsgi.status')
				print(a.read())
			else:
				raise
		except:
			#traceback.print_exc()
			print(
				"""
				command:
					start 			--开启 uwsgi  
					stop  			--关闭 uwsgi
					reload 			--重启 uwsgi
					status			--uwsgi状态查询

					stop reload 失败可以手动查询status 更改uwsgi/uwsgi.pid
				"""
				)
	