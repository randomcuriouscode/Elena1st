# EleNa #1: Elevation Based Navigation

REQUIRED: Python3

### Server:
Setup a virtualenv for the required python modules.
All commands should be run in the project base directory.

If you are using Python 3
```
virtualenv myenv
```
otherwise
```
virtualenv -p <path-to-python-3> myenv 
```
Then activate and install the requirements as follows.

(on MacOS:)
```
source myenv/bin/activate
```
(on Windows:)
```
source myenv\Scripts\activate
```
then
```
pip install -r requirements.txt
```
Run the server.
```
python -m fullstack
```

    
### Client: 
Change your working directory.
```
cd fullstack/client
```
Then run the following commands to setup and run the client.
```
npm install
npm run watch
```
    
Navigate to http://localhost:5000/ and the demo should be up!


### Running tests:

For backend:
```
cd <project-base-dir>
python -m unittest discover tests
```

For frontend:
```
cd fullstack/client
npm run test
```