# -*- coding: utf-8 -*-

#########自定义配置########

# Mod名字,为了副包的名称不冲突，请修改为自己的名字
MOD_NAME = "DBLOpenApi_YourName_"

#副包类型,可选值:World,Mod
PACKAGE_TYPE = "World"

########预设########
#以下部分请填写您导出的预设
#直接复制到等于号后即可（删除LUCKY_BLOCKS_INITIALIZE_PRESETS）
#系统会使用WHOLE_PRESET整体覆盖一遍
#再对单个预设特殊化覆盖

#整体覆盖
WHOLE_PRESET = None

#绿色幸运方块预设
LUCKY_BLOCK_1_PRESET = None

#黄色幸运方块预设
LUCKY_BLOCK_2_PRESET = None

#蓝色幸运方块预设
LUCKY_BLOCK_3_PRESET = None

#彩色幸运方块预设
LUCKY_BLOCK_4_PRESET = None

#红色幸运方块预设
LUCKY_BLOCK_5_PRESET = None

#白色幸运方块预设
LUCKY_BLOCK_6_PRESET = None


#########系统配置#########
# Mod版本
MOD_VERSION = "1.0.0"

# 服务端系统
SERVER_SYSTEM = "ServerSystem"
SERVER_SYSTEM_PATH = MOD_NAME + "Scripts.server.serverListen.ServerListen"

# 客户端系统
CLIENT_SYSTEM = "ClientSystem"
CLIENT_SYSTEM_PATH = MOD_NAME + "Scripts.client.clientListen.ClientListen"

# Ui
UI_BASE_PATH = "Scripts.client.ui."



