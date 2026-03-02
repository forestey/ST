import requests

from operator import itemgetter


# 执行API调用并存储响应
url  = r"https://hacker-news.firebaseio.com/v0/topstories.json"
req = requests.get(url)

print("Status code:", req.status_code)

# 处理有关每篇文章的信息
submission_ids = req.json()
print(submission_ids)
submission_dicts = []
for submission_id in submission_ids[:30]:
    # 对于每篇文章，都执行一个API调用
    url = (r"https://hacker-news.firebaseio.com/v0/item/" + str(submission_id) + ".json")
    submission_req = requests.get(url)
    print(submission_req.status_code)
    response_dict = submission_req.json()

    submission_dict = {
        'title': response_dict['title'],
        'link': r"http://news.ycombinator.com/item?id=" + str(submission_id),
        'comments': response_dict.get('descendants', 0),
    }
    submission_dicts.append(submission_dict)

submission_dicts = sorted(submission_dicts, key=itemgetter('comments'), reverse=True)

for submission_dict in submission_dicts:
    print("\nTitle:", submission_dict['title'])
    print("\nDiscussion link:", submission_dict['link'])
    print("\nComments:", submission_dict['comments'])
