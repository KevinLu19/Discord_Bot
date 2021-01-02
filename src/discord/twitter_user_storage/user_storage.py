import sqlite3

conn = sqlite3.connect("User.db")
c = conn.cursor()
c.execute("CREATE TABLE IF NOT EXISTS user(usernames text)")

def insert(twitter_usernames):
    check_data = get_desired_username(twitter_usernames)

    if check_data is None:
        print (f"{twitter_usernames} does not exists in the database!")
        return
    else:
        # More pythonic way. No need to constantly commit and close every single insert.
        # It won't work when there's an exception. That is when commit wont go through.
        with conn:
            c.execute("INSERT INTO user VALUES(:usernames)", {"usernames": twitter_usernames})

def filter_out_duplicates():
    c.execute("DELETE FROM user WHERE rowid NOT IN (SELECT MIN(rowid) FROM user GROUP BY usernames)")

def get_desired_username(username):
    c.execute("SELECT * FROM user WHERE usernames=:usernames", {"usernames": username})

    return c.fetchone()

def print_all_entries():
    c.execute("SELECT * FROM user")

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
