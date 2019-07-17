# L-System

This is a library that will generate random LSystems, let you classify them into good and bad
and then it will generate new ones based on how you classified them. To run this program first generate some candidates With


generate_random_systems.py
Once these are generated, classify them (with their text file) into generated/good and generated/bad.

Then (I think the script is missing?) You need to stick the numerical features into a dataset using get_feature_vec
and now you can use the notebook to train a classifier. Now the main script generate_random_systems will use that classifier to
generte images with a high probability. 


main.py/plot_blender.py are scripts that will help you view these as 3d models in blender.
