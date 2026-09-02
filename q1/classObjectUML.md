# SG4 - Understanding Classes and Objects

## Class Name

TikTokAccount 

## Class Description

The TikTokAccount class represents a user's account on TikTok. It stores basic account information and allows the user to perform actions such as posting videos, gaining followers, and updating their profile.

## Properties

| Property | Data Type | Description |
|---|---|---|
| username | string | The unique username of the TikTok account |
| DisplayName | string | The name displayed on the user's profile |
| followers | int | The number of followers the account has |
| VideosPosted | int | The number of videos posted by the account |


## Methods

| Method | Description |
|---|---|
| postVideo(title: string) | Posts a new video and increases the number of videos posted |
| gainFollowers | Adds a specified number of followers to the account |
| updateProfile(newName: string) | Changes the display name of the account |
| displayInfo() | Displays the account's username, display name, followers, and number of videos |

## Class Diagram
+------------------------------------------------+
|                 TikTokAccount                  |
+------------------------------------------------+
| username : string                              |
| DisplayName : string                           |
| followers : int                                |
| videosPosted : int                             |
|                                                |
+------------------------------------------------+
| postVideo(title : string)                      |
| gainFollowers                                  |
| updateProfile(newName : string)                |
| displayInfo()                                  |
+------------------------------------------------+


## Design Explanation

### Why did you choose this class?

I chose the TikTokAccount class because social media is a common part of my everyday life. I wanted my class to represent an actual user account that can create and manage content on TikTok.

### Which property is the most important? Why?

I think username is the most important property because it allows other users to recognize and find the account on the platform.

### Which method is the most useful? Why?

I think postVideo(title: string) is the most useful method because posting videos is one of the main actions performed on TikTok. 