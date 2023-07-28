

const menuEtComposant = {
    enseignants: [
      {nom: 'Enseignant',Modules:['Modules']},
      {nom: 'Ali', cle: 2,Modules:['Python','PHP']},
      {nom: 'Mbaye', cle: 3,Modules:['ALGO','LC']},
      {nom: 'Moussa', cle: 4,Modules:['JAVA','ALGO','LC']},
      {nom: 'Fatou', cle: 5,Modules:['JAVA','ALGO','JAVASCRIPT']},
      {nom: 'Djibi', cle: 6,Modules:['Python','ALGO','JAVASCRIPT']},
      {nom: 'Baila', cle: 7,Modules:['LC','ALGO','JAVASCRIPT']}
    ],
    classes: [
      {nom: 'Classes', Effectif: null},
      {nom: 'L2 MPI',  Effectif: 100},
      {nom: 'L1 PC',  Effectif: 200},
      {nom: 'M1 INFO',  Effectif: 30},
      {nom: 'DEV DATA',  Effectif: 21},
      {nom: 'Dev',  Effectif: 60}
    ],
    Salles: [
      {nom: 'Salles', capacite: null},
      {nom: '1A', capacite: 100},
      {nom: '3A', capacite: 60},
      {nom: '2B', capacite: 220},
      {nom: '2A', capacite: 40},
      {nom: '1B', capacite: 25},
      {nom: '3B', capacite: 70}
    ],
    Modules: [
      {nom: 'Modules',enseignants:['enseignants'] },
      {nom: 'Python', enseignants:['Ali','Djibi']},
      {nom: 'JAVASCRIPT',enseignants:['Fatou','Djibi','Baila']},
      {nom: 'PHP', enseignants:['Ali',]},
      {nom: 'JAVA',enseignants:['Moussa','Fatou'] },
      {nom: 'ALGO',enseignants:['Mbaye','Moussa','Fatou','Djibi','Baila']},
      {nom: 'LC',enseignants:['Mbaye','Baila'] }
    ]
  };
console.log(menuEtComposant.enseignants)
  
const enseignants=document.querySelector('.enseignants');
const Salles=document.querySelector('.salles');
const classes=document.querySelector('.classes');
const Modules=document.querySelector('.modules');

const longE=document.createElement('p')
const longC=document.createElement('p')
const longS=document.createElement('p')
const longM=document.createElement('p')
longE.textContent=menuEtComposant.enseignants.length-1
longC.style.fontSize='25px';longE.style.fontSize='25px';longS.style.fontSize='25px';longM.style.fontSize='25px'
longC.style.position='absolute';longE.style.position='absolute';longS.style.position='absolute';longM.style.position='absolute'
longC.style.right='-80%';longE.style.right='-80%';longS.style.right='-80%';longM.style.right='-80%';
longC.style.top='1%';longM.style.top='1%';longE.style.top='1%';longS.style.top='1%'
longC.textContent=menuEtComposant.classes.length-1
longS.textContent=menuEtComposant.Salles.length-1
longM.textContent=menuEtComposant.Modules.length-1

const PlusE=document.createElement('p')
const PlusC=document.createElement('p')
const PlusS=document.createElement('p')
const PlusM=document.createElement('p')
PlusE.textContent='+'
PlusC.style.fontSize='25px';PlusE.style.fontSize='25px';PlusS.style.fontSize='25px';PlusM.style.fontSize='25px'
PlusC.style.position='absolute';PlusE.style.position='absolute';PlusS.style.position='absolute';PlusM.style.position='absolute'
PlusC.style.right='-80%';PlusE.style.right='-80%';PlusS.style.right='-80%';PlusM.style.right='-80%';
PlusC.style.bottom='1%';PlusM.style.bottom='1%';PlusE.style.bottom='1%';PlusS.style.bottom='1%'
PlusC.style.cursor='pointer';PlusM.style.cursor='pointer';PlusE.style.cursor='pointer';PlusS.style.cursor='pointer'

PlusC.textContent='+'
PlusS.textContent='+'
PlusM.textContent='+'

