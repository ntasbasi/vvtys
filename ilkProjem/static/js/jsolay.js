var vid = document.getElementById("video");
var vveri = document.getElementById("anahtarlar");
var vdeger = document.getElementById("degerler");
var sure = "";
vid.controls = true;
veri = "";
kontrol = 0;
function calistir() {
    if (kontrol == 0)
        kontrol = 1;
    //else vdeger.value += vveri.value + ";";
    vveri.value = "";
    sure="";
    vid.play();    
}
function basla(){
    sure += vid.currentTime + "-";
}
function durdur() {
    vid.pause();
    sure += vid.currentTime + ":";   
}
function ekle()
{
    vdeger.value += sure + vveri.value + ";";
}
function goster()
{
    alert("deger:"+vdeger.value);
}