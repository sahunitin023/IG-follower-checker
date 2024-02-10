from bs4 import BeautifulSoup

# followings = []
# followers = []


def get_followings():
    with open('following.html', 'r', encoding='utf-8') as file:
        following_contents = file.read()

    soup = BeautifulSoup(following_contents, 'html.parser')
    followings_list = [tag.getText() for tag in soup.find_all(name='span', class_='_ap3a _aaco _aacw _aacx _aad7 _aade')]
    return followings_list


def get_followers():
    with open('followers.html', 'r', encoding='utf-8') as file1:
        follower_content = file1.read()

    soup1 = BeautifulSoup(follower_content, 'html.parser')
    followers_list = [tag.getText() for tag in soup1.find_all(name='span', class_='_ap3a _aaco _aacw _aacx _aad7 _aade')]
    return followers_list


followers = get_followers()
followings = get_followings()

not_following_accounts = [acc for acc in followings if acc not in followers]
print(not_following_accounts)