enseignants.appendChild(longE);Salles.appendChild(longS);classes.appendChild(longC);Modules.appendChild(longM)
enseignants.appendChild(PlusE);Salles.appendChild(PlusS);classes.appendChild(PlusC);Modules.appendChild(PlusM)


TabMenu=[enseignants,Salles,classes,Modules];
function selectOplabel(optionSelect){
    const ValuePlanning=document.querySelector('.s1');
    ValuePlanning.textContent=optionSelect.textContent;
}
TabMenu.forEach(element => {
    
    element.addEventListener('click',()=>{
        const monlabel=document.querySelector('#selection');
        
        monlabel.textContent=element.className
        let tab=[]
        if(element.className=='enseignants'){
            tab=menuEtComposant.enseignants
            
        }
        if(element.className=='classes'){
            tab=menuEtComposant.classes
        }
        if(element.className=='salles'){
            tab=menuEtComposant.Salles
        }
        if(element.className=='modules'){
            tab=menuEtComposant.Modules
        }
        
        tab.forEach((e,index)=>{
            const option=document.createElement('option');
            option.value='option'+index
            
            option.textContent=e.nom;
            option.style.fontSize='20px'
            monlabel.appendChild(option)
        })
        monlabel.addEventListener('change',function(){
            const optionSelect=this.options[this.selectedIndex];
            
            const ValuePlanning=document.querySelector('.s1');
            ValuePlanning.textContent=optionSelect.textContent;
            
        })

    })
});

// function AppelFormulEnse(){
//     let plusLundi=document.querySelector('#pl1');let plusMardi=document.querySelector('#pl2');let plusMercredi=document.querySelector('#pl3');
//     let plusJeudi=document.querySelector('#pl4');let plusVendredo=document.querySelector('#pl5');let plusSamdi=document.querySelector('#pl6');
//     plusLundi.addEventListener('click',()=>{
//         const form=document.querySelectorAll('.formula');
//         form.forEach(formu=>{
//             const p=document.querySelector('.newp1')
//             if(p.textContent=='Classes'){
//                 formu.style.display='none'
//             }
//         })
//         AjouterEnseig('lundi')})
//     plusMardi.addEventListener('click',()=>{AjouterEnseig('mardi')})
//     plusMercredi.addEventListener('click',()=>{AjouterEnseig('mercredi')})
//     plusJeudi.addEventListener('click',()=>{AjouterEnseig('jeudi')})
//     plusVendredo.addEventListener('click',()=>{AjouterEnseig('vendredi')})
//     plusSamdi.addEventListener('click',()=>{AjouterEnseig('samdi')})
// }
enseignants.addEventListener('click',()=>{
    
    const newlabel=document.querySelector('#selection')
    newlabel.addEventListener('change',function(){

        const optionSelect=this.options[this.selectedIndex];
        if(optionSelect.textContent=='Ali'){
           
            const message=document.querySelector('.message')
            console.log(message)
            const nd = document.querySelectorAll('.newdiv');

            nd.forEach((elem) => {
                elem.remove();
            });
            
            RemplirEmploiEnsei('Dev','Python','1A','mercredi','15h','2h')
            RemplirEmploiEnsei('DEV DATA','ALGO','1B','jeudi','8h','3h')
            

        }else if(optionSelect.textContent=='Mbaye'){
            
            const nd = document.querySelectorAll('.newdiv');

            nd.forEach((elem) => {
                elem.remove();
            });
            
            RemplirEmploiEnsei('Dev','PHP','2B','samdi','11h','2h')
            
            

        }else{
            
            const nd = document.querySelectorAll('.newdiv');

            nd.forEach((elem) => {
            elem.remove();
            });
            RemplirEmploiEnsei('Dev','PHP','2B','samdi','11h','2h')
        }


    })
})



