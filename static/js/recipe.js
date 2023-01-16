let updated_serving = false

function copy_url() {
    const dummy = document.createElement('input'),
        text = window.location.href;

    document.body.appendChild(dummy);
    dummy.value = text;
    dummy.select();
    document.execCommand('copy');
    document.body.removeChild(dummy);
}

function increase(serving, button) {
    if (updated_serving === false) {
        updated_serving = Number(serving)
    }
    let amounts = document.getElementsByClassName("ing_amount");
    let isNum;
    for (let i = 0; i < amounts.length; i++) {
        let amount = amounts[i].innerHTML
        isNum = /\d/.test(amount);
        if (isNum) {
            amount = Number(amount)
            serving = Number(serving)
            amount = amount / updated_serving * (updated_serving + 1)
            amount = amount.toFixed(3);
            amount = amount.toString()
            amounts[i].innerHTML = amount
        }
    }


    updated_serving = updated_serving + 1
    document.getElementById("serving_span").innerHTML = updated_serving
    document.getElementById("serving_span_1").innerHTML = updated_serving + " serving"
}
