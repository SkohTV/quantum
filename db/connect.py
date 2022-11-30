"""Allow to connect to database.sqlite

Methods
    Blabla : blabla    
"""
import sqlite3
from sty import ef, fg, rs
from src.logger import logger

# Connection to the database, will be passed as global
conn = sqlite3.connect("db/database.sqlite")