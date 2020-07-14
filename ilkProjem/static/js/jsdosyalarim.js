var vid = document.getElementById("video");
var vveri = document.getElementById("anahtarlar");
var vdeger = document.getElementById("degerler");
vid.controls = true;
zamani = 0;
veri = "";
kontrol = 0;
function calistir() {
    if (kontrol == 0)
        kontrol = 1;
    else
        vdeger.value += vveri.value + ";";
    vveri.value = "";
    vid.play();
}

function durdur() {
    vid.pause();
    zamani = vid.currentTime;
    vdeger.value += zamani+"-";   
}
function goster()
{
    alert("deger:"+vdeger.value);
}