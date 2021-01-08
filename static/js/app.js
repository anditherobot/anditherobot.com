$(document).ready(function(){
    
    //This is for the photo gallery
    $('ul.first').bsPhotoGallery({
      "classes" : "col-xl-3 col-lg-2 col-md-4 col-sm-4",
      "hasModal" : true,
      "shortText" : false,
      "showControl": true
    });


    console.log('initiallized');

 
  $("#contact").submit(function(e){

    if($('#faketcha').val() == 2 ) {
     
   }
   else {
      e.preventDefault();
      $('#faketcha').css("border", "1px solid #ff0000")
      if (!$('#faketchamessage').length) {
      $( "<p id='faketchamessage' style='color:red;'>Error: can't submit form. Unless you enter the result of 1 + 1 </p>" ).insertBefore( "#faketchapar" );
    }
   }  
  });
 
});

  
  


