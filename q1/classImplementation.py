class TikTokAccount:
    def __init__(self, username, displayName, followers, videosPosted):
        self.username = username
        self.displayName = displayName
        self.followers = followers
        self.__videosPosted = videosPosted

    def postVideo(self, title):
        self.__videosPosted += 1
        print(self.username, "posted:", title)

    def gainFollowers(self, amount):
        self.followers += amount

    def updateProfile(self, newName):
        self.displayName = newName

    def displayInfo(self):
        print("Username:", self.username)
        print("Display Name:", self.displayName)
        print("Followers:", self.followers)
        print("Videos Posted:", self.__videosPosted)


# Two objects
account1 = TikTokAccount("j.cooo", "Jacob Renzo", 500, 10)
account2 = TikTokAccount("krishpy_kremee", "Krishna", 800, 15)

# BEFORE
print("BEFORE")
account1.displayInfo()
print()
account2.displayInfo()

# Change only account1
print("\nACTION")
account1.postVideo("My New Video")
account1.gainFollowers(100)

# AFTER
print("\nAFTER")
account1.displayInfo()
print()
account2.displayInfo()