function AppelFormulCla(clas){
    let plusLundi=document.querySelector('#pl1');let plusMardi=document.querySelector('#pl2');let plusMercredi=document.querySelector('#pl3');
    let plusJeudi=document.querySelector('#pl4');let plusVendredo=document.querySelector('#pl5');let plusSamdi=document.querySelector('#pl6');
    plusLundi.addEventListener('click',()=>{ 
        formulaire(menuEtComposant.Modules,menuEtComposant.enseignants,menuEtComposant.Salles,'lundi',clas)
    })
    plusMardi.addEventListener('click',()=>{
        formulaire(menuEtComposant.Modules,menuEtComposant.enseignants,menuEtComposant.Salles,'Mardi',clas)
    })
    plusMercredi.addEventListener('click',()=>{ 
        formulaire(menuEtComposant.Modules,menuEtComposant.enseignants,menuEtComposant.Salles,'mercredi',clas)
    })
    plusJeudi.addEventListener('click',()=>{ 
        formulaire(menuEtComposant.Modules,menuEtComposant.enseignants,menuEtComposant.Salles,'jeudi',clas)
    })
    plusVendredo.addEventListener('click',()=>{ 
        formulaire(menuEtComposant.Modules,menuEtComposant.enseignants,menuEtComposant.Salles,'vendredi',clas)
    })
    plusSamdi.addEventListener('click',()=>{ 
        formulaire(menuEtComposant.Modules,menuEtComposant.enseignants,menuEtComposant.Salles,'samdidi',clas)
  
    })
}
classes.addEventListener('click',()=>{ 
    const newlabel=document.querySelector('#selection')
    newlabel.addEventListener('change',function(){
        
        const optionSelect=this.options[this.selectedIndex];
        if(optionSelect.textContent=='L2 MPI'){
            
            
            AppelFormulCla('L2 MPI')
            const nd = document.querySelectorAll('.newdiv');
        
            nd.forEach((elem) => {
            elem.remove();
            });
            RemplirEmploiClasse('Python','Ali','1A','mercredi','15h','2h','L2 MPI')
            RemplirEmploiClasse('ALGO','Mbaye','2B','jeudi','8h','3h','L2 MPI')
            
        
        }else if(optionSelect.textContent=='L1 PC'){

            AppelFormulCla('L1 PC')
            const nd = document.querySelectorAll('.newdiv');
        
            nd.forEach((elem) => {
                elem.remove();
            });
            
            RemplirEmploiClasse('PHP','Moussa','2B','samdi','11h','2h','L1 PC')
            RemplirEmploiClasse('ALGO','Fatou','2B','mardi','9h','3h','L1 PC')
            
        
        }else{

            delete AppelFormulCla(optionSelect.textContent)
            AppelFormulCla(optionSelect.textContent)
            const nd = document.querySelectorAll('.newdiv');
        
            nd.forEach((elem) => {
            elem.remove();
            });
            RemplirEmploiClasse('PHP','Djibi','2B','samdi','11h','2h',optionSelect.textContent)
        }

    })
})
Salles.addEventListener('click',()=>{
   
    const newlabel=document.querySelector('#selection')
    newlabel.addEventListener('change',function(){
        const optionSelect=this.options[this.selectedIndex];
        if(optionSelect.textContent=='3A'){
            const nd = document.querySelectorAll('.newdiv');
        
            nd.forEach((elem) => {
            elem.remove();
            });
            RemplirEmploiSall('Ali','Python','L1PC','mercredi','15h','2h')
            RemplirEmploiSall('Mbaye','ALGO','Dev','Lundi','8h','3h')
            
        
        }else if(optionSelect.textContent=='1A'){
            const nd = document.querySelectorAll('.newdiv');
        
            nd.forEach((elem) => {
                elem.remove();
            });
            
            RemplirEmploiSall('Moussa','PHP','Dev','samdi','11h','2h')
            RemplirEmploiSall('Fatou','ALGO','DEV DATA','mardi','9h','3h')
            
        
        }else{
            const nd = document.querySelectorAll('.newdiv');
        
            nd.forEach((elem) => {
            elem.remove();
            });
            RemplirEmploiSall('Djibi','PHP','M1 INFO','samdi','11h','2h')
        }

    })
})

