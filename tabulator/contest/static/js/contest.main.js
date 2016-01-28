function postScore(c, target_url) {
   var input_name = c.attr("name");
   var input_value = c.val();
   var input_data = {name: input_name, value: input_value};
  
   $.ajax({
       type: "GET",
       url: target_url,
       data: input_data,
       success: function(data, status){
        $('#staging').html(status)
       }
   })
};
   
$(document).ready(function() {

    $('a.candidate_link').click(function( eventObject ){
        var elem = $( this );
        eventObject.preventDefault();
        $('#jumbotron').load(elem.attr( "href" ));
        console.log(elem.attr( "href" ));
    });

    $('#jumbotron').on("change", ":input", function(){
        c = $(this);
        $.when(
        c.focusout()).then(function() {
            postScore(c, "/contest/setscore/")
        // alert("changed " + c.attr("name"));
	});
    });
});
