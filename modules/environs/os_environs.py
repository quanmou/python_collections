"""
os.environ: 一个表示字符串环境的 mapping 对象。
例如，environ['HOME'] 是你的主目录（在某些平台上）的路径名，相当于 C 中的 getenv("HOME")。
这个映射是在第一次导入 os 模块时捕获的，通常作为 Python 启动时处理 site.py 的一部分。
除了通过直接修改 os.environ 之外，在此之后对环境所做的更改不会反映在 os.environ 中。
"""
import os


print(os.environ)
print(os.environ.get("HOME", "default_value"))
print(os.getenv("HOME", "default_value"))


"""
如果我们想要设置非字符串类型的环境变量怎么办呢？比如设置 int 类型、float 类型、list 类型
"""
VAR1 = int(os.getenv('VAR1', 1))
VAR2 = float(os.getenv('VAR2', 5.5))


"""
更好的方式，使用environs库
"""
from environs import Env
env = Env()
VAR1 = env.int('VAR1', 1)
VAR2 = env.float('VAR2', 5.5)
VAR3 = env.list('VAR3', [])


"""
environs支持的变量类型
"""
# export GITHUB_USER=sloria
# export MAX_CONNECTIONS=100
# export SHIP_DATE='1984-06-25'
# export TTL=42
# export ENABLE_LOGIN=true
# export GITHUB_REPOS=webargs,konch,ped
# export COORDINATES=23.3,50.0
# export LOG_LEVEL=DEBUG
# export VAR_DICT=name=germey,age=25
# export VAR_JSON='{"name": "germey", "age": 25}'
# export VAR_URL=https://cuiqingcai.com
# export VAR_UUID=762c8d53-5860-4d5d-81bc-210bf2663d0e
# export VAR_PATH=/var/py/env

from environs import Env
env = Env()
# required variables
gh_user = env("GITHUB_USER")  # => 'sloria'
secret = env("SECRET")  # => raises error if not set

# casting
max_connections = env.int("MAX_CONNECTIONS")  # => 100
ship_date = env.date("SHIP_DATE")  # => datetime.date(1984, 6, 25)
ttl = env.timedelta("TTL")  # => datetime.timedelta(0, 42)
log_level = env.log_level("LOG_LEVEL")  # => logging.DEBUG

# providing a default value
enable_login = env.bool("ENABLE_LOGIN", False)  # => True
enable_feature_x = env.bool("ENABLE_FEATURE_X", False)  # => False

# parsing lists
gh_repos = env.list("GITHUB_REPOS")  # => ['webargs', 'konch', 'ped']
coords = env.list("COORDINATES", subcast=float)  # => [23.3, 50.0]


"""
将环境变量定义到文件中，使用environs进行读取和加载，默认会读取本地当前运行目录下的 .env 文件
"""
from environs import Env
env = Env()
# env.read_env()  # read .env file, if it exists
env.read_env(path='.env.test')  # 读取自定义的文件
# 在.env文件中写入如下内容
# APP_DEBUG=false
# APP_ENV=prod
APP_DEBUG = env.bool('APP_DEBUG')
APP_ENV = env.str('APP_ENV')
print(APP_DEBUG)
print(APP_ENV)


"""
前缀处理
environs 还支持前缀处理，一般来说我们定义一些环境变量，如数据库的连接，可能有 host、port、password 等，
但在定义环境变量的时候往往会加上对应的前缀，如 MYSQL_HOST、MYSQL_PORT、MYSQL_PASSWORD 等，但在解析时，我们可以根据前缀进行分组处理
"""
# export MYAPP_HOST=localhost
# export MYAPP_PORT=3000
with env.prefixed("MYAPP_"):
    host = env("HOST", "localhost")  # => 'lolcathost'
    port = env.int("PORT", 5000)  # => 3000

# nested prefixes are also supported:
# export MYAPP_DB_HOST=lolcathost
# export MYAPP_DB_PORT=10101
with env.prefixed("MYAPP_"):
    with env.prefixed("DB_"):
        db_host = env("HOST", "lolcathost")
        db_port = env.int("PORT", 10101)


"""
合法性验证
有些环境变量的传入是不可预知的，如果传入一些非法的环境变量很可能导致一些难以预料的问题。
比如说一些可执行的命令，通过环境变量传进来，如果是危险命令，那么会非常危险。
"""
# export TTL=-2
# export NODE_ENV='invalid'
# export EMAIL='^_^'
env = Env()
# simple validator
env.int("TTL", validate=lambda n: n > 0)
# => Environment variable "TTL" invalid: ['Invalid value.']
