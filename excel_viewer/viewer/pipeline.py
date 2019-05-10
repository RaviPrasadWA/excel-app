import requests
from django.shortcuts import redirect


def save_profile(backend, user, response, *args, **kwargs):

    def get_data(key, fetch_url=True):
        if fetch_url:
            resp = requests.get(response.get(key))
        else:
            resp = response.get(key)
        return resp

    repos_links = get_data("repos_url")
    followers = get_data("followers_url")
    subscriptions = get_data("subscriptions_url")

    public_repos_count = get_data("public_repos", fetch_url=False)
    followers_count = get_data("following", fetch_url=False)

    email = get_data("email", fetch_url=False)

    github_data = {"repos_links": repos_links,
                   "followers": followers,
                   "subscriptions": subscriptions,
                   "public_repos_count": public_repos_count,
                   "followers_count": followers_count,
                   "email": email}
    print(github_data)

    return redirect("github_detail",
                    data=github_data)
