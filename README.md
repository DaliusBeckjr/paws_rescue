# paws_rescue

![screenshot](Rescues_pic.png)

## Description
video to project: <br/>
[link to video](https://youtu.be/BtnIjh7Jxy8)
<br />
this project is made from the idea of starting a pet rescue website where the user is able to register a rescue and even adopt a rescue from the site.
This project was thought of from my past passion of working at a pet hospital and seeing other rescues at our hospital not having a place to go and we didn't have a website where we could register our own rescue site or a site for other's to see and adopt a pet.

### Main function
the main function the website does is based on CRUD methods 
- user is able to login and register if not the correct information. the user is given a warning that the credentials are incorrect
- user is able to create/ register a new rescue in the list of rescues
- main user is also able to delete and edit the rescue's information if anything is wrong
- if the rescue doesn't belong to the user, that user cannot edit nor delete the information of that designated Rescue
- Site also has protection where user not in session cannot go into the other pages without being in session

### Technologies Used:
<ul>
    <li> Python (flask) </li>
    <li> MySQL (Workbench)</li>
    <li> Bootstrap 5 (html, css, sass)</li>
</ul>

### Challenges
A challenge I was facing was adding in the petfinder api.
It was using curl to get the bearer key token and I want to find a way around it or maybe just deal with it in another ongoing battle.

### Future Ideas
change the UI more make it more diverse and even use a website for inspiration of creating these ideas

## How to run 

### Activate shell
```sh
pipenv shell
```

### Run The Project
```sh
python3 server.py
```
### Deactivate Shell
```sh
deactivate
```

