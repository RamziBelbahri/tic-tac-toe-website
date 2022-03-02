
$(() => {

    $(".grid-item").on("click", (event) => {
        console.log("event says:", event.target.id);
        console.log("item says:", this.id);
        // alert("You clicked the button using JQuery!");
        playerMove();
        computerMove();
    });
});


function verifyGameState() {
    return 0;
}

function playerMove() {
    return 0;
}

function computerMove() {
    return 0;
}