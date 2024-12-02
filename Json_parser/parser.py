import json
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


if __name__ == '__main__':

    with open('result.json', 'r') as file:
        ans = json.load(file)

    ans = [int(x["date_unixtime"]) for x in ans["messages"]]
    ans = np.array(ans[1:])
    ans = sorted(np.diff(ans))
    print(len(ans))

    print("Среднее:")
    print(np.mean(ans))
    print("Медиана:")
    print(ans[len(ans)//2])

    sns.displot(ans, kde=True)
    plt.ylabel("Количество")
    plt.xlabel("Время ответа в секундах")
    plt.show()