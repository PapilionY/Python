# coding:utf-8
# -----------------------------------------------------------------------------
# 应用程序的启动函数
# 如果不使用界面程序，则可自行处理
# -----------------------------------------------------------------------------

from app.views.win_main import App                  # 系统主窗体App

if __name__ == "__main__":
    App().open()
