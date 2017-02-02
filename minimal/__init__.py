from ts3plugin import ts3plugin, PluginHost
import ts3defines, ts3lib

class Minimal(ts3plugin):
    name 				= "Minimal example"
    requestAutoload 	= False
    version 			= "1.0"
    apiVersion 			= 21
    author 				= "your name"
    description 		= "a description"
    offersConfigure		= False
    commandKeyword 		= ""
    infoTitle			= None
    hotkeys 			= []
    menuItems           = []

    def __init__(self):
        pass