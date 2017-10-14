import pip
import os

def dependencies():
    """Instalando as dependencias do programa"""
    try:
        with open("requirements.txt", "r") as requirements:
            dependencies = requirements.read().splitlines()
    except IOError:
        print ("{}".format("requirements.txt not found, please redownload or do pull request again"))
        exit(1)

    for lib in dependencies:
        pip.main([lib])

def directory() :
	"""Criando os diretorios output/build output/extension"""
        if not os.path.exists("output"):
            os.mkdir('output')
            if os.path.exists("output"):
                output = os.chdir("output")
                os.mkdir('builds')
                os.mkdir('extensions')
                pass
            pass


if __name__== "__main__" : 
    directory()