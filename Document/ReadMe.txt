如何向git账号上提交代码

官方说明：https://help.github.com/articles/generating-ssh-keys/
博客说明：http://www.cnblogs.com/wangkongming/p/4158664.html

1，为Github账户设置SSH key

文章地址：http://zuyunfei.com/2013/04/10/setup-github-ssh-key/
什么是SSH key

一直使用SSH连接服务器，但是对它的原理却不太了解。这次设置Octopress的时候，需要使用SSH 方式连接Github, 正好对SSH的工作方式做了下了解。（好像Github推荐使用HTTPS的方式访问repo, 以前Github受到过SSH密匙攻击，之后升级了SSH key的安全措施，https方式视乎更方便安全，不过Octopress的设置文档中，我并没有找到怎么使用HTTPS连接Github）

简单来说，SSH提供了两种级别的安全验证：

    第一种级别是基于密码的安全验证，知道账号和密码，就可以登陆到远程主机。Team的开发工作中，就是使用这种方式登陆编译服务器，或者开发机器。因为是在内网中，这种级别的安全验证已经足够了。
    第二种级别是基于Public-key cryptography (公开密匙加密）机制的安全验证，原理如下图所示：

其优点在于无需共享的通用密钥，解密的私钥不发往任何用户。即使公钥在网上被截获，如果没有与其匹配的私钥，也无法解密，所截获的公钥是没有任何用处的。
产生SSH key

根据Github提供的help文档，具体过程如下


1 $ cd ~/.ssh
2 # Checks to see if there is a directory named ".ssh" in your user directory


使用ssh-keygen产生新的key


1 $ ssh-keygen -t rsa -C "your_email@example.com"
2 # Creates a new ssh key using the provided email
3 Generating public/private rsa key pair.
4 Enter file in which to save the key (/home/you/.ssh/id_rsa):


使用默认的文件名直接enter, 按提示输入密码（如果不提供密码，SSH将无密码连接，如果private key泄露可能会有安全问题）


1 Enter passphrase (empty for no passphrase): [Type a passphrase]
2 Enter same passphrase again: [Type passphrase again]


密匙产生成功

1 Your identification has been saved in /home/you/.ssh/id_rsa.
2 Your public key has been saved in /home/you/.ssh/id_rsa.pub.
3 The key fingerprint is:
4 01:0f:f4:3b:ca:85:d6:17:a1:7d:f0:68:9d:f0:a2:db your_email@example.com

上传public key到Github账户

    登录github
    点击右上方的Accounting settings图标
    选择 SSH key
    点击 Add SSH key

在出现的界面中填写SSH key的名称，填一个你自己喜欢的名称即可，然后将上面拷贝的~/.ssh/id_rsa.pub文件内容粘帖到key一栏，在点击“add key”按钮就可以了。
添加过程github会提示你输入一次你的github密码
设置SSH使用HTTPS的403端口

在局域网中SSH的22端口可能会被防火墙屏蔽，可以设置SSH使用HTTPS的403端口。

测试HTTPS端口是否可用


$ ssh -T -p 443 git@ssh.github.com
Hi username! You've successfully authenticated, but GitHub does not
provide shell access.


编辑SSH配置文件 ~/.ssh/config 如下:

  Host github.com
  Hostname ssh.github.com
  Port 443


测试是否配置成功

  $ ssh -T git@github.com
  Hi username! You've successfully authenticated, but GitHub does not
  provide shell access.

多个Github账号的SSH key切换:

如果在一台机器上要登陆多个Github账户，需要一些配置，虽然现在并没有用到，但是先记下来以备不时之需，过程参看这里。

 

2，【GitHub】解决每次push代码到github都需要输入用户名和密码的方法

在github上，建立一个项目test，去主页查看可以看到

 

如果使用HTTPS：

 
Create a new repository on the command line

touch README.md
git init
git add README.md
git commit -m "first commit"
git remote add origin https://github.com/guochy2012/test.git
git push -u origin master

Push an existing repository from the command line

git remote add origin https://github.com/guochy2012/test.git
git push -u origin master

 

 

如果采用SSH：


Create a new repository on the command line

touch README.md
git init
git add README.md
git commit -m "first commit"
git remote add origin git@github.com:guochy2012/test.git
git push -u origin master

Push an existing repository from the command line

git remote add origin git@github.com:guochy2012/test.git
git push -u origin master

 

 

使用HTTPS需要每次输入密码，SSH则不用，但SSH需要配置密钥 。

关于怎么产生密钥可以参见《Generating SSH Keys》一文

 

3，github地址 从https改成ssh

打开命令行工具，运行 git remote set-url origin 例如：
 
1
2 $ git remote set-url origin git@github.com:user/repo.git
3
4
	
然后再次 commit，如果出现类似：
 
1
2 Permission denied (publickey).
3
4
	
字样，那么说明你的 SSH key 没有设置或已经失效（譬如升级到 Mountain Lion 系统后），请重新参照上文的官方文档进行设置即可。

4，执行pull时报错

wangkongming@AY140527171808170503Z:~/github/collect$ git pull
Warning: Permanently added the RSA host key for IP address '192.30.252.130' to the list of known hosts.
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@ WARNING: UNPROTECTED PRIVATE KEY FILE! @
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
Permissions 0644 for '/home/wangkongming/.ssh/id_rsa' are too open.
It is recommended that your private key files are NOT accessible by others.
This private key will be ignored.
bad permissions: ignore key: /home/wangkongming/.ssh/id_rsa
Permission denied (publickey).
fatal: The remote end hung up unexpectedly

答案：http://stackoverflow.com/questions/1556119/ssh-private-key-permissions-using-git-gui-or-ssh-keygen-are-too-open

是因为给 id_rsa的权限太高了，改成700就可以了。也有人说600

You changed the permissions on the whole directory, which I agree with Splash is a bad idea. If you can remember what the original permissions for the directory are, I would try to set them back to that and then do the following

cd ~/.ssh
chmod 700 id_rsa

inside the .ssh folder. That will set the id_rsa file to rwx (read, write, execute) for the owner (you) only, and zero access for everyone else.

If you can't remember what the original settings are, add a new user and create a set of SSH keys for that user, thus creating a new .ssh folder which will have default permissions. You can use that new .ssh folder as the reference for permissions to reset your .ssh folder and files to.

If that doesn't work, I would try doing an uninstall of msysgit, deleting ALL .ssh folders on the computer (just for safe measure), then reinstalling msysgit with your desired settings and try starting over completely (though I think you told me you tried this already).

Edited: Also just found this link via Google -- Fixing "WARNING: UNPROTECTED PRIVATE KEY FILE!" on Linux While it's targeted at linux, it might help since we're talking liunx permissions and such.

 

======================================

以下是自己在使用git时，总结的：

1，查看当前项目远程分支的路径

git remote -v

2，查看项目所有分支 或当前所处分支

git branch -a　或 git branch -t

3，查看未提交修改(修改的文件和修改内容)：

git status / git diff

4，还原所有被修改的文件

git checkout .

５，添加commit内容后,注释信息需要重新修改：

git commit -n --amend
