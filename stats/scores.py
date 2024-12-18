import re
from datetime import datetime

def extract_scores_regex(html):
    pattern = r'class="privboard-position">\s*\d+\)</span>\s*(\d+)'
    return [int(score) for score in re.findall(pattern, html)]

if __name__ == '__main__':
    with open('./data/leaderboard.html') as f:
        html = f.read()
    scores = extract_scores_regex(html)
    print(scores)
    fn = f"./data/{datetime.now().strftime('%Y-%m-%d')}-scores.txt"
    with open(fn, 'w') as f:
        for score in scores:
            f.write(f'{score}\n')

    # make a histogram of the scores
    import matplotlib.pyplot as plt

    # make a collage of 4 by 4 figures with varying number of bins
    fig, axs = plt.subplots(4, 4)
    for i in range(4):
        for j in range(4):
            axs[i, j].hist(scores, bins=5*(i+1)+j)

    plt.show()