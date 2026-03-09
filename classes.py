from greate_logger import Logger

class Config:
    tg_token = None
    tg_id = None
    tg_hash = None
    def __init__(self, data: dict):
        self.tg_token = data['telegram']['token']
        self.tg_id = data['telegram']['app_id']
        self.tg_hash = data['telegram']['app_hash']
