# Un guide pour compter en binaire sur ses doigts

Suite à un nombre grandissant de demandes, j'ai conçu un guide pour compter sur ses mains avec la *technique binaire à dix chiffres* (dont je parle dans la conférence sur le syndrome de la Reine Rouge).


<div class="comptage plus">

</div>
  


  <style>
    .comptage div{
      display:inline-grid;
      grid-template-areas:
       "maing maind"
       "caption caption"
       ;
      border:1px solid black;
      margin:10px;

    }
    .comptage img{
    
      width:80px;
     filter: contrast(70%) grayscale(100%) !important;
     margin:0;
    }
    .comptage span{
      grid-area: caption;
      text-align:center;  
    }
    .comptage {
    text-align:center;

      font-size: 9pt;
      display:flex;
      flex-direction:row;
      flex-wrap:wrap;
            gap:4px;
    }
  </style>
  

<script>
  
  function createHandsElement(l,r){
     let n = l*32 + r;
     let div = document.createElement('div');                 
     let img1 = document.createElement('img');             
     let img2 = document.createElement('img');
     let caption = document.createElement('span');
     div.appendChild(img1);
     div.appendChild(img2);
     div.appendChild(caption);
     img1.src="img/mains/main_g"+("000"+l).slice(-3)+".jpg";
     img2.src="img/mains/main_d"+("000"+r).slice(-3)+".jpg";
     caption.innerHTML = n;
     return div;
  }
  
  function createHandElementByNumber(n){
    let r = n%32;
    let l = (n-r)/32;
    return createHandsElement(l, r);
  }
  
  for(let i=0; i <1024; i++){
    document.querySelector('.comptage').appendChild(createHandElementByNumber(i))
  }

 
</script>

  
</html> 

