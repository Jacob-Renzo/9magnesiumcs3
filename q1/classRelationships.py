class TikTokAccount:
    def __init__(self, username, displayName):
        self.username = username
        self.displayName = displayName
        self.facebook = None

    def linkFacebook(self, facebook):
        self.facebook = facebook

    def displayInfo(self):
        print("TikTok:", self.username)
        print("Name:", self.displayName)


class FacebookAccount:
    def __init__(self, username, Name):
        self.username = username
        self.Name = Name

    def displayInfo(self):
        print("Facebook:", self.username)
        print("Name:", self.Name)


# Create objects
tiktok = TikTokAccount("juan_milyon", "Juan Batumbakal")
facebook = FacebookAccount("nauJ lakabmutaB", "Juan Batumbakal")

# BEFORE RELATIONSHIP
print("--- BEFORE RELATIONSHIP ---")
tiktok.displayInfo()
facebook.displayInfo()

# BUILD RELATIONSHIP
print("\n--- BUILDING RELATIONSHIP ---")
tiktok.linkFacebook(facebook)
print("Facebook account linked!")

# AFTER RELATIONSHIP
print("\n--- AFTER RELATIONSHIP ---")
print("TikTok account:", tiktok.username)
print("Linked Facebook account:", tiktok.facebook.username)
print("Name:", tiktok.facebook.Name)