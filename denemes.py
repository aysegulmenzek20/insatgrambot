import instaloader
import json


L = instaloader.Instaloader()


USERNAME = "activite_20"  
PASSWORD = "DaX3S%zy4z=#D,_"

try:
    L.load_session_from_file(USERNAME)
except FileNotFoundError:
    L.login(USERNAME, PASSWORD) 
    L.save_session_to_file()  

target_username = "etkinlik_denizli"


profile = instaloader.Profile.from_username(L.context, target_username)

posts_data = []

for post in profile.get_posts():
    post_info = {
        "post_id": post.shortcode,
        "post_url": f"https://instagram.com/p/{post.shortcode}/",
        "profile_url": f"https://www.instagram.com/{target_username}/",
        "date": str(post.date),
        "likes": post.likes,
        "comments": post.comments,
        "caption": post.caption,
        "tagged_users":  [user for user in post.tagged_users],
        "thumbnail_image": post.url
    }
    posts_data.append(post_info)

  
  

with open("instagram_monitor.json", "w", encoding="utf-8") as json_file:
    json.dump(posts_data, json_file, ensure_ascii=False, indent=4)


print("Instagram post bilgileri 'instagram_posts.json' dosyasına kaydedildi.")