function recupereCapa(salle) {
    for (const salleObjet of menuEtComposant.Salles) {
      if (salleObjet.nom === salle){
        return salleObjet.capacite;
      }
    }
  }
 function recupereEffect(classe){
    for (const classeObjet of menuEtComposant.classes){
        if(classeObjet.nom==classe){
            return classeObjet.Effectif
        }
    }
 }
console.log(recupereCapa('3A'),recupereEffect('L2 MPI'))

function RemplirEmploiEnsei(classes,modules,salle,jours,heuresDeCours,NombreHeursDeCours,){
    const capaciteSal=recupereCapa(salle);
    const Effectifclas=recupereEffect(classes);
    if(capaciteSal>Effectifclas){
        let Jour='';
        if(jours=='LUNDI' || jours=='Lundi' || jours=='lundi'){
            Jour=document.querySelector('.l2');
    
        };
        if(jours=='MARDI' || jours=='Mardi' || jours=='mardi'){
            Jour=document.querySelector('.M2');
    
        };
        if(jours=='MERCREDI' || jours=='Mercredi' || jours=='mercredi'){
            Jour=document.querySelector('.me2');
    
        };
        if(jours=='JEUDI' || jours=='Jeudi' || jours=='jeudi'){
            Jour=document.querySelector('.j2');
    
        };
        if(jours=='VENDREDI' || jours=='Vendredi' || jours=='vendredi'){
            Jour=document.querySelector('.v2');
    
        };
        if(jours=='SAMDI' || jours=='Samdi' || jours=='samdi'){
            Jour=document.querySelector('.s2');
    
        }; 
        let h1=heuresDeCours.split('h');
        let h2=NombreHeursDeCours.split('h');
        let H1=parseFloat(h1[0]);
        let H2=parseFloat(h2[0]);
        let DiffH=H1-8;
        let marginleft=(DiffH+1)*8 +2;;
        
        const newdiv=document.createElement('div')
        const p1=document.createElement('p')
        const p2=document.createElement('p')
        const p3=document.createElement('p')
        p1.textContent=classes;
        p2.textContent=modules;
        p3.textContent=salle;
        newdiv.classList.add('newdiv')
        newdiv.style.marginLeft=marginleft+'%'
        newdiv.style.width=H2*8 +3+'%'
        newdiv.style.height='100%'
        newdiv.style.background='#3baeea'
        newdiv.style.position='absolute'
        p2.classList.add('p2')
        p1.classList.add('p1')
        p3.classList.add('p3')
        newdiv.appendChild(p1);
        newdiv.appendChild(p2);
        newdiv.appendChild(p3);
        Jour.appendChild(newdiv);
    }
    

}

