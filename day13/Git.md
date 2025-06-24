# Git

Git 是目前世界上最先进的分布式版本控制系统（没有之一）。

## 一、为什么需要版本控制工具

1. 因为开发中会出现代码的修改，修改前的代码如果没有版本管理， 那么是无法恢复。

所以使用版本控制工具之后，我们可以给代码加上版本，这样就可以不同版本之间切换。

2. 项目开发不是一个人单打独斗，是一个团队协作完成， 团队之间也需要代码的合并， 共享等，此时也需要版本控制工具

## 二、下载和安装

### 1. 下载地址

> https://git-scm.com/

<img src="Git.assets/image-20240821102423953.png" alt="image-20240821102423953" style="zoom:67%;" />

<img src="Git.assets/image-20240821102534278.png" alt="image-20240821102534278" style="zoom:67%;" />

### 2. 安装

<img src="Git.assets/image-20240821102723620.png" alt="image-20240821102723620" style="zoom:67%;" />

<img src="Git.assets/image-20240821102852704.png" alt="image-20240821102852704" style="zoom:67%;" />

<img src="Git.assets/image-20240821102930681.png" alt="image-20240821102930681" style="zoom:67%;" />

<img src="Git.assets/image-20240821103047576.png" alt="image-20240821103047576" style="zoom:67%;" />

<img src="Git.assets/image-20240821103246298.png" alt="image-20240821103246298" style="zoom:67%;" />

<img src="Git.assets/image-20240821103412089.png" alt="image-20240821103412089" style="zoom:67%;" />

<img src="Git.assets/image-20240821103502377.png" alt="image-20240821103502377" style="zoom:67%;" />

<img src="Git.assets/image-20240821103530023.png" alt="image-20240821103530023" style="zoom:67%;" />

<img src="Git.assets/image-20240821103743802.png" alt="image-20240821103743802" style="zoom:67%;" />

<img src="Git.assets/image-20240821103914101.png" alt="image-20240821103914101" style="zoom:67%;" />

<img src="Git.assets/image-20240821103951327.png" alt="image-20240821103951327" style="zoom:67%;" />

<img src="Git.assets/image-20240821104042641.png" alt="image-20240821104042641" style="zoom:67%;" />

<img src="Git.assets/image-20240821104126651.png" alt="image-20240821104126651" style="zoom:67%;" />

<img src="Git.assets/image-20240821104246028.png" alt="image-20240821104246028" style="zoom:67%;" />

<img src="Git.assets/image-20240821104320345.png" alt="image-20240821104320345" style="zoom: 67%;" />

<img src="Git.assets/image-20240821104443373.png" alt="image-20240821104443373" style="zoom:67%;" />

**右键菜单：**

![image-20240821104521162](Git.assets/image-20240821104521162.png)

## 三、Git中的工作分区

Git分成三个区：

- 工作目录：项目代码存放的目录
- 暂存区（index/stage）：是临时存储代码的区域，是一个虚拟的区域，仅仅是一个文件（index文件）
- 代码/版本库：是一个虚拟的区域，管理我们代码的版本（head指针指向最新的版本）

## 四、Git的使用

查看命名帮助信息：

```shell
$ git 命令 --help
```

### 1. 配置git的用户信息

```shell
git config --global user.name "用户名"
git config --global user.email "邮箱地址" 
```

<img src="Git.assets/image-20240821111231939.png" alt="image-20240821111231939" style="zoom:67%;" />

**git的bash中是可以直接使用linux命令的。**

### 2. 创建一个目录，存放git管理的项目

在D盘上创建一个新的文件夹： git_code

<img src="Git.assets/image-20240821112027227.png" alt="image-20240821112027227" style="zoom:67%;" />

此时，git_code和git没有任何关系，所以git也不会管理它， 所以我们需要让git_code和git产生关系。

**通过 git init 命令把git_code目录变成 Git 可以管理的仓库(需要先进入git_code)：**

<img src="Git.assets/image-20240821112257427.png" alt="image-20240821112257427" style="zoom:67%;" />

<img src="Git.assets/image-20240821112412691.png" alt="image-20240821112412691" style="zoom:67%;" />

<img src="Git.assets/image-20240821112533720.png" alt="image-20240821112533720" style="zoom: 50%;" />

<img src="Git.assets/image-20240821112659364.png" alt="image-20240821112659364" style="zoom:67%;" />

### 3.  在git_code下创建一个文件

<img src="Git.assets/image-20240821112906037.png" alt="image-20240821112906037" style="zoom:67%;" />

此时的a.txt仅仅存储在工作目录下，我们需要将a.txt提交到代码库，才会产生版本，方便版本管理。

> 注意：工作目录中的内容必须先添加到 "暂存区"，然后才能提交到"代码库"

### 4. 添加工作目录中的内容到暂存区

> git add .   表示工作目录中所有的文件到暂存区

<img src="Git.assets/image-20240821113510255.png" alt="image-20240821113510255" style="zoom:67%;" />

<img src="Git.assets/image-20240821113816003.png" alt="image-20240821113816003" style="zoom:67%;" />

<img src="Git.assets/image-20240821113929203.png" alt="image-20240821113929203" style="zoom: 50%;" />

### 5. 将暂存区的内容提交到代码库

> git commit .   -m "提交信息"   提交暂存区中所有的内容到代码库

<img src="Git.assets/image-20240821114332887.png" alt="image-20240821114332887" style="zoom:67%;" />

<img src="Git.assets/image-20240821114657506.png" alt="image-20240821114657506" style="zoom: 50%;" />

提交内容的时候，没有指定 `-m` 参数， 就会启动默认的编辑器。

