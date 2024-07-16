from flask import Flask #importing flask libraries

app = Flask(__name__) #configuring app settings

@app.route('/') #main route
def main():
	  return("<html><head><title>Fit Pics!!!</title></head><body><p>List of fits:</p><a href='/a$aprocky'>A$AP Rocky</a><p> </p><a href = '/lilyachty'>lil yachty</a><p> </p><a href = '/bakar'>Bakar</a><p> </p><a href = '/sampha'>Sampha</a><p> </p></body></html>") #returns html page in the browser

@app.route('/a$aprocky') #ASAP route
def ASAP():
	return ("<html><p>This is the A$AP Rocky fit!</p><img src = 'asappic.jpeg'></html>")

@app.route('/lilyachty') #yachty route
def YACHTY():
	return ("<html><p>This is the lil yacthy fit!</p><img src = 'yachtypic.jpeg'></html>")

@app.route('/bakar') #bk route
def BAKAR():
	return ("<html><p>This is the Bakar fit!</p><img src = 'bakarpic.png'></html>")

@app.route('/sampha') #Sampha route
def SAMPHA():
	return ("<html><p>This is the Sampha fit!</p><img src = 'samphapic.jpg'></html>")



if __name__ == '__main__': #running the app
	app.run(debug=True)