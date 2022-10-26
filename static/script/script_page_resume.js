$(document).ready(function () {
  var skills = [];
  var tmp = $("#skills").text().split("\n");
  var number = 0;
  var text_skills = ""
  for (let index = 0; index < tmp.length; index++) {
    tmp[index] = tmp[index].replace(/^\s+/, "");
    if (tmp[index] != "") {
      skills.push(tmp[index]);
    }
  }
  
  $("#search_skill").autocomplete({
    source: skills,
  });
  $("#search_skill").keypress(function (event) {
    if (event.which == 13) {
      skill();
    }
  });
  $("#submit").click(function () {
    text_skills = $("#block_skill").text().split(",");
    var input_skills = ""
    for (let index = 0; index < text_skills.length; index++) {
      if (text_skills[index].trim() != ""){
        if (input_skills.length == 0){
          input_skills = text_skills[index].trim()
        }
        else {
          input_skills += "," + text_skills[index].trim()
        }
      }   
    }
    $("#input_skills").val(input_skills)
  })

  $("#add").click(function () {
    skill();
  })

  $("#clear").click(function () {
    $("#block_skill").empty();
    $("#search_skill").val("");
    number = 0;
  });

  $("p").css({
    cursor: "default",
  });

  function skill() {
    var status = false
    $("#search_skill").focus();
    var tmp_skill = $("#block_skill").html();
    if ($("#search_skill").val() == "") {
      return;
    }

    for (let index = 0; index < skills.length; index++) {
      if ($("#search_skill").val() == skills[index]){
        status = true
        break
      }
    }
    if(status){
      
      if (tmp_skill == "") {
       
        $("#block_skill").addClass("mb-4");
        tmp_skill =
          '<div id="option_skill_' +
          number +
          '" class="mt-2 p-1 me-2 text-white bg-success rounded">\
              <span>'+
              $("#search_skill").val()+ '<span class="d-none">,</span>' +
          '</span>\
              <img style="width: 15px;" src="../static/img/button_close.png">\
              </div>\n';
        number++;
      } else {
        
        tmp_skill +=
          '<div id="option_skill_' +
          number +
          '" class="mt-2 p-1 me-2 text-white bg-success rounded">\
              <span>' +
          $("#search_skill").val()+ '<span class="d-none">,</span>' +
          '</span>\
              <img style="width: 15px;" src="../static/img/button_close.png">\
              </div>';
        number++;
      }
    }

    $("#block_skill").html(tmp_skill);

    for (let index = 0; index < number + 1; index++) {
      let tmp_a = "#option_skill_" + index;
      $(tmp_a + " img").css({
        cursor: "pointer",
      });
      $(tmp_a + " span").css({
        cursor: "default",
      });
      $(tmp_a + " img").click(function () {
        $(tmp_a).remove();
      });
    }
    $("#search_skill").val("");
  }
});
