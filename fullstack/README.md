# Running the Web App

### Server:
1. cd into Elena1st/fullstack/server
2. Run the following commands:
	
	`source firstenv/bin/activate`
    `pip install -r requirements.txt`
	`python server.py`
    
### Client: 
1. cd into Elena1st/fullstack/client
2. Run the following commands:

	`npm install`
    
    `npm run watch`
    
Navigate to http://localhost:5000/ and the demo should be up!

In order to add functionality to the server, check Elena1st/fullstack/server/server.py for the route which currently prints out the values received from the client. Clicking the submit button in the client will trigger this function, so you can take that information and use it to calculate routes and things.
