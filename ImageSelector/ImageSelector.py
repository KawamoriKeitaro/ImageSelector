import sys
import tkinter
from tkinter import messagebox
from ImageSelection import ImageSelection

#入力フォルダパス
input_folder_path_value = "C:/Graduated/Album/input_images/input_test"
#出力フォルダパス
output_folder_path_value = "C:/Graduated/Album/input_images/output_images"
#選定枚数[%](1～99)
rate_of_selected_photo_value = "99"
#人物写真割合[%](1～99)
rate_of_portrait_photo_value = "99"


if ImageSelection.ImageSelection(input_folder_path_value, output_folder_path_value, rate_of_selected_photo_value, rate_of_portrait_photo_value):
    print("Complete Successfully")

else :
    print("Error")


"""
def button_click():
    input_folder_path_value = input_folder_path.get()
    output_folder_path_value = output_folder_path.get()
    rate_of_selected_photo_value = rate_of_selected_photo.get()
    rate_of_portrait_photo_value = rate_of_portrait_photo.get()

    show_message = "入力フォルダパス：" + input_folder_path_value + 'が入力されました。\n'
    show_message += "出力フォルダパス：" + output_folder_path_value + 'が入力されました。\n'
    show_message += "選定枚数[%](1～99)：" + rate_of_selected_photo_value + "が入力されました。\n"
    show_message += "人物写真割合[%](1～99)：" + rate_of_portrait_photo_value + "が入力されました。\n"

    show_message += "\n---選別を開始します---\n"

    #ここに入れるのが上記コード


    print(show_message)

    # 入力内容をポップアップ画面で表示
    messagebox.showinfo("入力内容" ,show_message)


app = tkinter.Tk()
app.title(u"IMAGE SELECTOR")
app.geometry("400x200")
bg_color = 'gray27'
app.configure(bg=bg_color)

# 入力フォルダパスラベル
input_folder_path_label = tkinter.Label(text="入力フォルダパス", foreground='#faf0e6', background=bg_color)
input_folder_path_label.grid(row=1, column=1, padx=30,)

# 入力欄の作成(入力フォルダパス)
input_folder_path = tkinter.Entry(width=40)
input_folder_path.grid(row=1, column=2)


# 出力フォルダパスラベル
output_folder_path_label = tkinter.Label(text="出力フォルダパス", foreground='#faf0e6', background=bg_color)
output_folder_path_label.grid(row=2, column=1, padx=10,)

# 入力欄の作成(出力フォルダパス)
output_folder_path = tkinter.Entry(width=40)
output_folder_path.grid(row=2, column=2)


# 選定枚数ラベル
rate_of_selected_photo_label = tkinter.Label(text="選定枚数[%](1～99)",foreground='#faf0e6', background=bg_color)
rate_of_selected_photo_label.grid(row=3, column=1, padx=10,)

# 入力欄の作成(選定枚数)
rate_of_selected_photo = tkinter.Entry(width=40)
rate_of_selected_photo.grid(row=3, column=2)

# 人物写真割合ラベル
rate_of_portrait_photo_label = tkinter.Label(text="人物写真割合[%](1～99)",foreground='#faf0e6', background=bg_color)
rate_of_portrait_photo_label.grid(row=4, column=1, padx=10,)

# 入力欄の作成(選定枚数)
rate_of_portrait_photo = tkinter.Entry(width=40)
rate_of_portrait_photo.grid(row=4, column=2)

#ボタンの作成
button = tkinter.Button(text="実行ボタン",command=button_click)
button.place(x=10, y=80)

#ウインドウの描画
app.mainloop()
"""