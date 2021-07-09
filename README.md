# IngressMissionsTool
This is a tool that semi-automates the creation of Ingress Banners.
With this tool you only need to choose the portals without worrying about the "mission settings".
This tool can be used if your Ingress account is linked to the 
It's very easy to use it. Make sure to have the [ChromeDriver](https://chromedriver.chromium.org/downloads) installed as global program and then:
* Clone the repository.
* Read the README.md in the [config folder](https://github.com/Anatras02/IngressMissionsTool/tree/master/config) and create the files.
* Run ` python __init__.py`.
* A browser tab will open and if the file `credentials.yaml` exists it will automatically login otherwise you will have to login manually.
* The tool will create the missions and the only thing you have to do is create the "mission path".
* When every mission is done the tool will stop running.

![Alt Text](assets/example.gif)


### Disclaimer
Read the code to ensure I'm not stealing your credentials. I'm not, but you shouldn't take my word for it. If you don't know how to read it, downloading stuff off the internet and giving it your password is probably a bad idea anyway.
Also it's not mandatory to insert the password (you can manually login) 😃!