function RemplirEmploiClasse(modules,Enseignat,salle,jours,heuresDeCours,NombreHeursDeCours,clas){
    let Jour='';
    const capaciteSal=recupereCapa(salle);
    const Effectifclas=recupereEffect(clas);
    if(capaciteSal>Effectifclas){
        if(jours=='LUNDI' || jours=='Lundi' || jours=='lundi'){
            Jour=document.querySelector('.l2');
    
        };
        if(jours=='MARDI' || jours=='Mardi' || jours=='mardi'){
            Jour=document.querySelector('.M2');
    
        };
        if(jours=='MERCREDI' || jours=='Mercredi' || jours=='mercredi'){
            Jour=document.querySelector('.me2');
    
        };
        if(jours=='JEUDI' || jours=='Jeudi' || jours=='jeudi'){
            Jour=document.querySelector('.j2');
    
        };
        if(jours=='VENDREDI' || jours=='Vendredi' || jours=='vendredi'){
            Jour=document.querySelector('.v2');
    
        };
        if(jours=='SAMDI' || jours=='Samdi' || jours=='samdi'){
            Jour=document.querySelector('.s2');
    
        }; 
        let h1=heuresDeCours.split('h');
        let h2=NombreHeursDeCours.split('h');
        let H1=parseFloat(h1[0]);
        let H2=parseFloat(h2[0]);
        let DiffH=H1-8;
        let marginleft=(DiffH)*150 ;
        
        const newdiv=document.createElement('div')
        const p1=document.createElement('p')
        const p2=document.createElement('p')
        const p3=document.createElement('p')
        p1.textContent=Enseignat;
        p2.textContent=modules;
        p3.textContent=salle;
        newdiv.classList.add('newdiv')
        newdiv.style.marginLeft=marginleft+'px'
        newdiv.style.background='orange'
        newdiv.style.width=H2*160 +'px'
        newdiv.style.height='100%'
        newdiv.style.position='absolute'
        p2.classList.add('p2')
        p1.classList.add('p1')
        p3.classList.add('p3')
        newdiv.appendChild(p1);
        newdiv.appendChild(p2);
        newdiv.appendChild(p3);
        Jour.appendChild(newdiv);
    }
 
}
function RemplirEmploiSall(Enseignat,modules,classes,jours,heuresDeCours,NombreHeursDeCours,){
    let Jour='';
    if(jours=='LUNDI' || jours=='Lundi' || jours=='lundi'){
        Jour=document.querySelector('.l2');

    };
    if(jours=='MARDI' || jours=='Mardi' || jours=='mardi'){
        Jour=document.querySelector('.M2');

    };
    if(jours=='MERCREDI' || jours=='Mercredi' || jours=='mercredi'){
        Jour=document.querySelector('.me2');

    };
    if(jours=='JEUDI' || jours=='Jeudi' || jours=='jeudi'){
        Jour=document.querySelector('.j2');

    };
    if(jours=='VENDREDI' || jours=='Vendredi' || jours=='vendredi'){
        Jour=document.querySelector('.v2');

    };
    if(jours=='SAMDI' || jours=='Samdi' || jours=='samdi'){
        Jour=document.querySelector('.s2');

    }; 
    let h1=heuresDeCours.split('h');
    let h2=NombreHeursDeCours.split('h');
    let H1=parseFloat(h1[0]);
    let H2=parseFloat(h2[0]);
    let DiffH=H1-8;
    let marginleft=DiffH*8 + DiffH/2 +1;
    
    const newdiv=document.createElement('div')
    const p1=document.createElement('p')
    const p2=document.createElement('p')
    const p3=document.createElement('p')
    p1.textContent=Enseignat;
    p2.textContent=modules;
    p3.textContent=classes;
    newdiv.classList.add('newdiv')
    newdiv.style.marginLeft=marginleft+'%'
    newdiv.style.background='#0ba00d'
    newdiv.style.width=H2*8 +3+'%'
    newdiv.style.height='100%'
    p2.classList.add('p2')
    p1.classList.add('p1')
    p3.classList.add('p3')
    newdiv.appendChild(p1);
    newdiv.appendChild(p2);
    newdiv.appendChild(p3);
    Jour.appendChild(newdiv);
}

let nouveaudiv=document.createElement('div');
nouveaudiv.style.display='none'
nouveaudiv.style.display='flex';
nouveaudiv.style.flexDirection='column'
const E=menuEtComposant.enseignants
const C=menuEtComposant.classes
const S=menuEtComposant.Salles
const M=menuEtComposant.Modules
const tableau=[E,C,S,M];
tableau.forEach(menu =>{
    menu.forEach(liste=>{         
        let newp=document.createElement('p');
        newp.textContent=liste.nom;
        newp.style.position='relative'
        newp.style.marginTop='20px'
        newp.style.marginleft='30px'
        newp.style.fontSize='25px'
        newp.className='newp'
        nouveaudiv.appendChild(newp)       
    })

    
})
const recherche=document.querySelector('#recherche1');
recherche.addEventListener('input',e=>{
    console.log(e)
    let mot=e.target.value.toLowerCase();
    console.log(mot)
    const d1=document.querySelector('.d1');
    const d11=document.querySelector('.d11');
    const d12=document.querySelector('.d12');
     const d13=document.querySelector('.d13');
    if(mot==''){
        
        d11.style.display='flex'
        d12.style.display='flex'
        d13.style.display='block'
        nouveaudiv.style.display='none'

    }else{

        nouveaudiv.style.display='block'
        d11.style.display='none'
        d12.style.display='none'
        d13.style.display='none'
        d1.appendChild(nouveaudiv)
        let monp=document.querySelectorAll('.newp')
        monp.forEach(p=>{

            let element=p.textContent.toLowerCase();
            if(element.includes(mot)){
                p.style.display='block'
                p.addEventListener('mouseover', () => {
                    p.style.backgroundColor = 'red';
                    p.style.color='black'
                  });
                  
                  p.addEventListener('mouseout', () => {
                    p.style.backgroundColor = '#5e6767';
                    p.style.color='white'
                  });
                  p.addEventListener('click',()=>{
                    d11.style.display='flex'
                    d12.style.display='flex'
                    d13.style.display='block'
                    nouveaudiv.style.display='none'
                    
                    let newop=document.querySelector(".op1");
                    newop.textContent=p.textContent
                    newop.addEventListener('click',selectOplabel(newop))
                    
                  })
            }else{
                p.style.display='none'
            }
        })
    }



    
})







