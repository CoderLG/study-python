from ctypes import *
from pynput import keyboard
import datetime
import pyautogui
import winsound


pyautogui.PAUSE = 1
pyautogui.FAILSAFE = True

startTime = datetime.datetime.now()

def get_color(x,y):
    gdi32 = windll.gdi32
    user32 = windll.user32
    hdc = user32.GetDC(None)  # 获取颜色值# 获取颜色值
    pixel = gdi32.GetPixel(hdc, x, y)  # 提取RGB值
    r = pixel & 0x0000ff
    g = (pixel & 0x00ff00) >> 8
    b = pixel >> 16
    return  [r, g, b]


def mouse_todo():
    # pass
    # 模拟鼠标键盘操作
    # https: // blog.csdn.net / guangmingsky / article / details / 80009547
    # 分辨率
    # print(pyautogui.size())

    # 鼠标当前坐标
    # print(pyautogui.position())

    # 移动鼠标
    # pyautogui.moveTo(300, 300, duration=0.25)

    # 鼠标双击
    # pyautogui.doubleClick(x=873, y=472, button='left')

    # 鼠标的拖动
    pyautogui.mouseDown(x=873, y=472, button='left')
    pyautogui.moveTo(973, 472, duration=0.25)
    pyautogui.mouseUp(button='left')

def key_todo():
    # pass
    pyautogui.doubleClick(x=873, y=472, button='left')
    pyautogui.typewrite('Hello world')
    pyautogui.typewrite('\n')
    pyautogui.press('f5')
    pyautogui.keyDown('ctrlleft');
    pyautogui.press('s');
    pyautogui.keyUp('ctrlleft')

def sound():
    duration = 1000  # millisecond
    freq = 540  # Hz
    winsound.Beep(freq, duration)

def on_press(key):
    pass

def on_release(key):
    try:
        if key.char == '2':
            return False     #返回False 就停止监听

        if key.char == '1':
            mouse_todo()

        # print(key)

    except Exception as e:
        pass


# 监听键盘按键
# with keyboard.Listener(on_press=on_press,on_release=on_release) as listener:
#         listener.join()


if __name__ == '__main__':
    # print(get_color(10,10))

    sound()
    endTime = datetime.datetime.now()
    print("运行结束共用时："+ str((endTime-startTime).seconds) + "秒")