i / o  插入模式

esc  命令模式

:wq  保存并退出

### 6. 撤销工作目录中增加的内容

**撤销工作目录中增加的内容的前提是： 没有添加到暂存区**

(use "git restore <file>..." to discard changes in working directory)

<img src="Git.assets/image-20240821141431720.png" alt="image-20240821141431720" style="zoom:67%;" />

如果已经添加到暂存区，此时要撤销修改，需要先将内容从暂存区移出来，然后再撤销修改

![image-20240821141835226](Git.assets/image-20240821141835226.png)

### 7. 版本回退

当内容提交到代码库，就永久生效了，会产生一个新的版本号。

我们可以使用版本回退的方式回退到想要的版本上。

```shell
# HEAD^ 表示回退上一个版本   
# HEAD^^ 表示回退上上一个版本 
git reset --hard HEAD^
# 可以直接使用版本号回退到想要的版本上
git reset --hard commit_id
```

**要重返未来，用 git reflog 查看命令历史，以便确定要回到未来的哪个版本。**

## 五、.gitignore忽略文件

在工作目录中如果有的内容是我们不需要添加到git代码库中的， 此时可以使用 .gitignore文件进行配置。

.gitignore的作用就是用来配置需要 git忽略的内容

![image-20250114145042121](Git.assets/image-20250114145042121.png)



**在.gitignore中添加需要git忽略的内容：**

![image-20250114145115349](Git.assets/image-20250114145115349.png)

## 六、分支

提交代码， 拉取代码都是以分支作为单位进行操作的。

``` shell
$ git branch -v  # 查看当前的分支
* master 243d87c 第四次提交，将hello改成了welcome  （*所在的位置就是当前的分支）

$ git branch 分支名称  # 创建分支

$ git checkout test  # 切换分支
Switched to branch 'test'

49357@pc_lee MINGW64 /d/git_code (master)
$ git merge test   # 表示将test分支合并到当前所在的分支(master)
# 如果想将test分支合并到master分支， 必须先将当前分支切换成master
$ git add a.txt
$ git commit -m "内容" # 提交
```

如果多个分支同时修改了相同位置的代码，此时合并就会出现冲突，此时需要手动解决冲突。

合并分支后commit提交内容的时候，git commit 后面不能添加文件名, 而是直接提交整个分支

## 七、远程代码库

github  gitee  gitlab

### 1. 查看远程库信息

``` shell
git remote -v #查看远程库信息
```

### 2. 添加远程库

``` shell
git remote add 别名 远程库地址
```

### 3. 删除远程库

```shell
git remote rm 别名
```

### 4. 将本地代码推送到远程库

注意： 代码推送是以分支为单位的， 也就是多分支的时候需要指定推送的分支

``` shell
$ git push 远程库的别名 本地分支名
```

### 5. 拉取远程库中的代码

``` shell
$ git pull 远程库的别名 远程分支名
远程分支名要求是本地分支关联的远程跟踪分支
```

**注意： 在推送代码之前先拉取代码**

### 6. 克隆项目

``` shell
git clone https://gitee.com/hehziwei/student-system.git
```

## 八、PyCharm中使用git

### 1. PyCharm中集成git

![image-20240821164446721](Git.assets/image-20240821164446721.png)

<img src="Git.assets/image-20240821164558807.png" alt="image-20240821164558807" style="zoom: 50%;" />

### 2. PyCharm中安装gitee插件

<img src="Git.assets/image-20240821164905931.png" alt="image-20240821164905931" style="zoom:67%;" />

### 3. 添加gitee账号信息

<img src="Git.assets/image-20240821165209890.png" alt="image-20240821165209890" style="zoom:67%;" />

### 4. 使用token进行登录

先将刚才添加的账户信息删除

<img src="Git.assets/image-20240821170448017.png" alt="image-20240821170448017" style="zoom:67%;" />

![image-20240821170515955](Git.assets/image-20240821170515955.png)

<img src="Git.assets/image-20240821170548333.png" alt="image-20240821170548333" style="zoom:67%;" />

<img src="Git.assets/image-20240821170637193.png" alt="image-20240821170637193" style="zoom:67%;" />

<img src="Git.assets/image-20240821170829310.png" alt="image-20240821170829310" style="zoom:67%;" />

<img src="Git.assets/image-20240821170925151.png" alt="image-20240821170925151" style="zoom:67%;" />

<img src="Git.assets/image-20240821171006610.png" alt="image-20240821171006610" style="zoom:67%;" />

### 5. 将项目分享到gitee上

<img src="Git.assets/image-20240821165427083.png" alt="image-20240821165427083" style="zoom:67%;" />

<img src="Git.assets/image-20240821165607648.png" alt="image-20240821165607648" style="zoom:50%;" />

<img src="Git.assets/image-20240821165733534.png" alt="image-20240821165733534" style="zoom:67%;" />

### 6. 在PyCharm中使用git本地管理代码

<img src="Git.assets/image-20240821171307970.png" alt="image-20240821171307970" style="zoom:67%;" />

<img src="Git.assets/image-20240821171332383.png" alt="image-20240821171332383" style="zoom:67%;" />

## 九、Pycharm中添加.gitignore

### 9.1 方式一

直接在工程下创建一个 .gitignore的文件， 在文件中添加需要忽略的内容

![image-20250114165622635](Git.assets/image-20250114165622635.png)

### 9.2 方式二

![image-20250114165737957](Git.assets/image-20250114165737957.png)

![image-20250114165913689](Git.assets/image-20250114165913689.png)

![image-20250114165953117](Git.assets/image-20250114165953117.png)
