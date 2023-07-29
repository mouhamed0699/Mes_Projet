const clickp1=document.querySelector(".p1");
console.log('clickp1');

clickp1.addEventListener("click",()=>{
    const monDiv=document.querySelector('.d1');
    const newdiv=document.createElement('div');
    const newP=document.createElement('p');
    const input1=document.createElement('input');
    const buton1=document.createElement('button');
    const buton2=document.createElement('button');
    const im1=document.createElement('img')
    const im2=document.createElement('img')
    im1.classList.add('icon1')
    im2.classList.add('icon2')
    im1.src='TP.png'
    im2.src='delete.png'
    newdiv.classList.add('newdiv');
    buton1.appendChild(im1)
    buton2.appendChild(im2)
    newP.appendChild(buton1)
    newP.appendChild(buton2)
    newP.classList.add('newp')
    monDiv.appendChild(newdiv);
    newdiv.appendChild(newP);
    newdiv.appendChild(input1);
    newP.appendChild(buton1)
    buton2.addEventListener('click',()=>{
        newdiv.remove();
    });
    buton1.addEventListener('click',()=>{
        input1.value='';
    });
});