// ajout---------------------------------------------------------------------------
 
function AjouterClasse(jour,clas){   
    
    console.log('desac')
    formulaire(menuEtComposant.Modules,menuEtComposant.enseignants,menuEtComposant.Salles)
    const s1p2=document.querySelector('.s1p2')
    console.log(s1p2)
    const monSelect1=document.querySelector('.selectdiv1');
    const monSelect2=document.querySelector('.selectdiv2')
    const monSelect3=document.querySelector('.selectdiv3')
    const monSelect4=document.querySelector('.selectdiv4')
    const monSelect5=document.querySelector('.selectdiv5')
    console.log(monSelect1)
    
    


      monSelect1.addEventListener('change', updateSelection);
      monSelect2.addEventListener('change', updateSelection);
      monSelect3.addEventListener('change', updateSelection);
      monSelect4.addEventListener('change', updateSelection);
      monSelect5.addEventListener('change', updateSelection);
      s1p2.addEventListener('click',()=>{
        const capa=recupereCapa(C)
        const eff=recupereEffect(clas)
        console.log(clas)
        console.log(capa,eff)
        const message=document.querySelector('.message');
        console.log(message)
        if(capa<=eff){
            message.textContent="cette salle ne peut contenir l'effectif de cette classe"
        }
        RemplirEmploiClasse(A,B,C,jour,D,E,clas)
        const form1=document.querySelector('.formula');
        form1.style.display='none'
    })
}

