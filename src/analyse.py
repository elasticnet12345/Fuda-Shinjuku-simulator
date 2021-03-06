import numpy as np
import os
import csv
import matplotlib.pyplot as plt
import japanize_matplotlib







def convert_minute(s):
    """ 時間から分にする
    """
    s = s.replace("時間", ":").replace("分",":").split(":")
    h, m = int(s[0]), int(s[1])
    return h * 60 + m





def main():
    """ 
        1. 記録用の配列用意
        2. 経路(調布経由するか？)の指定
            A. 時間(hour)の指定. 各csvには[0, 59]の60個のデータがある
                a. csvの各行の1セル目から所要時間(minutes)を抽出する
        3. それぞれの経路の所要時間を赤線と緑線でplotする
    """ 
    memo = {}
    # names_ = ["Fuda-Shinjuku", "Fuda-Shinjuku-via-Chofu"]
    names_ = [name for name in os.listdir("../data/") if "Ashigara" in name and "Shinjuku" in name]

    for name in names_:
        path_dir = os.path.join("../data", name)
        tmp = []
        for hour in range(4, 24):
            name_csv = name + "_%02d.csv"%hour
            path_csv = os.path.join(path_dir, name_csv)
            with open(path_csv, "r") as f:
                reader = csv.reader(f)
                for minute, line in zip(range(0, 60), reader):
                    leaving_hour, leaving_minute = int(line[1][:2]), int(line[1][3:5])# 出発時刻(h)
                    try:
                        #required_time = int(line[1][-3:-1])
                        _tmp = line[1][11:]
                        required_time = convert_minute(_tmp)

                    except:
                        print("error:", line[1])
                        print("error:", line[1][11:])
                        exit()

                    # print(name, hour, minute, required_time)
                    if hour == leaving_hour:
                        required_time += leaving_minute - minute
                    else:
                        required_time += (60 + leaving_minute) - minute
                    tmp.append(required_time)
        tmp = np.array(tmp)
        memo[name] = tmp

    colors_ = ["red", "green"]
    # labels_ = ["布田--新宿", "布田--調布--新宿"]
    # labels_ = ["足柄-新松田", "足柄-小田原-新松田"]
    labels_ = ["足柄-新宿", "足柄-小田原-新宿"]
    for name, y in memo.items():
        x = np.arange(60*20)
        plt.plot(x, y, color=colors_[names_.index(name)], label=labels_[names_.index(name)])


    interval = 2
    xtick = np.array([str(hour) + "時" for hour in range(4, 25, interval)])
    locs = np.linspace(0, (24-4)*60, len(xtick))
    plt.xticks(locs, xtick, rotation="30")
    plt.xlabel("時刻")
    plt.ylabel("所要時間(分)")
    # plt.title("新宿駅までの所要時間")
    # plt.title("新松田までの所要時間")
    plt.title("新宿までの所要時間")
    plt.legend(loc="best")
    plt.show()
                    


if __name__ == "__main__":
    main()
