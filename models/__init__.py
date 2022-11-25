#!/usr/bin/python3
""" Initializes the model dictionary """
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
