# 博客
##博客介绍
* 基于django1.10的博客系统
* 博客地址: [BlueFeng丨羽枫的博客](http://www.iwill.fun)
* 使用python3.x运行

##开发运行环境搭建
1. 克隆项目（确认已经安装好git）
2. cd 到 存放项目的目录，打开命令行输入： 
	
	`git clone https://github.com/bluefeng/django-1-10.git`
	 
3. 确认已经安装 python3.x 版本，以及pip，以及mysql，自行到blogproject/settings 设置数据库信息，因为用到的python包比较多，建议使用virtualenv管理虚拟环境， 使用pip 安装 virtualenv
4. 安装完成以后使用 virtuallenv 建立虚拟环境，到项目同级目录新建py_env文件夹，在文件夹内运行：  

	`virtualenv django_1_10 `  
	
	如果电脑上有 多个python 版本 可以使用 -p 置顶版本 如：
	
	`virtualenv django_1_10 -p python3`

	完成以后需要激活虚拟环境
	
	```
	#windows
	django_1_10\Scripts\activate
	
	#linux mac
	source django_1_10/bin/activate
	```
	这时 命令行前面会有（`django_1_10`）的标志 表示成功进入虚拟环境  
	
	退出虚拟环境运行:
	
	```
	#windows
	django_1_10\Scripts\deactivate
	
	#linux
	deactivate
	
	```
	
5. 在虚拟环境内安装项目需要的python包 （先激活虚拟环境）在项目文件夹下运行：  
	
	`pip install -r requirements/local.txt`
  
6. 迁移数据库

    ```
   python manage.py makemigrations --settings=blogproject.settings.local
   ```
   在上一步所在的位置运行如下命令迁移数据库：

   ```
   python manage.py migrate --settings=blogproject.settings.local
   ```

7. 创建后台管理员账户

   在上一步所在的位置运行如下命令创建后台管理员账户

   ```
   python manage.py createsuperuser --settings=blogproject.settings.local
   ```

8. 运行开发服务器

   在上一步所在的位置运行如下命令开启开发服务器：

   ```
   python manage.py runserver --settings=blogproject.settings.local
   ```

   在浏览器输入：127.0.0.1:8000

9. 进入后台发布文章

   在浏览器输入：127.0.0.1:8000/admin

   使用第 5 步创建的后台管理员账户登录
  
##生产运行环境
生产运行环境和开发运行环境大同小异，需要安装nginx配合运行，需要将static文件收集到一起，详见 根目录下ctr.py 的快捷命令 
