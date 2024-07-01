import instaloader
import re

def extract_shortcode(link):
    # Extract shortcode from the link using regex
    match = re.search(r'/reel/([^/]+)/', link)
    if match:
        return match.group(1)
    else:
        raise ValueError("Invalid Instagram Reel URL")
    

#----------------------------------------------------------------------------------#



def download_instagram_reel(link, save_path):
    # Create an instance of Instaloader
    loader = instaloader.Instaloader(dirname_pattern=save_path)

    try:
       
        shortcode = extract_shortcode(link)

        # Load the post using the shortcode
        post = instaloader.Post.from_shortcode(loader.context, shortcode)

       
        if post.is_video:
            # Download the post
            loader.download_post(post, target=f"{save_path}/{post.owner_username}_reels")
            print(f"Reel from {post.owner_username} has been downloaded at the highest quality.")
        else:
            print("The provided link does not point to a Reel (video) post.")
    except instaloader.exceptions.InstaloaderException as e:
        print(f"An error occurred: {e}")