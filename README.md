# Advanced Batch Alpha Channel Remover
This GIMP plugin is designed for people who have a bunch of images with transparency and need to replace this with a color of their choice. many tools set the color to a default black or white when converting file formats but none offer you a choice. This plugin is developed for those who do.

The foundation of the comes from the author of [this Reddit post](https://www.reddit.com/r/GIMP/comments/xcep2/how_to_remove_alpha_channel_from_a_ton_of_images/). His work has been expanded on for more functionality and ease of use.

## How to install
Download the 'advanced_batch_remove_alpha.py' file and paste it into the 'plug-ins' folder of your GIMP installation. On my installation this was at: 
"C:\Program Files\GIMP 2\lib\gimp\2.0\plug-ins\"
After restarting GIMP the tool will be available under Layer > Transparency > Batch Remove Alpha Advanced

## How to use
1. Select the file extension of the images you want to remove the background from (or leave at \*.* to try for all files)
2. Select the folder where the images are located
3. Choose whether you want to process all images in every sub directory or only the images in the first folder.
4. Choose a color to replace the transparency with.
5. Run the tool.

![batch remove alpha advanced](https://user-images.githubusercontent.com/36103001/65701771-2a350980-e082-11e9-9cc9-86c4e3e603ea.PNG)
## How to contribute
The best way to contribute to the tool is by testing and using the plugin and report any issues or malfunctions. If you can find ways to improve the utility of the tool you will definitely contribute by sharing your thoughts!