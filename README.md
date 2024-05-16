# StyleMate

## Overview
StyleMate is a web application designed to help users effortlessly choose outfits suitable for various occasions . Whether you're heading to work, a casual outing, or a special event, StyleMate has got you covered. Simply input your destination, and StyleMate will curate a stylish ensemble saving you time and effort in deciding what to wear. Here's our project blog post: https://medium.com/@amarachiuvere/how-i-developed-my-very-first-web-application-ever-stylemate-82ef7f087e86

## Features
**Outfit Generation**: Generate outfits tailored to different occasions. Styling is made easy, as only the clothing items you actually have are used in outfit recommendation.

**Wardrobe Description and Management**: Easily manage and categorize your wardrobe items within the application.

## Authors

- [Fortune Peter](https://www.linkedin.com/in/fortune-peter-fullstack-engr?miniProfileUrn=urn%3Ali%3Afs_miniProfile%3AACoAAEko9TYBitrs-_nzfAxEwkNuNtxS5HzSGlg&lipi=urn%3Ali%3Apage%3Ad_flagship3_search_srp_all%3Bxz1DdLiaToSw%2FqkXZ7we1g%3D%3D)

  Software Engineer; Mechanical Engineering Student, Ken Saro-wiwa Polytechnic, Delta State, Nigeria
- [Amarachi Uvere](https://www.linkedin.com/in/amarachiuvereminiProfileUrn=urn%3Ali%3Afs_miniProfile%3AACoAADt7CMwBNm4rgSwg3ENBYEkR6uMjSmQ_fq8&lipi=urn%3Ali%3Apage%3Ad_flagship3_search_srp_all%3BVOW%2BgV30TzOytB0MHcnmow%3D%3D)

  Software Engineer; Civil Engineering Student, Obafemi Awolowo University, Ile-Ife, Osun State, Nigeria
  
## The Story Behind Stylemate
> As part of our learning process at ALx Holberton School of Software Engineering, we were required to come up with an idea for our portfolio project and work on it from start to finish within 2–4 weeks in groups of 2–3.
Several thoughts ran through my head at the time. What would this project be about? What kind of app would I develop? What frameworks and technologies would I use?
Aha! Finally, the idea came.
A styling app.
We would build a web application that, with a minimally detailed description of the user's wardrobe, could recommend a customized outfit to the user. Why did I choose to develop a styling app, out of so many possible project ideas? I'm an engineering student, and often, I get weighed down with assignments and early morning classes. I usually find it an hassle choosing an outfit for the day. At times, I would spend close to thirty minutes rummaging through my wardrobe, eventually settling for a very unfashionable outfit.
I discussed the idea with my teammate, who's also an Engineering student, and he thought it was an awesome idea.
> 
> We started the development process, opting for Python to write the app's core algorithms. We had initially planned to use SQL exclusively for storage, but we later decided to incorporate JSON file storage as well. While we used an SQL database to store the user's clothing items (in other words, the SQL database served as a 'wardrobe'), the JSON files contained the various clothing items that would be made available at the app's front-end. It was nice having an opportunity to hone our skills with SQL, so we didn't completely replace SQL database storage with JSON file storage.
> 
> For the app’s framework, we employed Flask to manage the Application Programming Interface and to render the HTML pages that would be displayed at the front-end. There was the option of using Django framework, but neither of us was conversant with it, hence we chose to leverage on our knowledge of Flask, especially considering the short development time frame. We didn’t have an ever-running web server at our disposal, so we decided the app would be in the form of a repository that the user would clone to his/her computer.The back-end and the Command Line Interface version of the app took roughly a week and a half to build, and it was a long process of coding and iterative testing. The back-end was fully functional before we dived into front-end and API development.
> 
> The two major features of the application are the 'Describe Wardrobe' and the 'Get Outfit Recommendation' features. The former can be accessed upon a click on a button in the Stylemate home page. The user essentially inputs the number of each clothing item displayed in a list on the page and clicks on a button to record the information. The latter feature can be accessed on another page that leads from the home page, where four 'themes' are available to choose from.
In retrospect, I'm amazed at how we went from a place of confusion and uncertainty, to a place where we're able to call a finished app our own. I believe two major factors that contributed to our success in developing the app within the time frame given were time management and adequate planning.
> 
> I would say Stylemate's frontend has a very simple design, which is partially due to the time frame and our moderate level of expertise with UI/UX. We initially aimed for an app that was very simple to use, and we had a result very close to what we wanted, but the UI/UX of the application would certainly benefit from more touch-ups and refining.

## Installation
- Clone repository to your system
- Install the necessary dependencies (using the requirements.txt file)

## Usage
- Make sure your SQL server is up and running
- Run the _setup_mysql.sql_ file in your sql server if you're using the app for the first time
   ```
   sudo cat setup_mysql.sql | mysql -uroot -p
   ```
- Run _reset_user.sh_ if you are using the app for the first time
- Run _set_up.sh_ to start the app's Flask API and web_app in two different tmux sessions
- Navigate to your web browser and enter:
  ```
  http://0.0.0.0:5000
  ```
- Run _end_progam.sh_ in your terminal once you're done
  
  ### Explore the app!
  - Input your name and age in the user login page that comes up on your screen
  - Navigate to the page where you describe your wardrobe by clicking the 'Describe your Wardrobe' button
  - Navigate back to the home page and click the 'Get Outfit Recommendation' to instantly get a customised outfit recommendation
    ![Stylemate](Click2.png)
  

## Contributing
Contributions are welcome! If you'd like to contribute to StyleMate, please follow these steps:
1. Fork the repository.
2. Create your feature branch (`git checkout -b feature/YourFeature`).
3. Commit your changes with descriptive commit messages.(`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature/YourFeature`).
5. Open a pull request.

## Future Features
- [ ] Multiple User
- [ ] Image-based Outfit Recommendation
- [ ] Custom clothing items (input by the user)
- [ ] Colour Matching
- [ ] Outfit Recommendation Outside User Wardrobe

## Notes
If you wish to change your user information, 
- Run _end_program.sh_
- Run _set_up.sh_
- Run _reset_user.sh_
- Navigate to your web browser and enter:
  ```
  http://0.0.0.0:5000
  ```
- You can now input your new information
  
## Licensing 
MIT License
