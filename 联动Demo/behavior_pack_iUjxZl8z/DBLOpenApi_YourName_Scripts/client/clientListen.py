# -*- coding: utf-8 -*-

from .. import modConfig
from baseClient import (
    BaseClient, Listen, CF, LID, PID, clientApi
)


class ClientListen(BaseClient):

    def __init__(self, namespace, systemName):
        BaseClient.__init__(self, namespace, systemName)
        

    @Listen("UiInitFinished")
    def UiInitFinished(self, args):
        clientApi.RegisterUI(
            modConfig.MOD_NAME,
            "NotFoundTip",
            modConfig.MOD_NAME + modConfig.UI_BASE_PATH + "NotFoundTip.NotFoundTip",
            "diy_lucky_block_open_api_tip.main"
        )
        self.CallServer("UiInitFinished", {"__id__":PID})
    def NotFoundTip(self,args):
        """未安装主包时，弹出提示框"""
        clientApi.PushScreen(modConfig.MOD_NAME, "NotFoundTip")

    
