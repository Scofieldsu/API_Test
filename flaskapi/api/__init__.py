# encoding = utf-8

from jsonrpc.backend.flask import JSONRPCAPI
from jsonrpc.dispatcher import Dispatcher

dispatcher = Dispatcher()
api = JSONRPCAPI(dispatcher)
api_add = api.dispatcher.add_method