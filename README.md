# StyleMate

## Overview
StyleMate is a web application designed to help users effortlessly choose outfits suitable for various occasions . Whether you're heading to work, a casual outing, or a special event, StyleMate has got you covered. Simply input your destination, and StyleMate will curate a stylish ensemble saving you time and effort in deciding what to wear. Here's our project blog post: https://medium.com/@amarachiuvere/how-i-developed-my-very-first-web-application-ever-stylemate-82ef7f087e86

## Features
<!-- - **Outfit Generation**: Generate outfits tailored to different occasions. Styling is made easy, as only the clothing items you actually have are used in outfit recommendation. -->
<!-- - **Wardrobe Description and Management**: Easily manage and categorize your wardrobe items within the application. -->
- **Favorites**: Save your favorite outfits for future reference or inspiration.
- **User-friendly Interface**: StyleMate offers an intuitive and visually appealing interface for seamless navigation.

## Authors

- [Fortune Peter](https://www.linkedin.com/in/fortune-peter-fullstack-engr?miniProfileUrn=urn%3Ali%3Afs_miniProfile%3AACoAAEko9TYBitrs-_nzfAxEwkNuNtxS5HzSGlg&lipi=urn%3Ali%3Apage%3Ad_flagship3_search_srp_all%3Bxz1DdLiaToSw%2FqkXZ7we1g%3D%3D)
- [Amarachi Uvere](https://www.linkedin.com/in/amarachiuvere?miniProfileUrn=urn%3Ali%3Afs_miniProfile%3AACoAADt7CMwBNm4rgSwg3ENBYEkR6uMjSmQ_fq8&lipi=urn%3Ali%3Apage%3Ad_flagship3_search_srp_all%3BVOW%2BgV30TzOytB0MHcnmow%3D%3D)

## Installation
- Clone repository to your system
- Install the necessary dependencies (using the requirements.txt file)

## Usage
- Make sure your SQL server is up and running
- Run the _setup_mysql.sql_ file in your sql server
   ```
   sudo cat setup_mysql.sql | mysql -uroot -p
   ```
- Run _reset_user.sh_ if you are using the app for the first time
- Run _set_up.sh_ to start the app's Flask API and web_app in two different tmux sessions
- Navigate to your web browser and enter:
  ```
  http://0.0.0.0:5000
  ```
- Explore the app!

  

## Contributing
Contributions are welcome! If you'd like to contribute to StyleMate, please follow these steps:
1. Fork the repository.
2. Create your feature branch (`git checkout -b feature/YourFeature`).
3. Commit your changes with descriptive commit messages.(`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature/YourFeature`).
5. Open a pull request.
