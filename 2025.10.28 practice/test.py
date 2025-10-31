import tkinter as tk
import random
import threading
import pyautogui
import time

messages = [
    "加油！你可以的！", "喝水记得休息", "起来跑步", "有没有可乐",
    "保持好奇心！", "你正在进步！", "坚持是最好的魔法", "✨ 继续闪耀吧 ✨"
]

# 获取屏幕大小
screen_width, screen_height = pyautogui.size()

WIN_W, WIN_H = 200, 100

def create_popup():

    root = tk.Tk()
    root.overrideredirect(False)  # 去边框
    root.attributes("-topmost", True)
    root.configure(bg=random.choice(["#FFF0F0", "#F0FFF0", "#F0F0FF", "#FFFFE0", "#E0FFFF"]))

    msg = random.choice(messages)
    label = tk.Label(root, text=msg, font=("微软雅黑", 12, "bold"), fg="black", bg=root["bg"])
    label.pack(expand=True, fill="both")

    x = random.randint(0, screen_width - WIN_W)
    y = random.randint(0, screen_height - WIN_H)
    dx = random.choice([-2, -1, 1, 2])
    dy = random.choice([-2, -1, 1, 2])

    def move():
        nonlocal x, y, dx, dy
        x += dx
        y += dy

        # 边界反弹
        if x <= 0 or x >= screen_width - WIN_W:
            dx = -dx
        if y <= 0 or y >= screen_height - WIN_H:
            dy = -dy

        root.geometry(f"{WIN_W}x{WIN_H}+{x}+{y}")
        root.after(30, move)  # 每 30ms 移动一次

    move()
    root.mainloop()

def main():
    num_windows = 70
    for _ in range(num_windows):
        threading.Thread(target=create_popup, daemon=True).start()
        time.sleep(0.05)  # 弹出间隔

    while True:
        time.sleep(1)

if __name__ == "__main__":
    main()
