let texts = document.getElementsByClassName('qnt_itens')
let button = document.getElementsByClassName('button-quantidade-esquerda')
button.disabled = true;
for(var i = 0; i < texts.length; i++){
    if (texts[i].innerText <= 1){
        button[i].disabled = true;
    }
}

