//Load makes sure that js code will run after the css and html has ran

window.addEventListener("load", function ()
{
    //Get click element refrences
    let clickCounterElement = document.getElementById("click-counter");
    let clickButtonElement = document.getElementById("click-button");
    

    //Counter value
    let counter = 0;

    //Click button function
    let clickButtonFunction = function ()
    {
        //Increment counter
        counter++;

        //Update counter value
        clickCounterElement.innerHTML = counter;
    };

    //Attach the button function
    clickButtonElement.addEventListener("click", clickButtonFunction);
});

