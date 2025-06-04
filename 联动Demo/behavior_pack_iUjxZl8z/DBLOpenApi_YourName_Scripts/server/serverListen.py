# -*- coding: utf-8 -*-

from .. import modConfig
from baseServer import (
    BaseServer, Listen, CF, LID, serverApi
)


class ServerListen(BaseServer):

    def __init__(self, namespace, systemName):
        BaseServer.__init__(self, namespace, systemName)
        self.DLBserverSystem = None
        self.SystemCheck = False

    @Listen("LoadServerAddonScriptsAfter")
    def LoadServerAddonScriptsAfter(self,args):
        """服务端加载完毕后执行"""
        #获取幸运方块api系统
        self.DLBserverSystem = serverApi.GetSystem("DIYLuckyBlock", "OpenApiServerSystem")
        if self.DLBserverSystem is None:
            self.SystemCheck = False
        else:
            self.SystemCheck = True
            #设置包类型
            self.DLBserverSystem.PackageType(modConfig.PACKAGE_TYPE,modConfig.MOD_NAME,modConfig.SERVER_SYSTEM)
            #修改幸运方块数据
            self.DLBserverSystem.ChangeLuckyBlockData(modConfig.WHOLE_PRESET, modConfig.LUCKY_BLOCK_1_PRESET,
                                                    modConfig.LUCKY_BLOCK_2_PRESET,modConfig.LUCKY_BLOCK_3_PRESET,
                                                    modConfig.LUCKY_BLOCK_4_PRESET,modConfig.LUCKY_BLOCK_5_PRESET,
                                                    modConfig.LUCKY_BLOCK_6_PRESET)
    def UiInitFinished(self,args):
        pid = args["__id__"]
        if self.SystemCheck == False:
            self.CallClient(pid,"NotFoundTip",{})
    def Update(self):
        pass



    def Destroy(self):
        """持久化服务的数据"""
        pass
