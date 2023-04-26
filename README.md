# Instagram Post Creator

This Python script uses Selenium to automate the process of creating a post on Instagram. The script logs in to your account, selects the option to create a new post, uploads photos from a folder, adds a caption from a text file, and publishes the post.

## Installation

1. Clone the repository.
2. Install the required packages using pip:  
`pip install selenium`
3. Download the geckodriver for Firefox and add it to your PATH:  
https://github.com/mozilla/geckodriver/releases

4. Create a folder called "photos" in the root directory of the project.
5. Add a subfolder to the "photos" folder with the name of the day you want to create the post for in the format "dd" (e.g. "01" for the 1st of the month).
6. Add the photos you want to post to the subfolder you created in step 5.
7. Add a text file to the subfolder you created in step 5 with the name of the day you want to create the post for in the format "dd.txt" (e.g. "01.txt" for the 1st of the month) and add the caption for your post.

## Usage

1. Open the `main.py` file and edit the `username` and `password` variables with your Instagram login credentials.
2. Run the script:
3. The script will log in to your account, create a new post using the photos and caption from the subfolder you created in the "photos" folder, and publish the post.

Note: The script waits for a few seconds between each step to give time for the page to load. If the script doesn't work as expected, you can increase the waiting time in the relevant parts of the code.
