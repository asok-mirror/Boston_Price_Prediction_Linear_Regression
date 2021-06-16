$(document).ready(function(){
   $("#boston").submit(function(e){
      if ($("#boston")[0].checkValidity()) {
        //prevent Default functionality
        e.preventDefault();
        $("#overlay").show();
        //get the action-url of the form
        var actionurl = e.currentTarget.action;

        //do your own request an handle the results
        $.ajax({
           url: actionurl,
           type: 'post',
           dataType: 'json',
           data: $("#boston").serialize(),
                success: function(data) {
                    document.getElementById('result').innerHTML = data.homeValue;
                },
                error: function (xhr, ajaxOptions, thrownError) {
                    document.getElementById('result').innerHTML = "<p class='text-danger'> Error in predicting home value </p>";
                    console.log(thrownError);
                },
                complete: function() {
                 $("#overlay").hide();
                }
        });
      }
      else {
          e.preventDefault()
          e.stopPropagation()
       }
      $("#boston")[0].classList.add('was-validated')
   });
});