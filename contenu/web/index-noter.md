# Ce que vous en pensez

Si tu as un avis sur <em>Les Conférences de poche</em>, tu peux donner une note ci-dessous :

<div class="rating"><span>☆</span><span>☆</span><span>☆</span><span>☆</span><span>☆</span></div>
 
<div class=plus>
    <p>Je précise que la note que tu donnes ne sera ni enregistrée, ni envoyée nulle-part.</p>
    <p>Personne ne saura la note que tu as mise. C'est vraiment juste entre toi et toi.</p>
    <div class=plus>
    <p>C'est comme les questions à choix multiple qu'il y a <a href="#intro">au début du site</a>. Je n'enregistre pas les réponses, c'est juste pour toi.</p>
    <p>Pas la peine de prendre de précautions, tu peux être aussi honnête ou malhonnête que tu le souhaites, ça ne regarde que toi.</p>
    </div>
</div>

<style>

.rating {
   width: 180px;
   display: flex;
   justify-content: center;
   align-items: center;
   gap: .3em;
   padding: 5px;
   overflow: hidden;
    border:1px solid;
  border-radius:30px;
}


.rating span {
   font-size: 1.8em;
   cursor: pointer;
   transition: scale linear .1s;
}

.rating span:hover {
   scale: 150%;
}
</style>
<script>
// script piqué ici https://dev.to/leonardoschmittk/how-to-make-a-star-rating-with-js-36d3
const ratingStars = [...document.querySelectorAll(".rating span")];
executeRating(ratingStars,0);
function executeRating(stars, result) {
   stars.map((star) => {
      star.onclick = () => {
        for (let i=stars.indexOf(star); i >= 0; --i){
          stars[i].innerText = '★';
        }
        for (let i=stars.indexOf(star)+1; i < stars.length; ++i){
          stars[i].innerText = '☆';
        }
      }
   });
}
</script>
