const tableau=[
    {
            question: "Quel est le MeilleurLangage de Programmation en2022",
            a: "Java",
            b: "C",
            c: "Python",
            d: "JavaScript",
            correct:"JavaScript" ,
        },
    {
            question: "Qu'est-ce que le HTML?",
            a: "Un langage de programmation pour les applications web",
            b: " Un langage de balisage pour les pages web",
            c: " Un langage de programmation pour les applications mobiles",
            d: "Un système d'exploitation pour les ordinateurs portables",
            correct: " Un langage de balisage pour les pages web",
        },
        {
            question: "Qu'est-ce que CSS?",
            a: "Un langage de balisage pour les pages web",
            b: "Un langage de programmation pour les applications mobiles",
            c: "Un système d'exploitation pour les ordinateurs portables",
            d: "Un langage de programmation pour les jeux vidéo",
            correct:  "Un langage de balisage pour les pages web",
            },
        {
            question: "Qu'est-ce que JavaScript?",
            a: "Un langage de programmation pour les applications web",
            b: "Un langage de balisage pour les pages web",
            c: "Un système d'exploitation pour les ordinateurs portables",
            d: "Un langage de programmation pour les jeux vidéo   " ,     
            correct: "Un langage de programmation pour les applications web",
            },
        {
            question: "Qu'est-ce qu'une base de données?",
            a: "Un langage de programmation pour les applications web",
            b: "Un logiciel pour la création de graphiques",
            c: "Un système de stockage et de gestion de données",
            d: "Un type de processeur pour les ordinateurs portables",
            correct: "Un système de stockage et de gestion de données",
            },
        {
            question:"Qu'est-ce que Git?",
            a: "Un éditeur de texte pour les développeurs",
            b: "Un système de contrôle de version pour le code source",
            c: "Un langage de programmation pour les jeux vidéo",
            d: "Un système d'exploitation pour les ordinateurs portables",
            correct: "Un système de contrôle de version pour le code source",
            },
]
const contenerHtml=document.querySelector(".contener")
const questionHtml=document.querySelector(".question");
const choixhtml=document.querySelector(".choix");
const btnHtml=document.querySelector(".button");
const choix1=document.querySelector(".choix1");
const choix2=document.querySelector(".choix2");
const choix3=document.querySelector(".choix3");
const choix4=document.querySelector(".choix4");


let longtab=0;
let Score=0;

function loadquestion(){
    const question=tableau[longtab].question;
    const a=tableau[longtab].a;
    const b=tableau[longtab].b;
    const c=tableau[longtab].c;
    const d=tableau[longtab].d;
    questionHtml.textContent=question;
    choix1.textContent=a;
    choix2.textContent=b;
    choix3.textContent=c;
    choix4.textContent=d;
    
}
loadquestion()
const btn=document.querySelector('button');
btn.addEventListener('click',()=>{
    const elementCoche=document.querySelector("input[name='options']:checked");
    if(elementCoche){
        const correcte=tableau[longtab].correct;
        const reponeUtilisa=elementCoche.nextElementSibling.textContent;
        console.log(reponeUtilisa)
        if(correcte==reponeUtilisa){
            Score++;
        }
        longtab++;
        if(longtab<tableau.length){
            const btn=document.querySelector('.button');
            loadquestion();
        }else{
            contenerHtml.style.display='none';
            const divrejoue=document.createElement('div');
            divrejoue.classList.add('divrejou')
            const message=document.createElement('p');
            message.classList.add('message')
            const rejou=document.createElement('p');
            rejou.classList.add('rejou')
            rejou.textContent='Rejouer'
            message.textContent='vous avez trouver '+Score+'/6 questions'
            document.body.appendChild(divrejoue)
            divrejoue.appendChild(message)
            divrejoue.appendChild(rejou)
            rejou.addEventListener('click',()=>{
                divrejoue.style.display='none'
                Score=0;
                longtab=0;
                contenerHtml.style.display='block';
                loadquestion();
                
            })

        }
    }
    
}) 
