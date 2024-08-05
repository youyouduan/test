import tkinter as tk
from tkinter import filedialog
import subprocess
import webbrowser
import pyautogui
import time

class WebPageCycler:
    def __init__(self, master):
        self.master = master
        master.title("网页轮播器")
        master.geometry("300x200")

        self.select_file_button = tk.Button(master, text="选择TXT文件", command=self.load_urls)
        self.select_file_button.pack()

        self.file_label = tk.Label(master, text="未选择文件")
        self.file_label.pack()

        self.interval_label = tk.Label(master, text="按键间隔(秒):")
        self.interval_label.pack()
        self.interval_entry = tk.Entry(master)
        self.interval_entry.insert(0, "10")  # 默认间隔为10秒
        self.interval_entry.pack()

        self.start_button = tk.Button(master, text="开始轮播", command=self.start_cycling)
        self.start_button.pack()

        self.urls = []
        self.current_index = 0

        self.timer_id = None
        self.is_running = False
        self.is_paused = False

    def load_urls(self):
        file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
        if file_path:
            self.file_label.config(text=file_path)

            # 清空URL列表并重新加载
            self.urls.clear()

            # 从TXT文件中读取URLs
            with open(file_path, 'r') as file:
                for line in file:
                    url = line.strip()
                    if url:
                        self.urls.append(url)

    def start_cycling(self):
        self.current_index = 0  # 初始化当前索引为0
        self.cycle_urls()

    def cycle_urls(self):
        if not self.urls or self.current_index >= len(self.urls):
            return

        url = self.urls[self.current_index]
        self.open_url(url)

        self.current_index += 1  # 切换到下一个URL

        if self.current_index < len(self.urls):
            self.master.after(3000, self.cycle_urls)  # 5秒后继续循环遍历URL

    def fullscreen_and_cycle(self):
        edge_path = r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe'
        edge_process = subprocess.Popen([edge_path, self.urls[-1]])
        
        time.sleep(5)  # 等待浏览器窗口加载完成
        
        pyautogui.moveTo(self.master.winfo_screenwidth() / 2, self.master.winfo_screenheight() / 2)
        pyautogui.click()
    
    # 检查浏览器是否完全加载
        while not browser_is_loaded():
        time.sleep(0.5)
        
        pyautogui.press('f11')  # 进入全屏模式

        interval = int(self.interval_entry.get())
        self.is_running = True
        self.cycle_with_keys(interval * 2000)

    def cycle_with_keys(self, delay):
        if self.is_paused:
            return

        if not self.is_running:
            return

        pyautogui.hotkey('ctrl', 'pagedown')  # 触发Ctrl + Page Down按键
        time.sleep(0.5) 
        self.master.after(delay, lambda: self.cycle_with_keys(delay))

    def stop_cycling(self):
        self.is_running = False

    def toggle_pause(self):
        self.is_paused = not self.is_paused

    def open_url(self, url):
        webbrowser.open(url)

    def next_url(self):
        self.current_index += 1
        self.cycle_urls()

if __name__ == "__main__":
    root = tk.Tk()
    app = WebPageCycler(root)

    # 添加键盘事件监听
    def on_key_press(event):
        if event.keysym == 'Escape':
            if app.is_running:
                if app.is_paused:
                    app.toggle_pause()  # 继续按键循环
                else:
                    app.toggle_pause()  # 暂停按键循环

    root.bind('<KeyPress>', on_key_press)

    root.mainloop()