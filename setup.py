import pip
import os

def install():

    """Installing as Program Dependencies"""
    try:
        with open("requirements.txt", "r") as requirements:
            dependencies = requirements.read().splitlines()
    except IOError:
        print ("{}".format("requirements.txt not found, please redownload or do pull request again"))
        exit(1)

    for lib in dependencies:

        try:
            pip.main(["install", lib])
        except Exception as e:
            print("Unable to install %s using pip. Please read the instructions for \
        manual installation.. Exiting" % (lib))
            print("Error: %s" % e)

def createfolder() :

	"""Creating the necessary directories output / build output / extension"""

        try:
            folders = ['builds', 'extensions']

            if not os.path.exists("output/") :

                for folder in folders :
                    os.makedirs("output/{}".format(folder)) 

        except OSError as e:
            raise e
            
if __name__== "__main__" : 

    createfolder()
    install()