
const pElements = document.querySelectorAll('p');
const d200 = document.querySelector('.d200');const cd200=d200.style.backgroundColor;
const d20 = document.querySelector('.d20');const cd20=d20.style.backgroundColor;
const d2 = document.querySelector('.d2');const cd2=d2.style.backgroundColor;
const d21 = document.querySelector('.d21');const cd21=d21.style.backgroundColor;
const l2 = document.querySelector('.l2');const cl2=l2.style.backgroundColor;
const M2 = document.querySelector('.M2');const cM2=M2.style.backgroundColor;
const me2 = document.querySelector('.me2');const cme2=me2.style.backgroundColor;
const j2 = document.querySelector('.j2');const cj2=j2.style.backgroundColor;
const v2 = document.querySelector('.v2');const cv2=v2.style.backgroundColor;
const s2 = document.querySelector('.s2');const cs2=s2.style.backgroundColor;
const d1 = document.querySelector('.d1');const cd1=d1.style.backgroundColor;
const d10 = document.querySelector('#recherche1');const cd10=d10.style.backgroundColor;
const enseignant = document.querySelector('.enseignants');const cens=enseignant.style.backgroundColor;
const Salle = document.querySelector('.salles');const csal=Salle.style.backgroundColor;
const classe = document.querySelector('.classes');const ccl=classe.style.backgroundColor;
const Module = document.querySelector('.modules');const cMo=Module.style.backgroundColor;


let estEnModeNuit = false;


let modeNuitJour=document.querySelector('.d2000');
modeNuitJour.addEventListener('click', () => {
    estEnModeNuit = !estEnModeNuit;
  
    if (estEnModeNuit) {
        console.log(estEnModeNuit)
      // Appliquer les styles pour le mode sombre
      
      modeNuitJour.style.right = '7px';
      modeNuitJour.style.background = 'white';
  
      pElements.forEach((p) => {
        p.style.color = 'black';
      });
  
      d200.style.background = 'black';
      d20.style.background = '#efafb0';
      d21.style.background = '#c0bfc6';
      d2.style.background = '#efafb0';
      l2.style.background = '#c0bfc6';
      M2.style.background = '#c0bfc6';
      me2.style.background = '#c0bfc6';
      j2.style.background = '#c0bfc6';
      v2.style.background = '#c0bfc6';
      s2.style.background = '#c0bfc6';
      d1.style.background = '#b7c3cc';
      d10.style.background = '#dae1e4';
      enseignant.style.background = '#dae1e4';
      Salle.style.background = '#dae1e4';
      classe.style.background = '#dae1e4';
      Module.style.background = '#dae1e4';
    } else {
      // Appliquer les styles pour le mode clair
      modeNuitJour.style.left = '7px';
      modeNuitJour.style.background = 'black';
  
      pElements.forEach((p) => {
        p.style.color = 'white';
      });
  
      d200.style.background = cd200
      d20.style.background = cd20
      d21.style.background = cd21;
      d2.style.background = cd2;
      l2.style.background = cl2;
      M2.style.background = cM2;
      me2.style.background = cme2;
      j2.style.background = cj2;
      v2.style.background = cv2;
      s2.style.background = cs2;
      d1.style.background =cd1;
      d10.style.background = cd10;
      enseignants.style.background=cens;       Salle.style.background = csal;
      classe.style.background = ccl;
      Module.style.background = cMo;
    }
  


})