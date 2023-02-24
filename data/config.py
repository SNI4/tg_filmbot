from environs import Env 

env = Env()
env.read_env()

TOKEN = env.str("TG_FILMBOT")
ADMIN_ID = 6226556812
ADMIN_USERNAME = "sn1chz"
