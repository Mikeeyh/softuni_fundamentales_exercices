followers = {}

while True:
    command = input().split(": ")
    action = command[0]

    if action == "Log out":
        break

    if action == "New follower":
        username = command[1]
        if username not in followers:
            followers[username] = {"likes": 0, "comments": 0}

    elif action == "Like":
        username = command[1]
        likes = int(command[2])

        if username not in followers:
            followers[username] = {"likes": likes, "comments": 0}
        else:
            followers[username]["likes"] += likes

    elif action == "Comment":
        username = command[1]

        if username not in followers:
            followers[username] = {"likes": 0, "comments": 1}
        else:
            followers[username]["comments"] += 1

    elif action == "Blocked":
        username = command[1]
        if username in followers:
            del followers[username]
        else:
            print(f"{username} doesn't exist.")

print(f"{len(followers)} followers")

for current_follower, data in followers.items():
    sum_of_likes_and_comments = data["likes"] + data["comments"]
    print(f"{current_follower}: {sum_of_likes_and_comments}")

# New follower: George
# Like: George: 5
# New follower: George
# Log out
