const pgene=document.querySelector('p');
// const longcode=document.querySelector("input[type='number']");
// console.log(longcode)
// let randomNumber = Math.floor(Math.random() * 11);
// console.log(randomNumber);
// let randomLetter = String.fromCharCode(65 + Math.floor(Math.random() * 26));
// console.log(randomLetter);
// let randomLetters = String.fromCharCode(91 + Math.floor(Math.random() * 26));
// console.log(randomLetters);
pgene.addEventListener('click',()=>{
    let codegenerer='';
    const longcode=document.querySelector("input[type='number']").value;
    const zonetext=document.querySelector("input[type='text']");
    const chekMaj=document.querySelector(".Maj");
    const chekMin=document.querySelector(".Min");
    const chekNum=document.querySelector(".num");
    const chekcara=document.querySelector(".cara");
    const characters ='!@#$%^&*()/\?'
    if(longcode>=15 && longcode<=20){
        while(codegenerer.length<longcode-2){
            if(chekMaj.checked==true && chekMin.checked==true && chekNum.checked==true && chekcara.checked==true ){
                let randomIndex = Math.floor(Math.random() * characters.length);
                codegenerer+=Math.floor(Math.random() * 11)+String.fromCharCode(65 + Math.floor(Math.random() * 26))+characters.charAt(randomIndex)+String.fromCharCode(97 + Math.floor(Math.random() * 26));
            // le bloc suivant c'est quant l'utilisateurs check une  cases
            }else if(chekMaj.checked==true && chekMin.checked==false && chekNum.checked==false && chekcara.checked==false){
                codegenerer+=String.fromCharCode(65 + Math.floor(Math.random() * 26))+String.fromCharCode(65 + Math.floor(Math.random() * 26))+String.fromCharCode(65 + Math.floor(Math.random() * 26));
            }else if(chekMaj.checked==false && chekMin.checked==true && chekNum.checked==false && chekcara.checked==false){
                codegenerer+=String.fromCharCode(97 + Math.floor(Math.random() * 26)) +String.fromCharCode(97 + Math.floor(Math.random() * 26))+String.fromCharCode(97 + Math.floor(Math.random() * 26));
            }else if(chekMaj.checked==false && chekMin.checked==false && chekNum.checked==true && chekcara.checked==false){
                codegenerer+=Math.floor(Math.random() * 11)+Math.floor(Math.random() * 11)+Math.floor(Math.random() * 11)
            }else if (chekMaj.checked==false && chekMin.checked==false && chekNum.checked==false && chekcara.checked==true){
                let randomIndex = Math.floor(Math.random() * characters.length);
                randomCode += characters.charAt(randomIndex)+characters.charAt(randomIndex)+characters.charAt(randomIndex);
                // le bloc suivant c'est quant l'utilisateurs check deux cases
            } else if(chekMaj.checked==true && chekMin.checked==true && chekNum.checked==false && chekcara.checked==false){
                codegenerer+=String.fromCharCode(65 + Math.floor(Math.random() * 26))+String.fromCharCode(97 + Math.floor(Math.random() * 26))+String.fromCharCode(65 + Math.floor(Math.random() * 26))
            }else if(chekMaj.checked==true && chekMin.checked==false && chekNum.checked==true && chekcara.checked==false){
                codegenerer+=String.fromCharCode(65 + Math.floor(Math.random() * 26)) + Math.floor(Math.random() * 11)+String.fromCharCode(65 + Math.floor(Math.random() * 26))
            }else if(chekMaj.checked==true && chekMin.checked==false && chekNum.checked==false && chekcara.checked==true){
                let randomIndex = Math.floor(Math.random() * characters.length);
                codegenerer+=String.fromCharCode(65 + Math.floor(Math.random() * 26)) +  characters.charAt(randomIndex)+String.fromCharCode(65 + Math.floor(Math.random() * 26));
            }else if (chekcara.checked==true && chekMaj.checked==false && chekMin.checked==false && chekNum.checked==true){
                
                let randomIndex = Math.floor(Math.random() * characters.length);
                codegenerer += characters.charAt(randomIndex)+Math.floor(Math.random() * 11)+characters.charAt(randomIndex);
            }else if (chekcara.checked==true && chekMaj.checked==false && chekMin.checked==true && chekNum.checked==false){
                let randomIndex = Math.floor(Math.random() * characters.length);
                codegenerer += characters.charAt(randomIndex)+ String.fromCharCode(97 + Math.floor(Math.random() * 26))+characters.charAt(randomIndex);
            }else if (chekcara.checked==false && chekMaj.checked==false && chekMin.checked==true && chekNum.checked==true){
                codegenerer +=Math.floor(Math.random() * 11) + String.fromCharCode(97 + Math.floor(Math.random() * 26))+Math.floor(Math.random() * 11);
                        // le bloc suivant c'est quant l'utilisateurs check trois cases
            }else if (chekcara.checked==false && chekMaj.checked==true && chekMin.checked==true && chekNum.checked==true){
                codegenerer +=String.fromCharCode(65 + Math.floor(Math.random() * 26))+Math.floor(Math.random() * 11) + String.fromCharCode(97 + Math.floor(Math.random() * 26));
            }else if (chekcara.checked==true && chekMaj.checked==false && chekMin.checked==true && chekNum.checked==true){
                let randomIndex = Math.floor(Math.random() * characters.length);
                codegenerer +=characters.charAt(randomIndex)+Math.floor(Math.random() * 11) + String.fromCharCode(97 + Math.floor(Math.random() * 26));
            }else if (chekcara.checked==true && chekMaj.checked==true && chekMin.checked==true && chekNum.checked==false){
                let randomIndex = Math.floor(Math.random() * characters.length);
                codegenerer +=characters.charAt(randomIndex)+String.fromCharCode(65 + Math.floor(Math.random() * 26)) + String.fromCharCode(97 + Math.floor(Math.random() * 26));
            }else{
                let randomIndex = Math.floor(Math.random() * characters.length);
                codegenerer +=characters.charAt(randomIndex)+String.fromCharCode(65 + Math.floor(Math.random() * 26)) + Math.floor(Math.random() * 11);
        
            }
        };
    
        zonetext.value=codegenerer;
        console.log(zonetext);
        const copi=document.createElement('p');
        const contener=document.querySelector('.contener')
        copi.textContent='copy'
        copi.classList.add('pcopy')
        contener.appendChild(copi)
        copi.addEventListener('click', () => {
            // navigator.clipboard.writeText permet de copier du texte
            navigator.clipboard.writeText(zonetext.value)
              .then(() => {
                alert('Texte copié avec succès !');
                // Afficher une notification de réussite ou un message de confirmation ici
              })
              .catch((err) => {
                alert('Impossible de copier le texte :', err);
                // Afficher une notification d'échec ou un message d'erreur ici
              });
          });
        

    }else{
        alert('vous devez donner generer un code qui as une longueur superieur a 14 et inferieur a 21 ')
    };
}); 





