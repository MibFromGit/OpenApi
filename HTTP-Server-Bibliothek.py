from flask import Flask, redirect, url_for, request

# initialisiere Flask-Server
app = Flask(__name__)

@app.route('/success/<name>')
def success(name):
   return 'welcome %s' % name

@app.route('/')
def login():
   language = dict()
   if request.method == 'POST': # Das Funktioniert nicht 
      language = request.form['language']
      return language
   else:
      language = request.args.get('language')
      return language

# definiere Route für Hauptseite
@app.route('/')
def index():
    # gebe Antwort an aufrufenden Client zurück
    Link1 = '<a href="/eingaenge">Eingaenge</a>'
    Link2 = '<a href="/ausgaenge">Ausgaenge</a>'
    return Link1 + '<br>' + Link2

@app.route('/eingaenge')
def Seite1():
    Link = '<a href="/">zurück zur Haupseite</a>'
    Link2 = '<a href="/ausgaenge">Ausgaenge</a>'

    return Link + '<br>' + Link2

@app.route('/ausgaenge')
def Seite2():
    Link = '<a href="/">zurück zur Haupseite</a>'
    Link1 = '<a href="/eingaenge">Eingaenge</a>'
    return Link + '<br>' + Link1

if __name__ == '__main__':
    # starte Flask-Server
    app.run(host='0.0.0.0', port=5000)