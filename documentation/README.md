# Documentation

The purpose of this project is to provide a web application that allows a user to incorporate elevation into the routes they search for.

The client consists of two main components: 

* The input form allows the user to input their options to the appplication. These options include the coordinates from and to which they want to navigate, whether they want to maximize or minimize elevation, and the percent flexibility. The percent flexibility corresponds to the percent of the shortest path that they are willing to add on to their journey in order to minimize or maximize elevation. 
* The map component renders the route for the user upon submission. It also allows the user to click on the map to pick the locations they wish to travel between. 

Currently, the application only works for the Amherst area, since using more points would require much more data and powerful servers.

The app is hosted locally and set-up directions can be found in the README.md file in the top-level directory.

Sample Usage 1:
1. The user enters "42.40875563883781" in the "From Latitude" text input box.
2. The user enters "-72.53058761358263" in the "From Longitude" text input box.
3. The user enters "42.40444610741265" in the "To Latitude" text input box.
4. The user enters "-72.51513808965684" in the "To Longitude" text input box.
5. The user moves the slider to 150%.
6. The user selects the "Minimize elevation" radio button.
7. The user clicks the "Calculate Route" button.
8. The map renders a purple route corresponding to the correct navigation directions. The webpage will also display the distance and elevation gain of the route to the user.

Sample Usage 2:
1. The user clicks the "Select From" button.
2. The user clicks on the map in the Amherst area for the location from which they wish to travel.
3. The user clicks the "Select To" button.
4. The user clicks on the map in the Amherst area for the location to which they wish to travel.
5. The user moves the slider to 150%.
6. The user selects the "Minimize elevation" radio button.
7. The user clicks the "Calculate Route" button.
8. The map renders a purple route corresponding to the correct navigation directions. The webpage will also display the distance and elevation gain of the route to the user.

The route is found as follows:
1. The inputs are passed to the server as query params in a GET request.
2. The server sends the From and To coordinates, and the distance flexibility value to the Pathfinder component.
3. The Pathfinder returns all paths of length less than x% of the shortest path; where x is the distance flexibility value.
4. The server then chooses the path with the greatest or least elevation gain (as per the input) and returns that path to the client.

The algorithm used to find the candidate paths is a modified implementation of the Lawler improvement to [Yen's algorithm](https://en.wikipedia.org/wiki/Yen%27s_algorithm).

The backend is implemented entirely in Python.  
The front end is powered by React.js and styled with Bootstrap. The call to the backend is made with Ajax. The tests are written with Jest and Enzyme. Everything is bundled with webpack.
