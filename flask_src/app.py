from collections import OrderedDict

from flask import Flask, render_template
from flask_minify import minify


app = Flask(__name__)
minify(app=app, html=True, js=True, cssless=True)

app.config["TEMPLATES_AUTO_RELOAD"] = True

@app.route('/')
def index():
    return render_template("index.html")


@app.route("/favourite-music.html")
def favourite_music():
    # I don't want to use a DB here
    compositions = OrderedDict([('Classical', {
        'Frédéric François Chopin': [('Waltz Rain', ''), ('Nocturne in E Flat Major (Op. 9 No. 2)', ''), (
            'Paul de Senneville -- Mariage d\'Amour (aka Frédéric François Chopin -- Spring Waltz)',
            'In fact, author of this piece of music is a French composer Paul de Senneville, not Frederic Chopin as some people erroneously think. This myth appeared when this piece of music was uploaded on YouTube with the wrong title and reached over 34,000,000 views [Source: Wikipedia].')],
        'Ludwig Van Beethoven': [('Moonlight Sonata', ''), ('Für Elise', '')],
        'Antonio Lucio Vivaldi': [('Summer Storm (The Four Seasons Summer, Op. 8, Rv315)', '')],
        'Edvard Hagerup Grieg': [('Piano Concerto in A minor, Op 16 -- I. Allegro molto moderato', ''),
                                 ('In the Hall of the Mountain King', '')],
        'Pyotr Ilyich Tchaikovsky': [('The Nutcracker Suite, Op. 71a', '')]}), ('Rock', {
        'Queen': [('The Show Must Go On', ''), ('We Are the Champions', ''), ('I Want It All', ''),
                  ('Bohemian Rhapsody', '')],
        'Chris Rea': [('The Road to Hell (Part II)', ''), ('Looking for the Summer', '')],
        'Sting': [('Shape of My Heart', '')]}), ('Heavy Metal', {'Epica': [('Cry for the Moon', '')]}), ('Blues', {
        'Oscar Benton': [('Bensonhurst Blues', ''), ('I Believe in Love', ''), ('Josie', ''), ('Vitta Bella', '')]}),
                 ('Jazz', {'Candy Dulfer': [('Lily Was Here', '')]}), ('Performed by David Garrett', {
            '': [('Cry me a river', ''), ('Beethoven scherzo', ''), ('Tico tico (feat. arturo sandoval)', ''),
                 ('Chopin nocturne (feat. david foster; violin cover; modern cover)', ''),
                 ("He's a Pirate (Pirates of the Carribbean Theme)", '')]})])
    return render_template("favourite-music.html", compositions=compositions)

@app.route("/favourite-movies.html")
def favourite_movies():
    return render_template("favourite-movies.html")

@app.route("/favourite-books.html")
def favourite_books():
    return render_template("favourite-books.html")

if __name__ == '__main__':
    app.run()
