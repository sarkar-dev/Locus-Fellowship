// alert("Alert alert")

const form = document.querySelector('form');

function onSubmit(e){
    e.preventDefault();     //page reload prevented

    const name = document.querySelector('#name').value;
    const amount = document.querySelector('#amount').value;

    const ul = document.querySelector('ul');
    const li = document.createElement('li');
   
    li.innerText = `${name} Rs ${amount}`
   
    ul.appendChild(li);

    //console.log(name, amount);

   // alert(`Form submitted with name: ${name} and amount: ${amount}`);
}

form.addEventListener('submit', onSubmit);