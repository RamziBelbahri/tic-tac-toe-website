
// var sdsd = import('../../views.py');

// view.sayHi();

var csrf = $("input[name=csrfmiddlewaretoken]").val();

$(() => {

    $(".grid-item").on("click", (event) => {
        console.log($("#about-btn"));
        console.log("event says:", event.target.id);
        console.log("item says:", this.id);
        // alert("You clicked the button using JQuery!");
        endGame("win");
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

function endGame(result) {
    $.ajax({
        type: 'POST',
        url: 'home',
        data: { 
            res: result,
            csrfmiddlewaretoken: csrf
        },
        success: function(resp) {
            let body = $().html();
            var $corp = $(body);
            $corp = resp;
            console.log(body);
            return resp;
        },
        error: function() {
      
        }
      });
}