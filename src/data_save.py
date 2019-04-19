from data_crawler_ import TimeResearcher
import csv
import os

def main():
    flags = [True, False]
    # files = ["../data/Fuda-Shinjuku-via-Chofu/Fuda-Shinjuku-via-Chofu", "../data/Fuda-Shinjuku/Fuda-Shinjuku"]
    files = ["../data/Ashigara-Shinjuku-via-Hotaruda/Ashigara-Shinjuku-via-Hotaruda", "../data/Ashigara-Shinjuku-via-Odawara/Ashigara-Shinjuku-via-Odawara"]

    for flag, _file in zip(flags, files):
        for hour in range(4, 25):
            __file = _file + "_%02d.csv"%hour
            with open(__file, "w") as f:
                writer = csv.writer(f, lineterminator="\n")
                for minute in range(0, 60):
                    time = {"year":2019, "month":4, "day":15, "hour":hour, "minute":minute}
                    time_researcher = TimeResearcher(flag, time)
                    time_researcher.research()
                    res = time_researcher.get_first_line()
                    writer.writerow(res)
                    print(res)


if __name__ == "__main__":
    main()
