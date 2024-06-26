from pytube import YouTube
import tkinter as tk #basic lib for gui select folder
from tkinter import filedialog
 
def download_video(url,save_path):
    try:
        yt=YouTube(url)
        streams=yt.streams.filter(progressive=True,file_extension="mp4")
        highest_res=streams.get_highest_resolution()
        highest_res.download(output_path=save_path)
        print("video downloaded")
    except Exception as e:
        print(e)


def open_file_dialog():
    folder=filedialog.askdirectory()
    if folder:
        print(f"Selected folder:{folder}")
    return folder


if __name__=="__main__":
    root =tk.Tk()
    root.withdraw()#hides window
    
    vid_url=input("Enter the link: ")
    save_dir=open_file_dialog()

    if save_dir:
        print("Downloading... ")
        download_video(vid_url,save_dir)
        
    else:
        print("Invalid save Location.")

# from pytube import YouTube
# import tkinter as tk
# from tkinter import filedialog, messagebox

# def download_video():
#     url = url_entry.get()
#     save_path = save_dir.get()
#     if not url:
#         messagebox.showerror("Error", "Please enter a valid URL.")
#         return
#     if not save_path:
#         messagebox.showerror("Error", "Please select a save directory.")
#         return
#     try:
#         yt = YouTube(url)
#         streams = yt.streams.filter(progressive=True, file_extension="mp4")
#         highest_res = streams.get_highest_resolution()
#         highest_res.download(output_path=save_path)
#         messagebox.showinfo("Success", "Video downloaded successfully!")
#     except Exception as e:
#         messagebox.showerror("Error", f"Failed to download video: {e}")

# def open_file_dialog():
#     folder = filedialog.askdirectory()
#     if folder:
#         save_dir.set(folder)
#         print(f"Selected folder: {folder}")

# # Define colors and fonts
# bg_color = "#2C2C2C"  # Dark background color
# fg_color = "#FFFFFF"  # White text color
# button_color = "#404040"  # Darker button color
# font_style = ("Arial", 12, "bold")  # Professional font style

# # Set up the main window
# root = tk.Tk()
# root.title("YouTube Video Downloader")
# root.config(bg=bg_color, padx=20, pady=20)

# # URL entry
# tk.Label(root, text="YouTube Video URL:", bg=bg_color, fg=fg_color, font=font_style).grid(row=0, column=0, padx=10, pady=10, sticky="w")
# url_entry = tk.Entry(root, width=50, font=font_style, bg=button_color, fg=fg_color, insertbackground=fg_color)
# url_entry.grid(row=0, column=1, padx=10, pady=10)

# # Save directory
# tk.Label(root, text="Save Directory:", bg=bg_color, fg=fg_color, font=font_style).grid(row=1, column=0, padx=10, pady=10, sticky="w")
# save_dir = tk.StringVar()
# save_dir_entry = tk.Entry(root, textvariable=save_dir, width=50, font=font_style, bg=button_color, fg=fg_color, insertbackground=fg_color)
# save_dir_entry.grid(row=1, column=1, padx=10, pady=10)
# browse_button = tk.Button(root, text="Browse", command=open_file_dialog, font=font_style, bg=button_color, fg=fg_color)
# browse_button.grid(row=1, column=2, padx=10, pady=10)

# # Download button
# download_button = tk.Button(root, text="Download", command=download_video, font=font_style, bg=button_color, fg=fg_color)
# download_button.grid(row=2, column=1, pady=20)

# root.mainloop()
