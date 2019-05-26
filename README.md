# Seam

#### 介绍
Django开发的博客

#### 软件架构
软件架构说明
Python3.7
Django==2.2.1


#### 安装教程

1. pip install requirements
2. pip install https://codeload.github.com/sshwsfc/xadmin/zip/django2
3. python3 manage.py findstatic xadmin
4. ln -s /usr/local/lib/python3.6/site-packages/xadmin/static/xadmin static/
5. python3 manage.py findstatic ckeditor
6. ln -s /usr/local/lib/python3.6/site-packages/ckeditor/static/ckeditor/ static/
7. wget https://ckeditor.com/cke4/sites/default/files/prism/releases/prism_1.0.1.zip
8. wget http://seam.along.party/static/ckeditor/ckeditor/plugins/prism/prism.css
9. unzip prism_1.0.1.zip && mv prism static/ckeditor/ckeditor/plugins && 
mv prism.css static/ckeditor/ckeditor/plugins/prism/prism.css

#### 使用说明

1. xxxx
2. xxxx
3. xxxx

#### 参与贡献

1. Fork 本仓库
2. 新建 Feat_xxx 分支
3. 提交代码
4. 新建 Pull Request


#### 码云特技

1. 使用 Readme\_XXX.md 来支持不同的语言，例如 Readme\_en.md, Readme\_zh.md
2. 码云官方博客 [blog.gitee.com](https://blog.gitee.com)
3. 你可以 [https://gitee.com/explore](https://gitee.com/explore) 这个地址来了解码云上的优秀开源项目
4. [GVP](https://gitee.com/gvp) 全称是码云最有价值开源项目，是码云综合评定出的优秀开源项目
5. 码云官方提供的使用手册 [https://gitee.com/help](https://gitee.com/help)
6. 码云封面人物是一档用来展示码云会员风采的栏目 [https://gitee.com/gitee-stars/](https://gitee.com/gitee-stars/)