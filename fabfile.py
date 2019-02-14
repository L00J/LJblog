from fabric.api import env,run,cd,local,task,abort
from fabric.colors import green,yellow,red
from fabric.context_managers import settings,hide
from fabric.contrib.console import confirm 

import datetime
nowTime=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

env.user = 'root'
env.port = '55555'
env.hosts = 'ops.attacker.club' #主机地址
env.key_filename = ['~/.ssh/id_rsa'] #本地秘钥



def get_git_status():
    git_status_result = local("git status", capture=True)
    #if "无文件要提交，干净的工作区" not in git_status_result:
    if "modified"  in git_status_result:
        print (red("当前分支还有文件没有提交"))
        print (git_status_result)
        abort("已经终止")

def local_unit_test():
    with settings(warn_only=True):
        test_result = local("python3 manage.py test")
        if test_result.failed:
            print (test_result)
            if not confirm(red("单元测试失败，是否继续？")):
                abort("已经终止")


def download_code():
    run("git checkout .")
    run("git pull")
    print(green("\n[%s] 完成代码下载" % env.hosts))

def app ():
    run("python3 manage.py collectstatic --noinput &&python3 manage.py migrate")
    run('''sed -i "/ALLOWED_HOSTS/c ALLOWED_HOSTS= \['127.0.0.1','.attacker.club'\]" mysite/settings.py ''' )
    run("sed -i 's#/data/LJblog#/www/django/blog#' mysite/settings.py")
    run("sed -i 's/DEBUG = True/DEBUG = False/' mysite/settings.py")
    run("/usr/bin/supervisord -c /etc/supervisor/supervisord.conf")
    print(green("\n[%s] app完成部署" % env.hosts))



@task
def upload():
    with settings(hide('running','stderr'), warn_only=True):
        local("git add .")
        local("git commit -m '%s 提交' " % (nowTime))
        local("git push")
        print(green("\n\n 完成代码上传"))


@task
def deploy():
    with settings(hide('running','stderr'), warn_only=True):
        with cd("/www/django/blog"):
            get_git_status()
            local_unit_test()
            run ("pkill sup")
            download_code()
            app()
            print(yellow("\n\n[%s] 部署完毕 !!!" % env.hosts))



@task
def ping ():
    with settings(hide('running','stderr'),warn_only=True):
        run("ping -c 1 114.114.114.114")

