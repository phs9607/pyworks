var watch = setInterval(myWatch, 1000)

function myWatch(){
    var date = new Date()
    var now = date.toLocaleTimeString(); //년원일 빼고, 시분초만 나오게
    document.getElementById("demo").innerHTML = now;
}