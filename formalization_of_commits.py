import requests
import json
import datetime


PREFIX = ['LEETCODE', 'GENERATOR', 'TRIANGLE', 'HEXNUMBER', 'REQUESTS']
GROUP = '1013'
ACTION = ['Added', 'Deleted', 'Updated']
TOKEN = ''


headers = {'Authorization': 'token ' + TOKEN}      

def get_all_user_pr(userName = 'vladimirdvd', repos = 'python_au', state = 'all'):
    all_prs = requests.get("https://api.github.com/repos/{}/{}/pulls?state={}".format(userName, repos, state), headers = headers).json()
    return all_prs

def get_all_pr_commits(pr):    
    list_of_commits = requests.get(pr['commits_url'], headers = headers).json()
#    print(pr['commits_url'])
    return list_of_commits

def get_title(dictionary):
    return dictionary['commit']['message']

def check_prefixes(title):
    title = title.replace('-', ' ')
    parsed_title = title.split(' ')
    errors = list()
    if len(parsed_title) < 4:
        return ('Dude...it is not even in right format.')
    if parsed_title[0] not in PREFIX:
        errors.append('Where have you found such homework({})? It is not from {}. \n'.format(parsed_title[0], PREFIX))
    if parsed_title[1] not in GROUP:
        errors.append('There is only one group({}), how could you make mistake here? So, it is definetly not {}. \n'.format(parsed_title[1], GROUP))
    if parsed_title[2] not in ACTION:
        errors.append('Wait...What did you do({})? It is not from {}.'.format(parsed_title[2], ACTION))
    if len(errors) == 0:
      return 'Wow, you are good boy, all is fine'
    else:
      title_errors = '\n'.join(errors)
    return title_errors

def create_pr_comment(title, title_errors):
    return 'VERIFICATION RESULT : \n Hello! \n I am here to help you with making your commit title looks better.\n Now it is: \n {} \n Mistakes: \n {}'.format(title, title_errors)

def send_pr_comment(pr, comment):
    data = {'body': comment,
            'path': requests.get(pr['url']+'/files', headers=headers).json()[0]['filename'],
            'position': 1,
            'commit_id': pr['head']['sha']}
    r = requests.post(pr['url']+'/comments', headers=headers, json=data)
#    print(r.json())

def change_date_format(date):
    date = date[:-1].replace('T', '-')
    date = datetime.datetime(date.split['-'])
    return date

def compare_date(pr):
    counter = 0
    date_of_commit = change_date_dormat(pr['commits_url']['commit']['date'])
    for i in (len(requests.get(pr['url']+'/comments').json) - 1):
      if pr['url'+'/comments'][i+1][body][:19] == 'VERIFICATION RESULT':
          date_of_comment = change_date_format(pr['url'+'/comments'][i]['created_at'])
          delta = date_of_commit - date_of_comment
          if delta.second < 0:
              counter += 1
    if counter > 0:
        return True
    else:
        return False 

def verify_pull_request(pr):
    commits = get_all_pr_commits(pr)
    if compare_date == True:
        comment=''
        i = 0
        for commit in commits:
            title = get_title(commit)
            title_errors = check_prefixes(title)
            if i = 0:
                comment += create_pr_comment(title, title_errors)
            else:
                comment += create_pr_comment(title, title_errors)[98:]
            i += 1
 #           print(comment)
            send_pr_comment(pr, comment)

def main():
    for pr in get_all_user_pr(userName = 'vladimirdvd'):
        print(pr['url']+'/comments')
        verify_pull_request(pr)

if __name__ == '__main__':
    main()
