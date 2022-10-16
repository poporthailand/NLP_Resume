$(document).ready(function () {
  var skills = [];
  var tmp = $("#skills").text().split("\n");
  var number = 0;

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

  $("#add").click(function () {
    skill();
  });

  $("#clear").click(function () {
    $("#block_skill").empty();
    $("#search_skill").val("");
    number = 0;
  });

  $("p").css({
    cursor: "default",
  });

  function skill() {
    $("#search_skill").focus();
    var tmp_skill = $("#block_skill").html();
    if ($("#search_skill").val() == "") {
      return;
    }
    if (tmp_skill == "") {
      $("#block_skill").addClass("mb-4");
      tmp_skill =
        '<div id="option_skill_' +
        number +
        '" class="mt-2 p-1 me-2 text-white bg-success rounded">\
            <span>' +
        $("#search_skill").val() +
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
        $("#search_skill").val() +
        '</span>\
            <img style="width: 15px;" src="../static/img/button_close.png">\
            </div>';
      number++;
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
