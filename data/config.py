from environs import Env 

env = Env()
env.read_env()

TOKEN = env.str("TG_FILMBOT")
ADMIN_ID = 622655681
ADMIN_USERNAME = "sn1chz"
