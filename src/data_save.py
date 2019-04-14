from data_crawler_ import TimeResearcher

def main():
    # 時刻検索オブジェクト
    for flag in [True, False]:
        for hour in range(5, 24):
            for minute in range(0, 60):
                time = {"year":2019, "month":4, "day":15, "hour":hour, "minute":minute}
                time_researcher = TimeResearcher(flag, time)
                time_researcher.research()
                res = time_researcher.get_first_line()
                print("res:", flag, res)


if __name__ == "__main__":
    main()
