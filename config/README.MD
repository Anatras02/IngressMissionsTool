# Config Files
The config of this code use [YAML Language](https://en.wikipedia.org/wiki/YAML)
### login.yaml (optional)
In this file you can put the Facebook credentials in order to automatically login when the tool starts working.
If you don't put them you will have to login manually when the tool starts. 
* **email**: your_email
* **password**: your_password

Example:
``` yaml
email: john.doe@example.com
password: _johnDoe1953!
```

### missions.yaml
In this file you have to put the mission settings
* **mission_type**: SEQUENTIAL | ANY ORDER
* **number_of_missions**: The total number of missions in the banner
* **title**: The missions title, use %d to represent the mission number and %n to represent the number of missions
* **description**: The missions description, use %d where you want to use the mission number
* **path_logo**: The path of the missions logo, each image has to have to same name with the difference in the mission number that in the path_logo has to be %d
* **location** (*optional*): The location where your missions will be (it will be searched on the maps when creating the "mission path"). If missing the location won't be searched.
* **passphrase_first_mission** (*optional*): The first portal passphrase. This will be the question and the answer will automatically be the mission number (for the users to check if they are doing the right mission)

Example:
``` yaml
mission_type: SEQUENTIAL
number_of_missions: 128
title: Amazing Banner %d/%n
description: This banner is amazing! This mission is the number %d 
path_logo: /home/anatras02/Documents/banner/mission-set-%d.png
location: Viareggio
passphrase_first_mission: Which mission are you doing?
```
