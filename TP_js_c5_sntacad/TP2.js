const butdroit=document.querySelector('.im1');
const butleft=document.querySelector('.im2');
const elementgauche=document.querySelector('.d1');
const elementdroite=document.querySelector('.d2')

const tab=['Mon premier','Mon deuxieme','Mon troisieme','Mon quatrieme'];
tab.forEach((texte)=>{
    
    const element=document.createElement('p');
    const texteNoeud=document.createTextNode(texte);
    element.appendChild(texteNoeud);
    elementgauche.appendChild(element);
});
let pselection=null;
elementgauche.addEventListener('click',(e)=>{
    const p=e.target.closest('p');
   
    if(p){
        p.style.backgroundColor='blue';
        pselection=p;
        pselection.style.backgroundColor='blue';
        console.log(pselection);

    }else{
        pselection=null;
        pselection.style.backgroundColor=''
    };

});
butdroit.addEventListener('click',()=>{
    if(pselection!=null){
        pselection.style.backgroundColor='';
        elementdroite.appendChild(pselection);
        pselection=null;
    };
 });

 elementdroite.addEventListener('click',(e)=>{
    const p=e.target.closest('p');
   
    if(p){
        p.style.backgroundColor='blue';
        pselection=p;
        pselection.style.backgroundColor='blue';
        console.log(pselection);

    }else{
        p.style.backgroundColor='';
        pselection=null;
    };

});

butleft.addEventListener('click',()=>{
    if(pselection!=null){
        pselection.style.backgroundColor='';
        elementgauche.appendChild(pselection);
        pselection=null;
    };
 });








//  elementgauche.addEventListener('mouseover',e=>{
//     const p=e.target.closest('p');
//     if(p){
//         p.style.backgroundColor='blue';
//     };
//     butdroit.addEventListener('click',()=>{
//         const pSelection=elementgauche.querySelectorAll('p[style="background-color: yellow;"]');
//         pSelection.forEach(p =>{
//             elementdroite.appendChild(p);
//             tap.style.backgroundColor='';
    
//         });
//      });
//  });
//  elementgauche.addEventListener('mouseout',e=>{
//     const p=e.target.closest('p');
//     if(p){
//         p.style.backgroundColor='';
//     };
//  });

