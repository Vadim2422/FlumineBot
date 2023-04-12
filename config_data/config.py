from environs import Env
from dataclasses import dataclass


@dataclass
class PostgresConfig:
    database: str
    db_host: str
    db_user: str
    db_password: str


@dataclass
class RedisConfig:
    database: str
    db_host: str
    db_user: str
    db_password: str


@dataclass
class TgBot:
    token: str
    admin_ids: list[int]


@dataclass
class Config:
    tg_bot: TgBot
    # postgres: PostgresConfig
    # redis: RedisConfig


def load_config(path: str = None) -> Config:
    env: Env = Env()
    if path:
        env.read_env(path)
    else:
        env.read_env()

    return Config(tg_bot=TgBot(token=env('BOT_TOKEN'), admin_ids=list(map(int, env.list('ADMIN_IDS')))))
    # return Config(tg_bot=TgBot(token=env('BOT_TOKEN'),
    #                            admin_ids=list(map(int, env.list('ADMIN_IDS')))),
    #               postgres=PostgresConfig(database=env('DATABASE'),
    #                                       db_host=env('DB_HOST'),
    #                                       db_user=env('DB_USER'),
    #                                       db_password=env('DB_PASSWORD')),
    #               redis=RedisConfig(database=env('DATABASE'),
    #                                 db_host=env('DB_HOST'),
    #                                 db_user=env('DB_USER'),
    #                                 db_password=env('DB_PASSWORD')))
