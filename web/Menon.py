import tkinter as tk
from tkinter import filedialog, messagebox
import webbrowser
import pyautogui
import time

class WebPageCycler:
    def __init__(self, master):
        self.master = master
        master.title("网页轮播器")
        master.geometry("300x200")

        # GUI组件初始化
        self.select_file_button = tk.Button(master, text="选择TXT文件", command=self.load_urls)
        self.select_file_button.pack()
        self.file_label = tk.Label(master, text="未选择文件")
        self.file_label.pack()
        self.interval_label = tk.Label(master, text="按键间隔(秒):")
        self.interval_label.pack()
        self.interval_entry = tk.Entry(master)
        self.interval_entry.insert(0, "10")
        self.interval_entry.pack()
        self.start_button = tk.Button(master, text="开始轮播", command=self.start_cycling)
        self.start_button.pack()

        # 添加暂停/开始按钮
        self.pause_button = tk.Button(master, text="暂停", command=self.toggle_pause)
        self.pause_button.pack()

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
        status = "轮播已暂停" if self.is_paused else "轮播已开始"
        self.pause_button.config(text=status)  # 更新按钮文本
        messagebox.showinfo("轮播状态", f"轮播{status}", icon='info')
        self.master.after(2000, lambda: messagebox.dismiss())

if __name__ == "__main__":
    root = tk.Tk()
    app = WebPageCycler(root)

    # 键盘事件监听
    def on_key_press(event):
        if event.keysym == 'F9' and app.is_running:
            app.toggle_pause()

    root.bind('<KeyPress>', on_key_press)
    root.mainloop()

    #测试
