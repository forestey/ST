import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS



# 执行API调用并存储响应
url = r'https://api.github.com/search/repositories?q=language:python&sort=stars'
req = requests.get(url)
print("Status code:", req.status_code)

# 将API响应存储在一个变量中
response_dict = req.json()
print("Total repositories:", response_dict['total_count'])

# 处理结果
# print(response_dict.keys())
# print(response_dict['total_count'])
# print(response_dict['items'])

# 研究有关仓库的信息
repo_dicts = response_dict['items']
print("Number of items:", len(repo_dicts))

names, plot_dicts = [], []
for repo_dict in repo_dicts:
    names.append((repo_dict['name']))
    plot_dict = {
        'value': repo_dict['stargazers_count'],
        'label': repo_dict['description'],
        'xlink': repo_dict['html_url'],
    }
    plot_dicts.append(plot_dict)

# 可视化
my_style = LS('#333366', base_style=LCS)
my_config = pygal.Config()
my_config.x_label_rotation = 45
my_config.show_legend = False
my_config.title_font_size = 24
my_config.label_font_size = 14
my_config.major_label_font_size = 18
my_config.truncate_label = 15
my_config.show_y_guides = False
my_config.width = 1000
chart = pygal.Bar(my_config, style=my_style)
chart.title = "Python Projects on Github"
chart.x_labels = names
chart.add('', plot_dicts)
chart.render_to_file('python_repos.svg')

# print("Repositories returned:", len(repo_dicts))
# names, stars = [], []
# for repo_dict in repo_dicts:
#     names.append(repo_dict['name'])
#     stars.append(repo_dict['stargazers_count'])
# 可视化
# my_style = LS('#333366', base_style=LCS)
# my_config = pygal.Config()
# my_config.x_label_rotation = 45
# my_config.show_legend = False
# my_config.title_font_size = 24
# my_config.label_font_size = 14
# my_config.major_label_font_size = 18
# my_config.truncate_label = 15
# my_config.show_y_guides = False
# my_config.width = 1000
# chart = pygal.Bar(my_config, style=my_style)
# chart.title = "Python Projects on Github"
# chart.x_labels = ['httpie', 'diango', 'flask']
# plot_dicts = [
#     {'value': 16101, 'label': 'Description of httpie.'},
#     {'value': 15028, 'label': 'Description of django.'},
#     {'value': 14798, 'label': 'Description of flask.'},
# ]
# chart.add('', plot_dicts)
# chart.render_to_file('bar_descriptions.svg')


# repo_dict = repo_dicts[0]
# # print("Repo_Dict:", repo_dict)
# # print("\nKeys:", len(repo_dict))
# for key in sorted(repo_dict.keys()):
#     print(key)
# print("\nSelected information about first repository:")
# print('Name:', repo_dict['name'])
# print('Owner:', repo_dict['owner']['login'])
# print('Stars:', repo_dict['stargazers_count'])
# print('Repository:', repo_dict['html_url'])
# print('Created:', repo_dict['created_at'])
# print('Updated:', repo_dict['updated_at'])
# print('Description:', repo_dict['description'])


