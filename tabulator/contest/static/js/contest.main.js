$(document).ready(function() {
    formmodified=0;
    $('form *').change(function(){
        formmodified=1;
    });
    window.onbeforeunload = confirmExit;
    function confirmExit() {
        if (formmodified == 1) {
            return "New information not saved. Do you wish to leave the page?";
        }
    }
    $("input[name='commit']").click(function() {
        formmodified = 0;
    });

    $('a.candidate_link').click(function( eventObject ){
        var elem = $( this );
        eventObject.preventDefault();
        $('#stage').load(elem.attr( "href" ));
        console.log(elem.attr( "href" ));
    });


});
