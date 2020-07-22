
#windows， python3.以上版本

# 进入dos，创建虚拟环境，创建成功生成一个venv文件
mkdir myproject
cd myproject
py -3 -m venv venv 
 
# 激活虚拟环境,激活成功后终端提示符显示虚拟环境名称  
venv\Scripts\activate

# 安装Flask，已激活的虚拟环境中执行
pip install Flask
