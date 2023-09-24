import tkinter as tk
import time
import keyboard
import pyautogui
import threading
firstTime = True
global loop
loop = True
root = tk.Tk()
root.geometry("300x200")
root.title("BassarHotkey")
icon = tk.PhotoImage(file="logo.png")
root.iconphoto(False, icon)
root.configure(bg="#222021")

def starttwo():
    global loop
    while loop:
        if keyboard.is_pressed("enter"):
            temp = pyautogui.locateOnScreen("hentet.png")
            if temp:
                res = pyautogui.center(temp)
                pyautogui.moveTo(res)
                pyautogui.click()
                time.sleep(0.1)
                pyautogui.click()
            else:
                temp2 = pyautogui.locateOnScreen("trekk.png")
                if temp2:
                    res = pyautogui.center(temp2)
                    pyautogui.moveTo(res)
                    pyautogui.click()
                    time.sleep(0.1)
                    pyautogui.click()
                    onOff.config(text="Bilde ble funnet", fg="green")
                else:
                    onOff.config(text="Bilde ble ikke funnet", fg="yellow")


def start():
    global loop
    loop = True
    onOff.config(text="AKTIV", fg="#00bfff", font=("Roboto", 12, "bold"))
    onOff.grid(column=0, row=2, columnspan=2, pady=10)
    threading.Thread(target=starttwo, daemon=True).start()
    stopButton["state"] = tk.NORMAL
    startButton["state"] = tk.DISABLED

def stop():
    global loop
    loop = False
    onOff.config(text="INAKTIV", fg="#ff1178", font=("Roboto", 12, "bold"))
    onOff.grid(column=0, row=2, columnspan=2, pady=10)
    stopButton["state"] = tk.DISABLED
    startButton["state"] = tk.NORMAL

title = tk.Label(root, text="Hotkeybassar", font=("roboto", 10, "bold"), bg="#222021", fg="white")
title.grid(column=0, row=0, columnspan=2, pady=10)

subTitle = tk.Label(root, text="Dette programmet er for å trekke i bassar appen\nTrykk enter mens du er i appen", font=("Lexend", 8, "bold"), bg="#222021", fg="white")
subTitle.grid(column=0, row=1, columnspan=2, pady=10)

onOff = tk.Label(root, text="",bg="#222021", fg="white")
onOff.grid(column=0, row=2, columnspan=2, pady=10)

startButton = tk.Button(root, text="start", command=start, padx=40, bg="#222021", fg="white")
startButton.grid(column=0, row=3)
stopButton = tk.Button(root, text="stop", command=stop, padx=40, bg="#222021", fg="white")
stopButton.grid(column=1, row=3)

if firstTime:
    firstTime = False
    stop()

root.rowconfigure(3)
root.columnconfigure(2)
root.mainloop()