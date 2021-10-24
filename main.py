# task1.変数の使い方

name1: str = "シンジ"
name2: str = "カヲルくん"

print("{}と{}は仲良し！".format(name1, name2))

# task2.if文の使い方

if name2 == "使徒":
    print("使徒です！")

# task3.配列の使い方

names: list = ["シンジ", "レイ", "カヲルくん"]     
names.append("アスカ")

# task4.for文の使い方

for name in names:
    print(name)

# task5.関数の使い方

def name_a():
    names: list = ["シンジ", "レイ", "カヲルくん"]  
    names.append("アスカ")
    for name in names:
        print(name)    

name_a()

# task6.引数を使う関数の使い方

def name_b(mari):
    names: list = ["シンジ", "レイ", "カヲルくん"]  
    names.append("アスカ")
    names.append(mari)
    for name in names:
        print(name)

name_b("マリ")

# 文字検索

input_name = input("名前を入力してください:")

if input_name in names:
    print("{}はいます。".format(input_name))
else:
    print("{}はいません。".format(input_name))    


