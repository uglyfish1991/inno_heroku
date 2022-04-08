
const angler = document.getElementById("angler")

if (angler !==null){

angler.addEventListener("mouseover", () => {
    angler.src = "../static/images/anglerfishglow.png"
})

angler.addEventListener("mouseout", () => {
    angler.src = "../static/images/anglerfish.png"
})
}

const truew = document.getElementById("true")

if (truew !==null) {
truew.addEventListener("mouseover", () => {
    truew.src = "../static/images/truewhale - Copy.png"
})

truew.addEventListener("mouseout", () => {
    truew.src = "../static/images/truewhale.png"
})
}

const jellyfish = document.getElementById("jelly");

if (jellyfish !==null) {
jellyfish.addEventListener("mouseover", () => {
    jellyfish.src = "../static/images/jellyfishover.png"
})

jellyfish.addEventListener("mouseout", () => {
    jellyfish.src = "../static/images/jellyfish.png"
})
}

const hag = document.getElementById("hagfish");

if (hag !==null) {
hag.addEventListener("mouseover", () => {
    hag.src = "../static/images/whaleover.png"
})

hag.addEventListener("mouseout", () => {
    hag.src = "../static/images/whale.png"
})
}




window.addEventListener("beforeunload", function () {
    document.body.classList.add("animate-out");
  });