function formulaire(list1,list2,list3,jour,clas){
    let semaine=document.querySelector('.semaine')
    let form=document.createElement('form');
    form.classList.add('formula')
    let p1form=document.createElement('p');
    
   
   
    let message=document.createElement('p')
    message.classList.add('message')
    p1form.classList.add('modeTitile')
    let div1form=document.createElement('div');div1form.style.position='relative';div1form.style.display='flex';div1form.style.justifyContent='space-between';div1form.style.marginTop='60px'
    div1form.className='div1'
    let div2form=document.createElement('div');div2form.style.position='relative';div2form.style.display='flex';div2form.style.justifyContent='space-between';div2form.style.marginTop='20px'
    let div3form=document.createElement('div');div3form.style.position='relative';div3form.style.display='flex';div3form.style.justifyContent='space-between';div3form.style.marginTop='20px'
    let div4form=document.createElement('div');div4form.style.position='relative';div4form.style.display='flex';div4form.style.justifyContent='space-between';div4form.style.marginTop='20px'
    let div5form=document.createElement('div');div5form.style.position='relative';div5form.style.display='flex';div5form.style.justifyContent='space-between';div5form.style.marginTop='20px'
    let pdiv1=document.createElement('p');pdiv1.style.position='relative'
    let pdiv2=document.createElement('p');pdiv2.style.position='relative'
    let pdiv3=document.createElement('p');pdiv3.style.position='relative'
    let pdiv4=document.createElement('p');pdiv4.style.position='relative'
    let pdiv5=document.createElement('p');pdiv5.style.position='relative'
    let selectdiv1=document.createElement('select');selectdiv1.classList.add('selectdiv1')
    let selectdiv2=document.createElement('select');selectdiv2.classList.add('selectdiv2')
    let selectdiv3=document.createElement('select');selectdiv3.classList.add('selectdiv3')
    let selectdiv4=document.createElement('select');selectdiv4.classList.add('selectdiv4')
    let selectdiv5=document.createElement('select');selectdiv5.classList.add('selectdiv5')
    let p2form=document.createElement('p');p2form.classList.add('p2form')
    let s1p2=document.createElement('span');s1p2.classList.add('s1p2')
    let s2p2=document.createElement('span');s2p2.classList.add('s2p2')
    
    p1form.textContent='Modal Title'
    
    form.appendChild(p1form);
    s1p2.textContent='Ajouter'
    s2p2.textContent='Annuler'
    p2form.appendChild(s1p2)
    p2form.appendChild(s2p2);
    pdiv1.className='newp1'
    pdiv1.textContent=list1[0].nom
    pdiv2.textContent=list2[0].nom
    pdiv3.textContent=list3[0].nom
    pdiv4.textContent='Heure de debut'
    pdiv5.textContent="Nombre d'heure"
    div1form.appendChild(pdiv1)
    div2form.appendChild(pdiv2)
    div3form.appendChild(pdiv3)
    div4form.appendChild(pdiv4)
    div5form.appendChild(pdiv5)

    list1.forEach((ele)=>{
        console.log(ele.nom)
        let optione=document.createElement('option');
        optione.className='optionA'
        optione.textContent=ele.nom
        selectdiv1.appendChild(optione)

    })
    console.log(selectdiv1)
    list2.forEach((elel)=>{
        let option=document.createElement('option');
        option.className='optionB'
        option.textContent=elel.nom
        selectdiv2.appendChild(option)
    })
   
    list3.forEach((ele)=>{
        let optione=document.createElement('option');
        optione.className='optionC'
        optione.textContent=ele.nom
        selectdiv3.appendChild(optione)
    })
    div1form.appendChild(selectdiv1);
    div2form.appendChild(selectdiv2);
    div3form.appendChild(selectdiv3);
    const tabl=['8h','9h','10h','11h','12h','13h','14h','15h','15h','16h','17'];
    tabl.forEach((heure)=>{
        let optione=document.createElement('option');
        optione.className='optionD'
        optione.textContent=heure

        selectdiv4.appendChild(optione)
    })
    const table=['1h','2h','3h','4h'];
    table.forEach((heure)=>{
        let optione=document.createElement('option');
        optione.className='optionE'
        optione.textContent=heure
        selectdiv5.appendChild(optione)
    })
    div4form.appendChild(selectdiv4);
    div5form.appendChild(selectdiv5);
    form.appendChild(div1form);form.appendChild(div2form);form.appendChild(div3form);form.appendChild(div4form);form.appendChild(div5form);
    form.appendChild(message)
    form.appendChild(p2form)
    s2p2.addEventListener('click',()=>{
        form.style.display='none'
    })
    semaine.appendChild(form)
    let A='';let B='';let C='';let D='';let E='';

    function updateSelection() {
        A = selectdiv1.options[selectdiv1.selectedIndex].textContent;
        let AlloptionB=document.querySelectorAll('.optionB')

        AlloptionB.forEach(option=>{
            console.log(option)
            option.style.display='none';
            
        })
        menuEtComposant.Modules.forEach(list=>{
            if(list.nom==A){
                const enseig=list.enseignants;
                console.log(enseig)
                enseig.forEach(enseignant=>{
                    console.log(enseignant)
                    const optionB=document.createElement('option');
                    optionB.textContent=enseignant;
                    selectdiv2.append(optionB)                 
                })
            }
        })
        B = selectdiv2.options[selectdiv2.selectedIndex].textContent;
        C = selectdiv3.options[selectdiv3.selectedIndex].textContent; 
        D =selectdiv4.options[selectdiv4.selectedIndex].textContent;
        E= selectdiv5.options[selectdiv5.selectedIndex].textContent;

        let AlloptionA=document.querySelectorAll('.optionA')
        AlloptionA.forEach(option=>{
            option.style.display='none';
            
        })

        menuEtComposant.enseignants.forEach(list=>{
            if(list.nom==B){
                const module=list.Modules;
                console.log(module)
                module.forEach(modl=>{
                    console.log(modl)
                    const optionA=document.createElement('option');
                    optionA.textContent=modl;
                    selectdiv1.append(optionA)                 
                })
            }
        })
            
        console.log(A,B,C,D,E)



    }
    
    selectdiv1.addEventListener('change', updateSelection)
    selectdiv2.addEventListener('change', updateSelection)
    selectdiv3.addEventListener('change', updateSelection)
    selectdiv4.addEventListener('change', updateSelection)
    selectdiv5.addEventListener('change', updateSelection)
    s1p2.addEventListener('click',()=>{
        const capa=recupereCapa(C)
        const eff=recupereEffect(clas)
        if(capa<=eff){
            message.textContent="cette salle ne peut contenir l'effectif de cette classe"
        }
        RemplirEmploiClasse(A,B,C,jour,D,E,clas)
        form.style.display='none'
        
    })

    

}
// function AjouterEnseig(jour){
    
