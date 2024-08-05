import tkinter as tk
from tkinter import filedialog, messagebox
from pynput import keyboard
import webbrowser
import pyautogui
import time

class WebPageCycler:
    def __init__(self, master):
        self.master = master
        master.title("美农网页轮播器")
        master.geometry("330x260")
        master.resizable(0, 0)

        # GUI组件初始化
        self.file_label_row0 = tk.Label(master, text="")
        self.file_label_row0.grid(row=0, column=0, sticky='ew')

        self.select_file_button = tk.Button(master, text="选择浏览器轮播的TXT文件", command=self.load_urls)
        #self.select_file_button.pack()
        self.select_file_button.grid(row=1, column=0, columnspan=2, sticky='ew')

        self.file_label = tk.Label(master, text="未选择文件")
        #self.file_label.pack()
        self.file_label.grid(row=2, column=0, columnspan=2, sticky='ew')

        self.file_label_row3 = tk.Label(master, text="")
        self.file_label_row3.grid(row=3, column=0, sticky='ew')

        self.interval_label = tk.Label(master, text="网页切换间隔(秒):")
        #self.interval_label.pack()
        self.interval_label.grid(row=4, column=0, sticky='E')

        self.interval_entry = tk.Entry(master)
        self.interval_entry.insert(0, "10")
        #self.interval_entry.pack()
        self.interval_entry.grid(row=4, column=1, sticky='ew')

        self.file_label_row5 = tk.Label(master, text="")
        self.file_label_row5.grid(row=5, column=0, sticky='ew')

        self.start_button = tk.Button(master, text="开启网页轮播", command=self.start_cycling)
        #self.start_button.pack()
        self.start_button.grid(row=6, column=0, columnspan=2, sticky='ew')

        # 添加暂停/开始按钮
        self.pause_button = tk.Button(master, text="暂停[F9]", command=self.toggle_pause)
        #self.pause_button.pack()
        self.pause_button.grid(row=7, column=0, columnspan=2, sticky='ew')

        self.file_label_row8 = tk.Label(master, text="F11可退出浏览器全屏模式，关闭软件可停止网页轮播！")
        self.file_label_row8.grid(row=8, columnspan=2, column=0, sticky='ew')

        master.columnconfigure(0, weight=1)
        master.columnconfigure(1, weight=1)

        # 内部状态变量
        self.urls = []
        self.current_index = 0
        self.is_running = False
        self.is_paused = False

    def load_urls(self):
        file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
        if file_path:
            self.file_label.config(text=file_path)
            self.urls.clear()
            with open(file_path, 'r') as file:
                for line in file:
                    url = line.strip()
                    if url:
                        self.urls.append(url)

    def start_cycling(self):
        self.is_running = True
        self.open_all_urls()
        time.sleep(1)  # 等待所有URL加载完成
        pyautogui.press('f11')  # 进入全屏模式
        self.cycle_with_keys(int(self.interval_entry.get()) * 1000)

    def open_all_urls(self):
        for url in self.urls:
            webbrowser.open_new_tab(url)
            time.sleep(2)  # 增加2秒延迟

    def cycle_with_keys(self, delay):
        if self.is_paused or not self.is_running:
            return
        pyautogui.hotkey('ctrl', 'pagedown')
        self.master.after(delay, lambda: self.cycle_with_keys(delay))

    def toggle_pause(self):
        self.is_paused = not self.is_paused
        status = "已暂停[F9开始]" if self.is_paused else "已开始[F9暂停]"
        self.pause_button.config(text=status)  # 更新按钮文本
        messagebox.showinfo("轮播状态", f"轮播{status}", icon='info')

        # 如果从暂停状态变为开始状态，重新启动轮播
        if not self.is_paused and self.is_running:
            self.cycle_with_keys(int(self.interval_entry.get()) * 1000)

        self.master.after(2000, lambda: messagebox.dismiss())

# 定义一个用于处理全局热键的函数
def on_global_hotkey():
    if app.is_running:
        app.toggle_pause()

# 创建一个全局热键监听器
hotkey_listener = keyboard.GlobalHotKeys({'<f9>': on_global_hotkey})

# 在主程序开始运行前启动监听器
hotkey_listener.start()

if __name__ == "__main__":
    root = tk.Tk()
    app = WebPageCycler(root)

    # 键盘事件监听
    def on_key_press(event):
        if event.keysym == 'F9':
            if app.is_running:
                app.toggle_pause()

    root.bind('<KeyPress>', on_key_press)
    root.mainloop()