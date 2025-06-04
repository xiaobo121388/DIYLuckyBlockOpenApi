# -*- coding: utf-8 -*-

import mod.client.extraClientApi as clientApi
from ... import modConfig

ViewBinder = clientApi.GetViewBinderCls()
ViewRequest = clientApi.GetViewViewRequestCls()
ScreenNode = clientApi.GetScreenNodeCls()
CF = clientApi.GetEngineCompFactory()
LID = clientApi.GetLevelId()
PID = clientApi.GetLocalPlayerId()


class NotFoundTip(ScreenNode):

    def __init__(self, namespace, name, param):
        ScreenNode.__init__(self, namespace, name, param)
        

    def Create(self):
        buttonUIControl = self.GetBaseUIControl("/image/button").asButton()
        buttonUIControl.AddTouchEventParams({"isSwallow":True})
        buttonUIControl.SetButtonTouchUpCallback(self.onCheckButtonTouch)
        buttonUIControl = self.GetBaseUIControl("/image/image/button").asButton()
        buttonUIControl.AddTouchEventParams({"isSwallow":True})
        buttonUIControl.SetButtonTouchUpCallback(self.onCloseButtonTouch)
    def onCheckButtonTouch(self,args):
        """点击按钮触发事件，打开资源中心详情页，显示关闭按钮"""
            
        baseUIControl = self.GetBaseUIControl("/image/image/button")
        baseUIControl.SetVisible(True)
        CF.CreateNeteaseWindow(PID).OpenResourceCenterDetailWindow("4680004816558905032")
    def onCloseButtonTouch(self,args):
        """点击关闭按钮触发事件，关闭当前界面"""
        clientApi.PopScreen()



