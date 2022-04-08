#extensions that allow specific classes and functions

from flask import Flask, Blueprint, render_template, url_for, redirect
from fish import Fish

# a blueprint of the website structure

views = Blueprint(__name__, "views")

app = Flask(__name__)
# this is the prefix that distinguishes the pages
app.register_blueprint(views, url_prefix="/")

                #########################################################
                #                                                       #
                #                 Application Pages                     #                     
                #                                                       #
                #########################################################

# this is how the homepage is accessed
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/epi")
def epi_page():
    true = Fish("True's Beaked Whale","Mesoplodon mirus","15.5 ft","Small fish and cephalopods","The True's ropunded, sloping forehead is known as its melon!")
    return render_template("tidal.html", fish=true)

@app.route("/meso")
def meso_page():
    angler = Fish("Humpback Anglerfish","Melanocetus johnsonii","20cm","Anything it can get!","The bioluminescence of M. johnsonii is caused by symbiont Enterovibrio escacola bacteria!")
    return render_template("reef.html",fish=angler)
    
@app.route("/bathy")
def bathy_page():
    squid = Fish("Colossal Squid","Mesonychoteuthis hamiltoni","14m","Marine worms, fish and smaller squid","The colossal squid's eyes are nearly 3x bigger than other deepsea squid, and it believed that their eyes glow!")
    return render_template("photic.html",fish=squid)
    
@app.route("/abyss")
def abyss_page():
    hag = Fish("Pacific Hagfish","Eptatretus stoutii","42cm","Worms, invertebrates,shrimps","Hagfish can eat species much larger than it, by entering the prey through the mouth!")
    return render_template("aphotic.html", fish=hag)



                #########################################################
                #                                                       #
                #                  Redirects Pages                      #                     
                #                                                       #
                #########################################################

@app.route("/home")
def home_redirect():
    return redirect(url_for("home"))

@app.route("/epipelagic")
def epi_redirect():
    return redirect(url_for("epi_page"))

@app.route("/mesopelagic")
def meso_redirect():
    return redirect(url_for("meso_page"))

@app.route("/twilight")
def twil_redirect():
    return redirect(url_for("meso_page"))

@app.route("/twilightzone")
def twilz_redirect():
    return redirect(url_for("meso_page"))

@app.route("/bathypelagic")
def bathy_redirect():
    return redirect(url_for("bathy_page"))

@app.route("/midnight")
def mid_redirect():
    return redirect(url_for("bathy_page"))

@app.route("/midnightzone")
def midz_redirect():
    return redirect(url_for("bathy_page"))

@app.route("/abyssopelagic")
def ab_redirect():
    return redirect(url_for("abyss_page"))


                #########################################################
                #                                                       #
                #                     Error Pages                       #                     
                #                                                       #
                #########################################################

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404

@app.errorhandler(500)
def internal_error(e):
    return render_template("404.html"), 500


                #########################################################
                #                                                       #
                #                 Initialising                          #                     
                #                                                       #
                #########################################################

if __name__ == "__main__":
    app.run(debug=True, port = 8000)