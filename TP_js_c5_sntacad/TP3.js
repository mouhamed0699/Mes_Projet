

const tab=['.p1','.p2','.p3','.p4'];
tab.forEach((text)=>{
    const p=document.querySelector(text);
    p.addEventListener('click',()=>{
        const pNotifi=document.createElement('p');
        pNotifi.textContent='Mon Projet 4';
        pNotifi.classList.add('pnotif');
        pNotifi.style.backgroundColor= window.getComputedStyle(p).backgroundColor;
        document.body.appendChild(pNotifi);
        setTimeout(()=>{
            pNotifi.style.display = "none";
    
        },3000)
    });
});

// #2a124d
// #e5b63e