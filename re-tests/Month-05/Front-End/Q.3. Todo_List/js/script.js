
const feedhide = document.querySelector('.feedhide');
const clearBtn = document.querySelector('#clearList');
const form = document.querySelector('#itemForm'); 
const inputitems = document.querySelector('#inputitems'); 
const items_list = document.querySelector('.item-list');

let itemToDo = [];

const handleItem = function(itemName){

    const items = items_list.querySelectorAll('.item');
 
    items.forEach(function(item){
        
        if(item.querySelector('.item-name').textContent === itemName){

            item.querySelector('.complete-item').addEventListener('click', function(){

                item.querySelector('.item-name').classList.toggle('completed');

                this.classList.toggle('visibility');
            });

            item.querySelector('.edit-item').addEventListener('click', function(){

                inputitems.value = itemName;
                
                items_list.removeChild(item);

                itemToDo = itemToDo.filter(function(item){

                    return item !== itemName;
                });
            });

            item.querySelector('.delete-item').addEventListener('click', function(){
                
                items_list.removeChild(item);

                itemToDo = itemToDo.filter(function(item){
                    return item !== itemName;
                });

                showFeedback('item delete', 'success');
            })
        }
    })
}


const getList = function(itemToDo){

    items_list.innerHTML = '';

        itemToDo.forEach(function(item){
            items_list.insertAdjacentHTML('beforeend', `<div class="item my-3"><h5 class="item-name text-capitalize">${item}</h5>
            <div class="item-icons"><a href="#" class="complete-item mx-2 item-icon"><i class="bi bi-check2-circle"></i></a><a href="#" class="edit-item mx-2 item-icon"><i class="bi bi-pencil-square"></i></a><a href="#" class="delete-item item-icon"><i class="bi bi-x-circle"></i></a></div>
            </div>` );

            handleItem(item);
        });
}

const getLocalStorage = function(){

    const todoStorage = localStorage.getItem('itemToDo');

    if (todoStorage === 'undefined' || todoStorage === null){
        itemToDo = [];
    }
    else {
        itemToDo = JSON.parse(todoStorage);
        getList(itemToDo);
    }
}

const setLocalStorage = function(itemToDo){
    localStorage.setItem('itemToDo', JSON.stringify(itemToDo));
}


getLocalStorage();

const removeItem = function(item){

    console.log(item);
    
    const removeIndex = (itemToDo.indexOf(item));
    
    console.log(removeIndex);
    
    itemToDo.splice(removeIndex, 1);
}


form.addEventListener('submit', function(e){ 
    e.preventDefault();
    const itemName = inputitems.value;
    
    if (itemName.length === 0){
        feedhide.innerHTML = 'Write Valid text';
        feedhide.classList.add('showItem', 'alert-danger');
        setTimeout(
            function(){
                feedhide.classList.remove('showItem');
                }, 2000);
    }
    
    else {
        itemToDo.push(itemName);
        setLocalStorage(itemToDo);
        getList(itemToDo);
        
    }
    
    inputitems.value = '';

    });



clearBtn.addEventListener('click', function(){
    itemToDo = [];
    localStorage.clear();
    getList(itemToDo);
})



  