//     console.log('desac')
//     formulaire(menuEtComposant.classes,menuEtComposant.Modules,menuEtComposant.Salles)
//     const s1p2=document.querySelector('.s1p2')
//     console.log(s1p2)
//     const monSelect1=document.querySelector('.selectdiv1');
//     const monSelect2=document.querySelector('.selectdiv2')
//     const monSelect3=document.querySelector('.selectdiv3')
//     const monSelect4=document.querySelector('.selectdiv4')
//     const monSelect5=document.querySelector('.selectdiv5')
//     console.log(monSelect1)
    
//     let A='';let B='';let C='';let D='';let E='';

//     function updateSelection() {
//         A = monSelect1.options[monSelect1.selectedIndex].textContent;

//         B = monSelect2.options[monSelect2.selectedIndex].textContent;
//         C = monSelect3.options[monSelect3.selectedIndex].textContent;
//         D = monSelect4.options[monSelect4.selectedIndex].textContent;
//         E = monSelect5.options[monSelect5.selectedIndex].textContent;


        
//         console.log(A, B, C, D, E);
        


//       }
      
//       monSelect1.addEventListener('change', updateSelection);
//       monSelect2.addEventListener('change', updateSelection);
//       monSelect3.addEventListener('change', updateSelection);
//       monSelect4.addEventListener('change', updateSelection);
//       monSelect5.addEventListener('change', updateSelection);
//       s1p2.addEventListener('click',()=>{
//         const capa=recupereCapa(C)
//         const eff=recupereEffect(A)
//         console.log(capa,eff)
//         const message=document.querySelector('.message');
//         console.log(message)
//         if(capa<=eff){
//             message.textContent="cette salle ne peut contenir l'effectif de cette classe"
//         }
//         RemplirEmploiEnsei(A,B,C,jour,D,E)
//     })
    
//     // const Aj=[plusLundi,plusMardi,plusJeudi,plusMercredi,plusVendredo,plusSamdi];
//     // let forme=document.querySelector('.formula');
//     // let style=window.getComputedStyle(forme);
//     // let typeDisplaye=style.getPropertyValue('display');
   
// }
// let isFormulClaLoaded = false; // initialise la variable booléenne

// classes.addEventListener('click',()=>{ 
//     const newlabel=document.querySelector('#selection')
//     newlabel.addEventListener('change',function(){
//         // vérifie si la fonction a déjà été chargée
//         if (!isFormulClaLoaded) {
//             // charge la fonction si elle n'a pas encore été chargée
//             AppelFormulCla('L2 MPI');
//             isFormulClaLoaded = true;
//         }

//         const optionSelect=this.options[this.selectedIndex];
//         if(optionSelect.textContent=='L2 MPI'){
//             // code pour L2 MPI
//         } else if(optionSelect.textContent=='L1 PC'){
//             // code pour L1 PC
//         } else {
//             // code pour autres classes
//         }
//     })
// })
 