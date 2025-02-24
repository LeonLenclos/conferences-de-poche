# Les écrous

C'est une collection d'écrous qui est à l'origine de toute cette histoire de *Conférences de poche*.

<div class=plus>

J'explique ça dans la conférence sur les collections. Voilà les écrous en question (il y en a 32) :
<div class=ecrous>
<img src="img/illu-web/ecrou01.png">
<img src="img/illu-web/ecrou02.png">
<img src="img/illu-web/ecrou03.png">
<img src="img/illu-web/ecrou04.png">
<img src="img/illu-web/ecrou05.png">
<img src="img/illu-web/ecrou06.png">
<img src="img/illu-web/ecrou07.png">
<img src="img/illu-web/ecrou08.png">
<img src="img/illu-web/ecrou09.png">
<img src="img/illu-web/ecrou10.png">
<img src="img/illu-web/ecrou11.png">
<img src="img/illu-web/ecrou12.png">
<img src="img/illu-web/ecrou13.png">
<img src="img/illu-web/ecrou14.png">
<img src="img/illu-web/ecrou15.png">
<img src="img/illu-web/ecrou16.png">
<img src="img/illu-web/ecrou17.png">
<img src="img/illu-web/ecrou18.png">
<img src="img/illu-web/ecrou19.png">
<img src="img/illu-web/ecrou20.png">
<img src="img/illu-web/ecrou21.png">
<img src="img/illu-web/ecrou22.png">
<img src="img/illu-web/ecrou23.png">
<img src="img/illu-web/ecrou24.png">
<img src="img/illu-web/ecrou25.png">
<img src="img/illu-web/ecrou26.png">
<img src="img/illu-web/ecrou27.png">
<img src="img/illu-web/ecrou28.png">
<img src="img/illu-web/ecrou29.png">
<img src="img/illu-web/ecrou30.png">
<img src="img/illu-web/ecrou31.png">
<img src="img/illu-web/ecrou32.png">
</div>
</div>

<script>
 document.addEventListener("scroll", (ev)=>{
    document.querySelectorAll('.ecrous img').forEach(e=>{
        let angle = Math.floor(window.scrollY/3);
        e.style.rotate=angle+'deg'
    }); 
 }); 
</script>
<style>
.ecrous{
text-align:center
}
.ecrous img {
width:unset;
display:inline-block;
vertical-align:middle;
margin:0;
  transition: rotate .3s;
}
</style>
