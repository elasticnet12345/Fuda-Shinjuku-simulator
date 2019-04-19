import numpy as np
import os
import csv
import matplotlib.pyplot as plt
import japanize_matplotlib















def main():
    """ 
        1. 記録用の配列用意
        2. 経路(調布経由するか？)の指定
            A. 時間(hour)の指定. 各csvには[0, 59]の60個のデータがある
                a. csvの各行の1セル目から所要時間(minutes)を抽出する
        3. それぞれの経路の所要時間を赤線と緑線でplotする
    """ 
    memo = {}
    names_ = ["Fuda-Shinjuku", "Fuda-Shinjuku-via-Chofu"]
    for name in names_:
        path_dir = os.path.join("../data", name)
        tmp = []
        for hour in range(4, 24):
            name_csv = name + "_%02d.csv"%hour
            path_csv = os.path.join(path_dir, name_csv)
            with open(path_csv, "r") as f:
                reader = csv.reader(f)
                for minute, line in zip(range(0, 60), reader):
                    required_time = line[1][-3:-1]
                    # print(name, hour, minute, required_time)
                    tmp.append(int(required_time))
        tmp = np.array(tmp)
        memo[name] = tmp

    colors_ = ["red", "green"]
    labels_ = ["布田--新宿", "布田--調布--新宿"]
    for name, y in memo.items():
        x = np.arange(60*20)
        plt.plot(x, y, color=colors_[names_.index(name)], label=labels_[names_.index(name)])


    interval = 2
    xtick = np.array([str(hour) + "時" for hour in range(4, 25, interval)])
    locs = np.linspace(0, (24-4)*60, len(xtick))
    plt.xticks(locs, xtick, rotation="30")
    plt.xlabel("時刻")
    plt.ylabel("所要時間(分)")
    plt.title("新宿駅までの所要時間")
    plt.legend(loc="best")
    plt.show()
                    


if __name__ == "__main__":
    main()