// // Récupération de l'élément input
// const inputElement = document.getElementById('monCheckbox');

// // Récupération de la valeur de l'input
// const valeurInput = inputElement.checked;

// // Utilisation de la valeur de l'input
// console.log(valeurInput);
// Récupération de l'élément contenant le texte à copier
// const element = document.getElementById('monElement');

// Sélection du texte à copier
// const selection = window.getSelection();
// const range = document.createRange();
// range.selectNodeContents(element);
// selection.removeAllRanges();
// selection.addRange(range);

// // Copie du texte sélectionné dans le presse-papiers
// document.execCommand('copy');

// // Désélection du texte pour éviter que l'utilisateur soit surpris
// selection.removeAllRanges();
// // Dans cet exemple, nous récupérons d'abord l'élément contenant le texte à copier en utilisant document.getElementById. Nous créons ensuite une sélection de texte en utilisant les méthodes window.getSelection() et document.createRange(). Nous sélectionnons le contenu de l'élément avec range.selectNodeContents(element). Nous copions ensuite le texte sélectionné dans le presse-papiers en appelant document.execCommand('copy'). Enfin, nous désélectionnons le texte pour éviter que l'utilisateur soit surpris.

// Notez que cette méthode ne fonctionne pas sur tous les navigateurs, notamment sur les versions plus anciennes d'Internet Explorer. Il peut être nécessaire d'utiliser une bibliothèque externe pour une compatibilité maximale.










// En JavaScript, la méthode Math.random() est utilisée pour générer des nombres aléatoires 
//compris entre 0 et 1.

// Voici un exemple de code qui génère un nombre aléatoire entre 0 et 10 en JavaScript :

// javascript

// let randomNumber = Math.floor(Math.random() * 11);
// console.log(randomNumber);

// La méthode Math.floor() est utilisée pour arrondir le résultat à un nombre entier inférieur
// ou égal.

// Pour générer des lettres aléatoires en JavaScript, vous pouvez utiliser la méthode String.
//fromCharCode() et la méthode Math.floor().

// Voici un exemple de code qui génère une lettre aléatoire entre A et Z en JavaScript :

// javascript

// let randomLetter = String.fromCharCode(65 + Math.floor(Math.random() * 26));
// console.log(randomLetter);

// La valeur 65 représente le code ASCII pour la lettre "A". En ajoutant un nombre aléatoire compris entre 0 et 25 (correspondant aux 26 lettres de l'alphabet) à 65, nous obtenons un nombre aléatoire correspondant au code ASCII d'une lettre majuscule de l'alphabet. La méthode String.fromCharCode() est ensuite utilisée pour convertir le code ASCII en lettre.
// niahmouhammed99@gmail.com
// je veux generer un code de longueur 12 contenan de chiffre lettre majuscule minuscules de caractere speciaux en js

// Voici un exemple de code en JavaScript qui génère un code aléatoire de longueur 12 contenant
// des chiffres, des lettres majuscules et minuscules, et des caractères spéciaux :

// javascript

// function generateRandomCode() {
//   const characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()';
//   let randomCode = '';
//   for (let i = 0; i < 12; i++) {
//     let randomIndex = Math.floor(Math.random() * characters.length);
//     randomCode += characters.charAt(randomIndex);
//   }
//   return randomCode;
// }

// console.log(generateRandomCode());

// Explications :

//     La chaîne de caractères characters contient tous les caractères possibles qui peuvent apparaître dans le code généré.
//     La variable randomCode est initialisée avec une chaîne de caractères vide.
//     Une boucle for est utilisée pour générer chaque caractère du code aléatoire.
//     À chaque itération de la boucle, un nombre aléatoire est généré avec Math.random() et multiplié par la longueur de la chaîne characters. Math.floor() est utilisé pour arrondir le nombre à un entier inférieur ou égal.
//     La méthode charAt() est utilisée pour récupérer le caractère à l'index aléatoire de la chaîne characters, et ce caractère est ajouté à la variable randomCode.
//     Finalement, la fonction renvoie la chaîne de caractères aléatoire de longueur 12.