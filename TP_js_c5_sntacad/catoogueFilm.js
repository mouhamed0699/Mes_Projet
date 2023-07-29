const APIURL ="https://api.themoviedb.org/3/discover/movie?sort_by=popularity.desc&api_key=04c35731a5ee918f014970082a0088b1&page=1";
const IMGPATH = "https://image.tmdb.org/t/p/w1280";
const SEARCHAPI ="https://api.themoviedb.org/3/search/movie?&api_key=04c35731a5ee918f014970082a0088b1&query=";

fetch(APIURL)
    .then(response=>response.json())
    .then(data=>{
        const newData=data;
        const Element=newData.results;
        Element.forEach(element => {
            const contener=document.querySelector('.contener')
            const newdiv=document.createElement('div');
            const imag=document.createElement('img');
            const p=document.createElement('p');
            const span1=document.createElement('span');
            const span2=document.createElement('span');
            const describ=document.createElement('p')
            describ.textContent=element.overview;
            describ.classList.add('describ') 
            newdiv.classList.add("newdiv")
            p.classList.add('pim')
            imag.classList.add('img')
            imag.src="https://image.tmdb.org/t/p/w1280"+element.poster_path;
            span1.textContent=element.title;
            span2.textContent=element.vote_average;
            span2.classList.add('span2')
            newdiv.appendChild(describ)
            p.appendChild(span1);
            p.appendChild(span2);
            newdiv.appendChild(imag);
            newdiv.appendChild(p);
            contener.appendChild(newdiv);

            imag.addEventListener('mouseover',()=>{
                imag.style.cursor='pointer'
                p.style.display='none'
                describ.style.display='block'

                
            })
            imag.addEventListener('mouseout',()=>{
                
                describ.style.display='none'
                p.style.display='block'
                
            })

        });
    })
    .catch(error=>console.error(error));



const searchInput = document.getElementById("search-input");
const resultsContainer = document.querySelector(".contener");

searchInput.addEventListener('input',(event)=>{
    const searchTerm = event.target.value.toLowerCase();
    const allNewDivs = resultsContainer.querySelectorAll('.newdiv');
    
    allNewDivs.forEach((newdiv)=>{
        const title = newdiv.querySelector('.pim span:first-child').textContent.toLowerCase();
        if(title.includes(searchTerm)){
            newdiv.style.display = "block";
        } else {
            newdiv.style.display = "none";
        }
    });
});


// Fonction pour animer une nouvelle div
function animateNewDiv(newdiv) {
  newdiv.style.transform = "translateY(0)";
  newdiv.style.opacity = "1";
}

// Gestionnaire d'événements de scroll
window.addEventListener("scroll", () => {
  // Récupération de toutes les nouvelles div
const allNewDivs = resultsContainer.querySelectorAll(".newdiv");

// Variable pour stocker le nombre de nouvelles div déjà vues
let numNewDivsSeen = 0;

  allNewDivs.forEach((newdiv, index) => {
    // Si la nouvelle div est déjà visible, passer à la suivante
    if (newdiv.classList.contains("show")) {
      return;
    }
    
    // Si la nouvelle div est dans la vue, l'animer
    if (window.scrollY + window.innerHeight > newdiv.offsetTop) {
      newdiv.classList.add("show");
      animateNewDiv(newdiv);
      numNewDivsSeen++;
    }
    
    // Si c'est la première nouvelle div, l'animer sans attendre le scroll
    if (index === 0 && numNewDivsSeen === 0) {
      newdiv.classList.add("show");
      animateNewDiv(newdiv);
      numNewDivsSeen++;
    }
  });
});
