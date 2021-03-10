import requests


"""
sample failing links
2021-02-24T17:37:27.8831304Z Link 'https://github.com/ripple/rippled/pull/2013' in page out/2017/rippled-0.60.0.html is still down.
2021-02-24T17:37:27.8833005Z Testing remote link 'https://github.com/ripple/rippled/pull/1983'
2021-02-24T17:37:27.8834278Z ... Broken remote link in out/2017/rippled-0.60.0.html to 'https://github.com/ripple/rippled/pull/1983'
2021-02-24T17:37:27.8836275Z Link 'https://github.com/ripple/rippled/pull/1983' in page out/2017/rippled-0.60.0.html is still down.
2021-02-24T17:37:27.8839667Z Link 'https://github.com/ripple/rippled/pull/1993' in page out/2017/rippled-0.60.0.html is back online
2021-02-24T17:37:27.8841336Z Testing remote link 'https://github.com/ripple/rippled/pull/1995'
2021-02-24T17:37:27.8842593Z ... Broken remote link in out/2017/rippled-0.60.0.html to 'https://github.com/ripple/rippled/pull/1995'
2021-02-24T17:37:27.8844238Z Link 'https://github.com/ripple/rippled/pull/1995' in page out/2017/rippled-0.60.0.html is still down.
2021-02-24T17:37:27.8845346Z Testing remote link 'https://github.com/ripple/rippled/pull/2014'
2021-02-24T17:37:27.8846953Z ... Broken remote link in out/2017/rippled-0.60.0.html to 'https://github.com/ripple/rippled/pull/2014'
2021-02-24T17:37:27.8847936Z Link 'https://github.com/ripple/rippled/pull/2014' in page out/2017/rippled-0.60.0.html is still down.
2021-02-24T17:37:27.8848790Z Testing remote link 'https://github.com/ripple/rippled/pull/1997'
2021-02-24T17:37:27.8849681Z ... Broken remote link in out/2017/rippled-0.60.0.html to 'https://github.com/ripple/rippled/pull/1997'
2021-02-24T17:37:27.8850639Z Link 'https://github.com/ripple/rippled/pull/1997' in page out/2017/rippled-0.60.0.html is still down.
021-02-24T17:37:29.9731503Z ... Broken remote link in out/2018/rippled-1.1.0.html to 'https://github.com/ripple/rippled/pull/2532/commits/2ac1c2b433b8825b9a6f203f1ee65a126e20620c'
2021-02-24T17:37:29.9736228Z Link 'https://github.com/ripple/rippled/pull/2532/commits/2ac1c2b433b8825b9a6f203f1ee65a126e20620c' in page out/2018/rippled-1.1.0.html is still down.
2021-02-24T17:37:29.9739653Z Testing remote link 'https://github.com/ripple/rippled/pull/2650/commits/04745b11a888cea412f410d0036a0db23574d61c'
2021-02-24T17:37:30.0393902Z ... Broken remote link in out/2018/rippled-1.1.0.html to 'https://github.com/ripple/rippled/pull/2650/commits/04745b11a888cea412f410d0036a0db23574d61c'
2021-02-24T17:37:30.0396206Z Link 'https://github.com/ripple/rippled/pull/2650/commits/04745b11a888cea412f410d0036a0db23574d61c' in page out/2018/rippled-1.1.0.html is still down.
2021-02-24T17:37:30.0398062Z Testing remote link 'https://github.com/ripple/rippled/pull/2532/commits/7d163a45dcd2c5cca0fc45eb8775f169575995c1'
2021-02-24T17:37:30.1059028Z ... Broken remote link in out/2018/rippled-1.1.0.html to 'https://github.com/ripple/rippled/pull/2532/commits/7d163a45dcd2c5cca0fc45eb8775f169575995c1'
2021-02-24T17:37:30.1061478Z Link 'https://github.com/ripple/rippled/pull/2532/commits/7d163a45dcd2c5cca0fc45eb8775f169575995c1' in page out/2018/rippled-1.1.0.html is still down.
2021-02-24T17:37:30.1066290Z Testing remote link 'https://github.com/ripple/rippled/pull/2566/commits/34d3f93868b87f33fdf76a5b6c8b376956346a16'
2021-02-24T17:37:30.1772210Z ... Broken remote link in out/2018/rippled-1.1.0.html to 'https://github.com/ripple/rippled/pull/2566/commits/34d3f93868b87f33fdf76a5b6c8b376956346a16'
2021-02-24T17:37:30.1773970Z Link 'https://github.com/ripple/rippled/pull/2566/commits/34d3f93868b87f33fdf76a5b6c8b376956346a16' in page out/2018/rippled-1.1.0.html is still down.
2021-02-24T17:37:30.1777635Z Testing remote link 'https://github.com/ripple/rippled/pull/2586/commits/5b733fb4857ff1076d2e106afeb9931fca198d51'
2021-02-24T17:37:30.2466313Z ... Broken remote link in out/2018/rippled-1.1.0.html to 'https://github.com/ripple/rippled/pull/2586/commits/5b733fb4857ff1076d2e106afeb9931fca198d51'
"""

sample_links = ['https://github.com/ripple/rippled/pull/1983',
                'https://github.com/ripple/rippled/pull/1995', 'https://github.com/ripple/rippled/pull/1997', 'https://github.com/ripple/rippled/pull/2532/commits/2ac1c2b433b8825b9a6f203f1ee65a126e20620c', 'https://github.com/ripple/rippled/pull/2650/commits/04745b11a888cea412f410d0036a0db23574d61c', 'https://github.com/ripple/rippled/pull/2532/commits/7d163a45dcd2c5cca0fc45eb8775f169575995c1', 'https://github.com/ripple/rippled/pull/2566/commits/34d3f93868b87f33fdf76a5b6c8b376956346a16', 'https://github.com/ripple/rippled/pull/2586/commits/5b733fb4857ff1076d2e106afeb9931fca198d51']

for link in sample_links:
    for i in range(2000):
        github_request = requests.get(link)
        if github_request.status_code != 200:
            print("Ooops an error occured, code= ", github_request.status_code)
            raise requests.RequestException

print(f'completed without any error')
