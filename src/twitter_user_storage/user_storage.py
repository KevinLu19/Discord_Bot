import sqlite3
from typing import NewType

conn = sqlite3.connect("User.db")
c = conn.cursor()
c.execute("CREATE TABLE IF NOT EXISTS user(usernames text)")

def insert(twitter_usernames):
    check_data = get_desired_username(twitter_usernames)

    if check_data is None:
        # More pythonic way. No need to constantly commit and close every single insert.
        # It won't work when there's an exception. That is when commit wont go through.
        with conn:
            c.execute("INSERT INTO user VALUES(:usernames)", {"usernames": twitter_usernames})

        # c.execute("INSERT INTO user VALUES(:usernames)", {"usernames": twitter_usernames})
        # conn.commit()
        message = f"{twitter_usernames} have been added!"

        return message
    else:
        print (f"{twitter_usernames} already exists in the database!")
        message = f"{twitter_usernames} already exists in the database!"

        return message

def delete_entry_from_table(twitter_username):
    check_data = get_desired_username(twitter_username)

    if check_data is None:
        # If the desired username does not exist in the database (null) then we wont try to delete
        # As that will cause an error.
        message = f"{twitter_username} does not exist in database!"

        return message
    else:
        with conn:
            c.execute("DELETE FROM user WHERE usernames=:twitter_username", {"twitter_username": twitter_username})

        message = f"{twitter_username} has been deleted from the database!"

        return message

def update_entry_from_table(old_twitter_name, new_twitter_name):
    check_data = get_desired_username(old_twitter_name)

    if check_data is None:
        message = f"{old_twitter_name} does not exist in the database!"

        return message
    else:
        with conn:
            c.execute("UPDATE user SET usernames=? WHERE usernames=?", (new_twitter_name, old_twitter_name))

        message = f"{old_twitter_name} have been update to {new_twitter_name}."
        return message

def clear_database():
    # USE THIS COMMAND WITH CAUTION. Along with Update command.
    # These are permanent commands.
    with conn:
        c.execute("DELETE FROM user;")

def filter_out_duplicates():
    c.execute("DELETE FROM user WHERE rowid NOT IN (SELECT MIN(rowid) FROM user GROUP BY usernames)")

def get_desired_username(username):
    c.execute("SELECT * FROM user WHERE usernames=:usernames", {"usernames": username})

    return c.fetchone()

def print_all_entries():
    # By default, sqlite3 orders data ascending.
    c.execute("SELECT * FROM user ORDER BY usernames")

    return c.fetchall()

if __name__ == "__main__":
    # user = UserStorage()
    # user.insert("Noahgraphicz")

    # insert("Noahgraphicz")
    # insert("VG_Worklog")
    # s = get_desired_username("VG_Worklog")

    # print (s)

    # get_desired_username("VG_Worklog")

    x = print_all_entries()

    for i in x:
        print (i[0])

    # insert("BewyxAnims")