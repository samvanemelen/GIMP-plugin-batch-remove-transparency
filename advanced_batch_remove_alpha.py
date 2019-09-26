import os, re, glob
from gimpfu import *
from gimpenums import *

def batchremove(file_extension,  source, deepsearch, color) :
    
    #Save original background color to reset at the end, then change background to desired color.
	original_BG = gimp.get_background()
	gimp.set_background(color)

    #If the user wants to search for images in subdirectories a list is composed of all folders to browse.
	dirlist = [source]
	if deepsearch: dirlist = [x[0] for x in os.walk(source)]

	for direct in dirlist:
        #Find all files with defined extension and loop through them.
		glob_result = pdb.file_glob(direct + os.sep + file_extension,  1)
		filecount = glob_result[0]
		for f in glob_result[1]:
			imagefile = f
			try:
                #Load the image, flatten it which replaces alpha channel with the background color and save the image.
				image = pdb.gimp_file_load(imagefile,  imagefile)
				d = pdb.gimp_image_get_active_layer(image)
				pdb.gimp_layer_flatten(d)
				pdb.gimp_file_save(image,  d,  imagefile,  imagefile)
				pdb.gimp_image_delete(image)

			except:
				pdb.gimp_message("Opening Error: " + imagefile)
	
	gimp.set_background(original_BG)
	return
    
register(
	"advanced_batch_remove_alpha",    
	"Advanced settings for removing the alpha channel from multiple files at once.",   
	"A Python Script that offers you more advanced settings for removing transparancy from multiple images. Choose to search for images in subfolders and select the color to replace transparency with. Based on Robotur's basic alpha channel remover.",
	"Sam Van Emelen",
	"Sam Van Emelen",
	"October 2019",
	"<Toolbox>/Layer/Transparency/Batch Remove Alpha",
	"",
	[
		(PF_STRING, "file_extension", "File Extension (optional)", "*.*"),
		(PF_DIRNAME, "source_directory", "Source Directory", ""),
		(PF_BOOL, "search_sub_directories", "Search in Subdirectories", FALSE),
		(PF_COLOR, "BG_color", "Replace Transparancy by:", (0,0,0)),
	],  
	[],
	batchremove,
)

main()