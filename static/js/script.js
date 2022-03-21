$(function(){
  $(".v-error").hide();
  $("#id_date_of_birth").on("change", function(){
      let date = $(this).val().split("-")
      let year = parseInt(date[0]);
      let month = date[1];
      let day = date[2];
      let age = 18;
      let setDate = new Date(year + age, month - 1, day);
      let currDate = new Date();
      if(currDate <= setDate){
        $(".v-error").show();
        $("[role='menuitem']").hide();
        alert("You are below 18, sorry you can't proceed." );
      }else{
        $("[role='menuitem']").show();
        $(".v-error").hide();
      }   
  });
  
  var option = $(".select option:selected");
  option.prop("disabled", true);
  option.attr("value", " ");
  option.text("----Select----");
});