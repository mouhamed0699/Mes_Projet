const joursht=document.querySelector('.jours');
const heurht=document.querySelector('.heurs');
const minutesht=document.querySelector('.minutes');
const secondesht=document.querySelector('.secondes');


function compteRebour(){
    const dateActuel=new Date().getTime();
    const datefuture=new Date('2024-01-01').getTime();
    const difference=datefuture-dateActuel;

    const jours=Math.floor(difference/(1000*60*60*24)) ;
    const heurs=Math.floor((difference%(1000*60*60*24))/(1000*60*60));
    const minutes=Math.floor((difference%(1000*60*60)/(1000*60)));
    const secondes=Math.floor((difference%(1000*60)/1000));
    joursht.innerHTML=`${jours}`;
    heurht.innerHTML=`0-${heurs}`;
    minutesht.innerHTML=`0-${minutes}`;
    secondesht.innerHTML=`0-${secondes}`;
    console.log(jours,heurs,minutes,secondes)
}

const rebourAutomatic=setInterval(()=>{
    compteRebour()
},1000)